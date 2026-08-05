"""
erp.py -- the ERP (Explicit Rational Pair) type.

This is the ONLY representation of an RS state anywhere in this toolkit.
Design rules, enforced structurally, not just by convention:

  1. Components must be plain Python `int`. Never float, Fraction, Decimal,
     numpy scalar, or sympy Rational -- all of those either carry a
     continuum representation or auto-reduce via gcd on construction.
  2. No operation on an ERP ever reduces it. There is no .simplify(),
     no .reduce(), no gcd() anywhere in this file, deliberately.
  3. Equality is EXACT componentwise equality. (3,6) != (1,2), even though
     they are the "same value" under reduction -- in RS they are different
     states with different histories, and conflating them is exactly the
     mistake this type exists to prevent.
  4. evaluate() is the ONLY sanctioned exit to a real number. It is for
     one-way comparison against a current-theory constant ONLY. Its
     return value is a bare float, not an ERP, and cannot be fed back in.
"""

class ERP:
    __slots__ = ('n', 'd')

    def __init__(self, n, d):
        if type(n) is not int or type(d) is not int:
            raise TypeError(
                f"ERP components must be plain int, got {type(n).__name__} and {type(d).__name__}. "
                f"Never construct an ERP from float, Fraction, Decimal, or a numpy/sympy scalar."
            )
        self.n = n
        self.d = d

    def __repr__(self):
        return f"ERP({self.n},{self.d})"

    def __eq__(self, other):
        # Exact componentwise equality ONLY. Never equality-after-reduction.
        if not isinstance(other, ERP):
            return NotImplemented
        return self.n == other.n and self.d == other.d

    def __hash__(self):
        return hash((self.n, self.d))

    def is_absence(self):
        """True if this is either mediant absence (0,0) or fractional absence (0,1)."""
        return (self.n, self.d) in ((0, 0), (0, 1))

    def evaluate(self):
        """
        The ONLY sanctioned exit point to a real number.
        Plain division -- never routes through Fraction/Rational, so gcd()
        is never invoked. Use this ONLY for one-way comparison against a
        current-theory value (e.g. checking closeness to sqrt(2) or phi).
        The result must never be wrapped back into an ERP.
        """
        return self.n / self.d  # rs-guard: allow: sole sanctioned exit point, one-way only


# Zero Logic constants -- see zero_logic.py for the resolution rule these feed into.
MEDIANT_ABSENCE = ERP(0, 0)
FRACTIONAL_ABSENCE = ERP(0, 1)
