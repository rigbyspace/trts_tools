"""
barycentric_oscillation_upsilon_beta.py

TWO ASSUMPTIONS MADE HERE, STATED EXPLICITLY (neither was pinned down in
conversation, both are my calls, not yours):

1. WHICH MECHANISM. "Barycentric" is formally defined in
   rs_operator_findings.md Section 1 as the operator ⊞ (mediant addition /
   boxplus). But ⊞ has no established attractor of its own -- Section 8
   explicitly flags its growth/convergence behavior as "not re-tested this
   session." The only mechanism in the corpus with THREE confirmed
   attractors to "cycle through" is the TRTS convergence proof (Section 10,
   tested directly against logandsqrttrts.pdf), which is built on ⊕
   (oplus, ordinary fractional addition), NOT ⊞. Since "three attractors
   cycling" only matches the ⊕ mechanism, that's what this script builds.
   If you actually meant ⊞'s own (currently unestablished) oscillatory
   behavior, this script does not show that -- it would need to be derived
   and tested from scratch.

2. WHICH REGISTER IS WHICH. upsilon (Y) is the n-2 slot (older term), beta
   (B) is the n-1 slot (newer term, always one tick ahead of upsilon) --
   matching the paper's A_{n-2}/A_{n-1} roles and this toolkit's
   seed_prev2/seed_prev1 convention (engine.py). Swap if you meant it the
   other way.

Rule (matches logandsqrttrts.pdf exactly, revert-every-3):
    at a revert tick (n % 3 == 0): new_term = upsilon        (discard the sum)
    otherwise:                     new_term = oplus(beta, upsilon)
  then shift forward: upsilon <- beta, beta <- new_term

Attractors -- and a real conflict found INSIDE logandsqrttrts.pdf itself
while building this, worth flagging to whoever maintains that document:

The paper's Proof section (3.1) derives, via the 3-iterate map
F(R)=(R+1)/(2R+1) and Banach fixed-point theorem: R_{3k} -> 1/sqrt2, then
R_{3k+1} = 1+1/R_{3k} -> 1+sqrt2, then R_{3k+2} -> sqrt2. The paper's own
appendix code (mod_index logic) computes the SAME mapping. But the paper's
narrative Table 1 labels R_1 as expecting 1/sqrt2 -- which contradicts both
the proof and the paper's own code (R_1 has n%3==1, which the proof/code
say should expect 1+sqrt2). Verified numerically here (independent of any
label, run against this exact seed/rule): n%3==1 converges to ~2.414
(1+sqrt2), n%3==2 to ~1.414 (sqrt2), n%3==0 to ~0.707 (1/sqrt2) -- matching
the proof and the code, not Table 1. The mapping below follows the proof
and the code.
    R_n -> 1 + sqrt(2) when n % 3 == 1
    R_n -> sqrt(2)     when n % 3 == 2
    R_n -> 1/sqrt(2)   when n % 3 == 0
  where R_n = A_n / A_{n-1} = beta.evaluate() / upsilon.evaluate() at tick n.

PART 1 -- pure RS propagation: builds the entire upsilon/beta sequence
using ONLY ERP construction and oplus. No float, no math module, no
.evaluate() call anywhere in this part.

PART 2 -- evaluated at each step: re-walks the EXACT SAME states already
built in Part 1 (not recomputed differently) and calls .evaluate() -- the
one sanctioned exit point -- to show the ratio beta/upsilon at each tick
converging on the attractor predicted for that tick's phase. This is an
equivalence check: the same integers, looked at two ways.
"""

import math
from rs_toolkit import ERP, oplus

# External comparison targets ONLY -- sqrt() builds a target to compare
# against, exactly as logandsqrttrts.pdf's own Table 1 does. Never fed back
# into propagation; Part 1 never touches this.
SQRT2 = math.sqrt(2)
ATTRACTOR_BY_PHASE = {
    1: 1 + SQRT2,     # R_{3k+1} -> 1+sqrt2 (proof + paper's own code; NOT Table 1's label)
    2: SQRT2,         # R_{3k+2} -> sqrt2
    0: 1 / SQRT2,     # rs-guard: allow: external comparison target only, matches evaluate() # R_{3k}   -> 1/sqrt2
}
PHASE_LABEL = {1: "1+sqrt2", 2: "sqrt2", 0: "1/sqrt2"}


# ---------------------------------------------------------------------
# PART 1 -- pure RS propagation
# ---------------------------------------------------------------------

def propagate_pure(seed_upsilon: ERP, seed_beta: ERP, n_ticks: int):
    """
    Builds the upsilon/beta history purely: ERP construction and oplus
    only. Returns a list of (tick, upsilon, beta, phase, is_revert) --
    the STATE at each tick. Nothing here is a float.

    Uses TickCounter (tick_counter.py) rather than raw `n % 3` --
    formalizes the same mod-free bookkeeping pattern the rest of this
    toolkit uses, rather than reintroducing % locally.
    """
    from rs_toolkit import TickCounter
    upsilon, beta = seed_upsilon, seed_beta
    history = [(1, upsilon, beta, 1, False)]  # tick 1 = the seed pair itself

    counter = TickCounter(3)
    counter.advance()  # move from representing tick 1 to tick 2

    for n in range(2, n_ticks + 1):
        is_revert = counter.is_at_boundary()
        if is_revert:
            new_term = upsilon                 # discard the sum, carry n-2 forward
        else:
            new_term = oplus(beta, upsilon)     # exact fractional addition
        upsilon, beta = beta, new_term
        history.append((n, upsilon, beta, counter.position, is_revert))
        counter.advance()

    return history


def show_pure_propagation(history):
    print("PART 1 -- pure RS propagation (ERP + oplus only, no floats anywhere)")
    header = f"{'tick':>4}  {'phase':>5}  {'revert?':>7}  {'upsilon (Y)':>26}  {'beta (B)':>26}"
    print(header)
    print("-" * len(header))
    for n, upsilon, beta, phase, is_revert in history:
        flag = "REVERT" if is_revert else ""
        print(f"{n:>4}  {phase:>5}  {flag:>7}  "
              f"{f'ERP({upsilon.n},{upsilon.d})':>26}  {f'ERP({beta.n},{beta.d})':>26}")
    print()


# ---------------------------------------------------------------------
# PART 2 -- evaluated at each step, to show equivalence with Part 1
# ---------------------------------------------------------------------

def show_evaluated_equivalence(history):
    """
    Re-walks the SAME (upsilon, beta) states from Part 1 and evaluates
    them -- the one sanctioned exit point -- to confirm the exact integer
    propagation above actually converges to the three attractors it's
    supposed to, phase by phase.
    """
    print("PART 2 -- evaluated at each step (equivalence check against Part 1)")
    header = f"{'tick':>4}  {'phase':>5}  {'expected':>10}  {'beta/upsilon':>16}  {'|diff|':>12}"
    print(header)
    print("-" * len(header))
    for n, upsilon, beta, phase, is_revert in history:
        ratio = beta.evaluate() / upsilon.evaluate()  # rs-guard: allow: sanctioned one-way exit only
        expected = ATTRACTOR_BY_PHASE[phase]
        diff = abs(ratio - expected)  # rs-guard: allow: external diagnostic diff between two evaluated floats
        print(f"{n:>4}  {phase:>5}  {PHASE_LABEL[phase]:>10}  {ratio:>16.10f}  {diff:>12.2e}")
    print()


if __name__ == "__main__":
    seed_upsilon = ERP(22, 7)   # matches logandsqrttrts.pdf's A0 = 22/7
    seed_beta = ERP(7, 19)      # matches logandsqrttrts.pdf's A1 = 7/19
    n_ticks = 24

    history = propagate_pure(seed_upsilon, seed_beta, n_ticks)
    show_pure_propagation(history)
    show_evaluated_equivalence(history)
