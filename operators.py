"""
operators.py -- the four verified-independent RS primitives.

Every function here uses ONLY +, * on plain Python ints. No -, no /, no **
(except the explicitly-permitted square/cube shorthand, unused here), no gcd.

Confirmed this session:
  - eta, boxplus, oplus, psi are genuinely independent (none reduces to another).
  - lambda is NOT independent -- it is exactly oplus(x, ERP(1,1)). It is
    deliberately NOT given its own function here, to avoid the toolkit
    implying it is a fifth primitive. Use oplus(x, ERP(1,1)) directly if
    lambda's behavior is needed, so the derivation stays visible at the
    call site.
  - psi is a pure permutation: it only ever rearranges its four input
    integers, never combines them arithmetically. This is why psi**4
    is structurally the identity, not just empirically observed.
"""

from .erp import ERP


def eta(a: ERP) -> ERP:
    """Mass-track native operator. Undriven, converges to phi. Proven NOT
    reducible to boxplus or oplus with any fixed operand."""
    return ERP(a.n + a.d, a.n)


def boxplus(a: ERP, b: ERP) -> ERP:
    """Mediant addition. Null element: ERP(0,0). Denominators only ADD --
    this is why it grows linearly under repetition, unlike oplus."""
    return ERP(a.n + b.n, a.d + b.d)


def oplus(a: ERP, b: ERP) -> ERP:
    """Fractional addition. Null element: ERP(0,1). Denominators MULTIPLY --
    this is the source of the double-exponential blowup found this session
    when used as a combine step without a compensating mechanism."""
    return ERP(a.n * b.d + b.n * a.d, a.d * b.d)


def psi(a: ERP, b: ERP):
    """
    The Transformative Reciprocal. Pure permutation -- proven to only
    rearrange (a.n, a.d, b.n, b.d) into (b.d, a.n, a.d, b.n), never combine
    them. Returns a PAIR of ERPs (a_new, b_new). Neither output is
    privileged; which one a caller keeps and which is discarded is a
    modeling decision made at the call site, not by this function.

    A bare tuple return made it easy to silently pick the wrong slot --
    confirmed this session, picking [1] instead of [0] in one config
    produced a 2000x difference in growth outcome. Prefer the named
    wrappers below so the choice is visible and intentional at the call
    site rather than an easily-mistaken index.
    """
    return ERP(b.d, a.n), ERP(a.d, b.n)


def psi_advance_a(a: ERP, b: ERP) -> ERP:
    """psi(a,b), keeping only the new 'a' line. Explicit about which
    output is being propagated forward -- see psi()'s docstring."""
    return psi(a, b)[0]


def psi_advance_b(a: ERP, b: ERP) -> ERP:
    """psi(a,b), keeping only the new 'b' line. Explicit about which
    output is being propagated forward -- see psi()'s docstring."""
    return psi(a, b)[1]
