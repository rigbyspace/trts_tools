"""
zero_logic.py -- absence, not zero, and constraint-vacuum resolution.

There is no zero in RS, only absence: MEDIANT_ABSENCE = ERP(0,0) or
FRACTIONAL_ABSENCE = ERP(0,1), chosen by which kind of math governs that
line of propagation. No state initializes at ERP(1,1) -- it is a
reachable state (e.g. eta(FRACTIONAL_ABSENCE) == ERP(1,1)), never a
starting one.

A "constraint vacuum" is an ERP with d==0 (e.g. ERP(n, 0)) -- a
suspended state. Confirmed this session: psi's ordinary formula ALREADY
resolves this correctly with no special-casing needed --
psi(ERP(n,0), ERP(c,d)) == (ERP(d,n), ERP(0,c)) falls straight out of
the general psi formula. This module exists to make that fact explicit
and documented, and to provide a named constructor for suspended states
so callers don't need to remember the bare mechanics.

IMPORTANT: ERP.evaluate() will raise ZeroDivisionError on a suspended
state (d==0). This is intentional, not a bug to work around -- a
suspended state should never be evaluated; it should be resolved via
psi first.
"""

from .erp import ERP, MEDIANT_ABSENCE, FRACTIONAL_ABSENCE
from .operators import psi


def suspended(n: int) -> ERP:
    """Construct a constraint-vacuum / suspended state: ERP(n, 0)."""
    return ERP(n, 0)


def resolve_suspended(suspended_erp: ERP, other: ERP):
    """
    Resolve a suspended state (d==0) by coupling it with another ERP via
    psi. Returns the same (a_new, b_new) pair psi() always returns --
    this function adds no new mechanics, it just documents that this is
    the sanctioned way to resolve a suspended state, and checks the
    precondition explicitly rather than silently accepting any input.
    """
    if suspended_erp.d != 0:
        raise ValueError(
            f"{suspended_erp} is not a suspended state (d != 0). "
            f"resolve_suspended() is specifically for constraint-vacuum states."
        )
    return psi(suspended_erp, other)
