# RigbySpace: Findings on η, λ, ⊞, ⊕ — Full Test Record

This document reports everything established in this testing session about the four candidate arithmetic operators: η (eta), λ (lambda), ⊞ (mediant addition), ⊕ (fractional addition). Every claim below is labeled as **PROVEN** (holds for all inputs, verified symbolically), **VERIFIED NUMERICALLY** (checked on specific example inputs, consistent with the general symbolic result), **EMPIRICALLY OBSERVED** (a pattern seen over a finite run, not proven for all cases), or **OPEN** (unresolved, stated as a question, not an answer).

---

## 1. The Four Operators as Defined

- **η (eta):** unary, single-ERP input.
  $$\eta(n,d) = (n+d,\ n)$$

- **λ (lambda):** unary, single-ERP input.
  $$\lambda(n,d) = (n+d,\ d)$$

- **⊞ (mediant addition / barycentric addition):** binary, two-ERP input.
  $$(n_1,d_1) \boxplus (n_2,d_2) = (n_1+n_2,\ d_1+d_2)$$
  Null state: $(0,0)$.

- **⊕ (fractional addition):** binary, two-ERP input.
  $$(n_1,d_1) \oplus (n_2,d_2) = (n_1 d_2 + n_2 d_1,\ d_1 d_2)$$
  Null state: $(0,1)$.

---

## 2. λ is Not Merely Similar to ⊕ — It Is Algebraically Identical to a Special Case of ⊕

**Claim tested:** is $\lambda(n,d)$ the same thing as applying $\oplus$ to $(n,d)$ with a fixed second operand?

**Method:** symbolic computation (sympy), treating $n,d$ as free symbolic variables, so the result holds for every possible input, not just examples.

**Result — PROVEN:**
$$\lambda(n,d) \;=\; (n,d) \oplus (1,1) \qquad \text{for all } n,d$$

Worked out explicitly:
$$(n,d)\oplus(1,1) = (n\cdot1 + 1\cdot d,\ d\cdot1) = (n+d,\ d) = \lambda(n,d)$$

Sympy confirmed this symbolically: both sides simplify to the identical expression $(d+n,\ d)$, with zero difference.

**VERIFIED NUMERICALLY** on four concrete pairs, chosen specifically to include cases with common factors (to stress-test the no-GCD requirement — see Section 5):

| $(n,d)$ | $\lambda(n,d)$ | $(n,d)\oplus(1,1)$ | Equal? |
|---|---|---|---|
| $(2,4)$ | $(6,4)$ | $(6,4)$ | Yes |
| $(6,3)$ | $(9,3)$ | $(9,3)$ | Yes |
| $(7,5)$ | $(12,5)$ | $(12,5)$ | Yes |
| $(9,9)$ | $(18,9)$ | $(18,9)$ | Yes |

**Conclusion:** $\lambda$ is not an independent primitive operator. It is exactly the operator $\oplus$ applied with the fixed second operand $(1,1)$.

---

## 3. η Cannot Be Reduced to Either ⊞ or ⊕ With Any Fixed Operand

**Claim tested:** is there some fixed constant pair $(a,b)$ such that $\eta(n,d) = (n,d)\oplus(a,b)$ for all $n,d$? Or such that $\eta(n,d) = (n,d)\boxplus(a,b)$ for all $n,d$?

**Method:** symbolic solve. Set up the equations that a fixed $(a,b)$ would have to satisfy to make the identity hold for every $n,d$ simultaneously, and asked sympy to solve for $(a,b)$.

**Result for ⊕ — NO FIXED SOLUTION EXISTS.**
Solving $\eta(n,d) = (n,d)\oplus(a,b)$ for $(a,b)$ gives:
$$a = \frac{d^2+dn-n^2}{d^2}, \qquad b = \frac{n}{d}$$
Both depend on $n$ and $d$. A valid fixed operand must be a constant, independent of $n,d$. Since the only "solution" varies with the input, **no fixed operand exists** — this is a proof of non-reducibility, not an inconclusive search.

**Result for ⊞ — NO FIXED SOLUTION EXISTS, and the near-solution requires a forbidden operation.**
Solving $\eta(n,d) = (n,d)\boxplus(a,b)$ for $(a,b)$ gives:
$$a = d, \qquad b = n - d$$
Again input-dependent, not fixed — so no constant operand works here either. Additionally worth noting explicitly: the expression $n-d$ requires **subtraction**, which is an operation RigbySpace forbids outright by axiom. So even setting aside the fact that this isn't a fixed constant, the expression that would be needed to make the identification work is itself an illegal operation under RS's own rules.

**Conclusion:** $\eta$ is a genuinely independent primitive. It cannot be expressed as "combine with a constant" the way $\lambda$ can.

---

## 4. Growth Rate, Measured Empirically Over 15 Iterations From Seed $(1,1)$

**Method:** iterate each operator 15 times starting from $(1,1)$, and record the numerator sequence.

**η numerator sequence (15 iterations):**
$$1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ 34,\ 55,\ 89,\ 144,\ 233,\ 377,\ 610,\ 987,\ 1597$$
(This is the Lucas sequence.)

**η successive ratios (last 5 shown):**
$$1.6181,\ 1.618,\ 1.618,\ 1.618,\ 1.618$$
This converges to the golden ratio $\varphi \approx 1.618$. A converging non-unit ratio is the signature of **exponential growth**.

**λ numerator sequence (15 iterations):**
$$1,\ 2,\ 3,\ 4,\ 5,\ 6,\ 7,\ 8,\ 9,\ 10,\ 11,\ 12,\ 13,\ 14,\ 15,\ 16$$

**λ successive differences (last 5 shown):**
$$1,\ 1,\ 1,\ 1,\ 1$$
A constant difference is the signature of **linear growth**, exactly — not approximately.

**EMPIRICALLY OBSERVED conclusion:** over the tested range, $\eta$ grows exponentially (ratio → $\varphi$), $\lambda$ grows linearly (constant first difference). This is the reverse of what was stated earlier in this conversation ("eta = linear, lambda = exponential") — that earlier statement was superseded and the person acknowledged it may have had the pairing backwards.

Note on scope: this is confirmed over 15 iterations from one seed. It is a very strong pattern (constant ratio to 4 decimal places for $\eta$, exactly constant difference for $\lambda$) and follows directly from the closed-form structure of each operator (η's recurrence is the same form as the Lucas/Fibonacci recurrence, which is proven elsewhere to converge to $\varphi$; λ's recurrence is a simple arithmetic progression by construction). It has not been re-derived as a general closed-form proof in this session.

---

## 5. The λ = ⊕(1,1) Identity Was Re-Checked Specifically Against the No-GCD-Ever Axiom

**Concern raised:** does the identity in Section 2 secretly rely on reducing a fraction (which RigbySpace forbids) to make the two sides match?

**Method:** re-ran the numeric check using input pairs that have common factors between numerator and denominator — $(2,4)$ [gcd 2], $(6,3)$ [gcd 3], $(9,9)$ [gcd 9] — specifically so that if reduction were happening anywhere, it would show up as a mismatch between the raw unreduced output and the claimed result.

**Result — PROVEN, axiom-compliant:**
In every case, $\lambda(n,d)$ and $(n,d)\oplus(1,1)$ matched **exactly, componentwise, with no reduction applied at any step** — e.g. for $(2,4)$, both sides give exactly $(6,4)$, gcd of 2 present and left untouched, not simplified to $(3,2)$.

**Conclusion:** the identity in Section 2 holds under the strict, unreduced definition of equality that No-GCD-Ever requires. It does not depend on, or secretly invoke, any reduction step.

---

## 6. Where the Fixed Operand $(1,1)$ Itself Comes From, Under Zero Logic

**Concern raised:** Zero Logic states no state initializes as $(1,1)$ — it's a reachable state, not a starting one. So is the operand $(1,1)$ used in Section 2 an illegitimate external constant?

**Method:** checked whether $(1,1)$ can be produced from fractional absence, $(0,1)$, using the operators already defined.

**Result — PROVEN:**
$$\lambda(0,1) = (0+1,\ 1) = (1,1)$$

**Conclusion:** $(1,1)$ is not an externally injected constant. It is exactly what you get from applying $\lambda$ once to fractional absence. The operand used in the Section 2 identity is itself the engine's own first emergent state, not a prop brought in from outside the system.

---

## 7. Summary Table

| Operator | Independent primitive? | Reduces to | Growth (empirical) |
|---|---|---|---|
| ⊕ (fractional) | Yes | — (base operator) | exponential-class (via λ) |
| ⊞ (mediant) | Yes | — (base operator) | not separately re-tested this session |
| λ | **No** — PROVEN identical to $\oplus(\cdot,(1,1))$ | ⊕, with fixed operand $(1,1)$ | **linear** |
| η | Yes — PROVEN not reducible to ⊞ or ⊕ with any fixed operand | — (independent primitive) | **exponential** ($\to\varphi$) |

---

## 8. Open Items Not Resolved by This Test Round

- Whether $\eta$ is reducible to $\boxplus$ or $\oplus$ using a *non-constant*, structurally-defined second operand (rather than a fixed constant) has not been tested. Section 3 only rules out fixed operands.
- Whether $\boxplus$'s own growth rate (independent of its relationship to $\eta$/$\lambda$) has been separately characterized — it was not re-tested in this session; the "linear growth" association with $\boxplus$ from earlier documents has not been independently re-verified here.
- Whether the golden-ratio convergence of $\eta$ has a general closed-form proof (as opposed to the strong 15-iteration empirical pattern shown here) was not re-derived in this session, though it follows the same form as the already-verified TRTS/Lucas convergence proofs from earlier documents.

---

## 9. Follow-up Test Round: Is ψ or ⊞ Reducible?

**Method:** flattened ψ's action on the raw four numbers a,b,c,d (from inputs A=(a,b), B=(c,d)) and compared to what a single application of η, ⊞, or ⊕ can ever produce.

**Result — PROVEN: ψ is a pure permutation, not an arithmetic operator.**
ψ(A,B) flattened = (d,a,b,c) — exactly a cyclic right-rotation by one position of the input tuple (a,b,c,d). No addition, no multiplication occurs. Verified symbolically: ψ's four output values are each a single bare input variable, untouched.

By contrast:
- η(A) = (a+b, a) — always a sum in one slot.
- ⊞(A,B) = (a+c, b+d) — always sums.
- ⊕(A,B) = (ad+bc, bd) — always sums-of-products.

None of these three can ever produce a bare, uncombined variable as output. Since ψ only ever produces bare variables (a relabeling, not a combination), **ψ cannot be built from any composition of η, ⊞, ⊕.** This is a stronger and more structural result than the η-vs-⊞/⊕ result in Section 3 (that one was "no fixed constant works"; this one is "categorically impossible, different kind of operation entirely").

**Consequence — PROVEN, not just re-confirmed empirically:** ψ⁴ = identity now has a structural reason: ψ is a 4-cycle rotation on a 4-slot tuple, and rotating 4 things by one position 4 times always returns to start. (Previously this was only checked case-by-case by hand; now it follows necessarily from the permutation structure itself.)

**Result — PROVEN: ⊞ (mediant) is also irreducible; it never equals ⊕ for generic inputs.**
⊞(A,B) = (a+c, b+d) vs ⊕(A,B) = (ad+bc, bd) — symbolically confirmed these are never equal for generic a,b,c,d.

**Unplanned finding, flagged as new and unexplained rather than interpreted:** conjugating ⊞ by ψ — i.e. computing ⊞(ψ(A,B)) — does NOT give ⊕(A,B). But it does give exactly the numerator/denominator flip of ⊞(A,B) directly:
- ⊞(A,B) = (a+c, b+d)
- ⊞(ψ(A,B)) = (b+d, a+c)  ← exactly the flip of the line above

So ψ does not convert mediant math into fractional math as originally speculated, but it does have an exact, verified relationship to ⊞ specifically: it inverts (flips) ⊞'s output. Meaning of this is currently unresolved — flagged as an open item, not a conclusion.

**Updated primitive count:** four confirmed independent primitives — η, ⊞, ⊕, ψ (ψ being a different KIND of primitive: permutation, not arithmetic). λ remains demoted — it is exactly ⊕ with fixed operand (1,1), proven in Section 2.

**New open item added:** what does "⊞ conjugated by ψ = flip of ⊞" mean structurally? Not yet investigated.

---

## 10. Koppa Mechanism: Graded Reduction Without Subtraction, and the Return-Tick Resolution

**Context:** earlier open question was how koppa gets a graded (non-collapse) tension value using only legal RS operations, since iterative subtraction (used to check the koppa signature table earlier in the session) is mechanically identical to division/modulus and is axiomatically banned. Also flagged: psi CAN produce a degenerate collapse-to-1 result under specific alignment conditions (koppa's numerator = microtick's denominator, or koppa's denominator = microtick's numerator) — verified symbolically and numerically — but that's a binary collapse/no-collapse outcome, not a graded remainder.

**New mechanism identified, tested against the original TRTS document (logandsqrttrts.pdf):**

The TRTS recurrence itself already contains a legal, non-subtractive reduction mechanism: at the revert tick, the rule does NOT sum the previous two terms — it discards the sum and simply carries forward the older term instead. Tested directly on the seeded sequence (A0=22/7, A1=7/19):

- At each revert tick n (n≡0 mod 3 in the paper's indexing), the actual kept value is A_(n-2), NOT A_(n-1)+A_(n-2).
- The amount excluded from propagation is exactly A_(n-1) — confirmed for four consecutive revert ticks (excluded values: 467/133, 565/133, 1597/133, 537/19).
- No subtraction occurs in the RS rule itself to produce this — it is pure SELECTION (choose the older value, skip the sum). A subtraction was used only in the diagnostic script to CONFIRM the excluded amount equals A_(n-1); this was an external check, not a claim that RS performs subtraction.
- Running the excluded amounts forward as a candidate koppa ledger (pure cumulative addition, no subtraction): 467/133 -> 1032/133 -> 2629/133 -> 6388/133. This is a real, monotonically growing, legally-constructed accumulator — a strong candidate for how koppa actually gets graded tension values, as opposed to the binary psi-collapse mechanism (Section 9) or the axiomatically-illegal iterative-subtraction method used earlier only as a numeric proxy check.

**Resolution of the E/M/R phase-labeling conflict:**

The TRTS paper's own phase-index formula (tick n=3t+s, role E if s=0, M if s=1, R if s=2) labels the revert tick as "E" (Emission). This directly conflicted with the engine-blueprint framing, where Return is supposed to be the special tick where ledgers must supply what propagation can't. User confirmed directly: **Return is the discarded-sum/revert tick.** The TRTS paper's own s=0/1/2 -> E/M/R labeling is therefore a labeling error in that document, not a real feature of the framework — the revert tick is Return, not Emission, regardless of how that older paper's formula indexes it.

**Physical picture, stated by user, connecting this back to the original wave/particle-duality thought experiment that produced the TRTS engine (documented in emrexplained.md):**

- Emission = the particle: expression of information at a point, no time elapses.
- Memory = the wave: transmission of information, no time elapses.
- Return = the mass-gap switch between the wave and particle states. This is the one place where an energetic cost is paid and where time/duration actually enters the structure.
- Analogy given: a radio signal weakening as it propagates/traverses distance. This lines up directly with the koppa-ledger finding above — the amount diverted into koppa at each Return is exactly the amount that would otherwise have continued propagating forward in the main chain, i.e., propagation "loses strength" to the ledger as it travels, tick after tick, the same shape as a signal attenuating over distance.

**Status:** this is a strong, structurally clean, axiom-compliant candidate mechanism for koppa's graded tension values. Not yet tested: whether this exact mechanism (excluded-sum-at-Return, accumulated additively) reproduces the specific koppa signature numbers already documented elsewhere in the corpus (e.g., the F_17=1597 signature table) — that would be the natural next verification step.

---

## 11. Decision Record: Scoping the Next Phase of Work

**Context:** after establishing the operator skeleton (Sections 1-10), the question of how to proceed was discussed. Two general approaches were considered: (a) map current theory's concepts broadly and check RS represents them; (b) run the engine with loose hypotheses and observe what falls out, ignoring primes for now.

**Objection raised and accepted:** running the engine "ignoring primes" past the point where a prime would have emerged is not a simplified/clean baseline — if prime emergence is a genuine branch point in propagation, everything computed past that point describes a hypothetical variant of the system that (per RS's own posited rules) doesn't actually happen. This was recognized as a valid structural objection, not just an expression of uncertainty. Revised approach: engine runs, when done, should be bounded strictly to the first prime emergence and stopped there, since everything before that point is valid regardless of what the branching rule turns out to be.

**Revised approach adopted:** concept-mapping against current theory is more useful when aimed at STRUCTURAL LOCATION (where/how/what kind of mechanism exists) rather than at NUMERIC VALUE (what number to match). The former does not invite curve-fitting; the latter is the same failure mode already identified elsewhere in the corpus (Sommerfeld, mass ratios). This reframing was accepted as the way forward, in place of a blanket rejection of concept-mapping.

**Decision: start narrow.** Rather than building a large concept map across all of current theory, or attempting a large engine-behavior exploration, the first concrete bite chosen is:

> Where and how does an irrational constant arise in the specific physics of wave/particle duality and the mass gap — the same physical story (documented in emrexplained.md) that originally produced the Emission/Memory/Return structure and the TRTS engine.

**Reasoning for this specific scope:** this question sits at the intersection of three things already independently established in this conversation: (1) the TRTS convergence proof (barycentric oscillation producing an irrational attractor from rational dynamics), (2) the Return-tick/mass-gap resolution (Section 10), and (3) the unresolved open question of which barycentric "limit" couples to which microtick. A structural finding here has an immediate place to plug into, rather than existing as an isolated fact. It is deliberately NOT scoped as "map all of current theory to RS" — that broader task remains explicitly parked, to be used only as passive background reference, not as an active fitting target.

**Explicit ground rule going forward:** proceed slowly, one bounded question at a time, and document each choice and its reasoning at the point the choice is made, rather than after the fact.
