"""
precession.py -- the k-periodic TRTS mechanism, formalized.

This is this session's strongest tested result (7 of 7 exact predictions,
k=3 through k=9) and it was never actually added to the toolkit -- every
test script rewrote it from scratch. This module fixes that.

The mechanism: revert every k ticks (carry the value from 2 ticks back,
discard the sum), combine via oplus otherwise. Confirmed: this converges
to R* where R*^2 = F(k-2)/F(k) (Fibonacci numbers), and embedding it in
an 11-tick engine produces a precession period of exactly k cycles
whenever gcd(11,k)=1.

sqrt() is used ONLY to build a comparison target for evaluate(), exactly
matching the original TRTS paper's own discipline -- never in the
generative rule itself.
"""

import math
from .erp import ERP
from .operators import oplus
from .tick_counter import TickCounter


def fibonacci(m: int) -> int:
    a, b = 0, 1
    for _ in range(m):
        a, b = b, a + b
    return a


def predicted_attractor(k: int) -> float:
    """
    Comparison-target ONLY -- this is the evaluate()-adjacent external
    check, computed via ordinary floats, never fed into propagation.
    R*^2 = F(k-2)/F(k), so R* = sqrt(F(k-2)/F(k)).
    """
    if k < 3:
        raise ValueError("k must be >= 3 for this construction")
    ratio = fibonacci(k - 2) / fibonacci(k)  # rs-guard: allow: external comparison target only, matches evaluate()
    return math.sqrt(ratio)   # rs-guard: allow: external comparison target only, matches evaluate()


def run_k_periodic(seed0: ERP, seed1: ERP, k: int, n_terms: int):
    """
    Generates the k-periodic TRTS sequence as a list of ERPs, using a
    TickCounter (not %) to track cyclic position -- formalizing the
    original TRTS paper's rational_index_tracker pattern.
    """
    seq = [seed0, seed1]
    counter = TickCounter(k)
    counter.advance()  # move from representing n=0 to n=1
    counter.advance()  # move from representing n=1 to n=2
    for n in range(2, n_terms):
        if counter.is_at_boundary():
            seq.append(seq[n - 2])  # rs-guard: allow: list-index bookkeeping, not ERP arithmetic
        else:
            seq.append(oplus(seq[n - 1], seq[n - 2]))  # rs-guard: allow: list-index bookkeeping, not ERP arithmetic
        counter.advance()  # move to represent n+1 for the next iteration
    return seq


def precession_period(k: int) -> int:
    """
    Predicted precession period when this construction is embedded in
    an 11-tick engine: exactly k, whenever gcd(11,k)=1 (true for every
    k tested this session, since 11 is prime).
    """
    g = math.gcd(11, k)  # rs-guard: allow: external structural analysis, not ERP arithmetic
    if g != 1:
        raise NotImplementedError(f"gcd(11,{k})={g} != 1 -- untested regime, not covered by this session's results")
    return k
