# RigbySpace: Review of Testing So Far, with Conceptual Map

This document reviews everything computationally tested in this session, tagged by confidence level, with the actual code included for each result, plus a visual map connecting tested behavior to candidate current-theory matches.

**Confidence tags used throughout:**
- **TESTED** — verified computationally, reproducible from the code shown
- **CONDITIONAL** — tested, but the result depends on specific parameters (not a blanket finding)
- **CONCEPT** — an untested resemblance to a current-theory phenomenon, offered as a candidate, not a claim
- **SPECULATION** — built on top of an untested concept; explicitly not falsifiable yet

---

## 1. Conceptual Map

![Conceptual Map](plots/conceptual_map.png)

This map is the honest current shape of things: two operators, their tested behaviors under various conditions, and — separately, visually distinguished — which current-theory concepts might match those behaviors, at what depth of speculation. The rejected/superseded box at the bottom is deliberately part of the same map: those results are equally real findings, just negative ones.

---

## 2. Operator Foundations (TESTED)

Four primitives were established as genuinely independent (not reducible to one another): $\eta$, $\boxplus$, $\oplus$, $\psi$. $\lambda$ was proven to be **not** independent — it's exactly $\oplus$ with a fixed operand:

```python
def lam(n, d): return (n+d, d)
def fractional(A, B):
    na,da = A; nb,db = B
    return (na*db + nb*da, da*db)

# lambda(n,d) == (n,d) (+) (1,1), proven symbolically and numerically, no reduction involved
```

$\psi$ was proven to be a pure permutation — no addition or multiplication occurs:

```python
def psi(A, B):
    na,da = A; nb,db = B
    return (db,na), (da,nb)
# Flattened output of psi((a,b),(c,d)) is exactly (d,a,b,c) -- a cyclic rotation of the input tuple.
# This is why psi^4 = identity is structural, not just empirically observed.
```

---

## 3. The Precession Mechanism (TESTED — strongest result of the session)

**Prediction, derived symbolically before any test was run:** for a construction that reverts every $k$ ticks, the attractor satisfies $R^{*2} = F_{k-2}/F_k$ (Fibonacci numbers), and embedding it in an 11-tick engine should produce a precession period of exactly $k$ cycles, since $\gcd(11,k)=1$ for every $k$ tested.

```python
def run_k_periodic(A0, A1, k, n_terms):
    seq = [A0, A1]
    for n in range(2, n_terms):
        if n % k == 0:
            seq.append(seq[n-2])          # revert: always exactly 2 ticks back
        else:
            seq.append(seq[n-1] + seq[n-2])  # combine via fractional addition
    return [seq[i]/seq[i-1] for i in range(1, len(seq))]
```

**Result: 7 of 7 exact matches, k=3 through k=9**, both for the predicted attractor value and the predicted precession period.

![Precession vs k](plots/precession_vs_k.png)

![sqrt2 and sqrt3 convergence](plots/convergence_sqrt2_sqrt3.png)

---

## 4. Mass-track vs Energy-track Behavior (TESTED, then corrected)

$\eta$ alone (no revert) converges to a single point, $\varphi$:

```python
def eta(pair):
    n,d = pair
    return (n+d, n)
# Repeated application from (1,1): value converges monotonically (with alternating-sign error) to phi.
```

**Robustness test (TESTED) — the result is conditional, not blanket:**

```python
def run_eta_revert(offset, k, n_terms):
    seq = [(1,1),(1,1)]
    for n in range(2, n_terms):
        if n % k == 0 and n-offset >= 0:
            seq.append(seq[n-offset])   # revert to a fixed distance back
        else:
            seq.append(eta(seq[-1]))
    return seq
```

At $k=3$: offsets 1 and 2 (less than the period) still converge to $\varphi$ despite the interruption. **Offset 3 (exactly equal to the period) breaks it — sustained 3-way oscillation results.** $\oplus$, tested the same way, showed no such resistance at any offset.

![eta vs oplus resonance](plots/eta_vs_oplus_resonance.png)

**This is why the finding is tagged CONDITIONAL, not TESTED-and-closed:** only $k=3$ has been checked across multiple offsets. Whether "breaks exactly at offset=k" generalizes to other $k$ is the next open test, not yet run.

---

## 5. Current-Theory Candidate Matches (CONCEPT and SPECULATION — none of these are claims)

**Resonance (CONCEPT, depth 1):** $\eta$ absorbing off-period perturbations but breaking exactly at exact-period matching is structurally the same shape as a driven oscillator resisting off-resonant driving and responding catastrophically at resonance. Strong because the *mechanism* matches, not just the appearance.

**Neutrino beat mechanism (CONCEPT, depth 1):** the precession itself is caused by a mismatch between two periods (11 and $k$) — structurally the same kind of mechanism (a beat between two periodicities) that causes real neutrino flavor oscillation (mismatched mass-eigenstate propagation rates), not just a shared involvement of the number three.

**Stable matter vs. oscillatory fields (CONDITIONAL, depth 2):** weaker on its own — needs the resonance framing underneath it to mean anything specific, since "settles vs. oscillates" alone is too generic a bar to be informative by itself.

**Three generations (SPECULATION, depth 3–4):** not yet falsifiable. The $k$-sweep confirmed the *mechanism* generalizes; it said nothing about whether real physical constants cluster into a small number of classes, since $k$ was freely chosen by us, not forced by anything in RS's actual architecture.

---

## 6. Rejected / Superseded (equally valuable findings)

- Mediant-addition "derives" cross-product multiplication — algebra did not hold under direct symbolic check.
- Rational Euler Cycle's claimed final state for register A — did not match what the stated operators actually produce.
- Ordinary Return as a $\psi$-collapse — alignment condition never occurs in the real sequence.
- Sommerfeld constant via continued fractions — violates the framework's own deprecation of continued fractions.
