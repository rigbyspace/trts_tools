"""
guard.py -- static scanner for RS-axiom violations.

Uses Python's `ast` module (safe: it only parses source text into a
syntax tree, no numeric evaluation involved) to catch violations that
are easy to introduce accidentally:

  - importing fractions.Fraction or decimal.Decimal (both auto-reduce
    or otherwise carry continuum representations)
  - importing numpy (its linear algebra is floating-point internally --
    this is what caused the eigenvalue mistake earlier this session)
  - calling abs()
  - using /, //, %, or - as binary operators
  - using ** with an exponent other than the literal 2 or 3 (square/cube
    are the framework's explicitly permitted temporary shorthand;
    anything else is an unpermitted root/power operation)
  - calling sympy.Rational, sympy.gcd, .simplify(), .cancel(), .together()
    (sympy.Rational auto-reduces exactly like Fraction does)

Default is deny. A line can be explicitly exempted with a trailing
comment `# rs-guard: allow: <reason>` -- this is intentional and
required to be a conscious, documented choice at the call site (e.g.
ERP.evaluate()'s division, or primality.py's use of % in a clearly
external analysis function), not a silent workaround.
"""

import ast

BANNED_IMPORTS = {'fractions', 'decimal', 'numpy'}
BANNED_CALLS = {'abs'}
BANNED_SYMPY_CALLS = {'Rational', 'gcd', 'nsimplify'}
BANNED_SYMPY_METHODS = {'simplify', 'cancel', 'together'}
BANNED_BINOPS = {
    ast.Div: '/ (division)',
    ast.FloorDiv: '// (floor division)',
    ast.Mod: '% (modulo)',
    ast.Sub: '- (subtraction)',
}


class Violation:
    def __init__(self, line, message):
        self.line = line
        self.message = message

    def __repr__(self):
        return f"line {self.line}: {self.message}"


def check_source(source: str, filename: str = "<string>") -> list:
    tree = ast.parse(source, filename=filename)
    lines = source.splitlines()
    violations = []

    def is_exempted(lineno):
        if 0 < lineno <= len(lines):
            return '# rs-guard: allow' in lines[lineno-1]
        return False

    for node in ast.walk(tree):
        lineno = getattr(node, 'lineno', -1)
        if is_exempted(lineno):
            continue

        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in BANNED_IMPORTS:
                    violations.append(Violation(lineno,
                        f"import of banned module '{alias.name}'"))

        elif isinstance(node, ast.Call):
            fname = None
            if isinstance(node.func, ast.Name):
                fname = node.func.id
            elif isinstance(node.func, ast.Attribute):
                fname = node.func.attr
            if fname in BANNED_CALLS:
                violations.append(Violation(lineno, f"call to banned builtin '{fname}()'"))
            if fname in BANNED_SYMPY_CALLS:
                violations.append(Violation(lineno, f"call to '{fname}' (likely gcd-reducing)"))
            if fname in BANNED_SYMPY_METHODS:
                violations.append(Violation(lineno, f"call to '.{fname}()' (may reduce/simplify)"))

        elif isinstance(node, ast.BinOp):
            for optype, desc in BANNED_BINOPS.items():
                if isinstance(node.op, optype):
                    violations.append(Violation(lineno, f"use of banned operator {desc}"))
            if isinstance(node.op, ast.Pow):
                exp = node.right
                # must be a literal int 2 or 3 -- checking type explicitly, not just
                # value, since 2.0 == 2 in Python and a float exponent would
                # otherwise silently pass (confirmed gap, patched here)
                ok = (isinstance(exp, ast.Constant)
                      and type(exp.value) is int
                      and exp.value in (2, 3))
                if not ok:
                    violations.append(Violation(lineno,
                        "use of ** with exponent other than literal 2 or 3"))

        elif isinstance(node, ast.UnaryOp):
            # confirmed gap: -n (negation of a variable/expression) bypassed
            # the guard entirely, since BANNED_BINOPS only matches ast.BinOp,
            # and a + (-b) is arithmetically subtraction. A negative LITERAL
            # (-7) is legitimate RS state (signed primes, etc.) and must
            # stay allowed -- the distinguishing factor is whether the
            # operand is a bare Constant or something computed.
            if isinstance(node.op, ast.USub) and not isinstance(node.operand, ast.Constant):
                violations.append(Violation(lineno,
                    "unary negation of a non-literal (equivalent to subtraction)"))

    return violations


def check_file(path: str) -> list:
    with open(path) as f:
        source = f.read()
    return check_source(source, filename=path)


if __name__ == "__main__":
    import sys
    for path in sys.argv[1:]:
        vs = check_file(path)
        if vs:
            print(f"{path}: {len(vs)} violation(s)")
            for v in vs:
                print(f"  {v}")
        else:
            print(f"{path}: clean")
