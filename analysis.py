"""
analysis.py -- EXTERNAL analysis tools. Read this docstring before using
anything in this file.

Everything here operates ON a structure built from ERPs (e.g. a
transition matrix built from plain-int tick-matrices) in order to
answer a question ABOUT that structure -- it never constructs, returns,
or implies an ERP. This is the same category as ERP.evaluate() and
is_prime_magnitude(): a one-way analytical exit, not a claim about how
RS itself computes anything.

The mistake this module exists to prevent: earlier this session,
np.linalg.eig() was used to analyze a transition matrix, and the
floating-point eigenvalues/eigenvectors it returned were then used to
draw conclusions fed back into reasoning about RS's actual behavior.
The matrix itself was legitimately integer-only; the analysis step was
not, and the boundary between "legitimate integer object" and
"external floating-point analysis" was not kept visible.

This module uses sympy for EXACT symbolic computation (integer
coefficients throughout, no floating point) wherever possible, and is
explicit in each function's docstring about exactly where floating
point becomes unavoidable (e.g. numerically isolating a root), so that
boundary is never implicit again.
"""

import sympy as sp


def characteristic_polynomial(matrix_of_ints, symbol_name='x'):
    """
    Given a matrix with plain-int or sympy-Integer entries (e.g. a
    monodromy matrix built purely from RS tick-matrices), returns its
    characteristic polynomial with EXACT integer coefficients. No
    floating point anywhere in this step.
    """
    x = sp.Symbol(symbol_name)
    M = sp.Matrix(matrix_of_ints)
    return sp.expand(M.charpoly(x).as_expr())


def has_repeated_root(polynomial_expr, symbol_name='x'):
    """
    Exact check via the discriminant (computed from integer polynomial
    coefficients only -- addition and multiplication, no floating
    point). Returns True if the polynomial has ANY repeated root
    somewhere in its full root set.

    IMPORTANT, confirmed this session: this does NOT tell you whether
    the DOMINANT (largest-magnitude) root is the repeated one, only
    that some pair of roots coincide somewhere. A nonzero-discriminant
    result is a clean negative (no repeated roots at all, anywhere).
    A zero-discriminant result requires further, harder work (dominant
    root isolation) before it says anything about long-term behavior.
    """
    x = sp.Symbol(symbol_name)
    disc = sp.discriminant(polynomial_expr, x)
    return disc == 0


def dominant_root_isolation_warning():
    """
    Isolating the DOMINANT root of a polynomial symbolically, and
    checking its specific multiplicity, is real, harder computer
    algebra than has been implemented in this toolkit so far -- it was
    identified as an open task, not solved. Do not assume
    has_repeated_root() alone answers questions about long-term
    dynamical stability; it does not.
    """
    raise NotImplementedError(
        "Dominant-root isolation was flagged as an open task, not implemented. "
        "Do not approximate this with floating-point eigendecomposition -- "
        "that is the exact mistake this module was built to prevent."
    )
