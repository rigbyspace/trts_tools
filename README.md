# RS Toolkit

A minimal, axiom-compliant Python environment for developing RigbySpace,
built from what this session's testing actually required and actually
got wrong at least once.

## Why default libraries aren't safe, specifically

| Library / function | Why it fails RS | What to use instead |
|---|---|---|
| `fractions.Fraction` | Auto-reduces via `gcd()` on construction, every time, even for a one-off comparison | `ERP` class + `.evaluate()` |
| `decimal.Decimal` | Still a continuum representation | `ERP` + `.evaluate()` |
| `numpy` (default float64) | Internal linear algebra (`eig`, `svd`, etc.) is floating-point throughout — this is what caused a real, in-session mistake (eigenvalue conclusions fed back into RS reasoning as if they were exact) | `sympy` with plain-int/`Integer` matrix entries for anything that must stay exact |
| `sympy.Rational` | Auto-reduces exactly like `Fraction` | plain `int` inside `ERP`; `sympy.Integer` only for matrix/polynomial entries, never for ERP components |
| `math.sqrt`, `math.log`, `math.floor`, `math.ceil`, `math.gcd`, `math.fmod` | Directly forbidden operations | Only invoke these to construct a **comparison target** (e.g. `math.sqrt(2)` to check an ERP's `.evaluate()` against), never inside propagation |
| `abs()` | Directly forbidden | `primality.py`'s sign-preserving magnitude helper, or explicit comparison |
| `/`, `//`, `%`, `-` | Division, floor-division, modulo, subtraction all forbidden inside propagation | `ERP.evaluate()` is the one sanctioned division; ledger/index bookkeeping on plain ints is fine and should be marked `# rs-guard: allow` with a reason |
| `**` with non-2/3 exponent | Only square/cube are the framework's explicitly-permitted temporary shorthand | Restructure via repeated `oplus`/`boxplus`/`eta`, or flag as a deliberate, documented exception |

## What's in this package

- **`erp.py`** — the `ERP` type. Strictly `int`-only components, exact
  componentwise equality (never equality-after-reduction), and exactly
  one sanctioned exit to a real number: `.evaluate()`.
- **`operators.py`** — `eta`, `boxplus`, `oplus`, `psi`: the four
  confirmed-independent primitives. `lambda` is deliberately **not**
  reimplemented as its own function — it's `oplus(x, ERP(1,1))`, and
  the toolkit keeps that derivation visible at the call site rather
  than hiding it behind a fifth primitive name.
- **`zero_logic.py`** — absence constants and the constraint-vacuum
  (`d==0`) resolution, confirmed to fall directly out of the general
  `psi` formula with no special-casing needed.
- **`primality.py`** — sign-preserving primality detection. Negative
  primes count as primes (magnitude-based check); the sign of the
  original value is never read *out* of, mutated, or discarded.
- **`ledgers.py`** — `Koppa` (tested mechanism: accumulates the
  excluded-sum-at-Return via pure addition) and `Omega` (implemented,
  but explicitly marked conditional/untested).
- **`analysis.py`** — exact, symbolic, integer-only external analysis
  tools (characteristic polynomials, discriminants). Clearly
  documents where this session's work stopped (dominant-root
  isolation is flagged as unimplemented, not faked).
- **`tick_counter.py`** — mod-free cyclic position tracking. Formalizes
  a pattern traced back to the very first TRTS paper this session
  worked from: its `rational_index_tracker` (increment, reset at the
  period) avoids `%` entirely in the generative rule, using it only in
  a block explicitly marked "for analytical verification only."
  `Engine` already did this implicitly; this module names the pattern
  so it can be reused directly.
- **`precession.py`** — the k-periodic TRTS mechanism, formalized. This
  was the session's strongest tested result (7 of 7 exact predictions,
  k=3 through k=9) and previously existed only as scratch scripts.
  `sqrt()` is used exactly once, to build a comparison target for
  `.evaluate()` — never in the generative rule, matching the original
  paper's own discipline exactly.
- **`guard.py`** — an AST-based static scanner for the whole banned
  list above. Default deny; violations must be explicitly exempted
  with a `# rs-guard: allow: <reason>` comment, so every exception is
  a conscious, documented choice rather than a silent gap.

## Basic usage

```python
from rs_toolkit import ERP, eta, oplus, psi, Koppa

a = ERP(22, 7)
b = eta(a)                      # legal RS propagation
val = b.evaluate()              # ONE-WAY exit, for comparison only
# val can never be fed back in as an ERP -- there is no ERP.from_float()
```

Run the guard against any new file before trusting it:

```
python3 -m rs_toolkit.guard your_new_module.py
```

Run the test suite:

```
pytest rs_toolkit/tests/test_rs_toolkit.py -v
```

### Wiring the guard into git, so it can't be forgotten

A linter only helps if it actually runs. Add this as
`.git/hooks/pre-commit` (make it executable: `chmod +x`):

```bash
#!/bin/sh
changed_py=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
if [ -n "$changed_py" ]; then
    python3 -m rs_toolkit.guard $changed_py
    if [ $? -ne 0 ]; then
        echo "rs-guard found violations -- fix or add '# rs-guard: allow: <reason>'"
        exit 1
    fi
fi
```

## Engine -- the canonical cycle (fixes a real bug)

Every hand-rolled cycle loop earlier this session was a fresh
opportunity to reintroduce the same mistake: reverting on
`global_tick % 3 == 0` instead of resetting local position every 11
ticks. Those rules only agree in the first cycle. `Engine` fixes this
once:

```python
from rs_toolkit import Engine, ERP, boxplus, Koppa

koppa = Koppa()

def on_boundary(engine, tick):
    pass  # wire in koppa/omega logic here

eng = Engine(ERP(22,7), ERP(7,19), combine_fn=boxplus, on_boundary=on_boundary)
history = eng.run_cycles(5)
```
