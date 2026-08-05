"""
primality.py -- sign-preserving primality detection.

Design requirement (explicit, from development discussion): sign is
structurally important in RS and must never be discarded. A negative
prime (e.g. -7) counts as a prime event exactly the same as a positive
one (magnitude is what matters for primality) -- but the value itself
must remain -7 afterward, never silently flipped to +7.

This means: do NOT use abs() anywhere here. abs() is itself a banned
continuum-adjacent operation, and more importantly, reaching for it
invites the exact bug this module exists to prevent -- a temporary
"unsigned magnitude" variable accidentally leaking out and replacing
the signed original somewhere downstream.

is_prime_magnitude() is a META/ANALYSIS utility, in the same category
as ERP.evaluate() -- it is a detection tool that looks at a value to
recognize a structural event (matching the framework's own account of
prime emergence as something the structure recognizes, not something
it computes via trial division). It is not a claim that RS itself
performs modulo arithmetic internally. It returns a bare bool and
never returns or constructs a modified (sign-stripped) copy of the
input.
"""

def _magnitude(n: int) -> int:
    """Magnitude without abs(). Comparison + multiplication only."""
    if type(n) is not int:
        raise TypeError(f"expected int, got {type(n).__name__}")
    return n if n >= 0 else n * (-1)


def is_prime_magnitude(n: int) -> bool:
    """
    True if |n| is prime. Sign of n is read, never altered or discarded --
    the caller's original signed n is completely untouched by this call.
    -7 and 7 both return True here; the ERP holding -7 still holds -7.
    """
    m = _magnitude(n)
    if m < 2:
        return False
    if m in (2, 3):
        return True
    if m % 2 == 0:  # rs-guard: allow: external analysis (primality detection), not RS propagation
        return False
    i = 3
    while i * i <= m:
        if m % i == 0:  # rs-guard: allow: external analysis (primality detection), not RS propagation
            return False
        i += 2
    return True


def sign_of(n: int) -> int:
    """
    Returns -1, 0, or 1. Provided so callers never need to reach for a
    workaround that risks discarding sign information (e.g. computing
    n // abs(n) or similar). Comparison only, no division.
    """
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0
