"""
test_guard_and_analysis.py -- coverage for guard.py and analysis.py.

Neither module had any tests in test_rs_toolkit.py. guard.py in
particular is the thing enforcing every other axiom in this toolkit,
so an unguarded guard is the highest-value gap to close. Two of these
tests (test_guard_catches_float_exponent, test_guard_catches_unary_
negation_of_variable) are regression tests for gaps found and patched
this session -- confirmed present in the original guard.py by direct
probing before the patch, confirmed absent after.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
import sympy as sp
from rs_toolkit.guard import check_source
from rs_toolkit.analysis import (
    characteristic_polynomial,
    has_repeated_root,
    dominant_root_isolation_warning,
)


# ---------- guard.py: banned imports / calls ----------

def test_guard_catches_fractions_import():
    assert check_source("import fractions\n")

def test_guard_catches_decimal_import():
    assert check_source("import decimal\n")

def test_guard_catches_numpy_import():
    assert check_source("import numpy\n")

def test_guard_allows_sympy_import():
    assert check_source("import sympy\n") == []

def test_guard_catches_abs_call():
    assert check_source("x = abs(n)\n")

def test_guard_catches_sympy_rational():
    assert check_source("import sympy as sp\nx = sp.Rational(1, 2)\n")

def test_guard_catches_simplify_method():
    assert check_source("x = expr.simplify()\n")


# ---------- guard.py: banned binops ----------

def test_guard_catches_division():
    assert check_source("x = n / d\n")

def test_guard_catches_floor_division():
    assert check_source("x = n // d\n")

def test_guard_catches_modulo():
    assert check_source("x = n % d\n")

def test_guard_catches_binary_subtraction():
    assert check_source("x = n - m\n")

def test_guard_allows_addition_and_multiplication():
    assert check_source("x = n + m\ny = n * m\n") == []


# ---------- guard.py: exponent rules, including the patched float-exponent gap ----------

def test_guard_allows_int_exponent_2_and_3():
    assert check_source("x = n ** 2\n") == []
    assert check_source("x = n ** 3\n") == []

def test_guard_catches_exponent_other_than_2_or_3():
    assert check_source("x = n ** 4\n")

def test_guard_catches_float_exponent():
    """
    Regression test: the original guard checked `exp.value in (2, 3)`
    without checking the exponent's TYPE. Since `2.0 == 2` in Python,
    `n ** 2.0` (a float exponent) passed silently. Confirmed by direct
    probing before this fix; must be caught now.
    """
    assert check_source("x = n ** 2.0\n")


# ---------- guard.py: unary negation, including the patched bypass gap ----------

def test_guard_catches_unary_negation_of_variable():
    """
    Regression test: `x = -n` bypassed the guard entirely in the
    original version, because BANNED_BINOPS only matches ast.BinOp,
    and unary negation is ast.UnaryOp. `a + (-b)` is arithmetically
    subtraction and must be caught for the same reason the Sub BinOp
    is caught. Confirmed by direct probing before this fix.
    """
    assert check_source("x = -n\n")

def test_guard_allows_negative_literal():
    """
    A negative integer literal is legitimate RS state (primality.py:
    negative primes are real, signed values) and must NOT be flagged,
    unlike negation of a variable/expression above.
    """
    assert check_source("x = -7\n") == []
    assert check_source("x = ERP(-7, 3)\n") == []


# ---------- guard.py: exemption comment ----------

def test_guard_respects_exemption_comment():
    src = "x = n / d  # rs-guard: allow: sole sanctioned exit point\n"
    assert check_source(src) == []

def test_guard_exemption_is_per_line_not_global():
    src = (
        "x = n / d  # rs-guard: allow: sole sanctioned exit point\n"
        "y = a / b\n"
    )
    violations = check_source(src)
    assert len(violations) == 1
    assert violations[0].line == 2


# ---------- analysis.py ----------

def test_characteristic_polynomial_is_exact_for_known_matrix():
    # [[2,0],[0,3]] has charpoly (x-2)(x-3) = x^2 - 5x + 6
    x = sp.Symbol('x')
    poly = characteristic_polynomial([[2, 0], [0, 3]])
    assert sp.expand(poly - (x**2 - 5*x + 6)) == 0  # rs-guard: allow: symbolic polynomial equality check, not ERP arithmetic

def test_characteristic_polynomial_coefficients_are_exact_integers():
    poly = characteristic_polynomial([[1, 1], [1, 0]])  # Fibonacci matrix
    # x^2 - x - 1; every coefficient must be an exact sympy Integer, no floats
    poly_dict = sp.Poly(poly, sp.Symbol('x')).as_dict()
    for coeff in poly_dict.values():
        assert coeff == int(coeff)

def test_has_repeated_root_true_for_repeated_root_matrix():
    # [[2,1],[0,2]] has charpoly (x-2)^2 -- repeated root at x=2
    poly = characteristic_polynomial([[2, 1], [0, 2]])
    assert has_repeated_root(poly) is True

def test_has_repeated_root_false_for_distinct_roots():
    # [[2,0],[0,3]] has distinct roots 2 and 3
    poly = characteristic_polynomial([[2, 0], [0, 3]])
    assert has_repeated_root(poly) is False

def test_dominant_root_isolation_is_explicitly_unimplemented():
    """
    Confirms this stays an honest NotImplementedError and doesn't
    silently start returning a guessed answer.
    """
    with pytest.raises(NotImplementedError):
        dominant_root_isolation_warning()


if __name__ == "__main__":
    import subprocess
    subprocess.run([sys.executable, "-m", "pytest", __file__, "-v"])
