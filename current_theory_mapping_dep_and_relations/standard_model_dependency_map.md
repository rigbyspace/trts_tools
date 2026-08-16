# STANDARD MODEL — DEPENDENCY AND RELATIONSHIP MAP

## 0. Purpose, Scope, and Governing Method

This document constructs an explicit dependency and relationship graph for the minimal renormalizable Standard Model (SM) of particle physics. It is not a pedagogical textbook summary and it is not a numerical parameter table. Its primary object is the structure of the theory: what mathematical objects, fields, symmetries, operators, constraints, representations, and observables depend on one another; what assumptions make each relationship valid; what information is preserved or lost; and where the dependency network terminates at an unresolved, model-dependent, formulation-dependent, or empirically supplied boundary.

The structural object is a typed directed graph with explicit feedback and constraint edges rather than a simple directed acyclic graph. Acyclic construction paths coexist with equivalence, constraint, correspondence, and feedback relationships.

The graph is restricted to the minimal renormalizable Standard Model with gauge group

\[
G_{SM}=SU(3)_C\times SU(2)_L\times U(1)_Y,
\]

three fermion generations, one complex Higgs doublet, no right-handed neutrinos, and the conventional electric-charge normalization

\[
Q=T_3+\frac{Y}{2}.
\]

The minimal Standard Model therefore contains massless neutrinos. Observed neutrino masses and lepton mixing are treated as an explicit boundary where the minimal SM must be extended, rather than silently incorporated into the minimal model. The current Particle Data Group review explicitly states this limitation. [1,4]

The numerical values of masses, couplings, mixing parameters, widths, and other measured quantities belong in a separate Standard Model numerical addendum and are not inserted into this structural map.

### 0.1 Governing Questions

Every important node and edge is evaluated by the following questions:

1. **What is it?** — ontology and node class.
2. **What does it require?** — direct prerequisites and assumptions.
3. **What does it generate or constrain?** — forward dependency.
4. **What information is preserved or lost?** — recoverability.
5. **What changes if an upstream premise changes?** — perturbation propagation.
6. **What is its epistemic status?** — definition, derivation, conditional construction, approximation, empirical input, or unresolved boundary.

### 0.2 Scope Boundary

Included:

- gauge-group structure;
- gauge and matter representations;
- anomaly cancellation;
- field content;
- renormalizable gauge-invariant Lagrangian;
- QCD sector;
- electroweak sector;
- Higgs potential and electroweak symmetry breaking;
- gauge-boson mixing and physical electroweak fields;
- fermion Yukawa structure;
- fermion mass generation;
- CKM flavor mixing and CP violation;
- accidental global symmetries of the renormalizable minimal theory;
- quantization, gauge fixing, ghosts, and BRST structure;
- renormalization and renormalization-group dependencies;
- spectral, scattering, decay, and precision-observable paths;
- perturbation propagation and feedback;
- parameter counting and structural dependence;
- explicit unresolved boundaries of the minimal SM.

Excluded as internal SM structure:

- neutrino masses and PMNS mixing;
- gravity and quantum gravity;
- dark matter candidates not present in the minimal SM;
- a dynamical explanation of the Higgs potential parameters;
- a theory explaining the SM gauge group or representation assignments;
- numerical parameter values, which belong to a separate numerical addendum;
- speculative beyond-Standard-Model mechanisms.

---

# 1. Graph Ontology

## 1.1 Node Classes

| Class | Meaning |
|---|---|
| OBJECT | Mathematical or physical entity such as a field, tensor, parameter, or state. |
| GROUP | Gauge or global symmetry group. |
| REPRESENTATION | Representation assignment of a field under a symmetry group. |
| OPERATOR | Differential, algebraic, or functional operator. |
| EQUATION | Dynamical or definitional equation. |
| IDENTITY | Mathematical identity such as a Bianchi or Jacobi identity. |
| CONSTRAINT | Restriction on allowed configurations, states, or parameters. |
| TRANSFORMATION | Gauge, global, flavor, or field-space transformation. |
| REPRESENTATION-MAP | Transformation between equivalent descriptions or bases. |
| OBSERVABLE | Quantity connected to experiment or measurement. |
| PARAMETER | Free or externally determined theory parameter. |
| APPROXIMATION | Controlled approximation to an exact or formal structure. |
| BOUNDARY | Point where the declared theory terminates, becomes conditional, or requires extension. |

## 1.2 Relationship Classes

| Relationship | Meaning |
|---|---|
| DEFINITION | Target is defined from source data. |
| CONSTRUCTION | Target is constructed from source under stated assumptions. |
| DERIVATION | Target follows mathematically from source and prerequisites. |
| CONSTRAINT | Source restricts target. |
| SPECIALIZATION | Target is a restricted case of source structure. |
| REPRESENTATION | Target is another representation of the same underlying content. |
| EQUIVALENCE | Two descriptions yield the same physical content under stated conditions. |
| GENERATION | Source produces target through a dynamical mechanism. |
| BREAKING | Target structure appears after symmetry or phase structure changes. |
| MIXING | Source basis and target basis are related by a nontrivial transformation. |
| RENORMALIZATION | Bare and renormalized quantities are related by regulator-removal and parameter redefinition. |
| RG-FLOW | Scale changes propagate through running parameters or operators. |
| CORRESPONDENCE | Different formalisms compute or represent the same quantity. |
| OBSERVABLE-LINK | Formal quantity propagates to an experimentally accessible quantity. |
| FEEDBACK | A dependency path returns to an upstream node. |
| BOUNDARY | A path reaches a declared limit of the model or mathematical construction. |

## 1.3 Edge Grammar

A structural edge is represented as

\[
A\xrightarrow[\text{preconditions}]{\text{relationship}}B.
\]

Each edge is evaluated for:

- mathematical bridge;
- required assumptions;
- directionality;
- reversibility;
- information preservation/loss;
- local/nonlocal character;
- exact/formal/perturbative/approximate status;
- gauge dependence;
- representation/basis dependence;
- model dependence;
- observable consequence;
- epistemic status.

## 1.4 Information and Recoverability Classes

| Class | Meaning |
|---|---|
| BIJECTIVE | Source and target determine one another under the stated domain. |
| CONDITIONALLY-REVERSIBLE | Reverse reconstruction requires additional declared data. |
| MANY-TO-ONE | Target discards distinctions in source. |
| ONE-WAY-CONSTRUCTIVE | Target can be constructed from source but not generally reconstructed. |
| REPRESENTATIONAL | Physical content is preserved while mathematical representation changes. |
| CONSTRAINING | Target restricts source rather than encoding all of it. |

## 1.5 Epistemic Ordering

The map distinguishes:

\[
\text{Definitional}
\rightarrow
\text{Derived}
\rightarrow
\text{Conditional}
\rightarrow
\text{Perturbative/Approximate}
\rightarrow
\text{Formal}
\rightarrow
\text{Unresolved}.
\]

Empirical support is recorded separately because experimental support does not convert a mathematical relation into a definition.

---

# 2. MODULE 1 — GAUGE GROUP, SPACETIME, AND FIELD PRIMITIVES

## 2.1 Node Definitions

**N1.1:** Minkowski spacetime \(M\)

Four-dimensional flat spacetime with metric \(\eta_{\mu\nu}\), used as the Standard Model background.

- Class: OBJECT.
- Status: Structural assumption of the conventional SM formulation.

**N1.2:** Spacetime metric \(\eta_{\mu\nu}\)

Defines Lorentzian causal and contraction structure.

- Class: OBJECT.
- Status: Supplied background structure.

**N1.3:** Poincaré symmetry \(ISO(1,3)\)

Translations and Lorentz transformations preserving \(\eta_{\mu\nu}\).

- Class: GROUP.
- Status: Conditional on Minkowski background.

**N1.4:** Standard Model gauge group

\[
G_{SM}=SU(3)_C\times SU(2)_L\times U(1)_Y.
\]

- Class: GROUP.
- Status: Model-defining input.

**N1.5:** Color group \(SU(3)_C\)

Acts on color-charged fields.

**N1.6:** Weak-isospin group \(SU(2)_L\)

Acts nontrivially on left-handed weak doublets and the Higgs doublet.

**N1.7:** Hypercharge group \(U(1)_Y\)

Acts through hypercharge \(Y\).

**N1.8:** Electric-charge generator \(Q\)

\[
Q=T_3+\frac{Y}{2}.
\]

This definition becomes the unbroken electromagnetic generator after electroweak symmetry breaking.

**N1.9:** Gauge couplings \(g_s,g_2,g_1\)

Couplings associated with \(SU(3)_C\), \(SU(2)_L\), and \(U(1)_Y\), respectively.

**N1.10:** Matter representations

For each generation, in the conventional right-handed-field notation and with \(Q=T_3+Y/2\):

\[
Q_L^i\sim(3,2)_{1/3},\quad
U_R^i\sim(3,1)_{4/3},\quad
D_R^i\sim(3,1)_{-2/3},
\]

\[
L_L^i\sim(1,2)_{-1},\quad
E_R^i\sim(1,1)_{-2},\quad
\nu_R^i\text{ absent}.
\]

The Higgs doublet is

\[
H\sim(1,2)_1.
\]

The minimal Standard Model contains no right-handed neutrino field. This field-content choice is essential to the statement that the minimal renormalizable SM has massless neutrinos. [1,4]

**N1.11:** Three fermion generations \(i=1,2,3\)

The minimal SM contains three sequential generations.

**N1.12:** Higgs doublet \(H\)

\[
H\sim(1,2)_1.
\]

Class: OBJECT/REPRESENTATION.

## 2.2 Relationship Table — Module 1

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Recoverability | Exact/Approx | Gauge/Basis Dependence | Observable Consequence | Epistemic Status |
|---|---|---|---|---|---|---|---|---|---|---|
| N1.2 Metric | N1.3 Poincaré | Definition | Isometries of \(\eta_{\mu\nu}\) | Minkowski spacetime | Uni | Conditionally-reversible | Exact | Coordinate representation dependent | Lorentz-covariant kinematics | Derived |
| N1.4 Gauge group | N1.5–N1.7 factors | Factorization | Direct product structure | SM definition | Uni | Bijective | Exact | Group-basis dependent | Distinct interactions | Definitional |
| N1.4 Gauge group | N1.9 Gauge couplings | Association | One coupling per simple gauge factor | Renormalizable gauge theory | Uni | One-way-constructive | Exact | Convention dependent | Interaction strengths | Definitional |
| N1.4 Gauge group | N1.10 Matter representations | Representation assignment | Field maps under group factors | Chosen SM content | Uni | Many-to-one | Exact | Basis/normalization dependent | Charges and interactions | Definitional |
| N1.10 Representations | N1.8 Electric charge | Generator relation | \(Q=T_3+Y/2\) after EW decomposition | Hypercharge normalization | Uni | Conditioned | Exact | Convention dependent | Electric charges | Definitional |
| N1.11 Generations | N1.10 Representations | Replication | Three copies of fermion representations | Experimental SM family count | Uni | Replicative | Exact within model | Flavor-basis dependent | Flavor structure | Model-dependent |
| N1.12 Higgs | N1.4 Gauge group | Compatibility | \(H\) transforms under \(SU(2)_L\times U(1)_Y\) | Gauge representation | Uni | One-way | Exact | Gauge-basis dependent | EWSB | Definitional |

## 2.3 Module 1 Synthesis

The minimal SM begins with a specified gauge group, field content, representation assignment, and flat-spacetime structure. The gauge group and representations are not derived internally by the minimal SM; they are model-defining inputs.

The representation assignments determine allowed covariant derivatives and gauge interactions. Hypercharge assignments, together with \(SU(2)_L\) generators, determine electric charge through the eventual unbroken generator \(Q=T_3+Y/2\).

The three-generation structure is replicated across the fermion representations and creates the flavor sector that later develops Yukawa matrices, mass eigenstates, CKM mixing, and CP violation.

## 2.4 Critical Dependency Test

Removing the gauge group removes the gauge-connection structure and therefore the gauge interactions. Removing the representation assignments leaves no rule for how the matter fields couple to the gauge fields. Removing the Higgs representation changes the allowed renormalizable Yukawa structure and electroweak symmetry-breaking mechanism.

---

# 3. MODULE 2 — GAUGE CONNECTIONS AND COVARIANT DERIVATIVES

## 3.1 Node Definitions

**N2.1:** Gauge fields

\[
G_\mu^A,
\quad
W_\mu^a,
\quad
B_\mu.
\]

Indices are \(A=1,\ldots,8\), \(a=1,2,3\).

**N2.2:** Gauge connections

The gauge fields form the connection associated with the product gauge group.

**N2.3:** Covariant derivative

For a field \(\Phi\),

\[
D_\mu=\partial_\mu-ig_s G_\mu^A T^A-ig_2 W_\mu^a t^a-ig_1\frac{Y}{2}B_\mu,
\]

with the appropriate generators acting according to the representation of \(\Phi\).

**N2.4:** Non-Abelian field strengths

\[
G^A_{\mu\nu}
=
\partial_\mu G^A_\nu-\partial_\nu G^A_\mu
+g_s f^{ABC}G^B_\mu G^C_\nu,
\]

\[
W^a_{\mu\nu}
=
\partial_\mu W^a_\nu-\partial_\nu W^a_\mu
+g_2\epsilon^{abc}W^b_\mu W^c_\nu.
\]

**N2.5:** Abelian field strength

\[
B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu.
\]

## 3.2 Relationship Table — Module 2

| Source | Target | Relationship | Mathematical Bridge | Required Assumptions | Recoverability | Status |
|---|---|---|---|---|---|---|
| N1.4 Gauge group | N2.1 Gauge fields | Connection assignment | Lie-algebra-valued one-form | Gauge theory | Conditionally-reversible | Definitional |
| N1.10 Representation | N2.3 Covariant derivative | Representation action | Generators act on field space | Representation specified | Bijective within representation | Definitional |
| N2.1 Gauge fields | N2.4 Non-Abelian strengths | Differential construction | \(F=dA+gA\wedge A\) | Non-Abelian group | One-way | Exact | Derived |
| N2.1 Gauge fields | N2.5 Abelian strength | Differential construction | \(F=dA\) | U(1) factor | One-way | Exact | Derived |
| N2.3 Covariant derivative | N2.4/N2.5 strengths | Commutator | \([D_\mu,D_\nu]\propto F_{\mu\nu}\) | Representation | Conditionally-reversible | Exact | Derived |

## 3.3 Module 2 Synthesis

The gauge group plus representation assignments determine the admissible gauge connections and covariant derivatives. The field strengths are the curvature of these connections. The non-Abelian commutator term is a structural consequence of the noncommutativity of the corresponding Lie algebra.

---

# 4. MODULE 3 — THE RENORMALIZABLE STANDARD MODEL LAGRANGIAN

## 4.1 Node Definitions

**N3.1:** Gauge kinetic Lagrangian

\[
\mathcal L_{\rm gauge}
=-\frac14G^A_{\mu\nu}G^{A\mu\nu}
-\frac14W^a_{\mu\nu}W^{a\mu\nu}
-\frac14B_{\mu\nu}B^{\mu\nu}.
\]

**N3.2:** Fermion kinetic Lagrangian

\[
\mathcal L_{\rm fermion}
=
\sum_f \bar f i\gamma^\mu D_\mu f.
\]

**N3.3:** Higgs kinetic term

\[
\mathcal L_H=(D_\mu H)^\dagger(D^\mu H).
\]

**N3.4:** Higgs potential

\[
V(H)= -\mu^2 H^\dagger H+\lambda(H^\dagger H)^2,
\qquad
\lambda>0.
\]

**N3.5:** Yukawa Lagrangian

\[
\mathcal L_Y
=-\bar Q_L Y_d H D_R
-\bar Q_L Y_u \widetilde H U_R
-\bar L_L Y_e H E_R
+\mathrm{h.c.},
\]

where

\[
\widetilde H=i\sigma_2 H^*.
\]

There is no renormalizable neutrino Yukawa term in the minimal SM because \(\nu_R\) is absent.

**N3.6:** QCD \(\theta\)-term

\[
\mathcal L_\theta
=\theta_{\rm QCD}\frac{g_s^2}{32\pi^2}G^A_{\mu\nu}\widetilde G^{A\mu\nu}.
\]

**N3.7:** Full renormalizable SM Lagrangian

\[
\mathcal L_{SM}
=
\mathcal L_{\rm gauge}
+\mathcal L_{\rm fermion}
+\mathcal L_H
- V(H)
+\mathcal L_Y
+\mathcal L_\theta.
\]

The Yukawa, gauge, and Higgs structures are fixed by gauge invariance and renormalizability once the field content and representations are chosen. The three gauge couplings, Yukawa parameters, Higgs-sector parameters, and \(\theta_{\rm QCD}\) constitute the free parameter content of the minimal model in the conventional counting. [2]

## 4.2 Relationship Table — Module 3

| Source | Target | Relationship | Bridge | Assumptions | Information | Status |
|---|---|---|---|---|---|---|
| N2.4/N2.5 strengths | N3.1 Gauge kinetic | Invariant contraction | \(F_{\mu\nu}F^{\mu\nu}\) | Lorentz + gauge invariance | Loss of orientation sign but gauge invariant | Definitional |
| N2.3 Covariant derivative | N3.2 Fermion kinetic | Minimal coupling | \(\bar\psi i\gamma^\mu D_\mu\psi\) | Representation | One-way | Exact | Derived |
| N2.3 | N3.3 Higgs kinetic | Minimal coupling | \((D H)^\dagger(DH)\) | Higgs representation | One-way | Exact | Definitional |
| N1.12 Higgs representation | N3.4 Potential | Gauge invariant renormalizable scalar operators | \(H^\dagger H\), \((H^\dagger H)^2\) | Renormalizability | One-way | Exact | Derived |
| N1.10 Fermion representations | N3.5 Yukawa | Gauge-singlet contractions | Hypercharge cancellation | Representation assignments | Strongly constraining | Exact | Derived |
| N2.4 QCD field strength | N3.6 \(\theta\)-term | Topological density | \(G\widetilde G\) | Non-Abelian SU(3) | One-way | Exact | Definitional |
| N3.1–N3.6 | N3.7 Full Lagrangian | Sum of allowed sectors | Direct assembly | Model assumptions | Preserves sector decomposition | Exact | Definitional |

## 4.3 Module 3 Synthesis

The Standard Model Lagrangian is not an arbitrary list of interaction terms. The dependency chain is

\[
\text{gauge group}
\rightarrow
\text{representations}
\rightarrow
D_\mu,F_{\mu\nu}
\rightarrow
\text{gauge-invariant renormalizable operators}
\rightarrow
\mathcal L_{SM}.
\]

The Yukawa sector is constrained by gauge invariance. The absence of \(\nu_R\) forbids the corresponding renormalizable neutrino Yukawa term. The Higgs potential is the unique renormalizable polynomial in the single gauge-invariant scalar bilinear \(H^\dagger H\) up to its coefficients.

---

# 5. MODULE 4 — ANOMALY CANCELLATION

## 5.1 Node Definitions

**N4.1:** Gauge anomaly

A quantum violation of gauge-current conservation that makes the gauge theory inconsistent if uncanceled.

**N4.2:** Cubic non-Abelian anomaly coefficients.

**N4.3:** Mixed gauge anomalies.

**N4.4:** Gravitational-hypercharge anomaly.

**N4.5:** Anomaly-cancellation conditions.

The SM fermion representations satisfy the required perturbative gauge-anomaly cancellation conditions generation by generation when expressed in a consistent all-left-handed convention.

## 5.2 Relationship Table — Module 4

| Source | Target | Relationship | Bridge | Consequence | Status |
|---|---|---|---|---|---|
| N1.10 Representations | N4.1 Gauge anomaly | Triangle diagrams | Group-theory traces | Potential inconsistency | Derived |
| N1.10 | N4.2–N4.4 anomaly coefficients | Trace construction | \(\mathrm{Tr}[T^a\{T^b,T^c\}]\), mixed traces | Consistency constraints | Derived |
| N4.2–N4.4 | N4.5 cancellation | Sum of representations | Vanishing anomaly coefficients | Quantum gauge consistency | Derived |
| N4.5 cancellation | N3.7 \(\mathcal L_{SM}\) | Consistency filter | No anomalous gauge symmetry | Valid quantization | Constraint |

## 5.3 Module 4 Synthesis

Anomaly cancellation is not an optional correction. It is a consistency filter on the allowed fermion representation content. If the gauge anomalies do not cancel, the BRST/gauge structure does not define a consistent quantum gauge theory.

The cancellation conditions constrain the representation content without uniquely deriving the entire Standard Model gauge group or three-generation pattern.

---

# 6. MODULE 5 — QCD SECTOR

## 6.1 Node Definitions

**N5.1:** Color gauge symmetry \(SU(3)_C\).

**N5.2:** Gluon fields \(G_\mu^A\), \(A=1,\ldots,8\).

**N5.3:** Quark color representations \(3\).

**N5.4:** QCD field strength \(G^A_{\mu\nu}\).

**N5.5:** Strong coupling \(g_s\).

**N5.6:** QCD beta function \(\beta_s(g_s)\).

**N5.7:** Asymptotic freedom.

At leading order, for the SM with six active quark flavors,

\[
\beta_{g_s}
=
-\frac{g_s^3}{16\pi^2}\left(11-\frac{2}{3}n_f\right)+\cdots.
\]

The negative leading coefficient produces asymptotic freedom for the relevant flavor range.

**N5.8:** Confinement boundary.

The minimal perturbative field description does not supply a closed analytic derivation of nonperturbative confinement from first principles.

## 6.2 Relationship Table — Module 5

| Source | Target | Relationship | Bridge | Required Conditions | Status |
|---|---|---|---|---|---|
| N1.5 \(SU(3)_C\) | N5.2 Gluons | Adjoint connection | 8 generators | SU(3) Lie algebra | Definitional |
| N1.10 Quarks | N5.3 Color reps | Fundamental representation | Triplet action | Gauge assignment | Definitional |
| N5.2 | N5.4 Field strength | Curvature | \(F=dA+gA\wedge A\) | Non-Abelian SU(3) | Derived |
| N5.5 | N5.6 Beta function | Quantum renormalization | Loop coefficient | Renormalization | Derived/perturbative |
| N5.6 | N5.7 Asymptotic freedom | Sign of leading beta coefficient | \(\beta_s<0\) | Perturbative regime | Derived |
| N5.7 | High-energy behavior | Weak coupling | \(g_s(\mu)\downarrow\) as \(\mu\uparrow\) | RG | Derived |
| QCD degrees of freedom | N5.8 Confinement boundary | Nonperturbative transition | Strong coupling/IR physics | No closed perturbative derivation | Unresolved |

## 6.3 Module 5 Synthesis

The QCD branch is structurally complete at the level of its local renormalizable Lagrangian and perturbative gauge dynamics, but the path from perturbative gluon/quark fields to the complete nonperturbative hadron spectrum contains unresolved mathematical and dynamical structure.

This distinction is essential: confinement is not treated as a definition of SU(3) gauge theory, nor as a direct consequence of the tree-level Lagrangian alone.

---

# 7. MODULE 6 — ELECTROWEAK GAUGE STRUCTURE

## 7.1 Node Definitions

**N6.1:** \(SU(2)_L\times U(1)_Y\) gauge sector.

**N6.2:** Weak gauge fields \(W^1_\mu,W^2_\mu,W^3_\mu\).

**N6.3:** Hypercharge field \(B_\mu\).

**N6.4:** Higgs representation \((1,2)_1\).

**N6.5:** Weak mixing angle \(\theta_W\).

**N6.6:** Electromagnetic coupling relation

\[
e=g_2\sin\theta_W=g_1\cos\theta_W
\]

in the normalization where \(Q=T_3+Y/2\) and \(g_1\) denotes the U(1) coupling in that convention.

**N6.7:** Physical gauge fields

\[
W^\pm_\mu
=\frac{W^1_\mu\mp iW^2_\mu}{\sqrt2},
\]

\[
A_\mu=B_\mu\cos\theta_W+W^3_\mu\sin\theta_W,
\]

\[
Z_\mu=-B_\mu\sin\theta_W+W^3_\mu\cos\theta_W.
\]

The photon corresponds to the unbroken electromagnetic U(1) generator.

## 7.2 Relationship Table — Module 6

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| N6.2 \(W^1,W^2\) | N6.7 \(W^\pm\) | Complex basis transformation | Linear combination | Definitional |
| N6.2 \(W^3\), N6.3 \(B\) | N6.7 \(A,Z\) | Orthogonal field rotation | \(\theta_W\) rotation | Definitional |
| N1.8 \(Q\) | N6.7 Photon | Unbroken generator | \(Q=T_3+Y/2\) | Derived after EWSB |
| N6.5 \(\theta_W\) | N6.6 \(e\) | Coupling matching | \(e=g_2s_W=g_1c_W\) | Derived |
| N6.4 Higgs rep | N6.7 physical fields | Symmetry-breaking compatibility | Higgs VEV preserves U(1)EM | Conditional |

---

# 8. MODULE 7 — HIGGS POTENTIAL AND ELECTROWEAK SYMMETRY BREAKING

## 8.1 Node Definitions

**N7.1:** Higgs doublet

\[
H=\begin{pmatrix}H^+\\H^0\end{pmatrix}.
\]

**N7.2:** Higgs potential

\[
V(H)=-\mu^2H^\dagger H+\lambda(H^\dagger H)^2.
\]

**N7.3:** Vacuum expectation value

For \(\mu^2>0\) and \(\lambda>0\), the minimum satisfies

\[
\langle H\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}0\\v\end{pmatrix},
\qquad
v^2=\frac{\mu^2}{\lambda}
\]

at tree level in this convention.

**N7.4:** Symmetry-breaking pattern

\[
SU(2)_L\times U(1)_Y
\rightarrow
U(1)_{EM}.
\]

**N7.5:** Goldstone directions.

Three scalar directions become gauge-sector longitudinal degrees of freedom.

**N7.6:** Physical Higgs scalar \(H\) or \(h\), depending on notation.

**N7.7:** Gauge-boson masses

\[
m_W=\frac12g_2v,
\qquad
m_Z=\frac12v\sqrt{g_2^2+g_1^2},
\]

and therefore

\[
\frac{m_W}{m_Z}=\cos\theta_W
\]

at tree level.

**N7.8:** Higgs mass

\[
m_h^2=2\lambda v^2
\]

at tree level.

## 8.2 Relationship Table — Module 7

| Source | Target | Relationship | Mathematical Bridge | Information | Status |
|---|---|---|---|---|---|
| N7.2 Potential | N7.3 VEV | Minimization | \(\partial V/\partial H=0\) | One vacuum choice among gauge-equivalent configurations | Derived |
| N7.3 VEV | N7.4 Symmetry breaking | Stabilizer subgroup | VEV invariant under U(1)EM | Conditional | Derived |
| N7.3 | N7.5 Goldstone directions | Tangent-space decomposition | Broken generators acting on vacuum | Conditionally reversible | Derived |
| N7.5 | N6.7 \(W,Z\) | Higgs mechanism | Goldstone modes supply longitudinal components | Physical DOF preserved globally | Derived |
| N7.3 + N6.2/N6.3 | N7.7 Gauge masses | Quadratic terms from \((DH)^\dagger DH\) | Tree-level EWSB | Exact at tree level | Derived |
| N7.3 + N7.2 | N7.8 Higgs mass | Curvature of potential | \(V''\) at vacuum | Exact at tree level | Derived |
| N7.4 | N6.7 Photon | Unbroken generator | U(1)EM | Photon remains massless at tree level | Derived |

## 8.3 Module 7 Synthesis

Electroweak symmetry breaking is the central convergence point of the electroweak branch:

\[
H\text{ potential}
\rightarrow
\langle H\rangle
\rightarrow
SU(2)_L\times U(1)_Y\to U(1)_{EM}
\]

and simultaneously

\[
\langle H\rangle
\rightarrow
m_W,m_Z,m_h.
\]

The gauge boson masses and the Higgs mass are therefore downstream quantities; they are not independent structural primitives.

The numerical value of \(v\), the Higgs mass, or the couplings belongs to the separate numerical layer.

---

# 9. MODULE 8 — YUKAWA STRUCTURE AND FERMION MASSES

## 9.1 Node Definitions

**N8.1:** Yukawa matrices \(Y_u,Y_d,Y_e\).

**N8.2:** Higgs VEV \(v\).

**N8.3:** Fermion mass matrices

\[
M_u=\frac{v}{\sqrt2}Y_u,
\qquad
M_d=\frac{v}{\sqrt2}Y_d,
\qquad
M_e=\frac{v}{\sqrt2}Y_e.
\]

**N8.4:** Biunitary diagonalization

\[
U_{uL}^\dagger M_uU_{uR}=D_u,
\qquad
U_{dL}^\dagger M_dU_{dR}=D_d,
\]

and similarly for charged leptons.

**N8.5:** CKM matrix

\[
V_{CKM}=U_{uL}^\dagger U_{dL}.
\]

**N8.6:** Yukawa-Higgs couplings

In the mass basis, the diagonal Yukawa couplings are proportional to fermion masses divided by \(v\).

**N8.7:** No renormalizable neutrino mass matrix in the minimal SM.

## 9.2 Relationship Table — Module 8

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| N3.5 Yukawa Lagrangian | N8.1 Yukawa matrices | Parameterization | Flavor-space matrices | Definitional |
| N8.1 + N8.2 | N8.3 Mass matrices | EWSB generation | \(M=Yv/\sqrt2\) | Derived |
| N8.3 | N8.4 Mass eigenstates | Singular-value decomposition | Biunitary diagonalization | Derived |
| N8.4 up/down rotations | N8.5 CKM | Basis mismatch | \(V=U_{uL}^\dagger U_{dL}\) | Derived |
| N8.3 | N8.6 Higgs couplings | Same Yukawa operator after EWSB | \(m_f/v\) | Derived |
| N1.10 absence of \(\nu_R\) | N8.7 no neutrino mass | No renormalizable Yukawa contraction | Minimal field content | Derived |

## 9.3 Module 8 Synthesis

Flavor structure follows the sequence

\[
Y_{u,d,e}
\rightarrow
M_{u,d,e}
\rightarrow
\text{mass-basis rotations}
\rightarrow
V_{CKM}
\rightarrow
\text{flavor-changing charged currents and CP violation}.
\]

The CKM matrix is therefore not an independent addition to the gauge theory. It is a derived mismatch between the left-handed diagonalizations of the up- and down-type quark mass matrices.

Because the minimal SM contains no right-handed neutrinos and no alternative renormalizable neutrino-mass operator, neutrino masses lie outside the minimal model. [4]

---

# 10. MODULE 9 — FLAVOR, CP, AND ACCIDENTAL GLOBAL SYMMETRIES

## 10.1 Node Definitions

**N9.1:** Flavor-basis transformations.

Unitary rotations of fermion multiplets that leave gauge kinetic terms invariant.

**N9.2:** Yukawa flavor breaking.

The Yukawa matrices break the large flavor symmetry of the fermion kinetic sector.

**N9.3:** CKM unitarity

\[
V_{CKM}V_{CKM}^\dagger=I.
\]

**N9.4:** CP-violating phase

For three generations, one irreducible CKM phase remains after allowed field rephasings.

**N9.5:** Jarlskog invariant.

A basis-invariant measure of CKM CP violation.

**N9.6:** Accidental global symmetries.

At the renormalizable level with the minimal field content, baryon number and separate lepton-family symmetries appear accidentally at the classical level, subject to quantum anomalies and nonperturbative electroweak effects.

**N9.7:** Sphaleron/nonperturbative electroweak violation of \(B+L\).

Perturbatively conserved \(B+L\) is violated by electroweak topology, while \(B-L\) remains conserved within the minimal SM.

## 10.2 Relationship Table — Module 9

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| N3.2 kinetic terms | N9.1 flavor basis symmetry | Degenerate kinetic structure | Unitary flavor rotations | Derived |
| N9.1 | N8.1 Yukawa matrices | Explicit symmetry breaking | Yukawa spurions/matrices | Derived |
| N8.4 rotations | N9.3 CKM unitarity | Unitary products | \(V^\dagger V=I\) | Exact |
| N8.5 | N9.4 CP phase | Rephasing-invariant residue | Three generations | Conditional |
| N9.4 | N9.5 CP invariant | Basis-independent construction | Jarlskog determinant/invariant | Derived |
| N4 anomaly structure | N9.6/9.7 global currents | Quantum violation | Triangle/topological effects | Derived |
| N9.7 | Baryon/lepton observables | Selection rules | \(\Delta(B+L)\neq0\) nonperturbatively | Conditional |

---

# 11. MODULE 10 — QUANTIZATION, GAUGE FIXING, AND BRST

## 11.1 Node Definitions

**N10.1:** Classical gauge redundancy.

**N10.2:** Gauge fixing condition \(F[A]=0\).

**N10.3:** Faddeev–Popov operator.

**N10.4:** Ghost fields \(c,\bar c\).

**N10.5:** Gauge-fixed action.

**N10.6:** BRST transformation \(s\).

**N10.7:** BRST charge \(Q_B\).

**N10.8:** Physical state cohomology

\[
\mathcal H_{phys}=\ker Q_B/\operatorname{im}Q_B.
\]

## 11.2 Relationship Table — Module 10

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| N10.1 | N10.2 | Gauge redundancy removal | Gauge choice | Conditional |
| N10.2 | N10.3 | Functional derivative | FP operator | Derived/formal |
| N10.3 | N10.4 | Determinant representation | Grassmann integral | Formal |
| N10.2–N10.4 | N10.5 | Gauge-fixed construction | FP/ghost terms | Formal |
| N10.5 | N10.6 | Global fermionic symmetry | BRST differential | Derived |
| N10.6 | N10.7 | Noether construction | BRST current/charge | Formal |
| N10.7 | N10.8 | Cohomological projection | BRST cohomology | Conditional |
| N10.8 | Observables | Physical-state restriction | Gauge-independent quantities | Derived/conditional |

## 11.3 Module 10 Synthesis

The gauge-fixed quantum theory is not the same mathematical object as the classical gauge-redundant description. Gauge fixing changes the representation while BRST structure preserves the physical content when the quantization is consistent.

The graph therefore treats gauge fixing as a representation transformation and BRST cohomology as a physical-state filter rather than as a new physical interaction.

---

# 12. MODULE 11 — RENORMALIZATION AND RENORMALIZATION-GROUP STRUCTURE

## 12.1 Node Definitions

**N11.1:** Bare parameters \(g_{a,0}\).

**N11.2:** Renormalized parameters \(g_a(\mu)\).

**N11.3:** Counterterms.

**N11.4:** Renormalization constants \(Z_i\).

**N11.5:** Beta functions \(\beta_a(g)\).

**N11.6:** Anomalous dimensions \(\gamma_i\).

**N11.7:** Running couplings.

**N11.8:** RG flow.

**N11.9:** Renormalization-scheme dependence.

**N11.10:** Physical observable invariance.

## 12.2 Relationship Table — Module 11

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| Loop graphs | N11.1 Bare quantities | Divergent contributions | Regularized amplitudes | Formal |
| N11.1 | N11.2 | Renormalization | \(g_0=\mu^d Z_g g(\mu)\) | Definitional |
| N11.3/N11.4 | N11.2 | Counterterm cancellation | Renormalized finite quantities | Perturbative |
| N11.2/N11.4 | N11.5 | Differential RG relation | \(\beta=\mu dg/d\mu\) | Derived |
| N11.4 | N11.6 | Field/operator scaling | \(\gamma=\mu d\ln Z/d\mu\) | Derived |
| N11.5 | N11.7 | Differential flow | \(dg/d\ln\mu=\beta(g)\) | Derived |
| N11.7 | N11.8 | Integrated flow | RG trajectory | Derived |
| N11.8 | N11.9 | Coordinate/scheme representation | Scheme changes | Conditional |
| N11.9 | N11.10 | Cancellation of unphysical dependence | Physical observables unchanged under consistent scheme transformations | Exact in exact theory |

## 12.3 Module 11 Synthesis

The renormalization graph introduces scale as a representational and dynamical organizing parameter:

\[
\text{bare theory}
\rightarrow
\text{renormalization}
\rightarrow
\text{running parameters}
\rightarrow
\text{RG flow}
\rightarrow
\text{scale-dependent intermediate quantities}
\rightarrow
\text{scale-independent observables}.
\]

The numerical value of a running coupling is incomplete without its scale and renormalization convention. This is why numerical entries are maintained outside the structural map.

---

# 13. MODULE 12 — SPECTRAL, SCATTERING, AND OBSERVABLE STRUCTURE

## 13.1 Node Definitions

**N12.1:** Correlation functions.

**N12.2:** Propagators.

**N12.3:** Spectral densities.

**N12.4:** Particle poles.

**N12.5:** Asymptotic states.

**N12.6:** LSZ reduction.

**N12.7:** Scattering amplitude \(\mathcal M\).

**N12.8:** Phase-space measure.

**N12.9:** Cross-section \(\sigma\).

**N12.10:** Decay width \(\Gamma\).

**N12.11:** Branching fractions.

**N12.12:** Precision electroweak observables.

## 13.2 Relationship Table — Module 12

| Source | Target | Relationship | Bridge | Status |
|---|---|---|---|---|
| SM action | Correlators | Functional/canonical quantization | \(Z[J]\), operator formalism | Formal/conditional |
| Correlators | Spectral density | Spectral decomposition | Källén–Lehmann where applicable | Conditional |
| Spectral density | Pole | Isolated state | Pole residue/mass | Conditional |
| Correlators | LSZ | Amputation/on-shell limit | Stable asymptotic states | Conditional |
| LSZ | \(\mathcal M\) | Reduction | On-shell amplitude | Conditional |
| \(\mathcal M\) | \(\sigma\) | Phase-space integration | \(|\mathcal M|^2d\Phi\) | Derived |
| \(\mathcal M\) | \(\Gamma\) | Decay phase space | \(|\mathcal M|^2d\Phi\) | Derived |
| \(\Gamma_i\) | Branching ratio | Normalization | \(Br_i=\Gamma_i/\Gamma_{tot}\) | Derived |
| Renormalized SM parameters | Precision observables | Radiative prediction | Loop corrections and running | Perturbative/derived |
| Observables | Parameter constraints | Statistical inference | Fits/global likelihoods | Empirical/inferred |

## 13.3 Observable Backbone

The principal observable routes are

\[
\boxed{
\text{SM parameters}
\rightarrow
\mathcal L_{SM}
\rightarrow
\text{correlators/amplitudes}
\rightarrow
\mathcal M
\rightarrow
\sigma,\Gamma,\text{precision observables}
}
\]

and

\[
\boxed{
G_F,\alpha,M_Z,\ldots
\rightarrow
\text{electroweak radiative corrections}
\rightarrow
W/Z/H\text{ predictions and precision tests}
}.
\]

---

# 14. MODULE 13 — PARAMETER DEPENDENCY GRAPH

## 14.1 Minimal SM Parameter Classes

The conventional minimal SM parameter content is grouped as follows:

### Gauge sector

\[
g_s,
\quad g_2,
\quad g_1.
\]

### Higgs sector

\[
\mu^2,
\quad \lambda.
\]

### Yukawa/flavor sector

The three complex Yukawa matrices \(Y_u,Y_d,Y_e\), reduced by flavor-basis transformations to the physical fermion masses and CKM parameters.

### Strong CP sector

\[
\theta_{QCD}.
\]

The conventional total count is 19 independent parameters for the minimal SM with massless neutrinos, before adding neutrino-mass parameters of extensions. [2]

## 14.2 Dependency Compression

The physical parameter space can be represented schematically as

\[
\{g_s,g_2,g_1,\mu^2,\lambda,Y_u,Y_d,Y_e,\theta_{QCD}\}
\]

\[
\downarrow
\]

\[
\{m_f,m_W,m_Z,m_h,\theta_W,e,V_{CKM},\theta_{QCD},\ldots\}
\]

subject to basis redundancies and conventional parameter choices.

The graph must not treat the entries in the first line and second line as interchangeable numerical constants. The second layer contains derived or basis-reduced physical parameterizations.

## 14.3 Parameter-to-Observable Paths

| Parameter | Primary downstream structures | Representative observables |
|---|---|---|
| \(g_s\) | gluon vertices, QCD RG, hadronic amplitudes | jets, scaling violations, hadronic rates |
| \(g_2,g_1\) | weak/electromagnetic mixing, gauge masses, vertices | \(W,Z\) properties, precision EW |
| \(\mu^2\) | Higgs vacuum structure | EWSB scale and derived masses |
| \(\lambda\) | Higgs mass and self-interactions | Higgs mass, self-coupling observables |
| \(Y_u\) | up-type masses and Higgs couplings | quark masses, Higgs decays/production |
| \(Y_d\) | down-type masses, CKM mismatch | flavor transitions, Higgs couplings |
| \(Y_e\) | charged-lepton masses/couplings | lepton masses, Higgs decay rates |
| \(V_{CKM}\) | charged-current flavor transitions | meson decays, CP violation |
| \(\theta_{QCD}\) | strong-CP observables | neutron EDM bounds and related constraints |

---

# 15. MODULE 14 — CONTROLLED PERTURBATION MAPPING

## 15.1 Governing Perturbation Operation

For any parameter or source \(p\), define

\[
p\rightarrow p+\delta p.
\]

The graph then traces

\[
\delta p
\rightarrow
\text{directly dependent nodes}
\rightarrow
\text{indirect dependencies}
\rightarrow
\text{constraints}
\rightarrow
\text{feedback}
\rightarrow
\delta\mathcal O.
\]

## 15.2 Perturbation Target: Strong Coupling

\[
\delta g_s
\rightarrow
\delta\beta_s
\rightarrow
\delta g_s(\mu)
\rightarrow
\delta\Sigma,\delta\mathcal M
\rightarrow
\delta\sigma.
\]

At nonperturbative scales the path encounters confinement and hadronization structure that is not captured by a finite-order perturbative expansion.

## 15.3 Perturbation Target: Higgs Potential

\[
\delta\mu^2,\delta\lambda
\rightarrow
\delta V(H)
\rightarrow
\delta v
\rightarrow
\delta m_W,\delta m_Z,\delta m_h
\rightarrow
\delta\text{Higgs/weak observables}.
\]

The dependence is nonlinear because the vacuum is determined by minimization of the effective potential, not simply the tree-level potential once radiative corrections are included.

## 15.4 Perturbation Target: Yukawa Matrix

\[
\delta Y_f
\rightarrow
\delta M_f
\rightarrow
\delta m_f,\delta U_{fL,R}
\rightarrow
\delta V_{CKM}
\rightarrow
\delta\mathcal M_{flavor}
\rightarrow
\delta\mathcal O.
\]

The response is matrix-valued and basis-dependent before physical observables are formed.

## 15.5 Perturbation Target: Gauge-Fixing Parameter

\[
\delta\xi
\rightarrow
\delta G_{\mu\nu}^{(\xi)},\delta\text{ghost terms},\delta\text{off-shell amplitudes}
\rightarrow
\text{cancellation in physical observables}.
\]

The physical observable is gauge-parameter independent when the calculation is consistently defined.

## 15.6 Perturbation Target: Renormalization Scale

\[
\delta\mu
\rightarrow
\delta g_a(\mu),\delta Y_f(\mu),\delta m(\mu)
\rightarrow
\delta\text{intermediate predictions}
\rightarrow
0\text{ exact response of physical observables}.
\]

At finite perturbative order a residual scale dependence remains and serves as a truncation diagnostic rather than a physical effect.

---

# 16. MODULE 15 — FEEDBACK AND SELF-CONSISTENCY STRUCTURE

## 16.1 Loop F1 — RG Feedback

\[
\mu
\rightarrow
g(\mu)
\rightarrow
\beta(g)
\rightarrow
\frac{dg}{d\ln\mu}
\rightarrow
g(\mu).
\]

Type: Differential feedback.

## 16.2 Loop F2 — Self-Energy Feedback

\[
g
\rightarrow
\Sigma(p^2)
\rightarrow
m_{phys}
\rightarrow
\Sigma(m_{phys}^2).
\]

Type: Algebraic/self-consistent feedback.

## 16.3 Loop F3 — Effective-Potential Feedback

\[
\phi_c
\rightarrow
\Gamma[\phi_c]
\rightarrow
V_{eff}(\phi_c)
\rightarrow
\phi_c.
\]

Type: Functional self-consistency.

## 16.4 Loop F4 — Flavor/Radiative Feedback

\[
Y_f
\rightarrow
\text{RG evolution}
\rightarrow
Y_f(\mu)
\rightarrow
\text{masses/couplings}
\rightarrow
\text{loop corrections}
\rightarrow
Y_f(\mu).
\]

Type: Renormalization-mediated feedback.

## 16.5 Loop F5 — Gauge-Parameter Cancellation

\[
\xi
\rightarrow
\text{gauge-dependent intermediate quantities}
\rightarrow
\text{Ward/Slavnov-Taylor/BRST constraints}
\rightarrow
\text{gauge-independent observables}.
\]

This is a cancellation/constraint loop rather than a dynamical feedback loop.

---

# 17. MODULE 16 — GLOBAL DEPENDENCY GRAPH

## 17.1 Structural Backbone

\[
\boxed{
M,\eta_{\mu\nu}
}
\rightarrow
\boxed{
SU(3)_C\times SU(2)_L\times U(1)_Y
}
\]

\[
\downarrow
\]

\boxed{\text{Representations + field content}}
\]

\[
\downarrow
\]

\boxed{D_\mu,F_{\mu\nu}}
\]

\[
\downarrow
\]

\boxed{\mathcal L_{SM}}
\]

with three major branches:

\[
\mathcal L_{SM}
\rightarrow
\text{QCD}
\rightarrow
\text{RG/asymptotic freedom}
\rightarrow
\text{high-energy QCD predictions}
\]

\[
\mathcal L_{SM}
\rightarrow
\text{Higgs potential}
\rightarrow
\text{EWSB}
\rightarrow
W,Z,\gamma,H
\]

\[
\mathcal L_{SM}
\rightarrow
\text{Yukawa sector}
\rightarrow
\text{fermion masses}
\rightarrow
\text{CKM}
\rightarrow
\text{flavor/CP observables}.
\]

These converge through quantization, renormalization, amplitudes, and observables.

## 17.2 Direct Dependency Chains

| Chain ID | Source | Intermediate Nodes | Target | Status |
|---|---|---|---|---|
| D1 | Gauge group | representations | gauge-invariant field content | Definitional |
| D2 | Representations | covariant derivative | gauge interactions | Derived |
| D3 | Gauge connections | field strengths | gauge kinetic terms | Derived |
| D4 | Higgs potential | VEV | EWSB | Conditional |
| D5 | EWSB | field mixing | photon, W, Z | Derived |
| D6 | EWSB | mass matrices | fermion masses | Derived |
| D7 | Yukawa matrices | mass-basis rotations | CKM | Derived |
| D8 | Renormalized parameters | RG equations | running parameters | Derived/perturbative |
| D9 | Correlators | LSZ | amplitudes | Conditional |
| D10 | Amplitudes | phase space | cross-sections/widths | Derived |
| D11 | Representations | anomaly traces | anomaly cancellation | Constraint |
| D12 | Quantum gauge theory | BRST cohomology | physical-state sector | Conditional |

## 17.3 Indirect Dependency Chains

| Chain ID | Perturbation | Intermediate Dependencies | Terminal Observable | Epistemic Status |
|---|---|---|---|---|
| I1 | \(\delta g_s\) | \(\beta_s\to g_s(\mu)\to\mathcal M\) | QCD cross-sections | Perturbative |
| I2 | \(\delta\lambda\) | \(V_{eff}\to v\to m_h,m_W,m_Z\) | Higgs/EW observables | Conditional/perturbative |
| I3 | \(\delta Y_d\) | \(M_d\to U_{dL}\to V_{CKM}\) | Flavor observables | Derived |
| I4 | \(\delta\mu\) | running parameters \(\to\) radiative corrections | Physical observable | Exact at all-orders / residual at truncation |
| I5 | Gauge-fixing \(\delta\xi\) | propagators/vertices \(\to\) BRST/Slavnov-Taylor cancellation | Gauge-independent observable | Conditional |

---

# 18. MODULE 17 — CONSTRAINT MAP

| Constraint | Nodes | Mathematical Form | Restriction |
|---|---|---|---|
| Gauge invariance | \(\mathcal L,A,\Phi\) | \(\delta_g\mathcal L=0\) | Allowed operators/interactions |
| Lorentz invariance | all fields | scalar action | Tensor/operator structure |
| Renormalizability | \(\mathcal L\) | operator dimension \(\le4\) | Allowed local operators |
| Anomaly cancellation | representations | anomaly coefficients = 0 | Fermion content |
| Unitarity | \(S\) | \(S^\dagger S=1\) | Scattering amplitudes |
| BRST physicality | \(Q_B\), states | \(Q_B|\Psi\rangle=0\) modulo exact states | Physical Hilbert space |
| Vacuum stability | \(V_{eff}\) | stable/selected vacuum | Background field |
| CKM unitarity | \(V_{CKM}\) | \(V^\dagger V=I\) | Flavor mixing |
| U(1)EM preservation | Higgs VEV | \(Q\langle H\rangle=0\) | Photon masslessness |
| RG consistency | renormalized quantities | \(d\mathcal O_{phys}/d\mu=0\) | Scale independence of observables |

---

# 19. MODULE 18 — GAUGE, BASIS, SCHEME, AND PHYSICAL-QUANTITY FILTER

| Quantity | Gauge dependent? | Flavor-basis dependent? | Scheme/scale dependent? | Physical? |
|---|---|---|---|---|
| Gauge potential \(A_\mu\) | Yes | No | Sometimes | No |
| Gauge-fixed propagator | Yes | No | Yes | No |
| Yukawa matrix \(Y_f\) | No as a gauge-invariant parameter, but representation/basis dependent | Yes | Yes after renormalization | Not directly |
| CKM matrix | No | Rephasing convention dependent but physical combinations invariant | Running/renormalization subtleties | Physical flavor structure |
| Quark running mass | No | No | Yes | Not directly |
| Pole mass | No for appropriate stable physical state | No | No | Yes |
| S-matrix element | No | No | No exact | Yes |
| Cross-section | No | No | No exact | Yes |
| Higgs VEV | Gauge/formulation subtleties in general | No | Scheme dependent beyond tree level | Not itself a universal observable |
| Higgs mass pole | No | No | No exact | Yes |
| \(\alpha_s(\mu)\) | No | No | Yes | No; scale-dependent parameter |
| \(\theta_{QCD}\) | No | No | Convention/basis relationships exist | Physical CP parameter in the minimal theory |

---

# 20. MODULE 19 — UNIVERSAL, MODEL-DEFINING, AND UNRESOLVED STRUCTURE

## 20.1 Model-Defining Structures

These are not derived by the minimal SM from more primitive internal equations:

1. The gauge group \(SU(3)_C\times SU(2)_L\times U(1)_Y\).
2. The representation assignment of the fermions and Higgs.
3. The existence of three sequential fermion generations.
4. The renormalizable local field-theory framework.
5. The absence of right-handed neutrinos in the minimal field content.

## 20.2 Derived Structures

1. Covariant derivatives.
2. Gauge field strengths.
3. Gauge kinetic interactions.
4. Electroweak mixing.
5. Photon, \(W\), and \(Z\) field combinations.
6. EWSB pattern given the Higgs potential and vacuum.
7. Gauge-boson masses given \(v\) and gauge couplings.
8. Fermion mass matrices given Yukawa matrices and \(v\).
9. CKM mixing given fermion mass-basis mismatch.
10. Higgs-fermion couplings given Yukawa structure.

## 20.3 Conditionally Derived Structures

1. Perturbative S-matrix predictions.
2. Spectral particle interpretation where asymptotic states exist.
3. BRST physical-state construction.
4. Nonperturbative QCD observables.
5. Precision predictions requiring renormalized input schemes and perturbative truncation.

## 20.4 Empirically Supplied Structures

The numerical values of the free SM parameters are not derived by the structural equations alone. They are determined from experimental data and global fits. The dependency graph therefore terminates certain parameter paths at empirical-input nodes rather than pretending the values emerge from the formalism.

## 20.5 Unresolved or Incomplete Boundaries

1. **Origin of the gauge group:** the minimal SM does not derive why this gauge group is realized.
2. **Origin of representation assignments:** the hypercharges and representations are model inputs.
3. **Origin of three generations:** the minimal SM does not derive family replication.
4. **Yukawa hierarchy:** the hierarchy of fermion masses and Yukawa couplings is not explained structurally by the minimal theory.
5. **Strong CP problem:** the smallness of \(\theta_{QCD}\) is unexplained.
6. **Nonperturbative confinement:** the complete analytic derivation of confinement and the hadron spectrum remains outside perturbative QCD.
7. **Neutrino masses:** observed neutrino masses and mixing are not accommodated by the minimal field content.
8. **Dark matter:** the minimal SM provides no viable dark-matter candidate.
9. **Baryon asymmetry:** the minimal SM does not provide an adequate explanation of the observed cosmological baryon asymmetry.
10. **Gravity:** the SM does not contain a quantum theory of gravity.
11. **Higgs-sector naturalness/origin:** the minimal theory parameterizes the Higgs potential but does not supply an underlying dynamical explanation for its parameters.
12. **Nonperturbative definition:** several exact continuum constructions remain mathematically incomplete in the strongly coupled regime.

The current PDG reviews explicitly identify several of these as limitations of the Standard Model, including neutrino masses, dark matter, baryon asymmetry, strong CP, and the unexplained pattern of parameters. [4,5]

---

# 21. MODULE 20 — DEPENDENCY INTERRUPTION AND COUNTERFACTUAL TESTS

The dependency graph is strengthened by testing what happens when an essential premise is removed.

## 21.1 Remove the Higgs Doublet

\[
H\notin\mathcal F_{SM}
\Rightarrow
\text{no minimal renormalizable Yukawa masses}
\]

and the usual Higgs-based electroweak symmetry-breaking mechanism disappears.

## 21.2 Remove the Yukawa Sector

\[
Y_f=0
\Rightarrow
M_f=0
\]

at the renormalizable level after EWSB, apart from any masses introduced by physics outside the declared model.

## 21.3 Remove One Fermion Generation

The structural flavor space changes. CKM mixing loses its full three-generation CP-violating structure; the physical parameter count changes.

## 21.4 Change the Hypercharge Assignments

Gauge invariance of Yukawa operators and anomaly cancellation generally change. The allowed interaction graph must be recomputed.

## 21.5 Remove SU(3) Color

The QCD branch disappears, including gluons, color interactions, QCD confinement dynamics, and the corresponding strong-coupling RG structure.

## 21.6 Remove SU(2)L

The electroweak structure collapses; there is no conventional Higgs-induced relation producing the observed charged-current and neutral-current gauge sector.

## 21.7 Add Right-Handed Neutrinos

This does not merely populate an empty node. It changes the allowed Yukawa operator basis and introduces new neutrino-mass and mixing parameters. This is therefore an explicit model-extension edge, not an internal minimal-SM dependency.

---

# 22. MODULE 21 — OBSERVABLE MAP

## 22.1 Particle Masses

\[
\text{Higgs VEV + gauge/Yukawa parameters}
\rightarrow
\text{mass matrices}
\rightarrow
\text{poles}
\rightarrow
m_{phys}.
\]

## 22.2 W and Z Properties

\[
(g_1,g_2,v)
\rightarrow
(m_W,m_Z,\theta_W,e)
\rightarrow
\text{EW amplitudes}
\rightarrow
\text{measured rates and precision observables}.
\]

## 22.3 Higgs Observables

\[
(\lambda,v,Y_f,g_1,g_2)
\rightarrow
m_h,\text{Higgs couplings, self-interactions}
\rightarrow
\text{production/decay amplitudes}
\rightarrow
\text{cross-sections and branching fractions}.
\]

## 22.4 Flavor Observables

\[
(Y_u,Y_d)
\rightarrow
V_{CKM}
\rightarrow
\text{charged-current amplitudes}
\rightarrow
\text{meson mixing, decay rates, CP violation}.
\]

## 22.5 QCD Observables

\[
(g_s,\text{quark masses})
\rightarrow
\text{RG evolution/QCD amplitudes}
\rightarrow
\text{partonic predictions}
\rightarrow
\text{hadronic observables}.
\]

The final step requires nonperturbative and factorization machinery in many experimentally relevant processes; the map must preserve that qualification.

---

# 23. MODULE 22 — GLOBAL RELATIONSHIP TABLE

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Recoverability | Exact/Approx | Gauge/Basis/Scheme Dependence | Observable Consequence | Epistemic Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Gauge group | Field content | Model definition | Representation assignment | Minimal SM specification | Uni | One-way | Exact | Representation convention | Charges/interactions | Definitional |
| Field content | Covariant derivative | Representation action | Lie generators | Gauge group | Uni | Conditional | Exact | Basis dependent | Gauge vertices | Derived |
| Covariant derivative | Field strength | Curvature | \([D_\mu,D_\nu]\) | Gauge connection | Uni | Conditional | Exact | Gauge-covariant | Force structure | Derived |
| Representations | Anomaly coefficients | Group traces | Triangle coefficients | Quantum gauge theory | Uni | One-way | Exact | Representation basis | Consistency | Derived |
| Anomaly coefficients | Consistent SM | Cancellation | Sums vanish | Required consistency | Uni | Constraint | Exact | Convention-independent result | Quantum consistency | Constraint |
| Lagrangian | QCD/EW/Higgs/Yukawa sectors | Decomposition | Sector separation | SM Lagrangian | Uni | Preserves structure | Exact | Basis dependent | Sector observables | Definitional |
| Higgs potential | VEV | Minimization | \(\partial V=0\) | Stable symmetry-breaking vacuum | Uni | Conditional | Tree exact | Gauge choice | EWSB scale | Derived |
| VEV | Gauge masses | Quadratic expansion | \((DH)^\dagger DH\) | EWSB | Uni | One-way | Exact at tree level | Gauge representation | W/Z masses | Derived |
| VEV | Fermion masses | Yukawa expansion | \(M=Yv/\sqrt2\) | Yukawa couplings | Uni | One-way | Exact at tree level | Flavor basis | Fermion masses | Derived |
| Up/down mass matrices | CKM | Basis mismatch | \(V=U_{uL}^\dagger U_{dL}\) | Three generations | Uni | Conditionally reversible | Exact | Flavor-basis covariant | Flavor transitions | Derived |
| CKM | CP violation | Rephasing invariant | Jarlskog structures | Three nondegenerate generations | Uni | One-way | Exact structurally | Rephasing independent | CP-violating observables | Derived |
| Bare parameters | Renormalized parameters | Renormalization | Z factors/counterterms | Regulator + renormalization scheme | Bi | Conditional | Formal/perturbative | Scheme dependent | Running inputs | Conditional |
| Renormalized parameters | Beta functions | RG derivative | \(\mu dg/d\mu\) | Renormalization | Uni | One-way | Perturbative | Scheme dependent beyond universal orders | Scale evolution | Derived |
| Correlators | S-matrix | LSZ | Amputation/on-shell limit | Asymptotic states | Uni | One-way | Formal/conditional | Gauge restrictions on intermediates | Scattering | Conditional |
| S-matrix | Cross-sections | Kinematics | \(|\mathcal M|^2 d\Phi\) | Standard normalization | Uni | One-way | Exact | Physical | Event rates | Derived |
| Gauge fixing | BRST | Quantum redundancy control | BRST differential | Consistent gauge fixing | Uni | Representation | Formal | Gauge dependent | Physical-state selection | Conditional |
| BRST | Physical Hilbert space | Cohomology | \(\ker Q_B/\mathrm{im}Q_B\) | Consistent gauge theory | Uni | One-way | Formal | Gauge representation | Gauge-independent states | Conditional |
| QCD coupling | RG flow | Beta function | \(\beta_s\) | Perturbation theory | Uni | Differential | Approx | Scheme dependent | High-energy scaling | Derived |
| SM parameters | Precision observables | Radiative prediction | Loop corrections | Renormalized perturbation theory | Uni | One-way | Approx at finite order | Scheme/input dependent intermediates | Precision tests | Empirical/derived |
| Observed neutrino mass | Minimal SM | Boundary | No renormalizable mass operator | Minimal field content | Uni | No internal reconstruction | Exact boundary statement | Model extension required | Oscillation data | Model boundary |

---

# 24. MODULE 23 — GLOBAL DEPENDENCY ANSWERS

## A. What is directly connected?

Direct structural connections include:

\[
G_{SM}\rightarrow\text{representations},
\]
\[
\text{representations}\rightarrow D_\mu,F_{\mu\nu},
\]
\[
D_\mu,F_{\mu\nu}\rightarrow\mathcal L_{SM},
\]
\[
V(H)\rightarrow\langle H\rangle\rightarrow\text{EWSB},
\]
\[
Y_f\rightarrow M_f,
\]
\[
M_u,M_d\rightarrow V_{CKM},
\]
\[
\text{renormalized couplings}\rightarrow\text{RG flow}.
\]

## B. What is only conditionally connected?

- correlators to asymptotic particle states;
- correlators to S-matrix elements;
- perturbative parameters to nonperturbative QCD observables;
- gauge-fixed quantities to physical states;
- effective-potential minima to a unique globally stable vacuum;
- finite-order predictions to exact physical observables.

## C. What is representation-dependent?

- gauge potentials;
- gauge-fixed propagators;
- flavor-basis Yukawa matrices;
- intermediate renormalized parameters;
- CKM parameterization conventions.

## D. What is physical?

- pole masses of physical states;
- S-matrix elements;
- cross-sections;
- decay widths;
- branching fractions;
- invariant CP-violating quantities;
- properly defined gauge-independent precision observables.

## E. What is constrained?

- field representations by gauge invariance;
- representations by anomaly cancellation;
- operator content by renormalizability;
- physical amplitudes by unitarity;
- flavor mixing by unitarity of basis rotations;
- physical states by BRST cohomology;
- scale dependence by RG consistency.

## F. What propagates?

Perturbations propagate through:

- equations of motion;
- Dyson/Schwinger–Dyson equations;
- RG equations;
- mass diagonalization;
- mixing matrices;
- radiative corrections;
- matching and factorization where required.

## G. What feeds back?

1. RG flow.
2. Self-energy/pole-mass determination.
3. Effective-potential vacuum determination.
4. Renormalization of Yukawa matrices and flavor parameters.
5. Gauge-parameter cancellation through BRST/Slavnov-Taylor identities.

## H. What lies outside the minimal SM?

1. Neutrino masses and PMNS mixing.
2. A viable dark-matter candidate.
3. An adequate mechanism for the observed baryon asymmetry.
4. A solution to the strong CP problem.
5. A derivation of the gauge group and representation pattern.
6. Quantum gravity.

---

# 25. MODULE 24 — CLOSURE AND SATURATION

## 25.1 Structural Closure Definition

For declared scope \(S\), define structural closure when recursive discovery produces no additional admissible nodes or edges:

\[
\Delta_S N=0,
\qquad
\Delta_S E=0.
\]

This is **scope-qualified closure**, not a claim that all mathematics or all phenomenology connected to the Standard Model has been exhausted.

The closure criterion applies only after fixing:

- the minimal renormalizable SM field content;
- the gauge group;
- the representation convention;
- the dimensionality and spacetime background;
- the allowed operator dimension;
- the formulation boundaries;
- the inclusion rules for observables and extensions.

Numerical data do not alter structural closure.

## 25.2 Closure Boundary

Within the declared scope, the map reaches the following principal boundaries:

\[
\text{SM parameter inputs}
\rightarrow
\text{observables}
\rightarrow
\text{empirical determination}.
\]

and

\[
\text{perturbative QCD}
\rightarrow
\text{nonperturbative confinement/hadronization boundary}.
\]

and

\[
\text{minimal SM}
\rightarrow
\text{neutrino-mass boundary}.
\]

These are not missing edges caused by incomplete notation; they are declared epistemic/model boundaries.

---

# 26. STATE OF THE STANDARD MODEL DEPENDENCY MAP

## Established / Definitional

- SM gauge group.
- Field representation assignments.
- Gauge connections and field strengths.
- Gauge-invariant renormalizable operator structure.
- Minimal SM Lagrangian.
- Electroweak symmetry-breaking construction given the Higgs potential and vacuum.
- Tree-level gauge-boson and fermion mass relations.
- CKM construction from fermion-basis mismatch.
- Gauge-anomaly cancellation conditions for the SM representation content.

## Derived

- Gauge interactions.
- Higgs-gauge interactions.
- Fermion-Higgs interactions.
- Photon/W/Z mixing.
- CKM unitarity.
- CP-violating invariant structures.
- RG equations and perturbative running.
- Observable formulas from amplitudes.

## Conditional / Formal

- BRST cohomology as the nonperturbative physical-state construction in all settings.
- LSZ and asymptotic particle interpretation in the presence of massless or confining sectors.
- Nonperturbative spectral reconstruction.
- Nonperturbative QCD prediction chains.

## Empirically determined

- Free SM parameters.
- Particle masses and widths.
- CKM parameters.
- Couplings at declared scales.
- Precision-observable inputs and fitted parameters.

## Unresolved / Boundary

- Origin of the gauge group.
- Origin of representation assignments.
- Origin of three generations.
- Yukawa hierarchy.
- Strong CP problem.
- Complete nonperturbative confinement derivation.
- Neutrino masses within the minimal field content.
- Dark matter.
- Adequate explanation of cosmological baryon asymmetry.
- Quantum gravity.

---

# 27. FINAL GOVERNING PRINCIPLE

The Standard Model dependency structure is a typed directed graph containing construction paths, constraints, representation changes, equivalences, feedback cycles, empirical-input boundaries, and unresolved model boundaries.

Its central structural chain is

\[
\boxed{
\text{Gauge group + field content + representations}
\rightarrow
\text{covariant structures}
\rightarrow
\mathcal L_{SM}
\rightarrow
\text{quantization}
\rightarrow
\text{renormalization}
\rightarrow
\text{EWSB/flavor/QCD dynamics}
\rightarrow
\text{amplitudes and correlators}
\rightarrow
\text{observables}
}
\]

with major convergent branches through

\[
\boxed{\text{QCD}},
\qquad
\boxed{\text{EWSB}},
\qquad
\boxed{\text{Yukawa/flavor}},
\qquad
\boxed{\text{RG/renormalization}}.
\]

The graph distinguishes what the Standard Model **defines**, what it **derives**, what it derives only **conditionally**, what is **perturbatively approximated**, what is **empirically supplied**, and what remains **outside or unresolved within the minimal theory**.

The principal mathematical and conceptual boundary is therefore not a lack of equations. It is the distinction between the formally specified Standard Model and the numerical, nonperturbative, empirical, and beyond-minimal structures required to connect that formal specification to the complete observed world.

---

# SOURCE REGISTRY

1. Particle Data Group, *Review of Particle Physics 2026*, current PDG edition and topical index. https://pdg.lbl.gov/2026/
2. Particle Data Group, *Grand Unified Theories*, 2025 review; Standard Model definition, representation assignments, parameter counting, and gauge-group convention. https://pdg.lbl.gov/2025/reviews/rpp2025-rev-guts.pdf
3. Particle Data Group, *Electroweak Model and Constraints on New Physics*, 2025 review/update; electroweak gauge structure, renormalization, EWSB, and electroweak observables. https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf
4. Particle Data Group, *Neutrino Masses, Mixing, and Oscillations*, 2025 review/update; minimal-SM neutrino-mass boundary. https://pdg.lbl.gov/2025/reviews/rpp2025-rev-neutrino-mixing.pdf
5. Particle Data Group, *Highlights of the 2026 Edition of the Review of Particle Physics*, current update status and major Standard Model review revisions. https://pdg.lbl.gov/2026/reviews/rpp2026-rev-highlights.pdf
6. Particle Data Group, *Quantum Chromodynamics*, 2025 review/update; QCD field content, coupling, perturbative structure, and strong-interaction observables. https://pdg.lbl.gov/2025/reviews/rpp2025-rev-qcd.pdf
7. Particle Data Group, *Status of Higgs Boson Physics*, 2025 review/update; Higgs potential, EWSB, Yukawa structure, and Higgs observables. https://pdg.lbl.gov/2025/reviews/rpp2025-rev-higgs-boson.pdf

## Numerical Separation Rule

Numerical values associated with the quantities defined here belong in a separate Standard Model numerical addendum. Numerical entries must retain scale, scheme, model, uncertainty, provenance, and definition metadata where applicable. They must not be inserted into this structural map merely because they are experimentally known.
