# QFT RELATIONSHIP MAP — GRAPH METHODOLOGY AND SCOPE

## PURPOSE OF THE DOCUMENT

This document constructs a **dependency/relationship graph of quantum field theory (QFT)**. It is not intended to function primarily as a conventional textbook, chronological derivation, or catalogue of equations. Its primary object is the **structured dependency network** connecting mathematical objects, physical structures, formulations, constraints, transformations, observables, approximations, and unresolved boundaries.

For every declared node and relationship, the map seeks to determine:

1. **What the object or statement is.**
2. **What it depends on.**
3. **What it defines, derives, constrains, transforms, or enables.**
4. **What assumptions or formulation choices are required.**
5. **Whether information is preserved, lost, or recoverable in the relationship.**
6. **Whether the relationship is exact, conditional, perturbative, formal, model-dependent, or unresolved.**
7. **Whether the source or target is gauge-, representation-, formulation-, or scheme-dependent.**
8. **Whether a change in an upstream node propagates to downstream nodes or enters a feedback loop.**
9. **Whether the relationship terminates at an observable, an unphysical intermediate quantity, or an unresolved mathematical boundary.**

The governing methodological statement is:

> **The purpose of the map is not merely to list what QFT contains. It is to determine, for each important object and claim, what must exist or be assumed before it can be constructed or asserted, what follows from it, what information is preserved or discarded in the transition, which formulation or approximation makes the relationship valid, and how changes propagate through the resulting dependency network.**

### DECLARED SCOPE

The map distinguishes at least four structural levels:

- **Universal or formulation-independent structure:** relationships that survive across the explicitly considered formulations when their stated axioms and preconditions hold.
- **Formulation-specific structure:** structures belonging to canonical, Lagrangian, path-integral, algebraic, lattice, or other selected formulations.
- **Model-specific structure:** structures depending on a specified theory such as scalar $\phi^4$, QED, QCD, or the Standard Model.
- **Approximation-specific structure:** relationships valid only after perturbative expansion, truncation, resummation, low-energy expansion, narrow-width approximation, or another controlled approximation.

A claim is not promoted from a lower level to a higher one merely because it is useful in a familiar formulation.

### NODE TAXONOMY

A node is an explicitly represented object, operation, equation, constraint, transformation, equivalence class, theorem, observable, or unresolved boundary. Node classes are distinguished as follows:

| Node Class | Meaning | Examples in this map |
| :---------- | :------ | :------------------- |
| **OBJECT** | Mathematical or physical entity | field, state, propagator, spectral density |
| **OPERATOR** | Operation acting on an object or space | $\partial_\mu$, functional derivative, Hamiltonian evolution |
| **EQUATION** | Equality expressing dynamics or a construction | Euler-Lagrange, Schwinger-Dyson, RG equation |
| **IDENTITY** | Relation holding by the defining structure or algebra | Ward identity, operator identities |
| **CONSTRAINT** | Restriction that admissible states, fields, parameters, or observables must satisfy | unitarity, microcausality, BRST condition |
| **TRANSFORMATION** | Map between configurations, variables, or descriptions | gauge transformation, field redefinition, Legendre transform |
| **REPRESENTATION** | Formulation or coordinate description of the same underlying structure | canonical, path-integral, Wilsonian |
| **EQUIVALENCE CLASS** | Collection of descriptions identified under an equivalence relation | gauge orbit, field-redefinition class |
| **OBSERVABLE** | Quantity with a specified physical interpretation and measurement connection | cross-section, decay rate, pole mass |
| **THEOREM** | Conditional logical statement establishing a relationship | LSZ theorem, decoupling theorem |
| **BOUNDARY** | Explicitly identified unresolved or insufficiently constructed node/path | interacting 4D QFT existence, nonperturbative measure |

### RELATIONSHIP TAXONOMY

The term **relationship** is broader than **dependency**. A dependency is a relationship in which the target requires the source, together with specified preconditions, for its construction, evaluation, interpretation, or validity.

The principal relationship classes are:

| Relationship Type | Meaning |
| :---------------- | :------ |
| **DEFINITIONAL** | The target is defined from the source. |
| **DERIVATIONAL** | The target follows mathematically from the source plus stated assumptions. |
| **CONDITIONAL** | The relation holds only under explicit preconditions. |
| **CONSTRAINT** | The source restricts the admissible target states or values. |
| **TRANSFORMATION** | The relation maps one representation or configuration to another. |
| **EQUIVALENCE** | The two descriptions encode the same physical or mathematical content under stated conditions. |
| **CORRESPONDENCE** | Two formulations or descriptions agree on a specified sector of predictions or structures. |
| **RECOVERABILITY** | The target can be reconstructed from the source, possibly only with additional retained information. |
| **SPECIALIZATION** | A general structure reduces to a more specific case under additional assumptions. |
| **GENERALIZATION** | A specific structure is embedded in a broader construction. |
| **OBSERVABLE-MAP** | A formal quantity is connected to a measurable quantity. |
| **FEEDBACK** | A directed path returns to an upstream node through a self-consistency, differential, statistical, or renormalization loop. |
| **UNRESOLVED** | A suspected relation is identified but cannot presently be established under the declared assumptions. |

### EDGE GRAMMAR

Every graph edge is interpreted in the following canonical form:

$$
\boxed{
\text{SOURCE}
\xrightarrow[\text{preconditions}]{\text{relationship / mathematical bridge}}
\text{TARGET}
}
$$

The corresponding edge record should answer, to the extent applicable:

- **Source:** What supplies the input?
- **Bridge:** What operation, theorem, equation, limit, transformation, or correspondence connects source and target?
- **Target:** What is produced, constrained, transformed, or inferred?
- **Preconditions:** What must already hold?
- **Direction:** Is the relation one-way, bidirectional, or cyclic?
- **Information behavior:** Is information preserved, discarded, or conditionally recoverable?
- **Epistemic status:** What is the strongest status justified for this edge?
- **Dependence class:** Universal, formulation-specific, model-specific, or approximation-specific.
- **Observable endpoint:** Does the path terminate in a physical quantity, a representation artifact, or an unresolved boundary?

### INFORMATION PRESERVATION AND RECOVERABILITY

The existing **Reversibility** fields are interpreted more precisely using three distinct categories:

1. **Information-preserving:** the source-to-target construction is invertible within the declared domain.
2. **Information-reducing:** multiple source states can map to the same target, so the target cannot uniquely reconstruct the source.
3. **Conditionally recoverable:** reconstruction is possible only when additional retained variables, constraints, gauge data, or structural assumptions are supplied.

Thus a statement that a relationship is reversible must not be inferred merely from the existence of an algebraic rearrangement; the required information and domain must also be present.

### FORMAL VALIDITY VS. MATHEMATICAL EXISTENCE

A symbolic relation may be meaningful as a **formal expression** without the mathematical object appearing in the expression having been rigorously constructed. The map therefore distinguishes three questions:

| Question | Meaning |
| :------- | :------ |
| **Formal expression valid?** | Does the symbolic manipulation define a coherent formal relation under its stated rules? |
| **Mathematical object constructed?** | Does the underlying integral, operator, state, limit, or theory exist within a specified rigorous framework? |
| **Physical use supported?** | Is the construction supported by empirical success or a controlled theoretical approximation in a stated domain? |

A formal relation must not be promoted to a rigorous existence claim merely because it is computationally useful.

### EPISTEMIC PROPAGATION RULE

Epistemic status applies to **paths**, not only isolated edges. For a path

$$
A \to B \to C \to \cdots \to Z,
$$

the epistemic status of the path cannot exceed the weakest necessary status of the edges, nodes, and preconditions on that path.

Operationally:

> **A downstream claim inherits every unresolved, formal, conditional, model-specific, or approximation-specific dependency that is necessary to reach it.**

A statement may therefore be exact as an algebraic identity while its use in a physical prediction remains conditional or perturbative because an upstream object is only formally or approximately defined.

### DEPENDENCY INTERRUPTION TEST

For each structurally important edge, the map should support the question:

> **What fails, changes class, or becomes undefined if an explicit prerequisite is removed?**

Examples include:

- Remove asymptotic states from the correlator-to-S-matrix path: the standard LSZ scattering construction is no longer available.
- Remove positive-metric assumptions from the standard Källén-Lehmann setting: the simple positive spectral-density conclusion no longer follows.
- Remove gauge fixing from the standard Faddeev-Popov construction: the corresponding gauge-fixed path-integral representation changes and must be reformulated.
- Remove a perturbative truncation: a finite-order numerical prediction is no longer the same mathematical object as the exact theory.

These interruption tests are part of the dependency semantics; they are not claims that every omitted structure makes the broader theory inconsistent.

### PROVENANCE PATHS

Important dependencies are assigned conceptual path identifiers of the form

$$
P_{\mathrm{QFT}-n}:
\quad
\text{source}
\to
\text{intermediate nodes}
\to
\text{target / observable / boundary}.
$$

A provenance path records the complete chain by which a claim is reached. This distinguishes a direct edge from an indirect dependency and makes it possible to audit where an approximation, representation choice, gauge condition, or unresolved node first enters the path.

### RECURSIVE DISCOVERY AND SCOPE-QUALIFIED CLOSURE

The map uses recursive discovery:

$$
\text{declared primitives}
\rightarrow
\text{relationships}
\rightarrow
\text{new candidate nodes}
\rightarrow
\text{new relationships}
\rightarrow\cdots
$$

A module is **closed only relative to its declared scope** when no additional nodes or edges are generated by the declared discovery rules:

$$
\Delta N = 0, \qquad \Delta E = 0.
$$

This is a **scope-qualified graph-closure statement**, not a claim that the mathematical or physical theory has been globally exhausted.

---

# MODULE 1 — MATHEMATICAL AND SPACETIME PRIMITIVES

## 1.1 SPACETIME STRUCTURE

### Node Definitions

**N1.1.1:** Spacetime manifold $M$

A connected, Hausdorff, paracompact, smooth (or at least $C^\infty$) manifold of dimension $d \in \mathbb{N}$.

- Assumption: Smooth structure exists.
- Status: Supplied mathematical structure.

**N1.1.2:** Spacetime points $x^\mu$

Local coordinate charts on open subsets $U \subset M$.

- Relationship: $x^\mu$ are coordinate functions $x^\mu: U \to \mathbb{R}^d$.
- Status: Definitional for a coordinate chart.

**N1.1.3:** Spacetime dimension $d$

The topological dimension of $M$.

- Status: Supplied parameter.

**N1.1.4:** Tangent bundle $TM$

The tangent bundle over $M$, sections of which are vector fields.

**N1.1.5:** Cotangent bundle $T^*M$

The cotangent bundle over $M$, sections of which are 1-forms.

**N1.1.6:** Metric structure $g_{\mu\nu}(x)$

A symmetric, nondegenerate, smooth section of $T^*M \otimes T^*M$.

- Assumption: A metric is not required for all QFT formulations.
- Status: Conditional structure.

**N1.1.7:** Inverse metric $g^{\mu\nu}(x)$

Defined by $g_{\mu\nu}g^{\nu\rho} = \delta_\mu^\rho$.

- Relationship: Algebraic inversion.
- Status: Definitional given $g_{\mu\nu}$.

**N1.1.8:** Signature

For Lorentzian signature: $(+,-,-,\ldots,-)$ or $(-,+,+,\ldots,+)$.

- Status: Conditional choice.

**N1.1.9:** Causal structure

For Lorentzian manifolds, defined by the light cone:

- Timelike separation: $g_{\mu\nu}(x-y)^\mu(x-y)^\nu > 0$ (depending on convention)
- Lightlike separation: $g_{\mu\nu}(x-y)^\mu(x-y)^\nu = 0$
- Spacelike separation: $g_{\mu\nu}(x-y)^\mu(x-y)^\nu < 0$

- Relationship: Derived from metric.
- Status: Conditional on Lorentzian metric.

**N1.1.10:** Lorentz transformations $\Lambda^\mu_{\;\nu}$

Elements of $O(d-1,1)$ satisfying:
$$\Lambda^\mu_{\;\rho}\Lambda^\nu_{\;\sigma}g_{\mu\nu} = g_{\rho\sigma}$$

- Status: Conditional symmetry group.

**N1.1.11:** Translations $a^\mu$

Elements of $\mathbb{R}^d$ acting as $x^\mu \mapsto x^\mu + a^\mu$.

- Status: Conditional symmetry group.

**N1.1.12:** Poincaré group $ISO(d-1,1)$

The semidirect product $(\mathbb{R}^d) \rtimes O(d-1,1)$.

- Status: Conditional symmetry group.

**N1.1.13:** Minkowski spacetime $\mathbb{M}^d$

The specific case where $M = \mathbb{R}^d$ and $g_{\mu\nu} = \eta_{\mu\nu} = \text{diag}(1,-1,\ldots,-1)$.

- Status: Conditional, model-specific spacetime.

**N1.1.14:** Spacelike hypersurface $\Sigma$

A codimension-1 submanifold of $M$ with spacelike normal vector.

- Status: Conditional structure.

---

## 1.2 FIELD STRUCTURE

### Node Definitions

**N1.2.1:** Scalar field $\phi(x)$

A smooth section of the trivial real (or complex) line bundle over $M$.

- Status: Supplied field type.

**N1.2.2:** Classical field $\Phi_i(x)$

A smooth section of a fiber bundle $E \to M$ with typical fiber $F$.

- General definition: $\Phi_i: M \to F$ in local coordinates.
- Status: Definitional.

**N1.2.3:** Field components $\Phi_i(x)$

The local coordinate representation of the field with index $i$.

- Relationship: $\Phi_i(x)$ are the values in local trivialization.
- Status: Representation-dependent.

**N1.2.4:** Internal indices $i$

Indices ranging over $1,\ldots,n$ where $n$ is the dimension of the representation space.

- Status: Model-dependent parameter.

**N1.2.5:** Spinor field $\psi(x)$

A section of the spinor bundle over $M$.

- Assumption: Requires $M$ to have a spin structure.
- Status: Conditional field type.

**N1.2.6:** Spinor indices $\alpha,\beta$

Indices ranging over $1,\ldots,2^{\lfloor d/2\rfloor}$ in $d$ dimensions.

- Status: Conditional, representation-dependent.

**N1.2.7:** Vector field $A_\mu(x)$

A section of $T^*M$ (or $TM$ with index placement via metric).

- Status: Supplied field type.

**N1.2.8:** General field multiplet $\Phi_i(x)$

A collection of fields with indices in some representation space.

- Status: Definitional.

**N1.2.9:** Representation label $R$

Labels the representation of some symmetry group $G$ on the field space.

- Status: Conditional, model-dependent.

**N1.2.10:** Quantum field $\hat{\Phi}(x)$

An operator-valued distribution on a Hilbert space $\mathcal{H}$.

- Relationship to classical field: Not an ordinary function; formally $\hat{\Phi}(f) = \int d^dx\, f(x)\hat{\Phi}(x)$ for test functions $f$.
- Status: Definitional.

**N1.2.11:** Field redefinition

An invertible transformation $\Phi_i \mapsto \Phi'_i = \mathcal{F}_i(\Phi)$ with nonzero Jacobian.

- Status: Not a physical change; representation artifact.

---

## 1.3 STATE SPACE PRIMITIVES

### Node Definitions

**N1.3.1:** Hilbert space $\mathcal{H}$

A complete complex inner product space.

- Status: Conditional on canonical quantization; not universal to all QFT formulations.

**N1.3.2:** State vector $|\Psi\rangle$

An element of $\mathcal{H}$ with unit norm: $\langle\Psi|\Psi\rangle = 1$.

- Status: Conditional on Hilbert space existence.

**N1.3.3:** Density operator $\rho$

A positive semidefinite, trace-class operator on $\mathcal{H}$ with $\text{Tr}(\rho) = 1$.

- Status: Conditional on Hilbert space existence.

**N1.3.4:** Expectation value $\langle\mathcal{O}\rangle$

For pure states: $\langle\Psi|\mathcal{O}|\Psi\rangle$.
For mixed states: $\text{Tr}(\rho\mathcal{O})$.

- Status: Conditional on operator definition.

**N1.3.5:** Vacuum state $|0\rangle$

A state invariant under the Poincaré group (if applicable) and of lowest energy.

- Assumption: Requires Poincaré symmetry and positive energy.
- Status: Conditional, model-dependent.

**N1.3.6:** Fock space

The direct sum of symmetrized (bosonic) or antisymmetrized (fermionic) $n$-particle Hilbert spaces:
$$\mathcal{F} = \bigoplus_{n=0}^\infty \mathcal{H}_n^{\text{sym/antisym}}$$

- Status: Conditional on particle interpretation and free theory.

---

## 1.4 OPERATOR PRIMITIVES

### Node Definitions

**N1.4.1:** Field operator $\hat{\Phi}(x)$

An operator-valued distribution acting on $\mathcal{H}$.

- Status: Conditional on quantization.

**N1.4.2:** Canonical momentum $\hat{\Pi}(x)$

For Lagrangian theory: $\hat{\Pi}(x) = \frac{\partial \mathcal{L}}{\partial(\partial_0\hat{\Phi})}$.

- Status: Conditional on canonical formulation.

**N1.4.3:** Hamiltonian operator $\hat{H}$

The generator of time translations.

- Status: Conditional on Hilbert space and time evolution.

**N1.4.4:** Momentum operator $\hat{P}_\mu$

The generator of spacetime translations.

- Status: Conditional on Poincaré symmetry.

**N1.4.5:** Local operator $\mathcal{O}(x)$

An operator constructed from fields and their derivatives at point $x$.

- Status: Definitional.

**N1.4.6:** Composite operator $\mathcal{O}[\Phi](x)$

A local operator polynomial in fields and derivatives.

- Status: Definitional.

**N1.4.7:** Gauge-invariant operator

An operator invariant under gauge transformations.

- Status: Conditional on gauge symmetry.

**N1.4.8:** Observable

A gauge-invariant, Hermitian operator with a well-defined measurement interpretation.

- Status: Conditional.

---

# RELATIONSHIP TABLE — MODULE 1

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N1.1.1 $M$ | N1.1.2 $x^\mu$ | Definitional | Local coordinate chart $x^\mu: U \to \mathbb{R}^d$ | Atlas exists on $M$ | Bidirectional (local) | Local | Exact | Coordinate-dependent | None | Supplied |
| N1.1.1 $M$ | N1.1.3 $d$ | Definitional | Topological dimension of $M$ | None | Unidirectional | Global | Exact | Independent | None | Supplied |
| N1.1.1 $M$ | N1.1.4 $TM$ | Definitional | Tangent bundle construction | Smooth manifold | Unidirectional | Global | Exact | Independent | None | Supplied |
| N1.1.1 $M$ | N1.1.5 $T^*M$ | Definitional | Cotangent bundle construction | Smooth manifold | Unidirectional | Global | Exact | Independent | None | Supplied |
| N1.1.6 $g_{\mu\nu}$ | N1.1.7 $g^{\mu\nu}$ | Algebraic | $g_{\mu\nu}g^{\nu\rho} = \delta_\mu^\rho$ | Nondegenerate $g_{\mu\nu}$ | Bidirectional | Global | Exact | Independent | None | Definitional |
| N1.1.6 $g_{\mu\nu}$ | N1.1.8 Signature | Definitional | Sign of eigenvalues of $g_{\mu\nu}$ | Nondegenerate $g_{\mu\nu}$ | Unidirectional | Global | Exact | Convention-dependent | None | Supplied |
| N1.1.6 $g_{\mu\nu}$ | N1.1.9 Causal | Derived | Light cone defined by $g_{\mu\nu}v^\mu v^\nu = 0$ | Lorentzian metric | Unidirectional | Global | Exact | Convention-dependent | Causal relations | Derived |
| N1.1.10 Lorentz | N1.1.6 $g_{\mu\nu}$ | Symmetry | $\Lambda^\mu_{\;\rho}\Lambda^\nu_{\;\sigma}g_{\mu\nu} = g_{\rho\sigma}$ | Lorentzian metric | Unidirectional | Global | Exact | Independent | None | Conditional |
| N1.1.10 Lorentz | N1.1.11 Translations | Algebraic | Semidirect product | Poincaré group | Bidirectional | Global | Exact | Independent | None | Definitional |
| N1.1.10 Lorentz + N1.1.11 | N1.1.12 Poincaré | Algebraic | $ISO(d-1,1) = \mathbb{R}^d \rtimes O(d-1,1)$ | Poincaré group | Unidirectional | Global | Exact | Independent | None | Definitional |
| N1.1.12 Poincaré | N1.1.13 Minkowski | Conditional | Minkowski spacetime is the homogeneous space $ISO(d-1,1)/O(d-1,1)$ | Flat spacetime | Unidirectional | Global | Exact | Independent | None | Conditional |
| N1.1.1 $M$ | N1.1.14 $\Sigma$ | Constraint | $\Sigma \subset M$, normal vector $n^\mu$ with $g_{\mu\nu}n^\mu n^\nu = 1$ | Lorentzian metric | Unidirectional | Global | Exact | Independent | None | Conditional |
| N1.2.1 $\phi$ | N1.2.2 Classical $\Phi$ | Specialization | Scalar field is a section of trivial line bundle | None | Unidirectional | Local | Exact | Independent | None | Definitional |
| N1.2.2 Classical $\Phi$ | N1.2.3 Components | Representation | $\Phi_i(x)$ are values in local trivialization | Local trivialization exists | Unidirectional | Local | Exact | Representation-dependent | None | Definitional |
| N1.2.3 Components | N1.2.4 Internal indices | Dimensional | $i = 1,\ldots,n$ where $n = \dim(F)$ | Finite-dimensional fiber $F$ | Unidirectional | Global | Exact | Representation-dependent | None | Definitional |
| N1.2.5 Spinor $\psi$ | N1.2.6 Spinor indices | Definitional | $\psi^\alpha(x)$ with $\alpha = 1,\ldots,2^{\lfloor d/2\rfloor}$ | Spin structure exists | Unidirectional | Local | Exact | Representation-dependent | None | Conditional |
| N1.2.7 Vector $A_\mu$ | N1.2.2 Classical $\Phi$ | Specialization | Vector field is a section of $T^*M$ | None | Unidirectional | Local | Exact | Independent | None | Definitional |
| N1.2.2 Classical $\Phi$ | N1.2.8 Multiplet | Generalization | $\Phi_i$ with $i$ in representation space | Internal symmetry group | Unidirectional | Local | Exact | Representation-dependent | None | Definitional |
| N1.2.9 Rep label $R$ | N1.2.3 Components | Dimensional | $\dim(R) = n$ | Symmetry group $G$ | Unidirectional | Global | Exact | Representation-dependent | None | Conditional |
| N1.2.2 Classical $\Phi$ | N1.2.10 Quantum $\hat{\Phi}$ | Quantization | $\hat{\Phi}(x)$ as operator-valued distribution; $\Phi$ is $c$-number section | Quantization prescription | Unidirectional | Local (distribution) | Formal | Quantization-dependent | Indirect | Conditional |
| N1.2.2 Classical $\Phi$ | N1.2.11 Redefinition | Transformation | $\Phi' = \mathcal{F}(\Phi)$, $\det(\partial\mathcal{F}/\partial\Phi) \neq 0$ | Invertible $\mathcal{F}$ | Unidirectional | Local | Exact | Field-redefinition dependent | None | Conditional |
| N1.3.1 Hilbert $\mathcal{H}$ | N1.3.2 State $|\Psi\rangle$ | Definitional | $|\Psi\rangle \in \mathcal{H}$, $\langle\Psi|\Psi\rangle = 1$ | Inner product | Unidirectional | Global | Exact | Independent | Probabilistic | Conditional |
| N1.3.1 Hilbert $\mathcal{H}$ | N1.3.3 Density $\rho$ | Definitional | $\rho: \mathcal{H} \to \mathcal{H}$, $\rho^\dagger = \rho$, $\rho \ge 0$, $\text{Tr}(\rho)=1$ | Trace class | Unidirectional | Global | Exact | Independent | Probabilistic | Conditional |
| N1.3.2 State $|\Psi\rangle$ | N1.3.3 Density $\rho$ | Specialization | $\rho = |\Psi\rangle\langle\Psi|$ for pure states | Pure state | Unidirectional | Global | Exact | Independent | Same as state | Derived |
| N1.3.2 $|\Psi\rangle$ | N1.3.4 Expectation | Definitional | $\langle\mathcal{O}\rangle_\Psi = \langle\Psi|\mathcal{O}|\Psi\rangle$ | Hermitian $\mathcal{O}$ | Unidirectional | Global | Exact | Independent | Measurement outcomes | Conditional |
| N1.3.3 $\rho$ | N1.3.4 Expectation | Definitional | $\langle\mathcal{O}\rangle_\rho = \text{Tr}(\rho\mathcal{O})$ | Trace class | Unidirectional | Global | Exact | Independent | Measurement outcomes | Conditional |
| N1.3.5 Vacuum $|0\rangle$ | N1.3.2 State $|\Psi\rangle$ | Specialization | $|0\rangle \in \mathcal{H}$, Poincaré invariant, lowest energy | Poincaré symmetry | Unidirectional | Global | Exact | Independent | Ground state | Conditional |
| N1.3.5 Vacuum | N1.3.6 Fock space | Construction | Fock vacuum is $|0\rangle = (1,0,0,\ldots)$ | Particle interpretation | Unidirectional | Global | Exact | Independent | None | Conditional |
| N1.2.10 Quantum $\hat{\Phi}$ | N1.4.1 Field operator | Same node | Quantum field = operator-valued distribution | Quantization | - | Local distribution | Exact | Quantization-dependent | None | Definitional |
| N1.2.10 $\hat{\Phi}$ | N1.4.2 Momentum $\hat{\Pi}$ | Definitional | $\hat{\Pi}(x) = \partial\mathcal{L}/\partial(\partial_0\hat{\Phi})$ | Lagrangian formulation | Unidirectional | Local | Exact | Lagrangian-dependent | None | Conditional |
| N1.4.2 $\hat{\Pi}$ | N1.4.3 Hamiltonian $\hat{H}$ | Definitional | $\hat{H} = \int_{\Sigma} d^{d-1}x\, (\hat{\Pi}\partial_0\hat{\Phi} - \mathcal{L})$ | Canonical quantization | Unidirectional | Nonlocal (integral) | Exact | Quantization-dependent | Energy spectrum | Conditional |
| N1.4.3 $\hat{H}$ | N1.3.5 Vacuum | Constraint | $\hat{H}|0\rangle = E_0|0\rangle$ with minimal $E_0$ | Positive energy | Unidirectional | Global | Exact | Independent | Ground state energy | Conditional |
| N1.4.4 $\hat{P}_\mu$ | N1.3.5 Vacuum | Constraint | $\hat{P}_\mu|0\rangle = 0$ | Poincaré invariance | Unidirectional | Global | Exact | Independent | Translation invariance | Conditional |
| N1.4.5 Local operator | N1.2.2 Classical $\Phi$ | Definitional | Constructed from $\Phi_i(x)$ and $\partial_\mu\Phi_i(x)$ at same $x$ | None | Unidirectional | Local | Exact | Field-dependent | Correlations | Definitional |
| N1.4.6 Composite operator | N1.4.5 Local operator | Specialization | Polynomial in fundamental fields at same point | None | Unidirectional | Local | Exact | Field-dependent | Composite correlations | Definitional |
| N1.4.7 Gauge-invariant | N1.4.5 Local operator | Constraint | $\mathcal{O}(x) \to \mathcal{O}(x)$ under gauge transformations | Gauge symmetry | Unidirectional | Local | Exact | Gauge-invariant | Observables | Conditional |
| N1.4.8 Observable | N1.4.7 Gauge-invariant | Constraint | Hermitian + gauge-invariant + measurement interpretation | Measurement theory | Unidirectional | Local/nonlocal | Exact | Gauge-invariant | Measurement | Conditional |

---

# MODULE 1 SYNTHESIS

## Relationships Established

### Spacetime Structure
1. **Definitional Chain:** $M \to \{x^\mu\} \to d \to \{TM, T^*M\}$
   - The spacetime manifold is the fundamental node.
   - Coordinates are local representations only; they do not define the manifold.

2. **Metric Structure:** Conditional on Lorentzian signature requirement.
   - $g_{\mu\nu} \to g^{\mu\nu}$ is algebraic inversion.
   - Causal structure is derived from $g_{\mu\nu}$, not independent.

3. **Symmetry Groups:** Conditional on flat Minkowski spacetime (or at least Poincaré symmetry).
   - Lorentz $\to$ translations $\to$ Poincaré $\to$ Minkowski.

4. **Separability:** The relationship between coordinates and metric is representation-dependent (coordinate choice).

### Field Structure
5. **Field Definition:**
   - Classical field: section of fiber bundle.
   - Components: representation-dependent local values.
   - Internal indices: dimensional labels.

6. **Field Types:**
   - Scalar: trivial line bundle.
   - Spinor: requires spin structure.
   - Vector: tangent/cotangent section.

7. **Classical vs. Quantum:**
   - Quantum field $\hat{\Phi}$ is an operator-valued distribution.
   - **Relationship to classical $\Phi$ is not identity but quantization.**
   - $\hat{\Phi}$ is formally $\int d^dx\, f(x)\hat{\Phi}(x)$ for test functions $f$.

8. **Field Redefinitions:**
   - Invertible transformations $\Phi \to \Phi'$ are allowed.
   - They change representation but not physical content.

### State Space
9. **Hilbert Space:** Conditional on canonical quantization.
   - $\mathcal{H} \to |\Psi\rangle \to \rho \to \langle\mathcal{O}\rangle$
   - Pure states $\subset$ density matrices via $\rho = |\Psi\rangle\langle\Psi|$.

10. **Vacuum:** Requires Poincaré symmetry and lowest-energy condition.
    - $\hat{P}_\mu|0\rangle = 0$, $\hat{H}|0\rangle = E_0|0\rangle$.
    - Fock space requires particle interpretation.

### Operators
11. **Field Operators:** $\hat{\Phi} \to \hat{\Pi} \to \hat{H}$ is conditional on Lagrangian and canonical quantization.
12. **Local vs. Composite:**
    - Local operator: fields and derivatives at same point.
    - Composite: polynomial in locals.
13. **Observables:**
    - Require gauge invariance + Hermiticity + measurement interpretation.
    - Not all gauge-invariant operators are observables.

---

## Unresolved or Conditional Relationships

### Missing Connections in Module 1
1. **Global Field Definition:** No global section of a fiber bundle exists unless the bundle is trivial.
   - QFT implicitly assumes fields can be defined globally or on patches.
   - **Unresolved:** Topological obstructions to global field definitions are not specified.

2. **Smoothness vs. Distributional:** Classical fields are smooth; quantum fields are distributions.
   - **Relationship not established:** The precise mathematical bridge between $C^\infty$ and $\mathcal{D}'$ is not automatic.

3. **State Space Independence:** Is $\mathcal{H}$ determined by the field algebra or vice versa?
   - GNS construction provides one bridge: $\mathcal{A} \to \mathcal{H}$ via state.
   - **Not established in Module 1:** General QFT does not assume a unique $\mathcal{H}$.

4. **Metric Independence:** QFT on curved vs. flat spacetime.
   - **Not established:** Whether $g_{\mu\nu}$ is dynamical (gravitational) or background.

5. **Causal Structure and Commutation:** Commutation relations depend on causality.
   - **Not established in Module 1:** No commutation relations yet specified.

6. **Field Redefinition and Gauge:** Are all field redefinitions gauge-equivalent?
   - **Unresolved:** The intersection of field redefinitions and gauge transformations.

7. **Observables and Locality:** Are all observables local?
   - Nonlocal observables (Wilson loops, etc.) exist.
   - **Unresolved:** General classification of observables.

8. **Spectral Conditions:** No positivity or spectral assumptions yet imposed.
   - Wightman axioms require spectral condition.
   - **Conditional:** Requires Module 7.

9. **Path-Integral vs. Canonical:** No bridge established between these formulations.
   - **Unresolved:** Correspondence requires Module 3.

10. **Statistical QFT:** No explicit distinction between Euclidean and Lorentzian.
    - **Unresolved:** Wick rotation not yet established.

---

## Epistemic Classification Summary

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 26 |
| Algebraic | 3 |
| Derived | 4 |
| Conditional | 18 |
| Formal | 1 |
| Supplied | 8 |
| **Total** | **60** |

---

## Critical Open Questions From Module 1

1. **Is the field algebra $\mathcal{A}$ generated by $\hat{\Phi}(x)$ sufficient to determine $\mathcal{H}$?**
   - GNS construction: yes for a given state.
   - But different states yield different representations.

2. **What is the exact relationship between a classical field configuration and a quantum state?**
   - Not simply: $\Phi \leftrightarrow |\Phi\rangle$ (coherent states exist, but not general).

3. **Does every QFT require a metric?**
   - No: topological QFTs exist without metric.
   - Therefore, metric structure is not universal QFT structure.

4. **Does every QFT require a Lagrangian?**
   - No: some constructions are algebraic (e.g., CFT, AQFT).
   - Lagrangian is conditional, not universal.

5. **Does every QFT require a Hilbert space?**
   - Algebraic QFT avoids fixing $\mathcal{H}$.
   - Therefore, Hilbert space is not universal QFT structure.

---

# STATE OF MODULE 1

**Established:**
- Spacetime manifold, coordinates, metric (where applicable).
- Fields as sections of bundles.
- Distinction between classical fields and operator-valued distributions.
- State vectors and density matrices.
- Operator construction from fields.
- Gauge-invariant observables as conditionally defined.

**Not Established:**
- Commutation relations.
- Equations of motion.
- Correlation functions.
- Quantization bridges.
- Renormalization.
- Particle interpretation.
- Scattering structure.

**Mathematical Gaps:**
- No globally well-defined field space in general.
- No Hilbert space construction without quantization.
- No measurement theory beyond formal expectation values.

---

# MODULE 2 — ACTION, VARIATIONAL STRUCTURE, AND EQUATIONS OF MOTION

## 2.1 ACTION AND LAGRANGIAN STRUCTURE

### Node Definitions

**N2.1.1:** Action functional $S[\Phi]$

A functional $S: \mathcal{F} \to \mathbb{R}$ (or $\mathbb{C}$ for Euclidean) mapping field configurations to numbers.

- Definitional form: $S[\Phi] = \int_M d^d x\, \mathcal{L}(\Phi(x), \partial_\mu\Phi(x), \ldots)$
- Assumption: Requires a Lagrangian density.
- Status: Conditional on Lagrangian formulation.

**N2.1.2:** Lagrangian density $\mathcal{L}$

A local function of fields and derivatives:
$$\mathcal{L} = \mathcal{L}(\Phi_i(x), \partial_\mu\Phi_i(x))$$

- Assumption: Locality (finite derivatives), usually first-order.
- Status: Conditional.

**N2.1.3:** Lagrangian $L(t)$ (spatial integral)

$$L(t) = \int_{\Sigma_t} d^{d-1}x\, \mathcal{L}(t,\mathbf{x})$$

- Status: Conditional, requires foliation.

**N2.1.4:** Kinetic term $\mathcal{L}_{\text{kin}}$

Quadratic part in derivatives and/or fields. Examples:
- Scalar: $\frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi$
- Spinor: $\bar{\psi}(i\gamma^\mu\partial_\mu - m)\psi$
- Vector: $-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$

- Status: Model-dependent, conditional.

**N2.1.5:** Interaction term $\mathcal{L}_{\text{int}}$

Polynomial (or non-polynomial) in fields of degree $\ge 3$, multiplied by coupling constants.

- Status: Model-dependent, conditional.

**N2.1.6:** Potential term $V(\Phi)$

A function of fields with no derivatives, typically part of $\mathcal{L}$:
$$\mathcal{L} = \mathcal{L}_{\text{kin}} - V(\Phi)$$

- Status: Model-dependent.

**N2.1.7:** Coupling constants $g_i$

Parameters multiplying interaction terms.

- Status: Supplied parameters, model-dependent.

**N2.1.8:** Mass parameter $m$

Coefficient of quadratic term $\frac{1}{2}m^2\phi^2$ for scalars, or $m\bar{\psi}\psi$ for fermions.

- Status: Model-dependent parameter.

**N2.1.9:** Dimensional analysis

Mass dimension of fields $[\Phi]$ and couplings $[g]$ in units where $\hbar = c = 1$, with $[x] = -1$.

- For scalar in $d$ dimensions: $[\phi] = (d-2)/2$.
- Coupling for $\phi^n$: $[g] = d - n(d-2)/2$.
- Status: Derived from scaling of action ($[S]=0$).

---

## 2.2 VARIATIONAL STRUCTURE

**N2.2.1:** Variation $\delta S$

The first variation of the action:
$$\delta S = \int d^d x\, \left( \frac{\partial\mathcal{L}}{\partial\Phi_i} - \partial_\mu \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi_i)} \right) \delta\Phi_i + \text{boundary term}$$

- Status: Definitional.

**N2.2.2:** Stationary action principle

$\delta S = 0$ for all variations $\delta\Phi_i$ with compact support (or vanishing boundary conditions).

- Status: Conditional variational principle.

**N2.2.3:** Euler-Lagrange equations

$$\frac{\partial\mathcal{L}}{\partial\Phi_i} - \partial_\mu \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi_i)} = 0$$

- Status: Derived from $\delta S=0$.

**N2.2.4:** Boundary term / Surface term

$$\int_{\partial M} d^{d-1}x\, \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi_i)} \delta\Phi_i$$

- Vanishes by boundary conditions or falls off at infinity.
- Status: Constraint on allowed variations.

**N2.2.5:** Field equations (general)

The Euler-Lagrange equations as PDEs for the fields.

- Status: Derived.

**N2.2.6:** Green's functions for equations

Linearized field equations define differential operators $K$, with Green functions $G$ satisfying $K G = \delta^{(d)}(x-y)$.

- Status: Derived, conditional on linearization.

---

## 2.3 CANONICAL STRUCTURE

**N2.3.1:** Canonical momentum $\Pi_i(x)$

$$\Pi_i(x) = \frac{\partial\mathcal{L}}{\partial(\partial_0\Phi_i(x))}$$

- Requires a preferred time direction (foliation).
- Status: Conditional on Lagrangian and foliation.

**N2.3.2:** Hamiltonian density $\mathcal{H}$

$$\mathcal{H} = \Pi_i \partial_0\Phi_i - \mathcal{L}$$

- Legendre transform with respect to $\partial_0\Phi_i$.
- Status: Conditional on invertibility of $\Pi_i$ relation (non-degenerate).

**N2.3.3:** Hamiltonian functional $H$

$$H = \int_{\Sigma_t} d^{d-1}x\, \mathcal{H}$$

- Status: Conditional.

**N2.3.4:** Hamilton's equations

$$\partial_0\Phi_i = \frac{\delta H}{\delta\Pi_i}, \qquad \partial_0\Pi_i = -\frac{\delta H}{\delta\Phi_i}$$

- Status: Derived from $H$ variation, equivalent to EL equations.

**N2.3.5:** Constraint structure (primary constraints)

If $\det(\partial^2\mathcal{L}/\partial(\partial_0\Phi_i)\partial(\partial_0\Phi_j)) = 0$, then Legendre transform is singular.

- Requires Dirac constraint analysis.
- Status: Conditional for gauge theories.

**N2.3.6:** Poisson brackets (classical)

$$\{\Phi_i(\mathbf{x}), \Pi_j(\mathbf{y})\} = \delta_{ij}\delta^{(d-1)}(\mathbf{x}-\mathbf{y})$$

- Status: Classical structure, conditional.

---

# RELATIONSHIP TABLE — MODULE 2

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N1.2.2 Classical $\Phi$ | N2.1.1 $S[\Phi]$ | Definitional | $S[\Phi] = \int \mathcal{L}(\Phi,\partial\Phi)$ | Lagrangian exists | Unidirectional | Nonlocal (integral) | Exact | Lagrangian-dependent | Dynamics generator | Conditional |
| N2.1.2 $\mathcal{L}$ | N2.1.1 $S$ | Functional | $S = \int_M d^d x\, \mathcal{L}$ | Lagrangian exists | Unidirectional | Nonlocal (integral) | Exact | Lagrangian-dependent | None | Definitional |
| N2.1.2 $\mathcal{L}$ | N2.1.3 $L(t)$ | Definitional | $L(t) = \int_{\Sigma_t} d^{d-1}x\, \mathcal{L}$ | Foliation of $M$ | Unidirectional | Nonlocal (spatial integral) | Exact | Foliation-dependent | Time evolution | Conditional |
| N2.1.2 $\mathcal{L}$ | N2.1.4 $\mathcal{L}_{\text{kin}}$ | Decomposition | $\mathcal{L} = \mathcal{L}_{\text{kin}} - V + \mathcal{L}_{\text{int}}$ | Specific field content | Unidirectional | Local | Exact | Field-dependent | None | Model-Dependent |
| N2.1.2 $\mathcal{L}$ | N2.1.5 $\mathcal{L}_{\text{int}}$ | Decomposition | As above | Specific interaction | Unidirectional | Local | Exact | Coupling-dependent | Scattering | Model-Dependent |
| N2.1.2 $\mathcal{L}$ | N2.1.6 $V(\Phi)$ | Decomposition | $\mathcal{L} = \mathcal{L}_{\text{kin}} - V(\Phi)$ | Potential exists | Unidirectional | Local | Exact | Field-dependent | None | Model-Dependent |
| N2.1.4 $\mathcal{L}_{\text{kin}}$ | N2.1.8 Mass $m$ | Parameterization | $m^2\phi^2/2$ or $m\bar{\psi}\psi$ | Quadratic term | Unidirectional | Local | Exact | Field-dependent | Pole of propagator | Model-Dependent |
| N2.1.5 $\mathcal{L}_{\text{int}}$ | N2.1.7 Coupling $g$ | Parameterization | $g \mathcal{O}_n(\Phi)$ | Specific operator | Unidirectional | Local | Exact | Coupling-dependent | Cross-sections | Model-Dependent |
| N2.1.1 $S$ | N2.1.9 Dimensional analysis | Constraint | $[S]=0 \Rightarrow [\mathcal{L}]=d \Rightarrow [\Phi]$ and $[g]$ | Scaling of action | Unidirectional | Global | Exact | Independent | Scaling of observables | Derived |
| N1.1.1 $M$ | N2.1.1 $S$ | Domain | Integration over $M$ | Manifold with measure | Unidirectional | Global | Exact | Coordinate-dependent (measure) | None | Conditional |
| N1.1.6 $g_{\mu\nu}$ | N2.1.1 $S$ | Coupling | $\sqrt{-g}\, d^dx$ in curved space | Metric exists | Unidirectional | Global | Exact | Coordinate-invariant (scalar density) | Gravity coupling | Conditional |
| N2.1.2 $\mathcal{L}$ | N2.2.1 $\delta S$ | Differential | $\delta S = \int d^d x \left( \frac{\partial\mathcal{L}}{\partial\Phi} \delta\Phi + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} \partial_\mu\delta\Phi \right)$ | Differentiable $\mathcal{L}$ | Bidirectional | Local | Exact | Field-dependent | Variation of action | Definitional |
| N2.2.1 $\delta S$ | N2.2.3 EL eq | Variational | $\frac{\partial\mathcal{L}}{\partial\Phi} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)} = 0$ | $\delta S=0$, $\delta\Phi$ compact support | Unidirectional | Local | Exact | Field-dependent | Field dynamics | Derived |
| N2.2.3 EL eq | N2.2.5 Field eq | Identity | EL equations are the field equations | None | Bidirectional | Local | Exact | Field-dependent | Dynamics | Definitional |
| N2.2.3 EL eq | N2.2.4 Boundary term | Constraint | Boundary term must vanish: $\int_{\partial M} \frac{\partial\mathcal{L}}{\partial(\partial_\mu\Phi)}\delta\Phi = 0$ | $\delta S=0$ | Unidirectional | Local (on boundary) | Exact | Field-dependent | Well-posed variation | Constraint |
| N2.2.3 EL eq | N2.2.6 Green's functions | Linearization | $K_{ij}(x)\Phi_j(x) = J_i(x)$, $K G = \delta$ | Linearization around background | Unidirectional | Local (operator) | Approximate (linear) | Field-dependent | Propagators | Conditional |
| N2.2.3 EL eq | N2.3.1 Canonical $\Pi$ | Legendre | $\Pi_i = \partial\mathcal{L}/\partial(\partial_0\Phi_i)$ | Time foliation | Unidirectional | Local | Exact | Time-direction dependent | None | Conditional |
| N2.2.3 EL eq | N2.3.2 Hamiltonian $\mathcal{H}$ | Legendre | $\mathcal{H} = \Pi_i\partial_0\Phi_i - \mathcal{L}$ | Invertible relation $\Phi_0 \leftrightarrow \Pi$ | Unidirectional | Local | Exact | Foliation-dependent | Energy density | Conditional |
| N2.3.1 $\Pi$ | N2.3.2 $\mathcal{H}$ | Algebraic | $\mathcal{H}$ expressed in terms of $\Phi$ and $\Pi$ | Legendre transform invertible | Bidirectional | Local | Exact | Foliation-dependent | Energy | Conditional |
| N2.3.2 $\mathcal{H}$ | N2.3.3 $H$ | Integral | $H = \int_{\Sigma_t} d^{d-1}x\, \mathcal{H}$ | Foliation | Unidirectional | Nonlocal (spatial) | Exact | Foliation-dependent | Energy observable | Conditional |
| N2.3.3 $H$ | N2.3.4 Hamilton's eq | Variational | $\partial_0\Phi = \delta H/\delta\Pi$, $\partial_0\Pi = -\delta H/\delta\Phi$ | Canonical structure | Bidirectional | Local (functional derivatives) | Exact | Foliation-dependent | Equivalent to EL | Derived |
| N2.3.2 $\mathcal{H}$ | N2.3.5 Constraints | Constraint | $\det(\partial^2\mathcal{L}/\partial(\partial_0\Phi_i)\partial(\partial_0\Phi_j)) = 0$ | Singular Hessian | Unidirectional | Local | Exact | Field-dependent | Gauge redundancy | Conditional |
| N2.3.5 Constraints | N2.2.3 EL eq | Modification | EL equations become constrained PDEs; Dirac analysis required | Gauge theory | Unidirectional | Local | Exact | Gauge-dependent | Constraint propagation | Conditional |
| N2.3.6 Poisson brackets | N2.3.1 $\Pi$ | Algebraic | $\{\Phi_i(\mathbf{x}), \Pi_j(\mathbf{y})\} = \delta_{ij}\delta^{(d-1)}(\mathbf{x}-\mathbf{y})$ | Canonical variables | Bidirectional | Local | Exact | Foliation-dependent | Classical dynamics | Conditional |
| N2.3.6 Poisson brackets | N2.2.3 EL eq | Dynamical | $\dot{\Phi} = \{\Phi, H\}$, $\dot{\Pi} = \{\Pi, H\}$ | Poisson bracket + $H$ | Unidirectional | Local | Exact | Foliation-dependent | Dynamics | Derived |

---

# MODULE 2 SYNTHESIS

## Relationships Established

### Action–Lagrangian Bridge
1. **$S \leftrightarrow \mathcal{L}$:** $S = \int \mathcal{L}$ is definitional, but not universal.
   - If $\mathcal{L}$ exists, $S$ is an integral functional.
   - If no $\mathcal{L}$ exists (e.g., algebraic QFT, some CFTs), the action concept is absent.

2. **Decomposition:** $\mathcal{L} = \mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{int}} - V$ is model-dependent.
   - Kinetic terms define propagation.
   - Interaction terms define scattering.
   - Potential terms affect vacuum structure.

3. **Dimensional analysis:** $[S]=0$ yields field dimensions and coupling dimensions.
   - This is not optional if scaling is to be preserved.

### Variational Principle
4. **Euler–Lagrange Equations:** Derived from $\delta S=0$ with boundary conditions.
   - This is the **only exact bridge** from action to field equations.
   - Requires compact support variations or asymptotic fall-off.

5. **Boundary Terms:** Must vanish for $\delta S=0$.
   - This imposes constraints on field variations and asymptotics.
   - If boundary terms survive, they yield boundary conditions or topological contributions.

6. **Green's Functions:** Obtained by linearizing the EL equations.
   - This step is **approximate** (linearization) and requires a background.
   - Propagators are not yet quantum; they are classical Green's functions.

### Canonical (Hamiltonian) Structure
7. **Legendre Transform:** $\Pi = \partial\mathcal{L}/\partial(\partial_0\Phi)$, $\mathcal{H} = \Pi\partial_0\Phi - \mathcal{L}$.
   - **Conditional on:** (a) Lagrangian, (b) time foliation, (c) non-degenerate Hessian.

8. **Hamilton's Equations:** Equivalent to EL equations via functional derivatives of $H$.

9. **Constraints:** For gauge theories (and any degenerate Lagrangian), the Legendre transform fails.
   - This requires Dirac's constraint analysis.
   - **Therefore, $\Pi \leftrightarrow \mathcal{H}$ is not a universal bridge.**

10. **Poisson Brackets:** Classical canonical structure that will later be promoted to commutators.
    - This is not quantum yet; it is a classical intermediate node.

---

## Unresolved or Conditional Relationships

### Critical Conditional Edges
1. **Lagrangian Existence:** Not every QFT has a local Lagrangian.
   - **Status:** Conditional – Module 2 relationships are **not universal QFT relationships**.

2. **Boundary Conditions:** The EL equations require boundary conditions to have a well-defined Cauchy problem.
   - **Not established:** Which boundary conditions are physically admissible for general QFT.

3. **Degenerate Lagrangians:** For gauge theories, the canonical momentum is not independent; $\Pi$ is constrained.
   - **Unresolved:** The exact constrained Hamiltonian structure requires Dirac's method; we have not mapped it in detail.

4. **Quantum–Classical Gap:** EL equations describe classical field dynamics.
   - The quantum equations (Heisenberg equations) are not the same; they include $\hat{\Phi}$ and commutators.
   - **Not established:** The bridge from classical EL to quantum operator equations. This requires Module 3.

5. **Higher-Derivative Theories:** If $\mathcal{L}$ depends on $\partial_\mu\partial_\nu\Phi$, the EL equations change (Ostrogradsky).
   - **Not established:** We assumed first-order derivatives. This is a hidden assumption.

6. **Topological Terms:** Terms like $\theta F\tilde{F}$ do not affect EL equations (total derivatives) but affect quantum amplitudes.
   - **Not established:** The relationship between terms that vanish by $\delta S$ and physical consequences (anomalies, instantons).

7. **Effective Action:** The classical action $S$ is not the same as the quantum effective action $\Gamma[\Phi]$.
   - **Not established:** This requires Module 4 (generating functionals).

8. **Hamiltonian Positivity:** The Hamiltonian $H$ may not be bounded below for unstable theories.
   - **Not established:** Stability conditions are model-dependent.

---

## Dependencies Propagating from Module 2

### To Module 3 (Quantization)
- The canonical momentum $\Pi$ will be promoted to an operator.
- The Poisson brackets will become (anti)commutators.
- The Hamiltonian $H$ will generate time evolution in the Heisenberg picture.

**Critical limitation:** The canonical quantization route requires a non-degenerate Lagrangian with a well-defined Hamiltonian. Gauge theories need a modified route (e.g., Dirac brackets, BRST).

### To Module 4 (Propagation)
- The EL equations (linearized) yield classical Green functions.
- These will become quantum propagators after quantization.

### To Module 5 (Symmetry)
- Symmetries of $\mathcal{L}$ yield Noether currents via EL equations.
- This bridge is contingent on $\mathcal{L}$.

### To Module 6 (Renormalization)
- Dimensional analysis of couplings determines whether interactions are relevant/marginal/irrelevant.
- This is exact at the classical level but receives quantum corrections.

---

## Epistemic Classification Summary (Module 2)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 6 |
| Derived | 6 |
| Conditional | 16 |
| Model-Dependent | 6 |
| Constraint | 3 |
| Approximate | 1 |
| **Total** | **38** |

---

## Key Open Questions After Module 2

1. **Is the variational principle $\delta S=0$ necessary for QFT?**
   - No – some QFTs (e.g., algebraic) do not start from an action.
   - Therefore, EL equations are not universal.

2. **Can the Hamiltonian be defined without a Lagrangian?**
   - In algebraic QFT, the Hamiltonian is a generator of time translations, often defined via modular theory or from the net of algebras.
   - Therefore, $\mathcal{L} \to H$ is one route, not the only route.

3. **What is the exact relationship between classical constraints and quantum constraints?**
   - Gauge constraints become conditions on physical states: $\hat{G}|\Psi\rangle = 0$.
   - This bridge is not established in Module 2; it requires Module 5.

4. **Does the action $S$ determine the quantum theory uniquely?**
   - No – different Lagrangians can yield the same S-matrix (field redefinitions, equivalence theorems).
   - The action is a representation, not the theory itself.

---

# STATE OF MODULE 2

**Established:**
- Action as integral of Lagrangian (where applicable).
- Euler–Lagrange equations from variational principle.
- Canonical momenta and Hamiltonian via Legendre transform.
- Hamilton's equations as equivalent dynamics.
- Dimensional analysis of parameters.

**Not Established:**
- Universal validity of Lagrangian formulation.
- Quantization of the canonical structure.
- Operator equations of motion (Heisenberg).
- Constraint quantization for gauge theories.
- Quantum effective action.

**Mathematical Gaps:**
- No proof that a given Lagrangian yields a well-posed Cauchy problem for all field configurations.
- No mapping of degenerate Lagrangian constraints beyond flagging them.
- No bridge from classical Green functions to quantum propagators.

---

# MODULE 3 — QUANTIZATION AND OPERATOR STRUCTURE

## 3.1 CANONICAL QUANTIZATION

### Node Definitions

**N3.1.1:** Canonical quantization map

A rule promoting classical fields and momenta to operators on a Hilbert space:
$$\Phi_i(x) \to \hat{\Phi}_i(x), \qquad \Pi_i(x) \to \hat{\Pi}_i(x)$$

- Assumption: Classical canonical variables exist (Module 2).
- Status: Conditional on canonical formulation.

**N3.1.2:** Equal-time (anti)commutation relations

For bosonic fields:
$$[\hat{\Phi}_i(t,\mathbf{x}), \hat{\Pi}_j(t,\mathbf{y})] = i\hbar\,\delta_{ij}\,\delta^{(d-1)}(\mathbf{x}-\mathbf{y})$$
$$[\hat{\Phi}_i(t,\mathbf{x}), \hat{\Phi}_j(t,\mathbf{y})] = [\hat{\Pi}_i(t,\mathbf{x}), \hat{\Pi}_j(t,\mathbf{y})] = 0$$

For fermionic fields:
$$\{\hat{\psi}_\alpha(t,\mathbf{x}), \hat{\pi}_\beta(t,\mathbf{y})\} = i\hbar\,\delta_{\alpha\beta}\,\delta^{(d-1)}(\mathbf{x}-\mathbf{y})$$
(and anti-commutators vanish).

- Status: Conditional on canonical quantization and field type.

**N3.1.3:** Creation and annihilation operators (free theory)

For a free scalar field, mode expansion:
$$\hat{\phi}(x) = \int \frac{d^{d-1}\mathbf{p}}{(2\pi)^{d-1}2E_p} \left( a_{\mathbf{p}} e^{-ip\cdot x} + a_{\mathbf{p}}^\dagger e^{ip\cdot x} \right)$$
with $[a_{\mathbf{p}}, a_{\mathbf{q}}^\dagger] = (2\pi)^{d-1}2E_p\,\delta^{(d-1)}(\mathbf{p}-\mathbf{q})$.

- Status: Conditional on free theory and particle interpretation.

**N3.1.4:** Fock space representation (free theory)

The Hilbert space is built from the vacuum by applying creation operators: $\mathcal{F} = \bigoplus_n \mathcal{H}_n$.

- Status: Conditional on free theory.

**N3.1.5:** Normal ordering $:\mathcal{O}:$

Moving all creation operators to the left of annihilation operators, subtracting vacuum expectation values.

- Status: Definitional, used to define finite operator products.

**N3.1.6:** Time-ordering operator $T$

For operators $\mathcal{O}_1(x_1), \ldots, \mathcal{O}_n(x_n)$:
$$T\{\mathcal{O}_1(x_1)\cdots\mathcal{O}_n(x_n)\} = \sum_{\sigma} \theta(t_{\sigma(1)} > \cdots > t_{\sigma(n)})\, \mathcal{O}_{\sigma(1)}(x_{\sigma(1)})\cdots \mathcal{O}_{\sigma(n)}(x_{\sigma(n)})$$

- Status: Definitional.

**N3.1.7:** Heisenberg picture

Operators evolve in time:
$$\hat{\mathcal{O}}_H(t) = e^{i\hat{H}t/\hbar}\,\hat{\mathcal{O}}_S\,e^{-i\hat{H}t/\hbar}$$
States are time-independent.

- Status: Conditional on Hamiltonian and Hilbert space.

**N3.1.8:** Schrödinger picture

States evolve: $|\Psi(t)\rangle_S = e^{-i\hat{H}t/\hbar}|\Psi(0)\rangle_S$; operators are time-independent.

- Status: Conditional on Hamiltonian.

**N3.1.9:** Interaction picture

Split $\hat{H} = \hat{H}_0 + \hat{H}_{\text{int}}$. Operators evolve with $\hat{H}_0$; states evolve with $\hat{H}_{\text{int}}$.

- Status: Conditional on perturbative splitting.

**N3.1.10:** Heisenberg equation of motion

For any operator $\hat{\mathcal{O}}$:
$$\frac{d\hat{\mathcal{O}}_H}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{\mathcal{O}}_H] + \frac{\partial\hat{\mathcal{O}}_H}{\partial t}$$

- Status: Derived.

**N3.1.11:** Quantum equations of motion

Heisenberg equation applied to field operators:
$$\partial_\mu\hat{\Phi} = \frac{i}{\hbar}[\hat{H}, \hat{\Phi}], \quad \partial_\mu\hat{\Pi} = \frac{i}{\hbar}[\hat{H}, \hat{\Pi}]$$
(plus equations equivalent to EL for operators).

- Status: Conditional on canonical structure.

**N3.1.12:** Ordering ambiguities

Products of non-commuting operators at the same point are not uniquely defined; require renormalization.

- Status: Unresolved, regularization-dependent.

---

## 3.2 PATH-INTEGRAL QUANTIZATION

**N3.2.1:** Path-integral quantization prescription

Transition amplitudes are expressed as functional integrals over classical fields:
$$\langle \Phi_f, t_f | \Phi_i, t_i \rangle = \int_{\Phi(t_i)=\Phi_i}^{\Phi(t_f)=\Phi_f} \mathcal{D}\Phi\, e^{\frac{i}{\hbar}S[\Phi]}$$

- Status: Formal, conditional on path-integral formulation.

**N3.2.2:** Generating functional $Z[J]$

$$Z[J] = \int \mathcal{D}\Phi\, e^{\frac{i}{\hbar}\left(S[\Phi] + \int J\Phi\right)}$$

- Status: Formal, conditional on path-integral.

**N3.2.3:** $n$-point functions from $Z[J]$

$$\langle 0|T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}|0\rangle = \frac{\hbar^n}{i^n}\frac{\delta^n Z[J]}{\delta J(x_1)\cdots\delta J(x_n)}\bigg|_{J=0}$$

- Status: Formal, conditional on $Z[J]$ and vacuum.

**N3.2.4:** Connected generating functional $W[J] = -i\hbar \ln Z[J]$

Then connected $n$-point functions are functional derivatives of $W[J]$.

- Status: Definitional.

**N3.2.5:** Effective action $\Gamma[\phi]$

Legendre transform of $W[J]$:
$$\Gamma[\phi] = W[J] - \int J\phi, \qquad \phi(x) = \frac{\delta W[J]}{\delta J(x)}$$

- Status: Conditional on invertibility of $\phi(J)$.

**N3.2.6:** Schwinger–Dyson equations

Functional differential equations relating $Z[J]$ to the classical action:
$$\left( \frac{\delta S}{\delta\phi(x)}\bigg|_{\phi = \frac{\delta}{\delta J}} + J(x) \right) Z[J] = 0$$

- Status: Exact (formal) if path integral is well-defined.

**N3.2.7:** Faddeev–Popov determinant

For gauge theories, introduce gauge-fixing and ghost determinants to define the path integral:
$$Z[J] = \int \mathcal{D}A\, \delta(G[A]) \det(\Delta_{\text{FP}})\, e^{iS[A] + i\int JA}$$

- Status: Conditional on gauge theory.

**N3.2.8:** Path-integral measure $\mathcal{D}\Phi$

Formal infinite-dimensional integration over field configurations. Not rigorously defined in general.

- Status: Formal, mathematically unresolved in interacting QFT.

---

## 3.3 BRIDGES BETWEEN FORMULATIONS

**N3.3.1:** Correspondence between operator and path-integral correlation functions

Formally, the time-ordered vacuum expectation values equal the path-integral $n$-point functions:
$$\langle 0|T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}|0\rangle = \frac{\hbar^n}{i^n}\frac{\delta^n Z[J]}{\delta J(x_1)\cdots\delta J(x_n)}\bigg|_{J=0}$$

- Status: Formal, not rigorously proven for interacting theories.

**N3.3.2:** Dyson series from path integral

Perturbative expansion of $Z[J]$ around the free theory yields the same Feynman diagrams as canonical perturbation theory.

- Status: Conditional on perturbative expansion and regularization.

**N3.3.3:** LSZ reduction formula

Relates scattering amplitudes to time-ordered correlation functions:
$$\langle \mathbf{p}_1\cdots\mathbf{p}_n | S | \mathbf{k}_1\cdots\mathbf{k}_m \rangle \propto \lim_{\text{on-shell}} \left[ \prod_i (p_i^2 - m^2) \prod_j (k_j^2 - m^2) \right] \langle 0|T\{\phi(x_1)\cdots\phi(x_n)\}|0\rangle$$

- Status: Conditional on asymptotic states and analyticity.

**N3.3.4:** Canonical–path-integral equivalence

The two quantization methods are expected to yield the same physical predictions (S-matrix, correlators) when both are well-defined. However, a general proof does not exist for interacting theories.

- Status: Assumed, not rigorously established.

---

# RELATIONSHIP TABLE — MODULE 3

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N2.3.1 $\Pi$ (classical) | N3.1.1 Quantization map | Quantization | $\Phi_i(x) \to \hat{\Phi}_i(x)$, $\Pi_i(x) \to \hat{\Pi}_i(x)$ | Canonical quantization | Unidirectional | Local (operator) | Formal | Quantization-dependent | None | Conditional |
| N2.3.6 Poisson brackets | N3.1.2 Commutators | Quantization | $\{\cdot,\cdot\}_{\text{PB}} \to \frac{i}{\hbar}[\cdot,\cdot]$ (bosons) or anticommutator (fermions) | Canonical quantization | Unidirectional | Local | Exact (formal) | Quantization-dependent | Quantum dynamics | Conditional |
| N3.1.2 Commutators | N3.1.3 Creation/annihilation | Derived | Mode expansion from free field solutions | Free theory, particle interpretation | Unidirectional | Nonlocal (momentum space) | Exact (free) | Independent | Particle states | Conditional |
| N3.1.3 $a,a^\dagger$ | N3.1.4 Fock space | Construction | $\mathcal{F} = \bigoplus_n (a^\dagger)^n|0\rangle$ | Free theory | Unidirectional | Global | Exact | Independent | Particle spectrum | Conditional |
| N3.1.3 $a,a^\dagger$ | N3.1.5 Normal ordering | Definitional | $:\mathcal{O}:$ moves $a^\dagger$ left, $a$ right | Free theory | Unidirectional | Local | Exact | Independent | Finite vacuum expectations | Definitional |
| N3.1.6 Time-ordering | N3.1.5 Normal ordering | Relationship | Wick's theorem: $T\{\phi_1\cdots\phi_n\} = :\phi_1\cdots\phi_n: + \text{contractions}$ | Free fields | Unidirectional | Local | Exact | Independent | Correlators | Derived |
| N3.1.7 Heisenberg picture | N3.1.8 Schrödinger picture | Unitary equivalence | $\mathcal{O}_H = e^{iHt/\hbar}\mathcal{O}_S e^{-iHt/\hbar}$, $|\Psi\rangle_H = e^{iHt/\hbar}|\Psi\rangle_S$ | Hamiltonian self-adjoint | Bidirectional | Global | Exact | Picture-independent | Same expectation values | Definitional |
| N3.1.7 Heisenberg | N3.1.10 Heisenberg equation | Dynamical | $d\mathcal{O}_H/dt = \frac{i}{\hbar}[H,\mathcal{O}_H] + \partial_t\mathcal{O}_H$ | Heisenberg picture | Unidirectional | Local (operator) | Exact | Independent | Time evolution | Derived |
| N3.1.10 Heisenberg eq | N2.2.3 EL equations | Quantization | Heisenberg equation for $\hat{\Phi}$ yields $\partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\hat{\Phi})) - \partial\mathcal{L}/\partial\hat{\Phi} = 0$ as operator equation | Lagrangian + quantization | Unidirectional | Local | Exact (formal) | Quantization-dependent | Operator dynamics | Derived |
| N3.1.10 Heisenberg eq | N3.1.11 Quantum field eq | Identity | Same as above | - | Bidirectional | Local | Exact (formal) | - | - | Derived |
| N3.1.12 Ordering ambiguities | N2.1.2 $\mathcal{L}$ | Constraint | Products like $\hat{\Phi}^2$ require definition; different orders yield different Hamiltonians | Non-commuting operators | Unidirectional | Local | Unresolved | Scheme-dependent | Observable corrections | Unresolved |
| N3.2.1 Path integral | N2.1.1 $S$ | Quantization | Amplitude = $\int \mathcal{D}\Phi\, e^{iS[\Phi]/\hbar}$ | Path-integral formulation | Unidirectional | Nonlocal (functional integral) | Formal | Gauge-fixing dependent | Transition amplitudes | Conditional |
| N3.2.2 $Z[J]$ | N3.2.1 Path integral | Definitional | $Z[J] = \int \mathcal{D}\Phi\, e^{i(S + \int J\Phi)/\hbar}$ | Path-integral formulation | Unidirectional | Nonlocal | Formal | Gauge-fixing dependent | Generating functional | Conditional |
| N3.2.2 $Z[J]$ | N3.3.1 Correlators | Functional derivative | $\langle T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}\rangle = \frac{\hbar^n}{i^n}\frac{\delta^n Z}{\delta J(x_1)\cdots\delta J(x_n)}\big|_{J=0}$ | Path-integral + vacuum | Bidirectional | Local (in $x$) | Formal | Gauge-fixing dependent (for gauge-invariant correlators, cancels) | Correlations | Conditional |
| N3.2.2 $Z[J]$ | N3.2.4 $W[J]$ | Algebraic | $W[J] = -i\hbar \ln Z[J]$ | $Z[J] \neq 0$ | Unidirectional | Global | Formal | Gauge-dependent | Connected correlators | Definitional |
| N3.2.4 $W[J]$ | N3.2.5 $\Gamma[\phi]$ | Legendre transform | $\Gamma[\phi] = W[J] - \int J\phi$, $\phi = \delta W/\delta J$ | Invertibility | Bidirectional | Nonlocal | Formal | Gauge-dependent (until gauge-fixed) | Quantum effective action | Conditional |
| N3.2.2 $Z[J]$ | N3.2.6 Schwinger–Dyson | Functional equation | $\left( \frac{\delta S}{\delta\phi}\big|_{\phi=\frac{\delta}{\delta J}} + J(x) \right) Z[J] = 0$ | Path-integral well-defined | Unidirectional | Local (in $x$) | Exact (formal) | Gauge-dependent | Ward identities | Derived |
| N3.2.1 Path integral | N3.2.8 Measure $\mathcal{D}\Phi$ | Definitional | Formal infinite product $\prod_x d\Phi(x)$ | Path-integral | Unidirectional | Nonlocal | Formal | Representation-dependent | None | Formal/Unresolved |
| N3.1.2 Commutators | N3.2.1 Path integral | Equivalence (assumed) | Canonical quantization and path integral yield same time-ordered correlators | Interacting QFT | Bidirectional | Global | Unproven | Quantization-independent (if true) | Physical predictions | Assumed/Unresolved |
| N3.1.3 $a,a^\dagger$ | N3.2.2 $Z[J]$ (free) | Correspondence | For free theory, $Z_0[J] = \exp\left(\frac{i}{2\hbar}\int J G_F J\right)$ | Free theory | Unidirectional | Nonlocal | Exact (free) | Independent | Propagator | Derived |
| N3.3.3 LSZ formula | N3.3.1 Correlators | Scattering | Amplitudes from pole residues of correlators | Asymptotic states, on-shell limit | Unidirectional | Nonlocal (momentum) | Approx (perturbative) | Gauge-invariant (physical) | Scattering cross-sections | Conditional |
| N3.1.9 Interaction picture | N3.2.2 $Z[J]$ | Perturbative expansion | $Z[J] = \sum_n \frac{i^n}{\hbar^n n!}\int \cdots \langle 0|T\{\mathcal{L}_{\text{int}}^n e^{i\int J\phi}\}|0\rangle$ | Perturbative splitting | Unidirectional | Nonlocal | Approx (series) | Gauge-dependent (unless gauge-fixed) | S-matrix elements | Conditional |
| N3.1.7 Heisenberg picture | N3.3.1 Correlators | Relationship | Time-ordered correlators are Heisenberg picture matrix elements | None | Unidirectional | Local | Exact (formal) | Independent | Correlations | Definitional |
| N3.1.5 Normal ordering | N3.1.12 Ordering ambiguities | Resolution (partial) | Normal ordering defines a specific operator ordering, but not unique | Free fields | Unidirectional | Local | Exact | Scheme-dependent | None | Conditional |

---

# MODULE 3 SYNTHESIS

## Relationships Established

### Canonical Quantization Route
1. **Classical to Quantum:** $\Phi,\Pi \to \hat{\Phi},\hat{\Pi}$ via promotion to operators.
   - Poisson brackets become (anti)commutators: $\{\cdot,\cdot\}_{\text{PB}} \to \frac{i}{\hbar}[\cdot,\cdot]$.
   - This is **conditional** on having a well-defined canonical structure.

2. **Free Field Construction:** Creation/annihilation operators $a,a^\dagger$ yield Fock space and particle interpretation.
   - This is **exact only for free theories**; interactions require renormalization.

3. **Heisenberg Equation:** Operator evolution driven by $\hat{H}$:
   - $d\hat{\mathcal{O}}/dt = \frac{i}{\hbar}[\hat{H},\hat{\mathcal{O}}] + \partial_t\hat{\mathcal{O}}$.
   - Applies to fields, yielding quantum equations of motion (formally identical to EL, but with operator ordering).

4. **Pictures:** Heisenberg, Schrödinger, Interaction pictures are unitarily equivalent if $\hat{H}$ is self-adjoint.

5. **Ordering Ambiguities:** Products of non-commuting operators at the same point are not uniquely defined.
   - Normal ordering is one choice, but not the only one.
   - This ambiguity signals the need for renormalization (Module 6).

### Path-Integral Quantization Route
6. **Generating Functional:** $Z[J] = \int \mathcal{D}\Phi\, e^{i(S + \int J\Phi)/\hbar}$.
   - This is a formal object; the measure $\mathcal{D}\Phi$ is not rigorously defined in general.
   - Yet it yields a powerful computational framework via functional differentiation.

7. **Correlators from $Z[J]$:** Time-ordered correlation functions are obtained as functional derivatives of $Z[J]$.
   - This is the main bridge to observables (via LSZ).

8. **Connected and Effective Functionals:** $W[J] = -i\hbar\ln Z[J]$ gives connected correlators; $\Gamma[\phi]$ is the effective action (Legendre transform).
   - These are central to renormalization and quantum equations of motion.

9. **Schwinger–Dyson Equations:** Exact functional equations relating $Z[J]$ to the classical action. These are quantum analogues of the classical EL equations.

10. **Gauge Theory Path Integral:** Requires gauge fixing and Faddeev–Popov determinant (or BRST), which we flag but do not fully map until Module 5.

### Canonical vs. Path-Integral Correspondence
11. **Formal Equivalence Assumed:** The two methods are expected to yield the same time-ordered correlators in overlapping domains, but a general rigorous equivalence theorem for interacting continuum theories in arbitrary dimensions is not established.
   - This is a **major unresolved structural issue for general interacting continuum theories under the stated assumptions**.

12. **Perturbative Equivalence:** In perturbation theory, both methods produce the same Feynman diagrams (after appropriate gauge fixing and regularization). This is well-established order-by-order.

13. **LSZ Formula:** Bridges correlators to scattering amplitudes, providing observable predictions.

---

## Unresolved or Conditional Relationships

### Critical Unresolved Issues
1. **Path-Integral Measure:** $\mathcal{D}\Phi$ is not a well-defined mathematical object for interacting QFT in $d>2$ (except for some exactly solvable cases). We mark this as **[Formal/Unresolved]**.

2. **Equivalence of Canonical and Path-Integral Quantization:** No general proof exists. The assumption that they yield the same physics is a foundational pillar, but not established.

3. **Operator Domain and Self-Adjointness:** Quantum field operators are unbounded; their domains are dense but not the whole Hilbert space. The commutation relations are only valid on suitable domains. This is often glossed over.

4. **Haag's Theorem:** In interacting QFT, the interaction picture is not unitarily equivalent to the free picture (Haag's theorem). This undermines the standard perturbative splitting $\hat{H} = \hat{H}_0 + \hat{H}_{\text{int}}$ in infinite volume.
   - **We have not yet mapped this consequence.** It affects the validity of the Dyson series and the perturbative expansion.

5. **Existence of Interacting QFT in $d=4$:** Rigorous construction of interacting QFT in 4 dimensions is a Millennium Problem; no mathematically rigorous examples exist (except trivial theories). This is a foundational unresolved issue.

6. **Ordering Ambiguities and Renormalization:** We have flagged ordering ambiguities, but the full mapping to renormalization (counterterms, etc.) is deferred to Module 6.

7. **Gauge Quantization:** We have not specified the full BRST or Dirac quantization for gauge theories; this requires Module 5.

---

## Dependencies Propagating from Module 3

### To Module 4 (Correlation and Propagation)
- The two-point function $\langle 0|T\{\hat{\Phi}(x)\hat{\Phi}(y)\}|0\rangle$ will be derived from $Z[J]$.
- Propagators will be defined as the inverse of the free-field kinetic operator.

### To Module 5 (Symmetry and Gauge)
- Ward identities follow from Schwinger–Dyson equations and gauge invariance.
- Gauge fixing in path integral leads to BRST symmetry.

### To Module 6 (Renormalization)
- The ordering ambiguities and divergences in $Z[J]$ require regularization and renormalization.
- The effective action $\Gamma[\phi]$ is the central object for renormalization.

### To Module 7 (Spectral and Particle Structure)
- LSZ formula connects correlators to S-matrix and particle poles.
- Spectral representation of the two-point function yields mass spectrum.

### To Module 8 (Perturbation Mapping)
- The perturbative expansion of $Z[J]$ is the basis for response functions.

---

## Epistemic Classification Summary (Module 3)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 7 |
| Derived | 7 |
| Conditional | 14 |
| Formal | 7 |
| Assumed/Unresolved | 3 |
| Approx | 2 |
| **Total** | **40** |

---

## Key Open Questions After Module 3

1. **Is canonical quantization unique?**
   - No – ordering ambiguities, representation choices (e.g., different vacua) lead to inequivalent quantizations.

2. **Is the path-integral measure well-defined for interacting theories?**
   - Not generally. It requires regularization and renormalization, which are defined perturbatively. Non-perturbative definitions exist in lattice QFT, but continuum limit is nontrivial.

3. **Does the path integral actually compute the same correlators as the operator formalism?**
   - This is assumed, not proven. The equivalence is a working hypothesis of QFT.

4. **What is the status of Haag's theorem?**
   - It shows that the interaction picture (and thus the standard perturbative expansion) is not rigorous. Yet perturbative QFT works empirically. This is a deep unresolved issue.

5. **How do ordering ambiguities affect physical predictions?**
   - They are absorbed into renormalization of parameters and operators; the physical S-matrix is finite and scheme-independent. But the mapping is not automatic; it requires careful renormalization.

---

# STATE OF MODULE 3

**Established:**
- Canonical quantization map and commutation relations.
- Creation/annihilation operators and Fock space (free theory).
- Heisenberg picture and equations of motion.
- Path-integral generating functional and correlators.
- Formal equivalence via functional derivatives.
- Schwinger–Dyson equations.

**Not Established:**
- Rigorous definition of path-integral measure.
- Proof of equivalence between canonical and path-integral quantization.
- Resolution of Haag's theorem.
- Existence of interacting QFT in $d=4$.
- Complete gauge quantization (deferred to Module 5).

**Mathematical Gaps:**
- Domain of operators not specified.
- Unbounded operator algebra not rigorously defined.
- Functional integration over infinite-dimensional spaces not well-defined.
- Legendre transform between $W[J]$ and $\Gamma[\phi]$ may be singular.

---

# MODULE 4 — CORRELATION, GREEN FUNCTIONS, AND PROPAGATION

## 4.1 CORRELATION FUNCTIONS

### Node Definitions

**N4.1.1:** Wightman function (two-point)

For a scalar field:
$$\mathcal{W}(x,y) = \langle 0|\hat{\Phi}(x)\hat{\Phi}(y)|0\rangle$$

- The non-time-ordered vacuum expectation value.
- Status: Conditional on vacuum state and field operators.

**N4.1.2:** Time-ordered two-point function (Feynman propagator)

$$G_F(x,y) = \langle 0|T\{\hat{\Phi}(x)\hat{\Phi}(y)\}|0\rangle$$

- Status: Conditional on vacuum and time-ordering.

**N4.1.3:** Retarded two-point function

$$G_R(x,y) = -i\,\theta(x^0 - y^0)\,\langle 0|[\hat{\Phi}(x), \hat{\Phi}(y)]|0\rangle$$

- Status: Conditional on vacuum and commutator.

**N4.1.4:** Advanced two-point function

$$G_A(x,y) = i\,\theta(y^0 - x^0)\,\langle 0|[\hat{\Phi}(x), \hat{\Phi}(y)]|0\rangle$$

- Status: Conditional on vacuum and commutator.

**N4.1.5:** General $n$-point Wightman function

$$\mathcal{W}_n(x_1,\ldots,x_n) = \langle 0|\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)|0\rangle$$

- Status: Conditional.

**N4.1.6:** Time-ordered $n$-point function

$$G_n(x_1,\ldots,x_n) = \langle 0|T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}|0\rangle$$

- Status: Conditional.

**N4.1.7:** Truncated/Connected $n$-point function

$G_n^c$ defined via the generating functional $W[J]$ (Module 3), or via cluster decomposition.

- Status: Conditional.

**N4.1.8:** Schwinger function (Euclidean)

For Euclidean QFT, the analytic continuation of the time-ordered correlator:
$$S_n(x_1,\ldots,x_n) = \langle \Phi(x_1)\cdots\Phi(x_n)\rangle_{\text{Euclidean}}$$

- Status: Conditional on Wick rotation.

---

## 4.2 PROPAGATORS AND GREEN FUNCTIONS

**N4.2.1:** Free scalar propagator (Feynman)

For a free scalar of mass $m$:
$$G_F^{(0)}(x-y) = \int \frac{d^d p}{(2\pi)^d} \frac{i}{p^2 - m^2 + i\epsilon} e^{-ip\cdot(x-y)}$$

- Status: Derived, exact for free theory.

**N4.2.2:** Retarded Green function (classical/quantum)

Satisfies the linearized field equation with a delta source and retarded boundary condition:
$$(\Box + m^2)G_R(x-y) = -\delta^{(d)}(x-y)$$
with support in the future light cone.

- Status: Derived.

**N4.2.3:** Advanced Green function

Same operator equation but with support in the past light cone.

- Status: Derived.

**N4.2.4:** Feynman Green function

Satisfies the same operator equation with $i\epsilon$ prescription; propagates both positive and negative frequency modes forward in time (within the time-ordered product).

- Status: Derived.

**N4.2.5:** Spectral density $\rho(s)$

The Källén–Lehmann representation for the two-point function:
$$G_F(p^2) = \int_0^\infty ds \frac{i\,\rho(s)}{p^2 - s + i\epsilon}$$

where $\rho(s) \ge 0$ and $\int_0^\infty ds\,\rho(s) = 1$ for unitarity.

- Status: Derived from axioms (Wightman).

**N4.2.6:** Field strength renormalization factor $Z$

From the spectral density, the residue at the one-particle pole:
$$\rho(s) = Z\,\delta(s - m^2) + \text{continuum}$$

- Status: Derived, model-dependent.

**N4.2.7:** Phase space measure

The measure in momentum integrals, e.g., $d\Phi_n$ for $n$-particle phase space.

- Status: Model-dependent.

---

## 4.3 GENERATING FUNCTIONALS AND CORRELATORS

**N4.3.1:** $Z[J]$ derivatives (repeated from Module 3, but now mapped explicitly)

$$\frac{\delta^n Z[J]}{\delta J(x_1)\cdots\delta J(x_n)}\bigg|_{J=0} = \left(\frac{i}{\hbar}\right)^n \langle 0|T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}|0\rangle$$

- Status: Formal.

**N4.3.2:** $W[J]$ derivatives (connected correlators)

$$\frac{\delta^n W[J]}{\delta J(x_1)\cdots\delta J(x_n)}\bigg|_{J=0} = \langle 0|T\{\hat{\Phi}(x_1)\cdots\hat{\Phi}(x_n)\}|0\rangle_c$$

- Status: Definitional.

**N4.3.3:** Effective action $\Gamma[\phi]$ and propagator

The inverse of the full propagator is the second functional derivative of $\Gamma$:
$$G_F^{-1}(x,y) = -i\frac{\delta^2 \Gamma[\phi]}{\delta\phi(x)\delta\phi(y)}\bigg|_{\phi=0}$$

- Status: Conditional on $\Gamma$ defined.

**N4.3.4:** Self-energy $\Sigma$

Define the full propagator $G_F$ and the free propagator $G_F^{(0)}$:
$$G_F^{-1} = (G_F^{(0)})^{-1} - \Sigma$$

Thus $i\Sigma$ is the sum of one-particle irreducible (1PI) diagrams.

- Status: Definitional.

**N4.3.5:** Dyson equation (Schwinger–Dyson for propagator)

$$G_F = G_F^{(0)} + G_F^{(0)} \Sigma G_F$$

- Status: Derived.

**N4.3.6:** Bethe-Salpeter equation

For two-particle correlation functions, a linear integral equation relating the two-particle irreducible (2PI) kernel to the four-point function.

- Status: Conditional on model.

---

## 4.4 CAUSAL AND SUPPORT STRUCTURE

**N4.4.1:** Microcausality (local commutativity)

For spacelike-separated observables:
$$[\hat{\mathcal{O}}_1(x), \hat{\mathcal{O}}_2(y)] = 0 \quad \text{if } (x-y)^2 < 0$$

- Status: Axiom in algebraic and Wightman QFT.

**N4.4.2:** Commutator function $\Delta(x-y)$

$$\Delta(x-y) = \langle 0|[\hat{\Phi}(x),\hat{\Phi}(y)]|0\rangle = G_R - G_A$$

- Support: vanishes outside the light cone.
- Status: Derived from microcausality.

**N4.4.3:** Support of retarded/advanced functions

$\operatorname{supp} G_R \subseteq \{x-y : (x-y)^2 \ge 0,\; x^0 \ge y^0\}$.
$\operatorname{supp} G_A \subseteq \{x-y : (x-y)^2 \ge 0,\; x^0 \le y^0\}$.

- Status: Derived.

**N4.4.4:** Källén–Lehmann representation (causal)

$$\Delta(x-y) = \int_0^\infty ds\, \rho(s)\, i\Delta_s(x-y)$$

where $\Delta_s$ is the free commutator for mass $\sqrt{s}$.

- Status: Derived from spectral decomposition.

**N4.4.5:** Temporal ordering and analyticity

Time-ordered functions have analytic continuations into complex time planes; $G_F$ is the boundary value of an analytic function.

- Status: Conditional on Wightman axioms.

---

# RELATIONSHIP TABLE — MODULE 4

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N3.1.6 Time ordering | N3.3.1 Correlators | Definitional | $G_n(x_1,\ldots,x_n) = \langle 0|T\{\Phi(x_1)\cdots\Phi(x_n)\}|0\rangle$ | Vacuum, operators | Unidirectional | Local (in arguments) | Exact (formal) | Gauge-dependent (unless gauge-invariant operators) | Correlations | Conditional |
| N4.1.1 Wightman $\mathcal{W}$ | N4.1.2 Time-ordered $G_F$ | Linear combination | For $x^0>y^0$: $G_F = \mathcal{W}(x,y)$; for $x^0<y^0$: $G_F = \mathcal{W}(y,x)$ | Time-ordering | Bidirectional | Local (step functions) | Exact | Gauge-dependent | Same as Wightman | Derived |
| N4.1.1 Wightman $\mathcal{W}$ | N4.1.3 Retarded $G_R$ | Linear combination | $G_R(x,y) = -i\theta(x^0-y^0)(\mathcal{W}(x,y) - \mathcal{W}(y,x))$ | Vacuum, commutator | Unidirectional | Local | Exact | Gauge-dependent | Causal response | Derived |
| N4.1.1 Wightman $\mathcal{W}$ | N4.1.4 Advanced $G_A$ | Linear combination | $G_A(x,y) = i\theta(y^0-x^0)(\mathcal{W}(x,y) - \mathcal{W}(y,x))$ | Vacuum, commutator | Unidirectional | Local | Exact | Gauge-dependent | Causal response | Derived |
| N4.1.3 $G_R$ | N4.1.4 $G_A$ | Algebraic | $G_R - G_A = \langle 0|[\Phi(x),\Phi(y)]|0\rangle$ (up to factors) | None | Bidirectional | Local | Exact | Gauge-dependent | Commutator | Derived |
| N4.2.4 $G_F$ (Feynman) | N4.1.2 Time-ordered | Identity | Same object | - | Bidirectional | Local | Exact (formal) | Gauge-dependent | Scattering amplitudes | Definitional |
| N4.2.1 Free $G_F^{(0)}$ | N2.2.6 Green's function | Specialization | $(\Box + m^2)G_F^{(0)} = i\delta^{(d)}$ (or $-\delta$ depending on convention) | Free field | Unidirectional | Local | Exact | Independent | Free propagation | Derived |
| N4.2.1 $G_F^{(0)}$ | N4.2.2 $G_R$ | Boundary condition | $G_R$ has $i\epsilon$ with poles in lower half-plane for $p^0$ | Causality | Unidirectional | Local | Exact | Independent | Retarded response | Conditional |
| N4.2.1 $G_F^{(0)}$ | N4.2.3 $G_A$ | Boundary condition | $G_A$ has $i\epsilon$ with poles in upper half-plane | Causality | Unidirectional | Local | Exact | Independent | Advanced response | Conditional |
| N4.2.5 Spectral density $\rho$ | N4.2.1 $G_F^{(0)}$ | Integral representation | $G_F(p^2) = \int_0^\infty ds \frac{i\rho(s)}{p^2-s+i\epsilon}$ | Wightman axioms | Unidirectional | Nonlocal (in $s$) | Exact | Independent | Mass spectrum | Derived |
| N4.2.5 $\rho$ | N4.2.6 Field strength $Z$ | Residue | $\rho(s) = Z\delta(s-m^2) + \rho_{\text{cont}}(s)$ | One-particle pole | Unidirectional | Global | Exact | Scheme-dependent (but $Z$ renormalizes) | Residue of propagator | Derived |
| N4.2.5 $\rho$ | N4.4.1 Microcausality | Constraint | $\operatorname{supp} \Delta(x-y) \subseteq \text{light cone}$ imposes $\rho(s)$ smooth except for poles | Microcausality | Unidirectional | Global | Exact | Independent | Causal support | Conditional |
| N3.2.2 $Z[J]$ | N4.3.1 $n$-point functions | Functional derivative | $\frac{\delta^n Z}{\delta J^n}\big|_{0} = \left(\frac{i}{\hbar}\right)^n G_n$ | Path integral | Bidirectional | Nonlocal (functionals) | Formal | Gauge-dependent | Correlations | Formal |
| N3.2.4 $W[J]$ | N4.3.2 Connected $n$-point | Functional derivative | $\frac{\delta^n W}{\delta J^n}\big|_{0} = G_n^c$ | Connected generating functional | Bidirectional | Nonlocal | Formal | Gauge-dependent | Connected correlations | Formal |
| N3.2.5 $\Gamma[\phi]$ | N4.3.3 Propagator inverse | Functional derivative | $G_F^{-1} = -i \frac{\delta^2\Gamma}{\delta\phi\delta\phi}\big|_{\phi=0}$ | Legendre transform | Unidirectional | Nonlocal (but local at tree level) | Exact (formal) | Gauge-dependent | Full propagator | Conditional |
| N4.3.4 Self-energy $\Sigma$ | N4.2.1 Free propagator | Algebraic | $G_F^{-1} = (G_F^{(0)})^{-1} - \Sigma$ | Dyson equation | Bidirectional | Nonlocal (in momentum, local in x? No, generally nonlocal) | Exact (definition) | Scheme-dependent | Mass shift, decay | Definitional |
| N4.3.4 $\Sigma$ | N4.3.5 Dyson equation | Algebraic | $G_F = G_F^{(0)} + G_F^{(0)}\Sigma G_F$ | None | Bidirectional | Nonlocal | Exact (formal) | Scheme-dependent | Full propagator | Derived |
| N4.3.5 Dyson eq | N4.2.5 Spectral density | Derived | The spectral function is determined by $\Sigma$: $\rho(s) = -\frac{1}{\pi}\operatorname{Im} G_F(s+i\epsilon)$ | Analyticity | Unidirectional | Nonlocal | Exact | Scheme-dependent | Spectrum | Derived |
| N4.4.2 Commutator $\Delta$ | N4.1.3 $G_R$, N4.1.4 $G_A$ | Algebraic | $G_R - G_A = -i\Delta$ (depending on convention) | None | Bidirectional | Local | Exact | Gauge-dependent | Causal structure | Derived |
| N4.4.2 $\Delta$ | N4.4.3 Support | Constraint | $\operatorname{supp}\Delta \subset \{x: x^2 \ge 0\}$ | Microcausality | Unidirectional | Global | Exact | Independent | Causality | Conditional |
| N4.4.4 Källén–Lehmann | N4.2.5 $\rho$ | Representation | $\Delta(x-y) = \int_0^\infty ds\,\rho(s)\,i\Delta_s(x-y)$ | Spectral decomposition | Unidirectional | Nonlocal (in $s$) | Exact | Independent | Causal commutator | Derived |
| N4.2.5 $\rho$ | N4.2.1 Free $G_F$ | Relation | $\operatorname{Im} G_F(p^2) = -\pi \rho(p^2)$ (with sign convention) | Unitarity | Unidirectional | Nonlocal | Exact | Independent | Spectral function | Derived |
| N4.2.2 $G_R$ | N4.4.5 Analyticity | Boundary value | $G_R(p^0 + i\epsilon) = G_F(p^0)$ for $p^0>0$ etc. | Analytic continuation | Unidirectional | Nonlocal | Exact | Independent | Retarded vs Feynman | Conditional |
| N4.3.6 Bethe-Salpeter | N4.3.1 Four-point function | Integral equation | $G_4 = G_2G_2 + G_2G_2 K G_2G_2 + \cdots$ | Two-body scattering | Unidirectional | Nonlocal | Exact (formal) | Model-dependent | Two-body bound states | Conditional |

---

# MODULE 4 SYNTHESIS

## Relationships Established

### Correlation Functions Hierarchy
1. **Wightman → Time-ordered → Retarded/Advanced:** The three types are linearly related via step functions and commutators.
   - Time-ordered $G_F$ splits into Wightman functions depending on time order.
   - Retarded/Advanced are combinations of Wightman functions with step functions.

2. **$n$-point Functions from Generators:** Functional derivatives of $Z[J]$ yield time-ordered correlators; $W[J]$ yields connected correlators; $\Gamma[\phi]$ yields 1PI vertices.

3. **Free Propagator:** $G_F^{(0)}$ is the inverse of the kinetic operator:
   - $(\Box + m^2)G_F^{(0)} = i\delta$ (depending on convention).
   - Exact for free theory; serves as the base for perturbative expansions.

4. **Retarded/Advanced vs. Feynman:** Boundary conditions ($i\epsilon$ prescriptions) distinguish them.
   - Retarded: support in future light cone.
   - Advanced: support in past light cone.
   - Feynman: boundary value of analytic function; propagates both poles with $i\epsilon$.

### Spectral and Causal Structure
5. **Källén–Lehmann Representation:**
   - $G_F(p^2) = \int_0^\infty ds \frac{i\rho(s)}{p^2-s+i\epsilon}$.
   - $\rho(s) \ge 0$ by unitarity.
   - One-particle pole residue $Z$: $\rho(s) = Z\delta(s-m^2) + \rho_{\text{cont}}(s)$.
   - This is an **exact** consequence of Wightman axioms (if they hold).

6. **Microcausality:**
   - $[\mathcal{O}(x), \mathcal{O}(y)] = 0$ for spacelike separation.
   - Implies the commutator function $\Delta(x-y)$ has support only within (or on) the light cone.

7. **Self-Energy and Dyson Equation:**
   - Full propagator $G_F$ related to free propagator $G_F^{(0)}$ via self-energy $\Sigma$:
   - $G_F^{-1} = (G_F^{(0)})^{-1} - \Sigma$.
   - Dyson equation: $G_F = G_F^{(0)} + G_F^{(0)}\Sigma G_F$.
   - This is an **exact** relation (definitional), though $\Sigma$ is non-perturbatively defined.

---

## Unresolved or Conditional Relationships

### Critical Unresolved Issues
1. **Existence of $n$-point Functions in Interacting Theories:**
   - For $d=4$, interacting correlators are defined perturbatively. Non-perturbative existence is not rigorously proven.
   - Therefore, the functional derivative relations are formal; they are mathematically well-defined only if the generating functional exists.

2. **Källén–Lehmann Representation in Gauge Theories:**
   - For gauge fields, the spectral representation must be modified because of gauge redundancy (e.g., longitudinal modes, indefinite metric).
   - We have not mapped gauge-specific spectral representations (e.g., for $A_\mu$). This requires gauge fixing and Gupta-Bleuler or BRST.

3. **Analyticity Properties:**
   - The analytic continuation from Minkowski to Euclidean is assumed (Wick rotation).
   - For general backgrounds (curved spacetime), Wick rotation may not exist.

4. **Local vs. Nonlocal in $\Gamma$:**
   - $\Gamma[\phi]$ is generically nonlocal. Its second derivative yields the inverse propagator, which is nonlocal in general. At tree level it is local, but at loop level it develops nonlocalities.
   - The relationship between the effective action and the classical action is not a simple one; it involves quantum corrections.

5. **Microcausality vs. Spacelike Correlations:**
   - Microcausality does **not** imply that spacelike correlation functions vanish; only commutators vanish. Correlations can be nonzero for spacelike separation (e.g., vacuum entanglement). This is often misunderstood.

6. **Unitarity and Spectral Density Positivity:**
   - $\rho(s) \ge 0$ follows from unitarity (positive norm of states). For gauge theories, physical-state Hilbert space must be positive definite; gauge-violating modes are unphysical.
   - We have not established the positivity in gauge theories.

7. **Bethe–Salpeter Equation:**
   - This is model-dependent (requires 2PI kernel). It is an exact integral equation for the four-point function in bound-state problems but is not a universal QFT relation.

---

## Dependencies Propagating from Module 4

### To Module 5 (Symmetry and Gauge)
- Ward identities relate $n$-point functions via symmetry transformations.
- Gauge invariance imposes constraints on $\Sigma$ (e.g., Ward–Takahashi identities for QED).
- The spectral density for gauge fields requires gauge-invariant observables.

### To Module 6 (Renormalization)
- The self-energy $\Sigma$ is divergent; requires renormalization.
- The spectral density $\rho$ receives corrections order-by-order.
- The Dyson equation is the basis for renormalized perturbation theory.

### To Module 7 (Spectral and Particle Structure)
- Källén–Lehmann yields the mass spectrum (poles of the propagator).
- The residue $Z$ gives the field strength renormalization.
- Continuum contributions give multi-particle states.

### To Module 8 (Perturbation Mapping)
- Perturbing sources $J$ directly affects the correlators via functional derivatives.
- Perturbing couplings changes the self-energy and propagator.

---

## Epistemic Classification Summary (Module 4)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 8 |
| Derived | 14 |
| Conditional | 7 |
| Formal | 4 |
| **Total** | **33** |

---

## Key Open Questions After Module 4

1. **Does the Källén–Lehmann representation hold for all QFTs?**
   - It holds for Wightman theories (with positive metric). For gauge theories, it holds only for gauge-invariant correlators (e.g., scalar bound states), not for the gauge field itself.

2. **What is the exact relation between the retarded Green function and the response of the quantum field to a source?**
   - At the linear level, $G_R$ gives the response: $\delta\langle\Phi(x)\rangle = \int G_R(x-y) J(y)$.
   - For nonlinear theories, the response is corrected by higher $n$-point functions.

3. **Is the Dyson equation convergent?**
   - No—it is a formal resummation. The series may be asymptotic.

4. **How do nonlocalities in $\Gamma$ affect propagation?**
   - The propagation is no longer simply local; it is modified by quantum corrections. This is captured by the momentum-dependent self-energy.

5. **Can the spectral density be measured?**
   - Yes, indirectly via scattering cross-sections and decay rates. But it is not directly observable; it is a theoretical construct.

---

# STATE OF MODULE 4

**Established:**
- Classification of two-point functions (Wightman, time-ordered, retarded, advanced).
- Free propagator as inverse of kinetic operator.
- Källén–Lehmann spectral representation (exact under Wightman axioms).
- Dyson equation linking free and full propagator via self-energy.
- Support properties from microcausality.
- Relation between generating functionals and correlators.

**Not Established:**
- Existence of correlators beyond perturbation theory in $d=4$.
- General spectral representation for gauge fields.
- Full analytic structure (e.g., branch cuts, poles) beyond simple poles.
- Proper definition of the effective action in all regimes.

**Mathematical Gaps:**
- The inverse of the propagator $G_F^{-1}$ may not exist if the propagator has zeros.
- The Legendre transform defining $\Gamma$ may be singular.
- The spectral decomposition requires a complete set of states; not always known.

---

# MODULE 5 — SYMMETRY, CONSERVATION, AND GAUGE STRUCTURE

## 5.1 SYMMETRY AND NOETHER'S THEOREM

### Node Definitions

**N5.1.1:** Continuous global symmetry transformation

A one-parameter (or multi-parameter) family of field transformations:
$$\Phi_i(x) \to \Phi'_i(x) = \Phi_i(x) + \alpha \Delta \Phi_i(x) + \mathcal{O}(\alpha^2)$$
where $\alpha$ is a constant parameter (independent of $x$), and $\Delta \Phi_i$ is a function of the fields and derivatives.

- Status: Conditional on Lagrangian formulation.

**N5.1.2:** Invariance of the action under a symmetry

$$S[\Phi'] = S[\Phi]$$
equivalently, the variation of $\mathcal{L}$ is a total derivative:
$$\delta \mathcal{L} = \partial_\mu K^\mu$$
for some $K^\mu$.

- Status: Conditional on Lagrangian.

**N5.1.3:** Noether current $J^\mu(x)$

For a continuous symmetry with variation $\delta \Phi_i$:
$$J^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi_i)} \delta \Phi_i - K^\mu$$
(up to sign conventions).

- Status: Derived from invariance.

**N5.1.4:** Noether's theorem (classical)

If the action is invariant under a continuous symmetry, then:
$$\partial_\mu J^\mu = 0$$
on-shell (i.e., using the Euler-Lagrange equations).

- Status: Derived, conditional on Lagrangian.

**N5.1.5:** Conserved charge $Q$

$$Q = \int_{\Sigma_t} d^{d-1}x\, J^0(t,\mathbf{x})$$

- Status: Derived.

**N5.1.6:** Charge as generator

The conserved charge $Q$ generates the symmetry via the Poisson bracket (classical) or commutator (quantum):
$$\delta \Phi_i = \{\Phi_i, Q\}_{\text{PB}} \quad \text{(classical)}, \qquad \delta \hat{\Phi}_i = \frac{i}{\hbar}[\hat{Q}, \hat{\Phi}_i] \quad \text{(quantum)}$$

- Status: Conditional on canonical structure.

**N5.1.7:** Spacetime symmetries (Poincaré)

Translations: $\delta \Phi = -a^\mu \partial_\mu \Phi$ → Noether current is the energy-momentum tensor $T^{\mu\nu}$.
Lorentz transformations: $\delta \Phi = \omega^\mu_{\;\nu} x^\nu \partial_\mu \Phi + \text{spin part}$ → Noether current is $M^{\mu\nu\rho}$.

- Status: Conditional on Poincaré invariance.

**N5.1.8:** Internal symmetries (global, e.g., $U(1)$, $SU(N)$)

$\Phi_i \to \Phi_i + i\alpha (T^a)_{ij}\Phi_j$ → Noether current $J_a^\mu$.

- Status: Model-dependent.

---

## 5.2 GAUGE SYMMETRY (LOCAL)

**N5.2.1:** Local (gauge) transformation

$\alpha \to \alpha(x)$ (space-time dependent). The field transformation is:
$$\Phi_i(x) \to \Phi'_i(x) = e^{i\alpha(x) T^a} \Phi_i(x)$$
for matter fields.

- Status: Conditional on gauge theory.

**N5.2.2:** Gauge field $A_\mu^a(x)$ (connection)

Transforms inhomogeneously to compensate for the local transformation of matter fields:
$$A_\mu \to A'_\mu = U A_\mu U^{-1} + \frac{i}{g} U \partial_\mu U^{-1}$$
for non-Abelian gauge groups, or $A_\mu \to A_\mu + \partial_\mu \alpha$ for Abelian.

- Status: Conditional on gauge theory.

**N5.2.3:** Covariant derivative $D_\mu$

$$D_\mu \Phi = \partial_\mu \Phi - i g A_\mu^a T^a \Phi$$
(convention dependent).

- Property: $D_\mu \Phi$ transforms covariantly: $(D_\mu \Phi)' = U (D_\mu \Phi)$.

- Status: Definitional.

**N5.2.4:** Field strength $F_{\mu\nu}^a$

$$F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c$$
For Abelian: $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$.

- Transforms covariantly: $F_{\mu\nu} \to U F_{\mu\nu} U^{-1}$.

- Status: Definitional.

**N5.2.5:** Gauge-invariant kinetic term

$$\mathcal{L}_{\text{gauge}} = -\frac{1}{4} F_{\mu\nu}^a F^{a\mu\nu}$$

- Status: Definitional.

**N5.2.6:** Gauge orbit

The equivalence class of all field configurations related by gauge transformations:
$$[A] = \{A' : A' = U A U^{-1} + \frac{i}{g} U \partial U^{-1}, \, U \in \mathcal{G}\}$$

- Status: Definitional.

**N5.2.7:** Gauge redundancy

Gauge orbits represent the same physical configuration. The path integral overcounts gauge-equivalent configurations.

- Status: Constraint.

---

## 5.3 GAUGE FIXING AND BRST STRUCTURE

**N5.3.1:** Gauge-fixing condition $G[A] = 0$

A condition that selects one representative from each gauge orbit, e.g., $\partial^\mu A_\mu = 0$ (Lorenz gauge), $A_0 = 0$ (temporal gauge).

- Status: Conditional on gauge theory, not physical.

**N5.3.2:** Faddeev–Popov determinant $\Delta_{\text{FP}}[A]$

Defined by:
$$\Delta_{\text{FP}}[A] = \det\left( \frac{\delta G[A^\alpha]}{\delta \alpha} \right)$$
where $A^\alpha$ is the gauge-transformed field.

- Status: Conditional on gauge fixing.

**N5.3.3:** Faddeev–Popov ghost fields $c^a(x), \bar{c}^a(x)$

Ghosts are anticommuting scalar fields (Grassmann-valued) introduced to represent the determinant as a functional integral:
$$\det(M) = \int \mathcal{D}c\, \mathcal{D}\bar{c}\, e^{i\int \bar{c} M c}$$

- Status: Conditional, formal.

**N5.3.4:** BRST symmetry

A global fermionic symmetry of the gauge-fixed Lagrangian, combining gauge transformations with ghost transformations:
$$s A_\mu = D_\mu c, \qquad s c = -\frac{g}{2} f^{abc} c^b c^c, \qquad s \bar{c} = b, \qquad s b = 0$$
where $b$ is the Nakanishi-Lautrup auxiliary field.

- Status: Conditional on gauge theory and Faddeev–Popov.

**N5.3.5:** BRST charge $Q_B$

The generator of BRST transformations, satisfying:
$$Q_B^2 = 0 \quad (\text{nilpotent})$$

- Status: Derived.

**N5.3.6:** Physical state condition (BRST cohomology)

Physical states are in the kernel of $Q_B$ modulo its image:
$$\mathcal{H}_{\text{phys}} = \ker Q_B / \operatorname{im} Q_B$$

- Status: Conditional on BRST quantization.

---

## 5.4 WARD IDENTITIES AND ANOMALIES

**N5.4.1:** Ward identity (quantum)

The quantum analogue of Noether's theorem:
$$\partial_\mu \langle J^\mu(x) \mathcal{O}_1(x_1)\cdots\mathcal{O}_n(x_n)\rangle = \text{contact terms} - i \sum_i \delta(x-x_i) \langle \delta \mathcal{O}_i \cdots \rangle$$

- Status: Derived from path integral (via Schwinger–Dyson) or canonical commutators.

**N5.4.2:** Gauge Ward identity (Takahashi identity)

For QED: $\partial_\mu \langle j^\mu(x) \psi(x_1)\bar{\psi}(x_2)\rangle = -\delta(x-x_1)\langle \psi(x_1)\bar{\psi}(x_2)\rangle + \delta(x-x_2)\langle \psi(x_1)\bar{\psi}(x_2)\rangle$ (plus contact terms).

- Status: Conditional on gauge symmetry.

**N5.4.3:** Slavnov–Taylor identities

The BRST generalization of Ward identities for non-Abelian gauge theories.

- Status: Conditional on BRST.

**N5.4.4:** Anomaly

A classical symmetry that is not preserved by quantization:
$$\partial_\mu \langle J^\mu(x) \cdots \rangle \neq 0$$
even when the classical action is invariant.

- Status: Conditional on quantum theory.

**N5.4.5:** Chiral anomaly (axial anomaly)

For a chiral current $J^{5\mu} = \bar{\psi}\gamma^\mu\gamma^5\psi$:
$$\partial_\mu J^{5\mu} = \frac{g^2}{16\pi^2} \epsilon^{\mu\nu\rho\sigma} F_{\mu\nu} F_{\rho\sigma}$$
(in 4d, for a single fermion).

- Status: Derived, model-dependent.

**N5.4.6:** Gauge anomaly cancellation condition

For a consistent gauge theory, all gauge anomalies must cancel:
$$\sum_{\text{fermions}} \text{Tr}(T^a \{T^b, T^c\}) = 0$$
and related triangle conditions.

- Status: Conditional on gauge theory and perturbative consistency.

---

## 5.5 SPONTANEOUS SYMMETRY BREAKING

**N5.5.1:** Symmetry-breaking potential

A potential $V(\Phi)$ with a minimum at $\langle \Phi \rangle \neq 0$ that is not invariant under the full symmetry group.

- Status: Model-dependent.

**N5.5.2:** Goldstone's theorem

For each spontaneously broken continuous global symmetry, there is a massless scalar (Goldstone boson).

- Status: Conditional on global symmetry, relativistic theory.

**N5.5.3:** Goldstone boson $\pi(x)$

The field mode along the flat directions of the potential.

- Status: Model-dependent.

**N5.5.4:** Higgs mechanism

For a spontaneously broken local gauge symmetry, the Goldstone boson becomes the longitudinal mode of the massive gauge boson, giving it mass.

- Status: Conditional on gauge theory.

**N5.5.5:** Nambu–Goldstone effective action

The effective action for the Goldstone modes: $\Gamma[\pi] = \frac{1}{2} \int (\partial \pi)^2 + \text{higher-order terms}$.

- Status: Model-dependent.

---

# RELATIONSHIP TABLE — MODULE 5

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N5.1.1 Symmetry | N2.1.1 $S$ | Constraint | $S[\Phi'] = S[\Phi]$ | Lagrangian | Unidirectional | Global | Exact | Field-dependent | Symmetry of dynamics | Conditional |
| N5.1.1 Symmetry | N2.2.3 EL eq | Constraint | Symmetry of action implies solutions map to solutions | Lagrangian | Unidirectional | Local | Exact | Field-dependent | Degeneracy of solutions | Derived |
| N5.1.1 Symmetry | N5.1.3 $J^\mu$ | Noether | $J^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} \delta \Phi - K^\mu$ | Lagrangian, continuous symmetry | Unidirectional | Local | Exact | Field-dependent | Current | Derived |
| N5.1.3 $J^\mu$ | N5.1.4 Noether theorem | Differential | $\partial_\mu J^\mu = 0$ (on-shell) | EL equations | Unidirectional | Local | Exact | Field-dependent | Conservation | Derived |
| N5.1.3 $J^\mu$ | N5.1.5 $Q$ | Integral | $Q = \int_{\Sigma_t} d^{d-1}x\, J^0$ | Spacelike foliation | Unidirectional | Nonlocal (spatial) | Exact | Foliation-dependent | Charge observable | Conditional |
| N5.1.5 $Q$ | N5.1.6 Generator | Algebra | $[Q, \Phi] = -i\hbar \delta \Phi$ (quantum) | Canonical quantization | Bidirectional | Global (nonlocal operator) | Exact (formal) | Quantization-dependent | Symmetry transformations | Conditional |
| N5.1.7 Poincaré | N5.1.3 $J^\mu$ | Specialization | $T^{\mu\nu}$ for translations, $M^{\mu\nu\rho}$ for Lorentz | Poincaré symmetry | Unidirectional | Local | Exact | Independent | Energy-momentum, angular momentum | Conditional |
| N5.1.8 Internal symmetry | N5.1.3 $J^\mu$ | Specialization | $J_a^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \Phi)} iT^a \Phi$ | Internal symmetry group | Unidirectional | Local | Exact | Representation-dependent | Conserved charges (e.g., electric charge) | Model-Dependent |
| N5.2.1 Local transformation | N5.1.1 Global symmetry | Generalization | $\alpha \to \alpha(x)$ | Gauge theory | Unidirectional | Local | Exact | Gauge-dependent | Gauge redundancy | Conditional |
| N5.2.1 Local gauge | N5.2.2 $A_\mu$ | Definition | $A_\mu$ transforms to compensate local phase | Gauge theory | Unidirectional | Local | Exact | Gauge-dependent | Force mediation | Conditional |
| N5.2.2 $A_\mu$ | N5.2.3 $D_\mu$ | Definition | $D_\mu \Phi = \partial_\mu \Phi - ig A_\mu \Phi$ (scalar case) | Gauge theory + matter | Unidirectional | Local | Exact | Gauge-dependent | Covariant derivative | Definitional |
| N5.2.3 $D_\mu$ | N5.1.1 Global symmetry | Modification | $\partial_\mu \to D_\mu$ in Lagrangian to enforce local invariance | Gauge theory | Unidirectional | Local | Exact | Gauge-dependent | Minimal coupling | Definitional |
| N5.2.2 $A_\mu$ | N5.2.4 $F_{\mu\nu}$ | Differential | $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + g[A_\mu, A_\nu]$ (non-Abelian) | Gauge theory | Unidirectional | Local | Exact | Gauge-dependent (but transforms covariantly) | Field strength | Definitional |
| N5.2.4 $F_{\mu\nu}$ | N5.2.5 Gauge kinetic term | Definitional | $\mathcal{L}_{\text{gauge}} = -\frac{1}{4} F^{\mu\nu}F_{\mu\nu}$ | Gauge theory | Unidirectional | Local | Exact | Gauge-invariant | Gauge boson propagation | Definitional |
| N5.2.2 $A_\mu$ | N5.2.6 Gauge orbit | Equivalence | $[A] = \{A^g : g \in \mathcal{G}\}$ | Gauge group | Unidirectional | Nonlocal (group action) | Exact | Gauge-dependent | Redundancy | Definitional |
| N5.2.6 Gauge orbit | N5.2.7 Gauge redundancy | Constraint | Path integral over gauge orbits overcounts; divide by volume of $\mathcal{G}$ | Gauge theory | Unidirectional | Global | Exact | Gauge-dependent | Overcounting in path integral | Constraint |
| N5.3.1 Gauge fixing | N5.2.7 Redundancy | Resolution | $G[A] = 0$ selects one representative per orbit | Gauge theory | Unidirectional | Nonlocal (in practice) | Exact | Gauge-dependent | None (unphysical) | Conditional |
| N5.3.1 $G[A]$ | N5.3.2 FP det | Functional determinant | $\Delta_{\text{FP}} = \det\left(\frac{\delta G[A^\alpha]}{\delta \alpha}\right)$ | Gauge theory | Unidirectional | Nonlocal | Exact (formal) | Gauge-dependent | Ghost determinant | Conditional |
| N5.3.2 FP det | N5.3.3 Ghosts | Functional representation | $\det(M) = \int \mathcal{D}c\mathcal{D}\bar{c}\, e^{i\int \bar{c} M c}$ | Grassmann integration | Unidirectional | Nonlocal (functional) | Formal | Gauge-dependent | Ghost fields | Formal |
| N5.3.3 Ghosts | N5.3.4 BRST | Transformation | $s A = Dc, sc = -\frac{g}{2}[c,c], s\bar{c} = b, sb=0$ | Gauge theory | Unidirectional | Local | Exact (formal) | Gauge-dependent | BRST symmetry | Conditional |
| N5.3.4 BRST | N5.3.5 $Q_B$ | Noether | $Q_B = \int d^{d-1}x\, j^0_{\text{BRST}}$ | BRST Lagrangian | Unidirectional | Nonlocal | Exact (formal) | BRST-dependent | Nilpotent charge | Derived |
| N5.3.5 $Q_B$ | N5.3.6 Physical states | Constraint | $Q_B|\Psi\rangle = 0$, $|\Psi\rangle \sim |\Psi\rangle + Q_B|\chi\rangle$ | BRST cohomology | Unidirectional | Global | Exact | BRST-invariant | Physical Hilbert space | Conditional |
| N5.4.1 Ward identity | N5.1.4 Noether theorem | Quantum generalization | $\partial_\mu \langle J^\mu(x) \prod \mathcal{O}_i(x_i)\rangle = -i\sum_i \delta(x-x_i)\langle \delta \mathcal{O}_i \cdots \rangle$ | Path integral or commutators | Unidirectional | Local (with deltas) | Exact (formal) | Gauge-dependent | Quantum conservation | Derived |
| N5.4.1 Ward identity | N4.3.6 Schwinger-Dyson | Relationship | Ward identity is S-D equation for symmetry transformation | Path integral | Unidirectional | Local | Exact (formal) | Gauge-dependent | Symmetry constraints on correlators | Derived |
| N5.4.2 Gauge Ward | N5.4.1 Ward identity | Specialization | $\partial_\mu \langle j^\mu \cdots \rangle$ with contact terms for charged fields | QED/gauge theory | Unidirectional | Local | Exact (formal) | Gauge-dependent (but physical charges gauge-invariant) | Charge conservation | Conditional |
| N5.4.3 Slavnov-Taylor | N5.4.1 Ward identity | Generalization | BRST Ward identities for non-Abelian gauge theories | BRST | Unidirectional | Local | Exact (formal) | BRST-dependent | Gauge-invariant amplitudes | Conditional |
| N5.4.1 Ward identity | N5.4.4 Anomaly | Breakdown | $\partial_\mu \langle J^\mu(x)\cdots\rangle \neq 0$ despite classical invariance | Quantum theory, divergent diagrams | Unidirectional | Local | Exact (quantum) | Gauge-dependent (but physical anomaly gauge-invariant) | Violation of conservation | Conditional |
| N5.4.4 Anomaly | N5.4.5 Chiral anomaly | Specialization | $\partial_\mu J^{5\mu} = \frac{g^2}{16\pi^2} \epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Chiral fermions | Unidirectional | Local | Exact (1-loop) | Gauge-invariant (axial) | Pion decay, etc. | Model-Dependent |
| N5.4.5 Chiral anomaly | N5.4.6 Gauge anomaly | Distinction | Gauge anomalies must cancel; chiral anomalies may be physical (e.g., Adler-Bell-Jackiw) | Gauge theory | Unidirectional | Global | Exact | Gauge anomaly: gauge-dependent (inconsistent if present) | Consistency condition | Conditional |
| N5.4.6 Gauge anomaly | N5.3.6 Physical states | Constraint | Gauge anomaly makes $Q_B^2 \neq 0$; no physical Hilbert space | Gauge theory | Unidirectional | Global | Exact | Gauge-dependent | Theory inconsistent unless cancellation | Conditional |
| N5.5.1 Symmetry-breaking potential | N2.1.6 $V(\Phi)$ | Specialization | $V(\Phi)$ with degenerate minima | Scalar potential | Unidirectional | Local | Exact | Field-dependent | Vacuum structure | Model-Dependent |
| N5.5.1 Potential | N5.5.2 Goldstone theorem | Dynamical | Shift in field $\Phi \to \langle \Phi \rangle + \pi$ yields massless mode | Global symmetry | Unidirectional | Nonlocal (massless mode) | Exact (tree) | Field-dependent | Massless boson | Conditional |
| N5.5.2 Goldstone | N5.5.3 Goldstone boson | Identity | The massless mode is the Goldstone boson | Global SSB | Unidirectional | Local | Exact | Field-dependent | None (unless coupled) | Model-Dependent |
| N5.5.2 Goldstone | N5.2.2 $A_\mu$ (Higgs) | Mechanism | Gauge boson eats Goldstone, becomes massive | Local gauge SSB | Unidirectional | Local | Exact | Gauge-dependent | Massive gauge boson | Conditional |
| N5.5.4 Higgs mechanism | N5.2.5 Gauge kinetic | Modification | $\mathcal{L} = -\frac{1}{4}F^2 + \frac{1}{2}m_A^2 A^2$ after SSB | Local gauge SSB | Unidirectional | Local | Exact (tree) | Gauge-dependent | Massive vector bosons | Model-Dependent |
| N5.5.5 Goldstone effective action | N5.3.5 $Q_B$ | Relationship | Goldstone modes are BRST-exact in the Higgs phase (eaten) | BRST + Higgs | Unidirectional | Local | Exact | BRST-dependent | Unphysical modes | Conditional |

---

# MODULE 5 SYNTHESIS

## Relationships Established

### Symmetry, Noether, and Conservation
1. **Noether's Theorem Bridge**: Continuous symmetry of the action $\to$ conserved current $J^\mu$ $\to$ $\partial_\mu J^\mu = 0$ on-shell $\to$ conserved charge $Q$ (via spatial integral).
   - **Conditional on**: Lagrangian formulation and differentiable symmetries.
   - **Exact** at the classical level.

2. **Charge as Generator**: $Q$ generates the symmetry transformation through Poisson brackets (classical) or commutators (quantum).
   - This establishes the algebra of symmetries.
   - For Poincaré symmetry, $Q$ = energy-momentum $P^\mu$ and angular momentum $M^{\mu\nu}$.

3. **Spacetime vs. Internal**: Separate routes for Poincaré (universal if present) and internal symmetries (model-dependent).

### Gauge Structure vs. Physical Symmetry
4. **Gauge Redundancy**: Local gauge transformations are not physical symmetries; they are redundancies of the description.
   - Gauge orbits represent the same physical state.
   - The path integral must divide by the volume of the gauge group (or fix a gauge).

5. **Gauge Fields**: The gauge field $A_\mu$ is a connection; its transformation is inhomogeneous, unlike matter fields.
   - Covariant derivative $D_\mu$ replaces $\partial_\mu$ to maintain gauge invariance.
   - Field strength $F_{\mu\nu}$ transforms covariantly.

6. **Gauge Fixing**: Requires a gauge condition $G[A]=0$, introduces the Faddeev–Popov determinant $\Delta_{\text{FP}}$, which is represented by ghost fields $c,\bar{c}$.
   - Ghosts are unphysical (fermionic scalars).

7. **BRST Symmetry**: A global fermionic symmetry of the gauge-fixed action, with nilpotent charge $Q_B^2=0$.
   - Physical states are defined by BRST cohomology: $\ker Q_B / \operatorname{im} Q_B$.
   - This is the exact mathematical bridge from gauge redundancy to a well-defined physical Hilbert space.

### Ward Identities and Anomalies
8. **Quantum Ward Identities**: The quantum analogue of Noether's theorem, derived from the path integral (via Schwinger–Dyson) or from commutators.
   - They relate correlation functions with insertions of $\partial_\mu J^\mu$ to contact terms involving variations of the operators.

9. **Anomalies**: Classical symmetries can be broken by quantum effects.
   - The chiral anomaly: $\partial_\mu J^{5\mu} \neq 0$ due to triangle diagrams.
   - **Critical Distinction**: Gauge anomalies must cancel for consistency (otherwise $Q_B^2 \neq 0$ and the physical Hilbert space does not exist). Chiral anomalies can be physical (e.g., axial anomaly, $\pi^0 \to \gamma\gamma$).

10. **Slavnov–Taylor Identities**: The BRST generalization of Ward identities; essential for proving gauge invariance of physical amplitudes in non-Abelian theories.

### Spontaneous Symmetry Breaking
11. **Goldstone's Theorem**: For each broken continuous global symmetry, a massless scalar (Goldstone boson) appears.
    - Requires a degenerate vacuum and relativistic invariance.
12. **Higgs Mechanism**: For a broken local gauge symmetry, the Goldstone boson is absorbed by the gauge field, giving it a mass.
    - This changes the degrees of freedom: the massless gauge boson (2 polarizations) becomes massive (3 polarizations), "eating" the Goldstone.
    - The physical spectrum is gauge-invariant; the Goldstone mode is unphysical (BRST-exact).

---

## Unresolved or Conditional Relationships

### Critical Unresolved Issues
1. **Non-Lagrangian QFTs**: Noether's theorem does not exist if there is no Lagrangian. In algebraic QFT, symmetries are represented by automorphisms of the algebra; Ward identities are derived from the algebraic structure, not from a current.
   - **Therefore, Noether's theorem is not a universal QFT relation.**

2. **Quantum Definition of the Noether Current**: The current $J^\mu$ must be renormalized (Module 6). The Ward identity $\partial_\mu \langle J^\mu \cdots \rangle = \text{contact terms}$ receives scheme-dependent corrections. The physical charge is scheme-independent.

3. **Gauge Anomaly and Consistency**: We have mapped the cancellation condition, but the **non-perturbative** status of gauge anomalies (e.g., global anomalies, Witten anomaly) is not fully mapped. These require topological considerations.

4. **BRST Quantization of Constrained Systems**: We have given the standard Faddeev–Popov–BRST route. However, for some gauges (e.g., axial gauge), the Faddeev–Popov determinant may be trivial, but ghosts are still needed for unitarity in covariant gauges. The complete mapping of all gauge choices and their equivalence is not established.

5. **Anomalies in Non-Perturbative Regime**: The chiral anomaly is exact (1-loop exact due to the Adler-Bardeen theorem for the axial anomaly in QED), but for non-Abelian anomalies, higher-loop corrections might appear? The Adler-Bardeen theorem states the axial anomaly is 1-loop exact. We should mark this as **Conditional/Supported** for specific cases.

6. **Higgs Mechanism in Curved Spacetime**: The Goldstone theorem and Higgs mechanism are modified in curved space or with non-minimal couplings. We have assumed flat Minkowski spacetime.

7. **Spontaneous Symmetry Breaking and the Effective Action**: The order parameter $\langle \Phi \rangle$ is derived from the effective potential $V_{\text{eff}}(\phi)$ (the effective action at constant field). The relationship $\langle \Phi \rangle = \text{minimum of } V_{\text{eff}}$ is exact but requires computing the effective potential, which is non-perturbative. We have not mapped the effective potential in detail (deferred to Module 6/9).

8. **Equivalence of Physical Symmetry and Gauge Redundancy in Observables**: Physical observables must be gauge-invariant. Therefore, the symmetry group acting on fields is not the same as the symmetry group acting on observables. This distinction is often blurred. We have explicitly separated them.

---

## Dependencies Propagating from Module 5

### To Module 6 (Renormalization)
- Anomalies affect renormalization group equations (e.g., trace anomaly, scale anomaly).
- Gauge Ward identities impose constraints on the renormalization of the gauge coupling (e.g., charge renormalization in QED).
- The effective potential for SSB receives quantum corrections.

### To Module 7 (Spectral and Particle Structure)
- Goldstone bosons appear as massless poles in the spectral density.
- The Higgs mechanism gives a mass to gauge bosons, altering the spectral representation of $A_\mu$.
- Anomalies contribute to decay rates (e.g., $\pi^0 \to \gamma\gamma$).

### To Module 8 (Perturbation Mapping)
- Perturbing a coupling constant changes the Ward identities at loop level.
- Gauge-fixing perturbations (changing gauge) should leave physical correlators invariant; this is a test of the perturbation mapping.

### To Module 9 (Effective Theories)
- Anomaly matching: anomalies must match between UV and IR descriptions.
- The Higgs mechanism in the SM leads to massive $W/Z$ bosons and Goldstone bosons in the electroweak effective theory.

---

## Epistemic Classification Summary (Module 5)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 8 |
| Derived | 9 |
| Conditional | 16 |
| Model-Dependent | 5 |
| Formal | 3 |
| Constraint | 4 |
| **Total** | **45** |

---

## Key Open Questions After Module 5

1. **Is Noether's theorem valid at the quantum level?**
   - Only if the symmetry is not anomalous. If anomalous, $\partial_\mu \langle J^\mu \rangle \neq 0$. So the classical conservation law does not survive quantization in general.

2. **What is the exact status of BRST cohomology for interacting theories?**
   - Formal. The physical Hilbert space is defined perturbatively. Non-perturbative definitions (e.g., in lattice gauge theory) do not use BRST in the same way.

3. **Does the Higgs mechanism always work?**
   - It works at tree level. At loop level, the effective potential may have additional minima, and the vacuum may be unstable or metastable (e.g., SM Higgs vacuum stability). The mapping of stability is model-dependent.

4. **How does gauge invariance constrain the effective action?**
   - The effective action $\Gamma[\phi]$ must be gauge-invariant (or BRST-invariant). This imposes powerful constraints on the form of $\Gamma$ (e.g., the $F^2$ structure). These constraints are exact but difficult to implement non-perturbatively.

5. **What is the relationship between anomalies and topology?**
   - The chiral anomaly is proportional to the instanton number $\int F\tilde{F}$. This connects symmetry to topology. We have not mapped the topological aspects (requires Module 9/10).

---

# STATE OF MODULE 5

**Established:**
- Noether's theorem (conditional on Lagrangian).
- Conservation laws and charges.
- Gauge symmetry as redundancy vs. global symmetry as physical.
- Gauge fixing, Faddeev–Popov determinant, ghost fields.
- BRST symmetry and physical state condition ($Q_B^2=0$).
- Ward identities and Slavnov–Taylor identities.
- Anomalies (chiral, gauge) and cancellation conditions.
- Goldstone theorem and Higgs mechanism (conditional on SSB).

**Not Established:**
- Non-Lagrangian symmetry structures (algebraic QFT).
- Non-perturbative BRST cohomology.
- General anomaly classification (global anomalies, non-perturbative).
- Topological aspects of anomalies (instantons, theta vacua) — deferred.

**Mathematical Gaps:**
- The Faddeev–Popov determinant requires the gauge-fixing condition to have a unique solution; the Gribov ambiguity (multiple solutions) is not addressed.
- BRST quantization of reducible gauge symmetries (e.g., higher-form gauge fields) is not mapped.
- The effective potential for SSB is not derived; only the tree-level result is given.

---

# MODULE 6 — RENORMALIZATION AND SCALE STRUCTURE

## 6.1 REGULARIZATION OF DIVERGENCES

### Node Definitions

**N6.1.1:** Ultraviolet (UV) divergence

Local (short-distance) singularities in loop integrals, e.g., 
$$\int^\Lambda \frac{d^d k}{(k^2)^a} \sim \Lambda^{d-2a} + \cdots$$
for large momentum $k$.

- Status: Arises in interacting QFT; perturbative definition requires handling.

**N6.1.2:** Infrared (IR) divergence

Long-distance singularities from massless particles or soft emissions.

- Status: Conditional on massless fields.

**N6.1.3:** Regularization

A systematic procedure to render divergent integrals finite by introducing a regulator.

- Status: Conditional on perturbative expansion; not a physical operation.

**N6.1.4:** Momentum cutoff regularization $\Lambda$

Replace $\int d^d k$ with $\int_{|k| < \Lambda} d^d k$ (or $\int_{0}^{\Lambda} dk\, k^{d-1}$).

- Status: Regulator, breaks translation invariance in momentum space, breaks gauge invariance generally.

**N6.1.5:** Dimensional regularization (DR)

Analytic continuation in spacetime dimension: $d \to d - 2\epsilon$ (or $d = 4 - 2\epsilon$). Divergences appear as poles $1/\epsilon^n$.

- Status: Regulator, preserves gauge and Lorentz invariance, breaks naive dimensional analysis for $\gamma_5$.

**N6.1.6:** Pauli–Villars regularization

Introduce heavy auxiliary fields (or form factors) to make propagators fall off faster.

- Status: Regulator, breaks unitarity at high scale but restores at low energy.

**N6.1.7:** Lattice regularization

Discretize spacetime: $x^\mu \to n^\mu a$ (lattice spacing $a$). Path integral becomes finite-dimensional.

- Status: Regulator, non-perturbative, breaks Lorentz invariance (restored in continuum limit).

**N6.1.8:** Regularized correlation function $G_n^{(\text{reg})}$

The $n$-point function computed with a regulator, finite for finite cutoff/epsilon.

- Status: Conditional on regularization.

---

## 6.2 BARE vs. RENORMALIZED QUANTITIES

**N6.2.1:** Bare fields $\Phi_{0,i}$

Fields appearing in the bare action $S_0[\Phi_0]$ (no counterterms yet).

- Status: Supplied/Definitional.

**N6.2.2:** Bare parameters $\{g_{0,a}, m_0, \dots\}$

Parameters in the bare Lagrangian, typically divergent as the regulator is removed ($\Lambda \to \infty$, $\epsilon \to 0$).

- Status: Definitional.

**N6.2.3:** Renormalized fields $\Phi_{R,i}$

Rescaled fields: $\Phi_{0,i} = Z_i^{1/2} \Phi_{R,i}$, where $Z_i$ is the wavefunction renormalization constant (divergent).

- Status: Definitional.

**N6.2.4:** Renormalized parameters $\{g_{R,a}, m_R, \dots\}$

Finite parameters related to bare ones by multiplicative renormalization: $g_{0,a} = \mu^{\Delta_a} Z_{g_a} g_{R,a}$ (with $Z_{g_a}$ divergent, $\Delta_a$ the engineering dimension shift from $d$).

- Status: Definitional.

**N6.2.5:** Renormalization scale $\mu$

An arbitrary mass scale introduced in dimensional regularization (or MS schemes) to keep couplings dimensionless in $d \neq 4$. For cutoff, $\mu$ is often implicit in the matching scale.

- Status: Supplied parameter, scheme-dependent.

**N6.2.6:** Counterterm Lagrangian $\mathcal{L}_{\text{CT}}$

Defined by $\mathcal{L}_0 = \mathcal{L}_R + \mathcal{L}_{\text{CT}}$, where
$$\mathcal{L}_{\text{CT}} = \sum_i (Z_i - 1) \mathcal{O}_{R,i} + \sum_a (Z_{g_a} - 1) \mathcal{O}_{R,a}$$
(up to field rescalings). Counterterms cancel divergences order-by-order.

- Status: Definitional.

**N6.2.7:** Renormalization conditions

Prescriptions fixing the finite parts of $Z$-factors. Examples:
- On-shell (OS): fix physical mass and residue of propagator at the physical pole.
- Minimal subtraction (MS): subtract only $1/\epsilon$ poles.
- Modified minimal subtraction ($\overline{\text{MS}}$): subtract $1/\epsilon + \gamma_E - \ln 4\pi$.

- Status: Conditional, scheme-dependent.

**N6.2.8:** Renormalized $n$-point function $G_{R}^{(n)}$

The limit of $Z^{n/2} G_{\text{reg}}^{(n)}$ as the regulator is removed, with $Z$ chosen to cancel divergences.

- Status: Conditional on renormalizability.

---

## 6.3 RENORMALIZATION GROUP (RG)

**N6.3.1:** Renormalization group equation (RGE) for correlation functions (Callan–Symanzik)

$$\left[ \mu \frac{\partial}{\partial \mu} + \beta_a \frac{\partial}{\partial g_{R,a}} + \sum_i n_i \gamma_{\Phi_i} \right] G_{R}^{(n)}(x_i; g_R, \mu) = 0$$
where $\beta_a = \mu \frac{d g_{R,a}}{d\mu}$ and $\gamma_{\Phi_i} = \frac{\mu}{2} \frac{d \ln Z_i}{d\mu}$.

- Status: Derived from renormalization independence of bare quantities.

**N6.3.2:** Beta function $\beta(g)$

$$\beta(g) \equiv \mu \frac{d g}{d\mu} = -\epsilon g + \beta_{\text{finite}}(g)$$
(where $\epsilon = (4-d)/2$ in DR; for $d=4$, $\beta(g)$ is the finite part).

- Status: Derived from $Z_g$: $\beta(g) = -g \frac{\mu \frac{d}{d\mu} \ln Z_g}{1 + g \frac{\partial}{\partial g} \ln Z_g}$ (or similar, depending on convention).

**N6.3.3:** Anomalous dimension $\gamma_\Phi(g)$

$$\gamma_\Phi(g) \equiv \frac{\mu}{2} \frac{d \ln Z_\Phi}{d\mu} = -\frac{1}{2} \beta(g) \frac{\partial \ln Z_\Phi}{\partial g}$$
(for the MS scheme).

- Status: Derived.

**N6.3.4:** Running coupling $g(\mu)$

The solution to the RGE: $\frac{d g}{d \ln \mu} = \beta(g)$.

- Status: Derived.

**N6.3.5:** RG flow

The map $\mu \mapsto g(\mu)$ for $g(\mu)$ satisfying the beta function.

- Status: Definitional.

**N6.3.6:** Fixed points $g^*$

Points where $\beta(g^*) = 0$.

- Classification: UV stable (attractive in UV), IR stable (attractive in IR).
- Status: Derived.

**N6.3.7:** Critical exponent $\theta = \beta'(g^*)$

Determines the rate of approach to the fixed point: $g(\mu) - g^* \sim \mu^{\theta}$.

- Status: Derived.

**N6.3.8:** Scale anomaly (trace anomaly)

In a scale-invariant classical theory, the trace of the energy-momentum tensor $T^\mu_\mu$ vanishes classically but obtains a quantum anomalous term proportional to $\beta(g) \mathcal{O}$.

- Status: Derived from RGE.

---

## 6.4 OPERATOR CLASSIFICATION AND POWER COUNTING

**N6.4.1:** Mass dimension of operator $[\mathcal{O}]$

Defined by scaling under $x \to \lambda x$: $[\mathcal{O}] = \Delta_\mathcal{O}$.

- Status: Classical dimensional analysis.

**N6.4.2:** Relevant operator

An operator with $[\mathcal{O}] < d$ (or $\Delta_\mathcal{O} - d < 0$). It grows in the IR and is suppressed in the UV.

- Status: Definitional.

**N6.4.3:** Marginal operator

An operator with $[\mathcal{O}] = d$.

- Status: Definitional.

**N6.4.4:** Irrelevant operator

An operator with $[\mathcal{O}] > d$. It is suppressed in the IR.

- Status: Definitional.

**N6.4.5:** Power-counting renormalizability

A theory is power-counting renormalizable if the Lagrangian contains only operators with $[\mathcal{O}] \le d$ (i.e., relevant and marginal operators).

- Status: Conditional, perturbative.

**N6.4.6:** Effective field theory (EFT) expansion

Operator scaling: irrelevant operators are suppressed by powers of $1/\Lambda_{\text{UV}}$, where $\Lambda_{\text{UV}}$ is the cutoff.

- Status: Definitional (preview of Module 9).

---

## 6.5 SCHEME DEPENDENCE vs. PHYSICAL OBSERVABLES

**N6.5.1:** Scheme independence of physical S-matrix

The physical S-matrix elements must be independent of the renormalization scheme and $\mu$ (though the perturbative series depends on scheme order-by-order).

- Status: Established (renormalization group invariance).

**N6.5.2:** Scheme dependence of Green functions

$G_R^{(n)}$ depends on $\mu$ and the renormalization scheme (OS vs MS, etc.).

- Status: Conditional.

**N6.5.3:** Invariance of the effective action

$\Gamma[\phi; g_R, \mu]$ satisfies the RG equation:
$$\left[ \mu \frac{\partial}{\partial \mu} + \beta \frac{\partial}{\partial g} - \int d^d x\, \gamma_\Phi \phi \frac{\delta}{\delta \phi} \right] \Gamma = 0$$
(up to field redefinitions).

- Status: Derived.

---

# RELATIONSHIP TABLE — MODULE 6

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N4.3.1 Loop integrals | N6.1.1 UV divergences | Constraint | $\int d^d k\, (k^2)^{-\alpha}$ diverges for $d \ge 2\alpha$ | Interacting QFT, perturbation theory | Unidirectional | Nonlocal (momentum) | Exact | Independent | Need for regularization | Derived |
| N6.1.1 UV divergences | N6.1.3 Regularization | Resolution | Insert regulator $\Lambda$, $\epsilon$, $a$, etc. | Perturbative QFT | Unidirectional | Nonlocal | Formal | Regulator-dependent | Finite intermediate results | Conditional |
| N6.1.3 Regularization | N6.1.8 Regularized correlators | Definitional | $G_n^{(\text{reg})} = \int_{\text{reg}} \cdots$ | Regularization scheme | Unidirectional | Nonlocal | Approx (regularized) | Regulator-dependent | Regularized correlations | Conditional |
| N6.2.1 Bare fields $\Phi_0$ | N6.2.3 Renormalized fields $\Phi_R$ | Algebraic | $\Phi_0 = Z^{1/2} \Phi_R$ | Renormalization | Bidirectional | Local | Exact (definitional) | Scheme-dependent | Field rescaling | Definitional |
| N6.2.2 Bare parameters $g_0$ | N6.2.4 Renormalized parameters $g_R$ | Algebraic | $g_0 = \mu^{\Delta} Z_g g_R$ | Renormalization | Bidirectional | Global | Exact (definitional) | Scheme-dependent | Parameter mapping | Definitional |
| N6.2.2 Bare params | N6.2.6 Counterterms | Definitional | $g_0 = g_R + \delta g$, $\mathcal{L}_{\text{CT}} = \delta g \mathcal{O}$ | Renormalization | Unidirectional | Local | Exact (definitional) | Scheme-dependent | Counterterm Lagrangian | Definitional |
| N6.2.6 Counterterms | N6.1.1 UV divergences | Cancellation | $\delta g$ chosen so $g_0$ finite as regulator removed | Renormalizability | Unidirectional | Local | Exact (perturbative) | Scheme-dependent | Finite observables | Conditional |
| N6.2.3 $\Phi_R$ | N6.2.7 Renormalization conditions | Constraint | Fix $Z$ via conditions on correlators (e.g., residue at pole = 1) | Renormalization prescription | Unidirectional | Nonlocal | Exact | Scheme-dependent | Scheme choice | Conditional |
| N6.2.8 Renormalized $G_R$ | N6.1.8 Regularized $G_{\text{reg}}$ | Limit | $G_R = \lim_{\text{reg}} Z^{n/2} G_{\text{reg}}$ | Renormalizability | Unidirectional | Nonlocal | Exact (formal limit) | Scheme-dependent | Physical correlations | Conditional |
| N6.3.1 Callan-Symanzik eq | N6.2.8 Renormalized $G_R$ | Differential | $\left( \mu \partial_\mu + \beta \partial_g + n\gamma_\Phi \right) G_R = 0$ | Renormalization group | Unidirectional | Local (in $\mu, g$) | Exact | Scheme-dependent | Scale dependence of correlators | Derived |
| N6.3.2 Beta function $\beta$ | N6.2.2 Bare params | Differential | $\beta(g) = \mu \frac{dg}{d\mu} = -g \frac{\mu \partial_\mu Z_g}{1 + g \partial_g \ln Z_g}$ (MS scheme) | Perturbative renormalization | Unidirectional | Global | Approx (series) | Scheme-dependent | Running of couplings | Derived |
| N6.3.2 $\beta$ | N6.3.4 Running coupling $g(\mu)$ | Differential eq | $\frac{dg}{d\ln \mu} = \beta(g)$ | RG flow | Unidirectional | Global | Approx (truncated) | Scheme-dependent | Coupling evolution | Derived |
| N6.3.2 $\beta$ | N6.3.6 Fixed points | Algebraic | $\beta(g^*) = 0$ | RG flow | Unidirectional | Global | Exact (definitional) | Scheme-dependent (but physical fixed points scheme-invariant) | Critical behavior | Derived |
| N6.3.6 Fixed points | N6.3.7 Critical exponent $\theta$ | Derivative | $\theta = \beta'(g^*)$ | RG flow | Unidirectional | Global | Exact | Scheme-invariant (if physical) | Scaling of operators | Derived |
| N6.3.3 Anomalous dimension $\gamma$ | N6.2.3 $Z_\Phi$ | Differential | $\gamma_\Phi = \frac{\mu}{2} \partial_\mu \ln Z_\Phi$ | Renormalization | Unidirectional | Global | Approx | Scheme-dependent | Scaling dimension of field | Derived |
| N6.3.1 RGE | N6.3.8 Scale anomaly | Derived | $\partial_\mu \langle T^\mu_\mu \rangle = \beta(g) \langle \mathcal{O} \rangle$ | Scale invariance + RGE | Unidirectional | Local (operator) | Exact (in MS) | Scheme-dependent (trace anomaly physical) | Breaking of scale invariance | Derived |
| N6.4.1 Mass dimension $[\mathcal{O}]$ | N6.4.2 Relevant/3 Marginal/4 Irrelevant | Classification | $\Delta = [\mathcal{O}]$; compare to $d$ | Dimensional analysis | Unidirectional | Global | Exact (classical) | Independent | Operator importance in IR | Definitional |
| N6.4.2-4 Classification | N6.4.5 Power-counting renormalizability | Constraint | Theory renormalizable iff all operators have $[\mathcal{O}] \le d$ | Perturbative QFT | Unidirectional | Global | Approx (perturbative) | Scheme-independent | Predictivity | Conditional |
| N6.4.4 Irrelevant operator | N6.4.6 EFT expansion | Power counting | $[\mathcal{O}] = d + n \Rightarrow$ suppressed by $(\Lambda_{\text{UV}})^{-n}$ | EFT | Unidirectional | Nonlocal | Approx | Scheme-independent | Low-energy effects | Conditional |
| N6.3.2 $\beta$ | N6.5.1 Scheme independence | Constraint | First two coefficients of $\beta$ are scheme-independent (in MS-like schemes); higher coefficients scheme-dependent | Renormalization group | Unidirectional | Global | Approx (truncated) | Scheme-dependent for higher orders | Physical predictions | Supported |
| N6.2.8 $G_R$ | N6.5.2 Scheme dependence | Conditional | $G_R$ depends on $\mu$ and scheme; physical amplitudes (S-matrix) do not | Renormalization | Bidirectional | Nonlocal | Exact | Scheme-dependent | Observables independent | Derived |
| N6.3.1 RGE | N6.5.3 Effective action RGE | Functional | $\left( \mu \partial_\mu + \beta \partial_g - \int \gamma_\Phi \phi \frac{\delta}{\delta\phi} \right) \Gamma = 0$ | RG + effective action | Unidirectional | Nonlocal | Exact (formal) | Scheme-dependent | Effective action scaling | Derived |

---

# MODULE 6 SYNTHESIS

## Relationships Established

### Regularization → Renormalization
1. **Divergence → Regulator**: UV divergences in loop integrals necessitate a regulator ($\Lambda$, $\epsilon$, $a$, etc.).
   - The regulator is an **artificial mathematical device**, not part of the physical theory.
   - Different regulators break different symmetries (cutoff breaks gauge invariance; dimensional regularization breaks $\gamma_5$ algebra; lattice breaks Lorentz invariance).

2. **Bare → Renormalized Mapping**: $\Phi_0 = Z^{1/2}\Phi_R$, $g_0 = \mu^\Delta Z_g g_R$, and $\mathcal{L}_0 = \mathcal{L}_R + \mathcal{L}_{\text{CT}}$.
   - **Counterterms** are the difference between bare and renormalized interactions; they are defined order-by-order to cancel poles (MS) or fix physical conditions (OS).

3. **Renormalized Correlation Function**: $G_R = \lim_{\text{reg}} Z^{n/2} G_{\text{reg}}$.
   - This limit exists only for **renormalizable** theories (or as an EFT with a finite cutoff).

### Renormalization Group (RG)
4. **Callan–Symanzik Equation**: The cornerstone of RG:
   $$(\mu \partial_\mu + \beta \partial_g + n\gamma_\Phi) G_R^{(n)} = 0$$
   - Expresses the invariance of the bare theory under changes of the renormalization scale $\mu$.
   - $\beta(g)$ and $\gamma_\Phi(g)$ are derived from the $Z$-factors.

5. **Beta Function and Running**: $\beta(g) = \mu \frac{dg}{d\mu}$.
   - The solution $g(\mu)$ gives the **running coupling**.
   - Fixed points $\beta(g^*) = 0$ determine critical behavior.
   - **First two coefficients** of $\beta$ are scheme-independent; higher orders are scheme-dependent.

6. **Scale Anomaly**: Even in a classically scale-invariant theory, $\langle T^\mu_\mu \rangle \neq 0$ due to quantum effects, proportional to $\beta(g) \langle \mathcal{O} \rangle$. This is a physical consequence of renormalization.

### Operator Classification and EFT
7. **Relevant/Marginal/Irrelevant**: Determined by mass dimension $[\mathcal{O}]$.
   - Relevant ($[\mathcal{O}] < d$) dominate IR.
   - Marginal ($[\mathcal{O}] = d$) define critical theories (e.g., $\phi^4$ in 4d).
   - Irrelevant ($[\mathcal{O}] > d$) are suppressed in IR by powers of $1/\Lambda_{\text{UV}}$.
   - **Power-counting renormalizability** requires only relevant/marginal operators in the bare Lagrangian (for a predictive UV-complete theory).

### Scheme Dependence vs. Physical Observables
8. **Scheme Independence**: The physical S-matrix and all observables are independent of the renormalization scheme and $\mu$.
   - However, finite-order perturbative results depend on the scheme; this dependence decreases order-by-order.
   - $G_R^{(n)}$ and $\Gamma[\phi]$ are scheme-dependent; only the physical quantities constructed from them (e.g., pole masses, S-matrix elements) are scheme-invariant.

---

## Unresolved or Conditional Relationships

### Critical Unresolved Issues
1. **Non-Perturbative Renormalization**: The RG equations we have mapped are perturbative (expansion in $g$). The exact (non-perturbative) beta function is known only for a few cases (e.g., $N=4$ SYM, 2d integrable models). For QCD, the beta function is known to 5 loops, but the full non-perturbative behavior (confinement, chiral symmetry breaking) is not captured by perturbative RGE.

2. **Triviality of $\phi^4$ in $d=4$**: The $\phi^4$ theory in 4 dimensions is trivial (non-interacting) in the continuum limit due to the Landau pole in the UV (for positive $\beta$). This is a rigorous result (from lattice and constructive QFT). However, the perturbative beta function indicates asymptotic freedom? No, $\phi^4$ is not asymptotically free; it has a Landau pole. This is an unresolved conceptual gap: perturbative RG suggests a UV Landau pole, but the theory is likely trivial, meaning the renormalized coupling vanishes in the continuum limit.
   - **Mapping**: We have flagged the beta function, but the relationship between the perturbative $\beta$ (which diverges at the Landau pole) and the non-perturbative triviality is not established.

3. **Confinement and RG Flow**: The RG flow for QCD shows asymptotic freedom (IR fixed point? No, QCD has an IR Landau pole/strong coupling). The exact IR behavior (confinement, mass gap) is not derivable from perturbative RGE. This is a major unresolved issue.

4. **Gauge Invariance and Renormalization**: We have not mapped the exact constraints of gauge invariance on the renormalization of gauge couplings (e.g., the Ward identity that ensures the gauge coupling is the same for vertices and propagators). While we flagged it in Module 5, the specific mapping of `Slavnov-Taylor` to `Beta function` (e.g., the Z-factors for the gauge field and ghost) is not fully detailed here.

5. **Renormalization of Composite Operators**: Composite operators (like $\phi^2(x)$) require additional renormalization (mixing with other operators). The operator renormalization matrix $Z_{\mathcal{O}}$ leads to **operator anomalous dimensions**, which we have only partially mapped for fundamental fields. Mixing of operators (e.g., in $\phi^4$ theory, $\phi^2$ mixes with the identity) is not mapped.

6. **Infrared Divergences**: We have not mapped the treatment of IR divergences (e.g., Bloch-Nordsieck, soft-photon resummation). These are essential for physical cross-sections.

7. **Borel Summability and Asymptotic Series**: The perturbative series in QFT is asymptotic (not convergent). The relationship between the perturbative expansion and the exact non-perturbative theory is not established. This is a foundational unresolved issue.

---

## Dependencies Propagating from Module 6

### To Module 7 (Spectral and Particle Structure)
- The **running mass** $m(\mu)$ and **field strength** $Z(\mu)$ affect the spectral representation.
- The **scale dependence** of the propagator pole (the physical mass is scheme-independent, but the running mass is scheme-dependent).
- **Anomalous dimensions** affect the large-momentum behavior of correlators.

### To Module 8 (Perturbation Mapping)
- Perturbing a coupling $g$ changes $\beta(g)$, which changes the RG flow, which changes the scale-dependent correlators.
- Perturbing the renormalization scale $\mu$ (which is an unphysical parameter) must leave physical observables invariant; this is a key test.

### To Module 9 (Effective Field Theories)
- Matching at a scale $\mu$ involves integrating out heavy fields and matching Wilson coefficients.
- The power counting of irrelevant operators is the foundation of EFTs.
- Running of Wilson coefficients follows the RGE.

### To Module 10 (Synthesis)
- The scale dependence of couplings and operators will be a major node in the global dependency map.
- The distinction between scheme-dependent quantities and physical observables will be critical.

---

## Epistemic Classification Summary (Module 6)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 10 |
| Derived | 10 |
| Conditional | 10 |
| Supported | 1 |
| Approx | 4 |
| Formal | 2 |
| **Total** | **37** |

---

## Key Open Questions After Module 6

1. **Is the perturbative beta function exact for any theory?**
   - Only for supersymmetric theories (e.g., $N=4$ SYM) or in special limits. Generally, it is a truncated series.

2. **How does the RG flow relate to the physical mass spectrum?**
   - The RG flow of the mass parameter gives the running mass, but the physical mass is the pole of the propagator. The relationship is non-trivial and involves solving the gap equation.

3. **What is the fate of the Landau pole in QED?**
   - Perturbatively, QED has a Landau pole at extremely high energy (near the Planck scale). However, the theory is expected to be embedded in a larger theory (GUT) or to have a Landau pole that indicates the breakdown of perturbation theory, not a physical singularity. This is unresolved.

4. **Can we rigorously define the RG flow non-perturbatively?**
   - In lattice QFT, yes (via the Wilsonian RG). But the mapping between the perturbative MS scheme and the lattice scheme is complex and requires non-perturbative matching.

5. **How do anomalies affect the RG flow?**
   - The trace anomaly modifies the RGE for the effective action. The chiral anomaly affects the running of couplings in theories with chiral fermions.

6. **Is the effective action $\Gamma[\phi]$ the generator of 1PI Green functions, and how does it run with scale?**
   - Yes, and its RG equation is $\left( \mu \partial_\mu + \beta \partial_g - \int \gamma_\Phi \phi \frac{\delta}{\delta\phi} \right) \Gamma = 0$. This is a powerful equation, but solving it non-perturbatively is impossible.

---

# STATE OF MODULE 6

**Established:**
- Relationship between UV divergences and regularization.
- Mapping of bare to renormalized quantities via $Z$-factors and counterterms.
- Callan–Symanzik equation (exact perturbative relation).
- Definition and derivation of $\beta(g)$, $\gamma_\Phi(g)$.
- Running couplings and fixed points.
- Classification of operators (relevant/marginal/irrelevant).
- Scheme independence of physical observables (S-matrix).

**Not Established:**
- Non-perturbative beta function for general theories.
- Renormalization of composite operators and mixing.
- Treatment of IR divergences.
- Rigorous proof of renormalizability beyond perturbation theory.
- Connection between perturbative RG and exact non-perturbative physics (confinement, triviality, etc.).

**Mathematical Gaps:**
- The perturbative series is asymptotic; its relationship to the exact theory is unproven.
- The RG flow equations are differential equations; solving them requires boundary conditions (which are not provided by the theory itself, but by experiments).

---

# MODULE 7 — SPECTRAL, PARTICLE, AND SCATTERING STRUCTURE

## 7.1 SPECTRAL REPRESENTATIONS AND PARTICLE POLES

### Node Definitions

**N7.1.1:** Källén–Lehmann spectral density $\rho(s)$ (refined)

The positive spectral function appearing in the Källén–Lehmann representation (Module 4):
$$\rho(s) = \sum_n (2\pi)^3 \delta^{(4)}(p - p_n) |\langle 0|\hat{\Phi}(0)|n\rangle|^2$$
for a scalar field (up to normalization).

- Status: Derived from completeness of states.
- Assumption: Wightman axioms, positive metric.

**N7.1.2:** One-particle pole

A contribution to $\rho(s)$ of the form:
$$\rho(s) = Z\,\delta(s - m^2) + \rho_{\text{cont}}(s)$$
where $Z > 0$ is the field strength renormalization factor (for a stable particle).

- Status: Derived from the spectral decomposition.

**N7.1.3:** Residue $Z$

$Z = |\langle 0|\hat{\Phi}(0)|p\rangle|^2$ for a single-particle state $|p\rangle$.

- Status: Derived.

**N7.1.4:** Multi-particle continuum

The smooth part $\rho_{\text{cont}}(s)$ for $s > (2m)^2$ (or threshold of multi-particle states).

- Status: Derived.

**N7.1.5:** Physical mass $m_{\text{phys}}$

The position of the pole of the full propagator:
$$G_F^{-1}(p^2)|_{p^2 = m_{\text{phys}}^2} = 0$$

- Status: Derived from the propagator.
- Scheme independence: Pole mass is scheme-independent and gauge-invariant (for gauge-invariant operators).

**N7.1.6:** Propagator pole structure (general)

Near the pole: $G_F(p^2) \sim \frac{i Z}{p^2 - m_{\text{phys}}^2 + i\epsilon}$ (for stable particles).

- Status: Derived.

---

## 7.2 ASYMPTOTIC STATES AND THE S-MATRIX

**N7.2.1:** Asymptotic in-state $|\text{in}\rangle$

A state constructed from creation operators in the distant past ($t \to -\infty$), representing incoming particles well-separated (no interactions).

- Status: Conditional on the existence of scattering states (Haag–Ruelle theory).

**N7.2.2:** Asymptotic out-state $|\text{out}\rangle$

A state constructed from creation operators in the distant future ($t \to +\infty$).

- Status: Conditional.

**N7.2.3:** In/out Fock spaces $\mathcal{H}_{\text{in}}, \mathcal{H}_{\text{out}}$

The Fock spaces of free (or asymptotic) particles. In an interacting theory, these are not the same as the full interacting Hilbert space $\mathcal{H}$ (Haag's theorem), but they are isomorphic for scattering purposes (assuming asymptotic completeness).

- Status: Conditional on scattering theory.

**N7.2.4:** Scattering matrix operator $\mathcal{S}$

The unitary operator mapping in-states to out-states:
$$|\text{out}\rangle = \mathcal{S}|\text{in}\rangle$$

- Status: Conditional on asymptotic completeness and unitary evolution.

**N7.2.5:** S-matrix elements

$$\langle \text{out}; p_1,\ldots,p_n | \text{in}; k_1,\ldots,k_m \rangle = \langle p_1,\ldots,p_n | \mathcal{S} | k_1,\ldots,k_m \rangle$$

- Status: Conditional.

---

## 7.3 LSZ REDUCTION FORMULA

**N7.3.1:** LSZ reduction formula (formal)

The bridge between time-ordered correlation functions and S-matrix elements:
$$\langle p_1,\ldots,p_n | \mathcal{S} | k_1,\ldots,k_m \rangle \propto \lim_{\text{on-shell}} \left[ \prod_{i=1}^n (p_i^2 - m^2) \prod_{j=1}^m (k_j^2 - m^2) \right] \times \int d^d x_1\cdots d^d x_{n+m} e^{i(\sum p_i x_i - \sum k_j y_j)} \langle 0|T\{\Phi(x_1)\cdots\Phi(x_n)\Phi(y_1)\cdots\Phi(y_m)\}|0\rangle$$
(amputated, truncated, with appropriate normalization).

- Status: Conditional on asymptotic states and analyticity.
- Assumptions: Stable particles in the initial/final states (for unstable particles, modifications required).

**N7.3.2:** Amputation (removing external propagators)

Multiplying by inverse propagators $(p_i^2 - m^2)$ to cancel the external legs in the correlator.

- Status: Definitional.

**N7.3.3:** LSZ for composite operators

For operators $\mathcal{O}_i$ with definite quantum numbers and anomalous dimensions, the formula generalizes to poles of the corresponding correlators (requires knowing the overlap with the particle state).

- Status: Conditional, model-dependent.

**N7.3.4:** Lehmann–Symanzik–Zimmermann (LSZ) reduction formula (full version)

For asymptotic states, the formula holds order-by-order in perturbation theory. A rigorous version exists for theories satisfying the Wightman axioms (Haag–Ruelle scattering theory).

- Status: Conditional on axioms; perturbatively derived.

---

## 7.4 SCATTERING AMPLITUDES AND CROSS-SECTIONS

**N7.4.1:** Connected, amputated, truncated $n$-point function $\mathcal{M}_n$

The scattering amplitude $\mathcal{M}$ is the coefficient of the momentum-conserving delta function in the S-matrix element after extracting external wavefunctions:
$$\langle p_1,\ldots,p_n | \mathcal{S} - 1 | k_1,\ldots,k_m \rangle = i (2\pi)^d \delta^{(d)}(p_{\text{in}} - p_{\text{out}}) \mathcal{M}_{m \to n}$$

- Status: Definitional.

**N7.4.2:** Phase space $d\Phi_n$

The Lorentz-invariant $n$-body phase space measure:
$$d\Phi_n = (2\pi)^d \delta^{(d)}(P - \sum_i p_i) \prod_i \frac{d^{d-1}p_i}{(2\pi)^{d-1}2E_i}$$

- Status: Definitional.

**N7.4.3:** Differential cross-section $d\sigma$

$$d\sigma = \frac{1}{4\sqrt{(p_1\cdot p_2)^2 - m_1^2 m_2^2}} |\mathcal{M}|^2 d\Phi_n$$
(for 2-to-$n$ scattering).

- Status: Derived.
- Assumption: Relativistic normalization of states.

**N7.4.4:** Total cross-section $\sigma_{\text{tot}}$

Integral of the differential cross-section over all phase space (with possible symmetry factors).

- Status: Derived.

**N7.4.5:** Decay rate $\Gamma_{1 \to n}$

For a parent particle of mass $M$:
$$d\Gamma = \frac{1}{2M} |\mathcal{M}|^2 d\Phi_n$$
(total decay rate is the integral).

- Status: Derived.

**N7.4.6:** Branching ratio

$\text{Br}(i) = \Gamma_i / \Gamma_{\text{tot}}$ for a specific decay channel $i$.

- Status: Derived.

---

## 7.5 UNITARITY AND THE OPTICAL THEOREM

**N7.5.1:** Unitarity of the S-matrix

$$\mathcal{S}^\dagger \mathcal{S} = \mathcal{S} \mathcal{S}^\dagger = \mathbb{1}$$

- Status: Conditional on unitary time evolution and asymptotic completeness.

**N7.5.2:** Optical theorem

From unitarity, for forward scattering ($\mathbf{p} = \mathbf{k}$):
$$\operatorname{Im} \mathcal{M}(i \to i) = 2 \sum_X \int d\Phi_X |\mathcal{M}(i \to X)|^2$$
(up to normalization factors and flux factors).

- Status: Derived from unitarity.
- Consequence: The imaginary part of the forward amplitude is related to the total cross-section.

**N7.5.3:** Discontinuity of the propagator

The discontinuities of the $n$-point functions across branch cuts are related to the imaginary parts of the amplitudes, which are given by unitarity (Cutkosky rules).

- Status: Derived.

**N7.5.4:** Cutkosky rules

A set of rules to compute the imaginary part of a Feynman amplitude by cutting internal lines and putting them on-shell.

- Status: Conditional on perturbation theory.

---

## 7.6 UNSTABLE PARTICLES AND COMPLEX POLES

**N7.6.1:** Unstable particle (resonance)

A state that has a finite lifetime and does not appear as a stable asymptotic state. Its propagator has a pole in the complex $p^2$-plane (second Riemann sheet):
$$p^2 = m_R^2 - i m_R \Gamma_R$$

- Status: Conditional on analytic continuation of the propagator.

**N7.6.2:** Breit–Wigner propagator

Near the complex pole:
$$G_F(p^2) \sim \frac{i Z}{p^2 - m_R^2 + i m_R \Gamma_R} + \text{regular}$$

- Status: Derived (approximation near the resonance).

**N7.6.3:** Width $\Gamma_R$

The decay width of the unstable particle, related to the imaginary part of the pole:
$$\Gamma_R = \frac{\operatorname{Im} \Sigma(m_R^2)}{m_R}$$
(where $\Sigma$ is the self-energy).

- Status: Derived from the pole condition.

**N7.6.4:** Lifetime $\tau = 1/\Gamma_R$ (in natural units).

- Status: Derived.

**N7.6.5:** Theta function and time evolution

The propagator in position space for an unstable particle shows exponential decay: $G_F(t) \sim e^{-i m_R t - \Gamma_R t/2}$ (for $t>0$).

- Status: Derived (from the Fourier transform of the Breit–Wigner).

---

# RELATIONSHIP TABLE — MODULE 7

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N4.1.2 Time-ordered $G_F$ | N7.1.1 Spectral density $\rho$ | Integral representation | $G_F(p^2) = \int_0^\infty ds \frac{i\rho(s)}{p^2-s+i\epsilon}$ | Wightman axioms | Unidirectional | Nonlocal (in $s$) | Exact | Gauge-invariant (for invariant operators) | Mass spectrum | Derived |
| N7.1.1 $\rho$ | N7.1.2 One-particle pole | Decomposition | $\rho(s) = Z\delta(s-m^2) + \rho_{\text{cont}}(s)$ | Isolated stable particle | Unidirectional | Global | Exact | Scheme-independent (pole) | Particle mass | Derived |
| N7.1.2 One-particle pole | N7.1.3 Residue $Z$ | Residue | $Z = \lim_{s\to m^2}(s-m^2)\rho(s)$ | Spectral representation | Unidirectional | Global | Exact | Scheme-dependent (renormalizes) | Field strength | Derived |
| N7.1.2 One-particle pole | N7.1.5 Physical mass | Pole condition | $G_F^{-1}(p^2)\big|_{p^2=m^2}=0$ | Propagator inversion | Unidirectional | Nonlocal (momentum) | Exact | Gauge-invariant (physical) | Particle mass | Derived |
| N7.1.5 $m_{\text{phys}}$ | N4.2.1 Free $G_F^{(0)}$ | Comparison | $m_{\text{phys}} \neq m_0$ (bare mass) in general | Renormalization | Unidirectional | Global | Exact | Scheme-independent | Physical mass | Conditional |
| N7.2.1 Asymptotic in-state | N7.2.2 Asymptotic out-state | Evolution | $|\text{out}\rangle = \lim_{t\to+\infty} e^{iHt} e^{-iH_0 t} |\text{in}\rangle$ (Møller operators) | Scattering theory, Haag-Ruelle | Unidirectional | Global | Formal | Independent | Scattering | Conditional |
| N7.2.3 S-matrix $\mathcal{S}$ | N7.2.1/2 In/Out | Definitional | $\mathcal{S} = \Omega_\text{out}^\dagger \Omega_\text{in}$ | Møller operators | Unidirectional | Global | Formal | Independent | Scattering amplitudes | Conditional |
| N7.3.1 LSZ formula | N4.1.6 Time-ordered correlator $G_n$ | Functional | $\langle \text{out}|\mathcal{S}|\text{in}\rangle = \lim_{\text{on-shell}} \left( \prod (p_i^2-m^2) \right) \tilde{G}_n $ | Asymptotic states, stable particles | Unidirectional | Nonlocal (Fourier) | Approx (perturbative in practice) | Gauge-invariant (for physical amplitudes) | S-matrix from correlators | Conditional |
| N7.3.1 LSZ | N7.3.2 Amputation | Algebraic | Multiply by inverse propagators to cancel external legs | LSZ | Unidirectional | Nonlocal | Exact | Gauge-invariant | Amputated amplitude | Definitional |
| N7.3.1 LSZ | N7.2.4 $\mathcal{S}$ | Definitional | LSZ is the formula that computes $\mathcal{S}$ elements from $G_n$ | Scattering theory | Unidirectional | Nonlocal | Formal/Approx | Independent | Physical amplitudes | Conditional |
| N7.4.1 Amplitude $\mathcal{M}$ | N7.3.1 LSZ | Identity | $\mathcal{M}$ is the coefficient of $(2\pi)^d\delta^{(d)}$ in $\mathcal{S}-1$ | LSZ | Unidirectional | Nonlocal | Exact (definitional) | Gauge-invariant | Scattering | Definitional |
| N7.4.1 $\mathcal{M}$ | N7.4.3 Differential cross-section | Dynamical | $d\sigma = \frac{1}{4F} |\mathcal{M}|^2 d\Phi_n$ | Relativistic normalization | Unidirectional | Nonlocal (phase space) | Exact | Gauge-invariant | Measurable event rates | Derived |
| N7.4.5 Decay rate $\Gamma$ | N7.4.1 $\mathcal{M}$ | Dynamical | $d\Gamma = \frac{1}{2M}|\mathcal{M}|^2 d\Phi_n$ | Relativistic normalization | Unidirectional | Nonlocal | Exact | Gauge-invariant | Decay widths | Derived |
| N7.4.3 Cross-section | N7.4.4 Total $\sigma_{\text{tot}}$ | Integral | $\sigma_{\text{tot}} = \int d\Phi_n \, d\sigma$ | Integration over phase space | Unidirectional | Nonlocal | Exact | Gauge-invariant | Total event rate | Derived |
| N7.4.5 Decay rate | N7.4.6 Branching ratio | Normalization | $\text{Br}(i) = \Gamma_i / \sum_j \Gamma_j$ | Decay channels | Unidirectional | Global | Exact | Gauge-invariant | Experimental branching ratios | Derived |
| N7.5.1 Unitarity $\mathcal{S}^\dagger\mathcal{S}$ | N7.2.4 $\mathcal{S}$ | Constraint | $\mathcal{S}\mathcal{S}^\dagger = \mathbb{1}$ | Unitary evolution | Bidirectional | Global | Exact | Independent | Probability conservation | Conditional |
| N7.5.1 Unitarity | N7.5.2 Optical theorem | Derived | $\operatorname{Im}\mathcal{M}(i\to i) = 2\sum_X \int d\Phi_X |\mathcal{M}(i\to X)|^2$ | Unitärity + completeness | Unidirectional | Nonlocal | Exact | Gauge-invariant | Cross-section from forward amplitude | Derived |
| N7.5.2 Optical theorem | N7.4.4 Total cross-section | Sum rule | $\sigma_{\text{tot}} \propto \operatorname{Im} \mathcal{M}(i\to i)/\text{flux}$ | Optical theorem | Unidirectional | Global | Exact | Gauge-invariant | Unitarity constraint | Derived |
| N7.5.3 Discontinuity | N7.5.2 Optical theorem | Functional | $\operatorname{Disc} \mathcal{M}(i\to i) = 2i \operatorname{Im}\mathcal{M}$ | Analyticity | Unidirectional | Nonlocal | Exact | Gauge-invariant | Branch cut structure | Derived |
| N7.5.4 Cutkosky rules | N7.5.2 Optical theorem | Diagrammatic | Cut internal lines in loop diagrams to compute discontinuities | Perturbation theory | Unidirectional | Nonlocal | Approx (perturbative) | Gauge-dependent (but gauge-invariant sum) | Imaginary parts of amplitudes | Conditional |
| N7.6.1 Unstable particle | N7.1.2 One-particle pole | Generalization | No real pole; pole at $p^2 = m_R^2 - i m_R \Gamma_R$ (second sheet) | Analytic continuation | Unidirectional | Nonlocal | Exact (analytic) | Gauge-invariant (physical pole) | Resonance | Derived |
| N7.6.1 Complex pole | N7.6.2 Breit-Wigner | Approximation | $G_F(p^2) \simeq \frac{iZ}{p^2-m_R^2+i m_R\Gamma_R}$ | Near resonance | Unidirectional | Nonlocal | Approx (Breit-Wigner) | Gauge-invariant | Experimental resonance shape | Approx |
| N7.6.2 Breit-Wigner | N7.6.3 Width $\Gamma_R$ | Pole condition | $\Gamma_R = \frac{\operatorname{Im}\Sigma(m_R^2)}{m_R}$ | Complex pole | Unidirectional | Global | Exact (definitional) | Gauge-invariant | Decay width | Derived |
| N7.6.3 Width | N7.6.4 Lifetime | Algebraic | $\tau = 1/\Gamma_R$ (in natural units) | Quantum mechanics | Unidirectional | Global | Exact | Gauge-invariant | Lifetime | Derived |
| N7.6.2 Breit-Wigner | N7.6.5 Time evolution | Fourier transform | $G_F(t) \sim e^{-i m_R t - \Gamma_R t/2}$ | Fourier transform | Unidirectional | Nonlocal | Approx | Gauge-invariant | Exponential decay | Derived |
| N7.4.5 Decay rate $\Gamma$ | N7.6.3 Width $\Gamma_R$ | Identity (for unstable particle) | $\Gamma_R$ (pole width) = $\Gamma_{1\to\text{all}}$ (decay rate) up to corrections | Narrow width approximation | Bidirectional | Global | Approx (for narrow resonances) | Gauge-invariant | Phenomenological | Approx |

---

# MODULE 7 SYNTHESIS

## Relationships Established

### Spectral Structure and Particles
1. **Spectral Density → Pole Decomposition**: $\rho(s) = Z\delta(s-m^2) + \rho_{\text{cont}}(s)$.
   - This is an **exact** consequence of the Källén–Lehmann representation and the existence of a stable one-particle state.
   - $Z$ is the field strength renormalization factor; the physical mass $m_{\text{phys}}$ is the pole of the propagator.

2. **Propagator Pole → Particle Interpretation**: The pole of the propagator defines the physical mass (scheme-independent, gauge-invariant for physical operators). This is the primary bridge from field theory to particle physics.

### LSZ and the S-Matrix
3. **LSZ Reduction Formula**: This is the central bridge between correlation functions and scattering amplitudes:
   - Correlators $\to$ Amputation (inverse propagators) $\to$ On-shell limit $\to$ $\mathcal{M}$ (S-matrix elements).
   - This is **conditional** on the existence of asymptotic states (Haag–Ruelle scattering theory) and stable external particles.
   - It is **exact** in the formal sense but perturbatively implemented.

4. **Scattering Cross-sections and Decay Rates**: From $\mathcal{M}$:
   - $d\sigma = \frac{1}{4F} |\mathcal{M}|^2 d\Phi_n$.
   - $d\Gamma = \frac{1}{2M} |\mathcal{M}|^2 d\Phi_n$.
   - These are **derived** from the S-matrix formalism and relativistic normalization. They are directly observable.

### Unitarity and the Optical Theorem
5. **S-matrix Unitarity**: $\mathcal{S}^\dagger\mathcal{S} = 1$ encodes probability conservation.
   - It leads to the **Optical Theorem**: $\operatorname{Im} \mathcal{M}(i\to i) \propto \sigma_{\text{tot}}$.
   - This is an **exact** consequence of unitary time evolution (if scattering theory holds).

6. **Cutkosky Rules**: The diagrammatic implementation of the optical theorem in perturbation theory (conditional, approximate).

### Unstable Particles
7. **Complex Poles**: Unstable particles do not appear as stable asymptotic states. They are represented by **complex poles** of the propagator in the second Riemann sheet:
   - $p^2 = m_R^2 - i m_R \Gamma_R$.
   - The **Breit–Wigner** propagator approximates the resonance shape: $\frac{iZ}{p^2 - m_R^2 + i m_R \Gamma_R}$.
   - The width $\Gamma_R$ is related to the self-energy's imaginary part: $\Gamma_R = \operatorname{Im} \Sigma(m_R^2)/m_R$.
   - The decay rate $\Gamma_{1\to\text{all}}$ equals $\Gamma_R$ in the narrow-width approximation.

---

## Unresolved or Conditional Relationships

### Critical Unresolved Issues
1. **Existence of Asymptotic States**: The Haag–Ruelle scattering theory provides a rigorous framework, but it requires certain conditions (e.g., mass gap, asymptotic completeness). For massless theories (e.g., QED, QCD with massless quarks), the construction is complicated by IR divergences. In $d=4$ QCD, confinement complicates the identification of asymptotic states (quarks/gluons are not asymptotic; hadrons are).

2. **LSZ for Composite/Gauge Particles**: The standard LSZ formula assumes the field has a non-zero overlap with the one-particle state. For composite operators (e.g., $\bar{\psi}\psi$ for the Higgs, or hadronic interpolating fields), the overlap is not trivial and requires additional renormalization. For gauge fields, only gauge-invariant combinations (e.g., $F_{\mu\nu}$ or gauge-invariant operators) have a well-defined LSZ formula.

3. **IR Divergences in Massless Theories**: For QED and massless QCD, the S-matrix elements for charged particles suffer from IR divergences. The standard resolution is to include soft photons/gluons or use inclusive cross-sections (Bloch–Nordsieck theorem). We have not mapped this fully.

4. **Confinement and Absence of Asymptotic Quarks**: In QCD, quarks and gluons are not asymptotic states. The LSZ formula cannot be directly applied to them. Instead, one must use hadronic operators (e.g., $\bar{q}q$, $\bar{q}\gamma^\mu q$, etc.) to define scattering of hadrons. This is a major unresolved issue in the mapping of QCD to particle scattering.

5. **Analyticity and Second Riemann Sheet**: The concept of the complex pole requires analytic continuation of the propagator. This is well-defined in perturbation theory but non-perturbatively, the analytic structure of Green's functions is not fully known (e.g., possible branch cuts, singularities).

6. **Unitarity and Perturbative Expansions**: The optical theorem is exact, but the perturbative expansion of $\operatorname{Im}\mathcal{M}$ is asymptotic (not convergent). Unitariy constraints are often used to resum perturbation theory (e.g., Dyson equations for unitarization), but this introduces model dependence.

---

## Dependencies Propagating from Module 7

### To Module 8 (Perturbation Mapping)
- Perturbing a coupling $g$ changes the scattering amplitude $\mathcal{M}$.
- Perturbing a mass parameter changes the pole position and the phase space.
- The LSZ formula provides a direct link from correlator perturbations to cross-section perturbations.

### To Module 9 (Effective Theories)
- Matching the S-matrix in an EFT to the UV theory requires computing amplitudes and demanding they agree.
- The optical theorem constrains the running of couplings.

### To Module 10 (Synthesis)
- The S-matrix and cross-sections are the primary observables.
- The bridge from field operators to data passes through spectral densities, LSZ, and phase space integrals.
- The distinction between stable (pole on real axis) and unstable (complex pole) particles is crucial for interpreting the particle spectrum.

---

## Epistemic Classification Summary (Module 7)

| Category | Number of Edges |
| :------- | :-------------: |
| Definitional | 5 |
| Derived | 14 |
| Conditional | 9 |
| Approx | 4 |
| Formal | 2 |
| **Total** | **34** |

---

## Key Open Questions After Module 7

1. **Is the S-matrix always well-defined?**
   - In massless theories, the S-matrix must be defined inclusively (with soft radiation). In theories with confinement, the S-matrix exists for bound states (hadrons), but not for elementary fields.

2. **What is the exact analytic structure of the propagator for an interacting theory?**
   - Beyond simple poles and branch cuts, non-perturbative effects (e.g., instantons, renormalons) can introduce additional singularities. This is largely unknown.

3. **How does the LSZ formula generalize to theories with unstable particles?**
   - Unstable particles are not asymptotic, so they cannot appear in initial/final states. Instead, they appear as intermediate resonances. The LSZ formula must be modified by including the complex pole prescription (e.g., using the Breit–Wigner propagator).

4. **Are the optical theorem and unitarity constraints sufficient to determine the theory?**
   - No—they are necessary but not sufficient. Many theories satisfy unitarity.

5. **How does the particle interpretation emerge from the spectral density in a gauge theory?**
   - Gauge-invariant operators (e.g., $F_{\mu\nu}$ for glueballs) have spectral representations. The physical states are gauge-invariant. The mapping from gauge-variant fields to physical states is non-trivial (requires BRST cohomology).

---

# STATE OF MODULE 7

**Established:**
- Källén–Lehmann representation as the bridge to particle poles.
- LSZ formula as the bridge from correlators to S-matrix (conditional, perturbative).
- Scattering amplitudes, cross-sections, decay rates as derived observable quantities.
- Unitarity and the optical theorem (exact conditional relations).
- Complex poles and Breit–Wigner for unstable particles.

**Not Established:**
- Rigorous construction of S-matrix for massless/confining theories.
- Generalization of LSZ for composite/gauge-invariant operators.
- Non-perturbative analytic structure of Green's functions.
- Relation between field-theoretic particles and asymptotic states in the presence of IR divergences.

**Mathematical Gaps:**
- The analytic continuation to the second Riemann sheet is not rigorously justified in all cases.
- The perturbative expansion of $\mathcal{M}$ is asymptotic; its relation to the exact S-matrix is unresolved.
- The existence of the infinite-volume limit for scattering amplitudes is assumed but not proven for general interacting QFTs in $d=4$.

---

## MODULE 8 AS METHODOLOGICAL PROOF-OF-CONCEPT

Module 8 is the explicit operational demonstration of the dependency-map method. Rather than merely cataloguing established structures, it selects a declared baseline theory, perturbs one target at a time, traces direct and indirect dependencies, computes first-order responses where justified, reassesses constraints, identifies observable consequences, and exposes feedback paths.

The intended analysis sequence is:

$$
\boxed{
\text{baseline theory}
\rightarrow
\text{perturbed node}
\rightarrow
\text{direct dependencies}
\rightarrow
\text{response}
\rightarrow
\text{constraint reassessment}
\rightarrow
\text{observable response}
\rightarrow
\text{feedback / unresolved boundary}
}
$$

This sequence is the operational form of the graph semantics defined at the beginning of the document. It is therefore treated as a demonstration of the method rather than as an independent change of subject.

---

# MODULE 8 — CONTROLLED PERTURBATION MAPPING

## BASELINE THEORY DEFINITION

**B8.0.1:** Theory: Massive real scalar $\phi^4$ in $d=4$ spacetime dimensions.

- Field content: Single real scalar field $\phi(x)$.
- Action:
$$S[\phi] = \int d^4 x \left[ \frac{1}{2} (\partial_\mu \phi)^2 - \frac{1}{2} m_0^2 \phi^2 - \frac{\lambda_0}{4!} \phi^4 \right]$$
- State: Poincaré-invariant vacuum $|0\rangle$.
- Boundary conditions: Fields vanish at infinity (so boundary terms in $\delta S$ vanish).
- Gauge choice: None (scalar theory, no gauge redundancy).
- Regularization: Dimensional regularization ($d = 4 - 2\epsilon$).
- Renormalization scheme: $\overline{\text{MS}}$ (modified minimal subtraction).
- Renormalized parameters: $m_R^2(\mu)$, $\lambda_R(\mu)$ at scale $\mu$.
- Approximation order: We compute responses to **first order** in perturbations of the input parameters. Higher-order responses are identified but not fully expanded unless required to expose a feedback loop. The perturbative expansion in $\lambda_R$ is treated as asymptotic.

**B8.0.2:** Baseline generating functional:
$$Z[J] = \int \mathcal{D}\phi\, \exp\left\{ iS[\phi] + i\int J\phi \right\}$$
with $S$ as above.

**B8.0.3:** Baseline correlation functions:
- Two-point function (Feynman propagator) $G_F(p^2)$.
- Connected four-point function (amplitude) $\mathcal{M}(s,t,u)$.

**B8.0.4:** Constraints in effect:
- Equations of motion (classical): $(\Box + m_0^2)\phi + \frac{\lambda_0}{6}\phi^3 = 0$.
- Quantum equations: Heisenberg equation for $\hat{\phi}$; Schwinger–Dyson equations for correlators.
- Ward identities: None (scalar, no gauge symmetry).
- Unitarity: $\mathcal{S}^\dagger\mathcal{S} = 1$ (imposes constraints on amplitudes).
- Normalization: $\langle 0|0\rangle = 1$.

---

## PERTURBATION TARGET #1: COUPLING CONSTANT $\lambda_R$

### Step 1 — Identify the Target
- Node: $\lambda_R(\mu)$ (renormalized quartic coupling at scale $\mu$).
- Perturbation: $\lambda_R \to \lambda_R + \delta\lambda$, with $\delta\lambda$ a small real parameter, $\mu$ held fixed.

### Step 2 — Constraint Check
- Does the perturbation preserve the equations of motion? The classical EOM becomes $(\Box + m^2)\phi + \frac{\lambda_R+\delta\lambda}{6}\phi^3 = 0$. This is a modified equation; the theory remains consistent if $\delta\lambda$ is small and the modified action is well-defined.
- Gauge constraints: None.
- State normalization: Not affected directly.
- Renormalization scheme: Changing $\lambda_R$ at fixed $\mu$ is a change of the physical theory, not a scheme change. It is permitted.

### Step 3 — Direct Dependencies
Every equation containing $\lambda_R$:
1. Action: $S = S_0 + \delta S$, $\delta S = -\frac{\delta\lambda}{4!}\int \phi^4$.
2. Lagrangian: $\mathcal{L} \to \mathcal{L} - \frac{\delta\lambda}{4!}\phi^4$.
3. Interaction term: $\mathcal{L}_{\text{int}} = -\frac{\lambda_R+\delta\lambda}{4!}\phi^4$.
4. Generating functional: $Z[J] \to Z[J] - i\frac{\delta\lambda}{4!} \int \frac{\delta^4 Z[J]}{\delta J(x)^4}$ (functional Taylor expansion).
5. Self-energy $\Sigma(p^2)$: Depends on $\lambda_R$ at 1-loop: $\Sigma^{(1)}(p^2) \propto \lambda_R$.
6. Beta function $\beta(\lambda_R)$: Depends on $\lambda_R^2$ at 1-loop.
7. Scattering amplitude $\mathcal{M}$: Depends on $\lambda_R$ (tree-level $\mathcal{M}_0 = -\lambda_R$).

### Step 4 — First-Order Response

Compute $\delta Y = \frac{\delta Y}{\delta \lambda_R} \delta\lambda$ for direct dependencies (functional derivatives where appropriate).

| Target $Y$ | Mathematical Bridge | Response $\delta Y$ | Type |
| :--------- | :------------------ | :------------------ | :--- |
| $S$ | $\delta S = -\frac{\delta\lambda}{4!}\int \phi^4$ | $\delta S = -\frac{\delta\lambda}{4!}\int \phi^4$ | Exact (definitional) |
| $\mathcal{L}$ | $\delta \mathcal{L} = -\frac{\delta\lambda}{4!}\phi^4$ | $\delta \mathcal{L} = -\frac{\delta\lambda}{4!}\phi^4$ | Exact |
| $Z[J]$ | $\delta Z = -i\frac{\delta\lambda}{4!}\int \frac{\delta^4 Z}{\delta J^4}$ | $\delta Z[J] = -i\frac{\delta\lambda}{4!}\int d^4x\, \frac{\delta^4 Z[J]}{\delta J(x)^4}$ | Formal (functional derivative) |
| Connected 4-pt $G_4^c$ | $\delta G_4^c = \frac{\delta^4 \delta W}{\delta J^4}$ | $\delta G_4^c(p_i) = -i \delta\lambda \, G_4^c \otimes G_4^c + \cdots$ (tree-level: $\delta \mathcal{M}_0 = -\delta\lambda$) | Approx (tree-level exact, loops involve higher derivatives) |
| Self-energy $\Sigma$ (1-loop) | $\Sigma^{(1)} = \frac{\lambda_R}{2} \int \frac{d^d k}{(2\pi)^d} \frac{i}{k^2-m^2+i\epsilon}$ | $\delta \Sigma^{(1)} = \frac{\delta\lambda}{2} \int \frac{d^d k}{(2\pi)^d} \frac{i}{k^2-m^2+i\epsilon}$ (divergent, renormalized by counterterms) | Approx (1-loop) |
| Beta function $\beta$ (1-loop) | $\beta^{(1)} = \frac{3\lambda_R^2}{16\pi^2}$ (MS) | $\delta\beta^{(1)} = \frac{3\lambda_R}{8\pi^2} \delta\lambda$ | Approx (1-loop) |

**Functional derivative for $Z[J]$:** This is an operator identity, valid to all orders if the functional integral exists. However, it is **formal** because $\delta^4 Z/\delta J^4$ requires renormalization.

### Step 5 — Higher-Order Response

- $\delta^2 S = 0$ (linear in $\lambda$).
- $\delta^2 Z$ receives contributions from $\frac{\delta^8 Z}{\delta J^8}$ times $(\delta\lambda)^2$, introducing new contact interactions.
- $\delta^2 \mathcal{M}$ includes two-loop corrections proportional to $\lambda_R (\delta\lambda)$ and $(\delta\lambda)^2$.
- **Unresolved**: The full non-perturbative dependence of $Z[J]$ on $\lambda$ is not known; the series in $\lambda$ is asymptotic.

### Step 6 — Constraint Reassessment
- The modified EOM is $(\Box + m^2)\phi + \frac{\lambda+\delta\lambda}{6}\phi^3 = 0$. The solution space changes continuously with $\delta\lambda$; no constraint is violated for small $\delta\lambda$.
- Unitarity: The S-matrix remains unitary if the theory is perturbatively unitary order-by-order. The change in $\mathcal{M}$ must satisfy the optical theorem to first order in $\delta\lambda$; this imposes relations between the imaginary parts of amplitudes, which are satisfied by the perturbative expansion.

### Step 7 — Observable Response
- **Scattering cross-section**: $\sigma_{2\to2}(s) \propto |\mathcal{M}|^2$. First-order response:
$$\delta \sigma = \frac{\partial \sigma}{\partial \lambda} \delta\lambda \simeq -2\frac{\lambda_R}{(4F)} \delta\lambda \, d\Phi_4 + \text{loop corrections}.$$
- **Physical mass**: $m_{\text{phys}}^2 = m_R^2 + \Sigma(m_{\text{phys}}^2)$. Since $\Sigma$ depends on $\lambda_R$, $\delta m_{\text{phys}}^2 = \frac{\partial \Sigma}{\partial \lambda}\delta\lambda$ (plus the implicit dependence through $m_{\text{phys}}$ itself). This is a feedback effect (see Step 8).

### Step 8 — Feedback
- **Self-energy feedback loop**: $\Sigma$ depends on $\lambda$ and $m_{\text{phys}}$. Changing $\lambda$ changes $\Sigma$, which changes $m_{\text{phys}}$, which changes $\Sigma$ (since $\Sigma$ depends on $m$). This is a loop:
$$\lambda \to \Sigma(\lambda, m) \to m_{\text{phys}} \to \Sigma(\lambda, m_{\text{phys}}) \to m_{\text{phys}}$$
- **Mathematical description**: The pole condition $m_{\text{phys}}^2 = m_R^2 + \Sigma(m_{\text{phys}}^2; \lambda)$ must be solved self-consistently. The response is:
$$\delta m_{\text{phys}}^2 = \frac{\partial \Sigma/\partial \lambda}{1 - \partial \Sigma/\partial m^2} \delta\lambda$$
(implicit function theorem). This is an exact relation if $\Sigma$ is known.
- **Unresolved**: $\Sigma$ is only known perturbatively; solving the full feedback equation is non-perturbative.

---

## PERTURBATION TARGET #2: MASS PARAMETER $m_R^2$

### Step 1 — Identify the Target
- Node: $m_R^2(\mu)$ (renormalized mass squared).
- Perturbation: $m_R^2 \to m_R^2 + \delta m^2$.

### Step 2 — Constraint Check
- The EOM becomes $(\Box + m^2+\delta m^2)\phi + \frac{\lambda}{6}\phi^3 = 0$. Valid.
- No gauge constraints.
- The perturbation is permitted.

### Step 3 — Direct Dependencies
1. Action: $\delta S = -\frac{\delta m^2}{2}\int \phi^2$.
2. Lagrangian: $\delta \mathcal{L} = -\frac{\delta m^2}{2}\phi^2$.
3. Free propagator: $G_F^{(0)}(p^2) = \frac{i}{p^2 - (m^2+\delta m^2) + i\epsilon}$.
4. Full propagator $G_F$ via Dyson equation.
5. Self-energy $\Sigma$: depends on $m$ through loop integrals (mass thresholds).
6. Phase space: $d\Phi_n$ depends on masses through $E_i = \sqrt{\mathbf{p}_i^2 + m_i^2}$.
7. Physical mass: $m_{\text{phys}}^2 = m_R^2 + \Sigma(m_{\text{phys}}^2)$.

### Step 4 — First-Order Response

| Target $Y$ | Mathematical Bridge | Response $\delta Y$ | Type |
| :--------- | :------------------ | :------------------ | :--- |
| $S$ | $\delta S = -\frac{\delta m^2}{2}\int \phi^2$ | $\delta S = -\frac{\delta m^2}{2}\int \phi^2$ | Exact |
| Free $G_F^{(0)}$ | $G_F^{(0)} = \frac{i}{p^2 - m^2}$ | $\delta G_F^{(0)} = \frac{i \delta m^2}{(p^2-m^2)^2}$ | Exact (differential) |
| Full $G_F$ | $G_F = G_F^{(0)} + G_F^{(0)}\Sigma G_F$ | $\delta G_F = \delta G_F^{(0)} + \delta G_F^{(0)}\Sigma G_F + G_F^{(0)}\delta\Sigma G_F + G_F^{(0)}\Sigma \delta G_F$ (implicit in $G_F$) | Exact (formal) |
| $\Sigma$ (1-loop) | $\Sigma \propto \int \frac{d^d k}{k^2-m^2}$ | $\delta \Sigma \propto \delta m^2 \int \frac{d^d k}{(k^2-m^2)^2}$ (IR sensitive) | Approx (1-loop) |
| Physical mass | $m_{\text{phys}}^2 = m^2 + \Sigma(m_{\text{phys}}^2)$ | $\delta m_{\text{phys}}^2 = \frac{\delta m^2 + \partial\Sigma/\partial m^2 \delta m^2}{1 - \partial\Sigma/\partial m^2}$ (feedback) | Exact (implicit) |
| Phase space $d\Phi_n$ | $E_i = \sqrt{\mathbf{p}_i^2 + m_i^2}$ | $\delta E_i = \frac{\delta m_i^2}{2E_i}$ | Exact (differential) |
| Cross-section $\sigma$ | $\sigma \propto |\mathcal{M}|^2 d\Phi_n$ | $\delta\sigma = \frac{\partial|\mathcal{M}|^2}{\partial m^2}\delta m^2 + |\mathcal{M}|^2 \delta(d\Phi_n)$ | Approx (if using perturbative $\mathcal{M}$) |

### Step 5 — Higher-Order Response
- $\delta^2 G_F$ involves $\delta m^4$ terms. The series in $\delta m^2$ is analytic around $m^2$ if the theory has a mass gap.
- The self-energy's dependence on $m^2$ through higher loops introduces non-linearities.

### Step 6 — Constraint Reassessment
- The modified EOM is valid.
- Unitarity: The optical theorem relates the change in $m^2$ to changes in the imaginary parts of amplitudes. The perturbative expansion satisfies this order-by-order.

### Step 7 — Observable Response
- **Physical mass shift**: $\delta m_{\text{phys}}^2$ is directly observable (e.g., as a shift in the pole of the propagator). This response includes the feedback from the self-energy.
- **Threshold behavior**: Changing $m^2$ shifts the threshold for multi-particle production, altering the spectral density $\rho(s)$ near $s = (2m)^2$.

### Step 8 — Feedback
- **Mass feedback**: $m^2 \to \Sigma(m^2) \to m_{\text{phys}}^2 \to \Sigma(m_{\text{phys}}^2)$ (same loop as above). The implicit function theorem gives the exact response as derived in Step 4.

---

## PERTURBATION TARGET #3: SOURCE TERM $J(x)$

### Step 1 — Identify the Target
- Node: $J(x)$ (external source field in $Z[J]$).
- Perturbation: $J(x) \to J(x) + \delta J(x)$, with $\delta J$ a smooth, compactly supported function.

### Step 2 — Constraint Check
- This is a permitted perturbation; it changes the generating functional and the vacuum expectation value of $\phi$.
- The equations of motion become $\langle \delta S/\delta\phi \rangle = -J(x)$ (Schwinger–Dyson). Perturbing $J$ changes the source term, but the theory remains consistent.

### Step 3 — Direct Dependencies
1. $Z[J]$: $\delta Z = \int \mathcal{D}\phi\, i\int \delta J \phi\, e^{iS+i\int J\phi}$.
2. $W[J] = -i\ln Z$: $\delta W = \langle \int \delta J \phi \rangle = \int \delta J \langle \phi \rangle$.
3. $\phi_c(x) = \delta W/\delta J(x)$: $\delta \phi_c(x) = \int d^4y\, \frac{\delta^2 W}{\delta J(x)\delta J(y)} \delta J(y) = \int G_F^c(x-y) \delta J(y)$.
4. Effective action $\Gamma[\phi_c]$: $\delta \Gamma/\delta \phi_c = -J$ (Legendre transform), so $\delta \phi_c$ is related to $\delta J$ via the inverse propagator.

### Step 4 — First-Order Response

| Target $Y$ | Mathematical Bridge | Response $\delta Y$ | Type |
| :--------- | :------------------ | :------------------ | :--- |
| $Z[J]$ | $\delta Z = i\int \delta J \phi \, e^{iS+i\int J\phi}$ | $\delta Z[J] = i\int d^4x\, \delta J(x) \frac{\delta Z[J]}{\delta J(x)}$ | Formal (exact functional) |
| $W[J]$ | $\delta W = \int \delta J \langle \phi \rangle$ | $\delta W[J] = \int d^4x\, \delta J(x) \phi_c(x)$ | Exact |
| $\phi_c(x)$ | $\phi_c(x) = \delta W/\delta J(x)$ | $\delta \phi_c(x) = \int d^4y\, G_F^c(x-y) \delta J(y)$ | Exact (connected propagator) |
| $G_F^c(x-y)$ | $\delta G_F^c = \frac{\delta^3 W}{\delta J^3}$ | $\delta G_F^c(x-y) = \int d^4z\, G_3^c(x,y,z) \delta J(z)$ | Formal (requires 3-point function) |
| $\Gamma[\phi]$ | $\delta \Gamma/\delta \phi_c = -J$ | $\delta \phi_c$ satisfies $-\int \frac{\delta^2 \Gamma}{\delta\phi_c\delta\phi_c} \delta\phi_c = \delta J$ | Exact (functional) |

### Step 5 — Higher-Order Response
- The full response of $\phi_c$ to $\delta J$ is non-linear: $\delta\phi_c$ includes terms proportional to $\delta J^2$ via the connected 3-point and higher functions. This is the generating functional of all correlators.

### Step 6 — Constraint Reassessment
- The Schwinger–Dyson equation is satisfied automatically by the definition of $\phi_c$.
- Boundary conditions: $\delta J$ is compactly supported, so $\phi_c$ falls off at infinity.

### Step 7 — Observable Response
- The change in the expectation value $\langle \phi(x) \rangle$ is $\delta\phi_c(x)$. This is the linear response function (susceptibility). It is measurable (e.g., as the response of a condensate to an external field).

### Step 8 — Feedback
- **Feedback through $\Gamma$**: The effective action $\Gamma$ depends on $\phi_c$. Changing $\phi_c$ changes $\Gamma$, which changes the relation between $J$ and $\phi_c$. This is the defining self-consistency of the Legendre transform:
$$J = -\frac{\delta \Gamma}{\delta \phi_c}, \quad \delta J = -\frac{\delta^2 \Gamma}{\delta \phi_c^2} \delta\phi_c - \frac{1}{2}\frac{\delta^3 \Gamma}{\delta \phi_c^3} (\delta\phi_c)^2 - \cdots$$
This is an exact loop: $\delta J \leftrightarrow \delta \phi_c$ through the full effective action. The inverse propagator $G^{-1} = -\delta^2\Gamma/\delta\phi_c^2$ is the response function.

---

## PERTURBATION TARGET #4: BACKGROUND FIELD $\phi_c(x)$ (Classical Configuration)

### Step 1 — Identify the Target
- Node: $\phi_c(x) = \langle \phi(x) \rangle$ (the vacuum expectation value, or a classical background).
- Perturbation: $\phi_c(x) \to \phi_c(x) + \delta \phi_c(x)$.

### Step 2 — Constraint Check
- This is a perturbation of the state (if $\phi_c \neq 0$ corresponds to spontaneous symmetry breaking) or a perturbation of the background. It is permitted if the effective action is convex (stability condition).
- The constraint is that the perturbed $\phi_c$ must satisfy the quantum EOM: $\frac{\delta \Gamma}{\delta\phi_c} = -J$. If we keep $J$ fixed, then $\delta\phi_c$ must satisfy $\frac{\delta^2 \Gamma}{\delta\phi_c^2}\delta\phi_c = 0$ (if $J$ fixed) or $-\frac{\delta^2 \Gamma}{\delta\phi_c^2}\delta\phi_c = \delta J$ (if $J$ changes). This is a dynamical constraint.

### Step 3 — Direct Dependencies
1. Effective action $\Gamma[\phi_c]$.
2. Effective potential $V_{\text{eff}}(\phi_c)$ (for constant $\phi_c$).
3. Propagator: $G^{-1}(x-y) = -\frac{\delta^2 \Gamma}{\delta\phi_c(x)\delta\phi_c(y)}$.
4. Higher $n$-point functions: $\Gamma^{(n)}(x_1,\ldots,x_n) = \frac{\delta^n \Gamma}{\delta\phi_c(x_1)\cdots\delta\phi_c(x_n)}$.

### Step 4 — First-Order Response

| Target $Y$ | Mathematical Bridge | Response $\delta Y$ | Type |
| :--------- | :------------------ | :------------------ | :--- |
| $\Gamma[\phi_c]$ | Taylor expansion | $\delta \Gamma = \int \frac{\delta\Gamma}{\delta\phi_c} \delta\phi_c + \frac{1}{2}\int\int \frac{\delta^2\Gamma}{\delta\phi_c\delta\phi_c}\delta\phi_c\delta\phi_c + \cdots$ | Exact (functional) |
| Effective potential $V_{\text{eff}}$ | For constant $\phi_c$: $V_{\text{eff}}(\phi_c)$ | $\delta V_{\text{eff}} = V'_{\text{eff}} \delta\phi_c + \frac{1}{2} V''_{\text{eff}}(\delta\phi_c)^2 + \cdots$ | Exact (if $V$ known) |
| Propagator inverse $G^{-1}$ | $G^{-1} = -\Gamma^{(2)}$ | $\delta G^{-1} = -\Gamma^{(3)} \delta\phi_c$ | Exact (requires 3-point function) |
| Mass of fluctuation | $m_{\text{eff}}^2 = V''_{\text{eff}}(\phi_c)$ | $\delta m_{\text{eff}}^2 = V'''_{\text{eff}} \delta\phi_c$ | Exact (tree-level effective potential) |

### Step 5 — Higher-Order Response
- The response of $G^{-1}$ to $\delta\phi_c$ involves $\Gamma^{(3)}$, $\Gamma^{(4)}$, etc. This is the full non-linear response of the spectrum to a background.

### Step 6 — Constraint Reassessment
- The stability condition: The Hessian $\Gamma^{(2)}$ must be positive (for a stable vacuum). If $\delta\phi_c$ moves the field into a region where $\Gamma^{(2)}$ has negative eigenvalues, the perturbation is unstable (tachyonic), and the perturbation is not permitted (it violates the constraint of a positive-definite physical spectrum).

### Step 7 — Observable Response
- A change in $\phi_c$ changes the masses of excitations (e.g., the Higgs mass in the Standard Model depends on the vacuum expectation value). This is observable via particle spectroscopy.

### Step 8 — Feedback
- **Self-energy feedback in the background**: The effective potential $V_{\text{eff}}(\phi_c)$ receives quantum corrections (the Coleman–Weinberg potential). The full $\phi_c$ dependence of $\Gamma$ means that changing $\phi_c$ changes the self-energy, which changes the mass, which changes $\Gamma$ again. This is encoded in the Schwinger–Dyson equations for the background.

---

## PERTURBATION TARGET #5: STATE (Vacuum → Thermal State)

### Step 1 — Identify the Target
- Node: The state, from vacuum $|0\rangle$ to a thermal density matrix $\rho_\beta = e^{-\beta H}/\text{Tr}(e^{-\beta H})$.

### Step 2 — Constraint Check
- This is a permitted perturbation if the theory admits a thermal state (KMS condition).
- **Constraint**: The thermal state is not translation-invariant in time (it is static but not Lorentz-invariant). The Poincaré invariance is broken by the thermal bath.

### Step 3 — Direct Dependencies
1. Correlation functions: $\langle \mathcal{O}_1(x_1)\cdots \rangle_\beta = \text{Tr}(\rho_\beta \mathcal{O}_1\cdots)$.
2. Propagator: Thermal propagator $G_\beta(p)$ with imaginary-time formalism (Matsubara frequencies).
3. Spectral density: $\rho_\beta(\omega, \mathbf{p})$ differs from $\rho(s)$ (has thermal factors).
4. Effective action: Thermal effective action $\Gamma_\beta[\phi]$.

### Step 4 — First-Order Response (Formal)
- **Response** (not a simple derivative; this is a state change):
$$\delta G_\beta(p) = G_\beta(p) - G_{T=0}(p) = \int d\omega' \, \frac{2i}{\omega-\omega'} n_B(\omega') \rho(\omega', \mathbf{p})$$
(in the imaginary-time formalism, $n_B$ is the Bose-Einstein distribution). This is an exact relation if the spectral function is known.

### Step 5 — Higher-Order Response
- Non-linear in $\beta$: higher-order terms involve multi-particle distributions.

### Step 6 — Constraint Reassessment
- The KMS condition must hold: $G_\beta(\tau) = G_\beta(\tau - \beta)$ in imaginary time.
- Unitarity: The thermal S-matrix is still unitary (if defined).

### Step 7 — Observable Response
- **Thermal masses**: The dispersion relation changes; particles acquire thermal masses (e.g., in a plasma).
- **Damping rates**: The spectral function has a width due to Landau damping.

### Step 8 — Feedback
- The thermal self-energy depends on the thermal distribution, which itself depends on the self-energy. This is a self-consistent Schwinger–Dyson equation at finite temperature (the gap equation). Unresolved non-perturbatively.

---

## PERTURBATION TARGET #6: OPERATOR INSERTION (Composite Operator $\mathcal{O}(x) = \frac{1}{2}\phi^2(x)$)

### Step 1 — Identify the Target
- Node: The operator $\mathcal{O}(x)$ inserted into a correlator.
- Perturbation: Add a term $\delta \mathcal{L} = \eta(x) \mathcal{O}(x)$ to the action (source for the composite operator).

### Step 2 — Constraint Check
- This is a valid perturbation; in $d=4$, the operator $\phi^2$ has canonical dimension 2 and is therefore relevant. The perturbation changes the mass parameter and is equivalent to perturbing $m^2$ (see Target #2), with $\delta m^2 = -\eta$ under the stated sign convention.

### Step 3 — Direct Dependencies
1. Action: $S \to S + \int \eta \mathcal{O}$.
2. Generating functional: $Z[J,\eta] = \int \mathcal{D}\phi\, e^{iS + i\int J\phi + i\int \eta \mathcal{O}}$.
3. Correlators with insertions of $\mathcal{O}$.

### Step 4 — First-Order Response
- $\frac{\delta Z[J,\eta]}{\delta \eta(x)}|_{\eta=0} = i \langle \mathcal{O}(x) \rangle_J$.
- The connected correlator $\langle \mathcal{O}(x) \phi(y) \rangle$ is the response of $\langle \phi(y) \rangle$ to $\eta$. This is the 3-point function with one $\mathcal{O}$ insertion.

### Step 5 — Higher-Order Response
- $\delta^2 Z/\delta\eta^2$ gives the 2-point function of $\mathcal{O}$.

### Step 6 — Constraint Reassessment
- The insertion of $\mathcal{O}$ must be renormalized (composite operator renormalization). The perturbation is defined only after specifying the renormalization of $\mathcal{O}$ (e.g., subtract divergences). This constraint is non-trivial.

### Step 7 — Observable Response
- The response of scattering amplitudes to a source of $\mathcal{O}$ can be measured (e.g., the response of cross-sections to changes in the Higgs vacuum expectation value, or to external scalar fields).

### Step 8 — Feedback
- The renormalization of $\mathcal{O}$ mixes with other operators (e.g., $\mathcal{O}$ mixes with the identity). This mixing introduces a feedback loop in the RG: $\eta$ runs with scale, and the running of $\eta$ depends on the anomalous dimension of $\mathcal{O}$, which depends on the couplings.

---

## PERTURBATION TARGET #7: RENORMALIZATION SCALE $\mu$

### Step 1 — Identify the Target
- Node: $\mu$ (the renormalization scale in $\overline{\text{MS}}$).
- Perturbation: $\mu \to \mu + \delta\mu$.

### Step 2 — Constraint Check
- This is **not** a perturbation of the physical theory. It is a change of the renormalization scheme parameter. It is permitted mathematically, but it must leave physical observables invariant.

### Step 3 — Direct Dependencies
1. Renormalized parameters: $m_R^2(\mu)$, $\lambda_R(\mu)$ run with $\mu$.
2. $Z$-factors: $Z_\phi(\mu)$, $Z_m(\mu)$, $Z_\lambda(\mu)$.
3. Correlation functions: $G_R^{(n)}$ depend on $\mu$.

### Step 4 — First-Order Response
- By the Callan–Symanzik equation:
$$\left( \mu\frac{\partial}{\partial \mu} + \beta \frac{\partial}{\partial \lambda} + \gamma_m m^2 \frac{\partial}{\partial m^2} + n\gamma_\phi \right) G_R^{(n)} = 0$$
Thus the response of $G_R^{(n)}$ to $\delta\mu$ is determined by the beta functions and anomalous dimensions. It is not zero; the correlator changes with $\mu$. However, physical observables (S-matrix elements) are independent of $\mu$ to all orders. This is a constraint.

### Step 5 — Higher-Order Response
- Higher-order derivatives of $\mu$ are governed by the RGE and its derivatives.

### Step 6 — Constraint Reassessment
- **Constraint**: $\frac{d}{d\mu} \mathcal{M}_{\text{phys}} = 0$ exactly. If this is not satisfied in a truncated perturbative expansion, the residual $\mu$-dependence is an artifact of the truncation.

### Step 7 — Observable Response
- **None**. The perturbation $\delta\mu$ produces no physical change; it only changes the intermediate representation. The observable consequence is zero (up to truncation errors).

### Step 8 — Feedback
- The RGE itself is a feedback equation: $dg/d\ln\mu = \beta(g)$. Changing $\mu$ changes $g$, which changes $\beta$, which changes how $g$ changes with $\mu$. This is a differential feedback loop.

---

## SUMMARY TABLE OF PERTURBATION TARGETS

| Perturbation Target | Permitted? | Gauge Artifact? | Field Redefinition? | Scheme Artifact? | Observable Consequence | Main Feedback Loop | Unresolved Step |
| :------------------ | :--------- | :-------------- | :------------------ | :--------------- | :--------------------- | :----------------- | :-------------- |
| $\lambda_R$ (coupling) | Yes | No | No (physical change) | No (if $\mu$ fixed) | Cross-sections change | Self-energy feedback via $m_{\text{phys}}$ | Full non-perturbative $\Sigma$ |
| $m_R^2$ (mass) | Yes | No | No | No | Pole mass shifts | Mass feedback in $\Sigma$ | IR divergences in massless limit |
| $J(x)$ (source) | Yes | No | No | No | $\langle\phi\rangle$ changes | $\Gamma$ feedback (Legendre) | Non-linear response requires all correlators |
| $\phi_c$ (background) | Yes (if stable) | No | No | No | Masses of excitations change | Effective potential feedback | Stability of effective potential |
| State (vacuum → thermal) | Yes | No | No | No | Thermal masses, damping | Thermal gap equation | Non-perturbative thermalization |
| $\mathcal{O}(x)$ (operator insertion) | Yes (with renormalization) | No | No | No | Correlators with $\mathcal{O}$ | Operator mixing (RG) | Composite operator renormalization |
| $\mu$ (scale) | Mathematically (not physical) | No | No | **Yes** | **None (scheme artifact)** | RGE differential loop | Truncation dependence of observables |

---

## FEEDBACK LOOP MAP (for $\lambda_R$ perturbation)

```
λ_R ────────────────────────────────────────────────┐
  │                                                  │
  ▼                                                  │
Self-energy Σ(p²; λ, m²)                           │
  │                                                  │
  ▼                                                  │
Dyson eq: G_F^{-1} = (G_F^{(0)})^{-1} - Σ          │
  │                                                  │
  ▼                                                  │
Physical mass: m_phys² = m² + Σ(m_phys²)           │
  │                                                  │
  ▼                                                  │
Σ depends on m_phys² (loop integrals) ◄─────────────┘
  │
  ▼
Scattering amplitude 𝒜 (depends on λ and m_phys)
  │
  ▼
Cross-section σ ∝ |𝒜|²
```

**Mathematical resolution of the loop**:
The self-consistent equation for $m_{\text{phys}}$ is:
$$m_{\text{phys}}^2 = m_R^2 + \Sigma(m_{\text{phys}}^2; \lambda_R, \mu)$$
The response to $\delta\lambda$ is:
$$\delta m_{\text{phys}}^2 = \frac{\partial \Sigma/\partial \lambda}{1 - \partial \Sigma/\partial m^2} \delta\lambda$$
This is **exact** if $\Sigma$ is known. However, $\Sigma$ is only known perturbatively; the exact solution of the gap equation is **unresolved**.

---

## SYMBOLICALLY UNRESOLVED STEPS

1. **Non-perturbative self-energy**: The full dependence of $\Sigma$ on $\lambda$ and $m$ is not known. The perturbative expansion is asymptotic; resummation techniques (e.g., Borel summation, RG improvement) are conditional.

2. **Stability of the effective potential**: For a background perturbation $\delta\phi_c$, the Hessian $\Gamma^{(2)}$ may develop negative eigenvalues (tachyonic instability). The full non-perturbative effective potential is not known; the perturbative expansion may fail.

3. **Thermal gap equation**: The self-consistent equation for the thermal mass involves divergent sums; requires resummation (e.g., hard thermal loop (HTL) approximation). The exact solution is not known.

4. **Operator mixing**: The composite operator $\phi^2$ mixes with the identity and with other operators under renormalization. The full mixing matrix is scheme-dependent and requires non-perturbative input.

5. **Scale invariance of observables**: The requirement $\frac{d}{d\mu}\mathcal{M}_{\text{phys}}=0$ is an exact constraint, but verifying it order-by-order in perturbation theory requires infinite-order cancellations. For truncated series, $\mu$-dependence remains; the convergence to the exact result is not proven.

6. **Haag's theorem**: The perturbation of the vacuum state (or the interaction picture) is not unitarily equivalent to the free theory in infinite volume. This undermines the perturbative definition of asymptotic states. The LSZ formula and S-matrix are defined formally; their rigorous existence is unresolved for $d=4$ interacting theories.

---

# MODULE 8 SYNTHESIS

## What is Directly Connected (for each perturbation)?
- Coupling $\lambda$ connects directly to $S$, $\mathcal{L}$, $Z[J]$, $\Sigma$, $\beta$, and $\mathcal{M}$.
- Mass $m^2$ connects directly to $S$, $G_F^{(0)}$, $\Sigma$, phase space, and $m_{\text{phys}}$.
- Source $J$ connects directly to $Z$, $W$, $\phi_c$, and $G_F^c$.
- Background $\phi_c$ connects directly to $\Gamma$, $V_{\text{eff}}$, and $G^{-1}$.
- Scale $\mu$ connects directly to $G_R$, $\lambda(\mu)$, $m(\mu)$, and $Z$-factors.

## What is Only Conditionally Connected?
- The response of $\mathcal{M}$ to $\lambda$ is only known perturbatively; exact relation requires the full non-perturbative amplitude.
- The response of the thermal state to temperature is only defined via the KMS condition; the thermal S-matrix requires careful IR regulation.

## What is Independent?
- Gauge-invariant physical observables (cross-sections, pole masses) are independent of the renormalization scale $\mu$ (exact constraint).
- Physical S-matrix is independent of field redefinitions (equivalence theorem).

## What is Constrained?
- The perturbation $\delta J$ is constrained by $\delta\phi_c = \int G_F^c \delta J$ (the response is the propagator).
- The perturbation $\delta\phi_c$ is constrained by stability: $\Gamma^{(2)}$ must be positive definite.
- The perturbation $\delta\mu$ is constrained by the Callan–Symanzik equation; it must leave observables invariant.

## What is Gauge-Dependent?
- None (scalar theory). In a gauge theory, responses of gauge-variant quantities (e.g., $A_\mu$) would be gauge-dependent.

## What is Observable?
- Changes in cross-sections, decay widths, and pole masses are observable.
- Changes in $\langle\phi\rangle$ are observable (condensates).
- Changes due to $\delta\mu$ are **not** observable.

## What Propagates?
- Perturbations propagate through the differential equations: EOM, Dyson equation, Schwinger–Dyson, RGE.
- The functional derivative chain propagates a change in $J$ to all $n$-point functions.

## What Feeds Back?
- Self-energy feedback: $\lambda \to \Sigma \to m_{\text{phys}} \to \Sigma$.
- Effective action feedback: $\phi_c \to \Gamma \to G^{-1} \to \phi_c$.
- RGE feedback: $\mu \to g \to \beta \to g$.

## What Changes Under Scale?
- Only scheme-dependent quantities (renormalized couplings, fields, Green functions) change with $\mu$.
- Physical observables do **not** change with $\mu$ (exact).

## What Remains Unresolved?
- Exact non-perturbative self-energy $\Sigma$.
- Stability of effective potential beyond perturbation theory.
- Thermal gap equation non-perturbatively.
- Composite operator mixing matrix.
- Convergence of perturbative series and $\mu$-independence to all orders.
- Rigorous scattering theory (Haag–Ruelle) for $d=4$ interacting theories.

---

# STATE OF MODULE 8

**Established:**
- Seven perturbation targets explicitly mapped.
- Direct, indirect, and feedback dependencies traced.
- First-order responses computed symbolically.
- Constraints checked for each perturbation.
- Observable consequences identified.
- Gauge/representation artifacts separated (none for scalar, but $\mu$-dependence flagged as scheme artifact).
- Unresolved steps explicitly marked.

**Not Established:**
- Numerical values are outside the declared scope of the mapping.
- Beyond first-order responses for non-linear couplings (higher-order functional derivatives).

**Mathematical Gaps:**
- The full non-perturbative solution of feedback loops is unresolved.
- The rigorous meaning of functional derivatives of $Z[J]$ in the presence of divergences is formal.

---

# MODULE 9 — CROSS-SCALE AND EFFECTIVE-THEORY RELATIONSHIPS

## 9.1 WILSONIAN EFFECTIVE ACTION AND CUTOFF

### Node Definitions

**N9.1.1:** Wilsonian effective action $S_{\text{eff}}[\phi; \Lambda]$

An action obtained by integrating out field modes with momenta above a cutoff $\Lambda$ (or above a matching scale):
$$e^{iS_{\text{eff}}[\phi_{<}; \Lambda]} = \int \mathcal{D}\phi_{>}\, e^{iS[\phi_{<}+\phi_{>}]}$$
where $\phi_{<}$ contains modes with $|p|<\Lambda$, $\phi_{>}$ with $|p|>\Lambda$.

- Status: Conditional on existence of a momentum-space decomposition; formal for non-perturbative.
- Assumption: A UV cutoff $\Lambda$ or a separation of scales.

**N9.1.2:** Cutoff $\Lambda$ (Wilsonian)

An energy scale separating "high-energy" modes that are integrated out from "low-energy" modes that remain dynamical.

- Status: Supplied parameter; not physical (scheme-dependent).
- Relationship: It is a regulator in the Wilsonian sense, but also a matching scale in EFT.

**N9.1.3:** High-energy modes $\phi_{>}$

Modes with $|p| > \Lambda$ (or $p^2 > \Lambda^2$). They are integrated out.

- Status: Formal.

**N9.1.4:** Low-energy modes $\phi_{<}$

Modes with $|p| < \Lambda$. They are the dynamical degrees of freedom of the effective theory.

- Status: Formal.

**N9.1.5:** Effective Lagrangian $\mathcal{L}_{\text{eff}}(\phi; \Lambda)$

The local (or quasi-local) Lagrangian obtained after integrating out heavy modes, expressed as an infinite series of local operators:
$$\mathcal{L}_{\text{eff}} = \sum_i c_i(\Lambda) \mathcal{O}_i[\phi]$$
with operator dimensions $d_i$ and Wilson coefficients $c_i(\Lambda)$.

- Status: Conditional on locality at low energy; typically formal.

---

## 9.2 WILSON COEFFICIENTS AND OPERATOR EXPANSION

**N9.2.1:** Wilson coefficients $c_i(\Lambda)$

The coefficients of the operators $\mathcal{O}_i$ in the effective Lagrangian. They encode the effects of the integrated-out heavy degrees of freedom.

- Status: Definitional.
- Dependencies: $c_i(\Lambda)$ are functions of the UV parameters (couplings, masses) and $\Lambda$.

**N9.2.2:** Operator basis $\{\mathcal{O}_i\}$

A complete set of local operators built from the low-energy fields and their derivatives, with definite symmetry properties.

- Status: Conditional on the low-energy field content and symmetries.

**N9.2.3:** Operator dimension $d_i$

The mass dimension of $\mathcal{O}_i$ in $d=4$: $d_i = [\mathcal{O}_i]$.

- Status: Derived from dimensional analysis.

**N9.2.4:** Power-counting suppression

The contribution of an operator $\mathcal{O}_i$ to amplitudes is suppressed by a factor of $(1/\Lambda)^{d_i-4}$ (for $d_i>4$) or enhanced by $\Lambda^{4-d_i}$ (for $d_i<4$). In a canonical EFT, the leading terms are those with the smallest $d_i$.

- Status: Derived; conditional on the existence of a hierarchy $\Lambda \gg m_{\text{low}}$.

---

## 9.3 MATCHING AND DECOUPLING

**N9.3.1:** Matching condition

The requirement that the effective theory reproduces the same low-energy physics (S-matrix elements, correlation functions) as the full UV theory, up to terms suppressed by powers of $E/\Lambda$ (where $E$ is the low-energy scale).
At the matching scale $\Lambda$:
$$S_{\text{eff}}[\phi; \Lambda] \simeq S_{\text{UV}}[\phi] + \text{terms suppressed by }1/\Lambda$$
or, more precisely, the Green functions of the effective theory equal those of the UV theory up to $O(E/\Lambda)$.

- Status: Conditional on perturbative matching; formal.

**N9.3.2:** Decoupling theorem (Appelquist–Carazzone)

If a heavy particle of mass $M$ is integrated out, its effects on low-energy observables are suppressed by powers of $E/M$ (or $1/M$), except for the renormalization of parameters (which may receive logarithms). In other words, heavy particles decouple from low-energy physics.

- Status: Conditional on a mass gap and renormalizable theory; holds in MS-like schemes with a careful definition of $\Lambda$.

**N9.3.3:** Matching scale $\mu_{\text{match}}$

The scale at which matching is performed. Often chosen to be the mass of the heavy particle ($\mu_{\text{match}} = M$) or the cutoff $\Lambda$.

- Status: Scheme-dependent; physical predictions are independent of the choice (up to higher-order corrections).

**N9.3.4:** Wilson coefficients at matching

At the matching scale, $c_i(\mu_{\text{match}})$ are computed by equating amplitudes in the full theory and the effective theory (tree-level or loop-level).

- Status: Approx (perturbative matching).

---

## 9.4 RG EVOLUTION OF WILSON COEFFICIENTS

**N9.4.1:** Renormalization group equation for Wilson coefficients

The Wilson coefficients $c_i(\mu)$ run with the renormalization scale $\mu$ (or with the cutoff $\Lambda$ in the Wilsonian sense):
$$\mu \frac{d}{d\mu} c_i(\mu) = \gamma_{ji} \, c_j(\mu)$$
where $\gamma_{ji}$ is the anomalous dimension matrix (including operator mixing).

- Status: Derived from the requirement that the effective action be independent of $\mu$.

**N9.4.2:** Anomalous dimension matrix $\gamma_{ji}$

Defined by $\gamma_{ji} = \frac{\mu}{2} \frac{d}{d\mu} \ln Z_{\mathcal{O}j}$ (with operator mixing). It is computed perturbatively.

- Status: Derived; scheme-dependent for off-diagonal elements, but physical combinations are scheme-independent.

**N9.4.3:** RG evolution of $c_i$ from $\mu_{\text{match}}$ to $\mu_{\text{low}}$

$$c_i(\mu_{\text{low}}) = U_{ij}(\mu_{\text{low}}, \mu_{\text{match}}) \, c_j(\mu_{\text{match}})$$
where $U$ is the path-ordered exponential of $\gamma$.

- Status: Derived; approximate if $\gamma$ is truncated perturbatively.

---

## 9.5 CONNECTION TO PERTURBATION MAPPING (MODULE 8)

**N9.5.1:** Response of Wilson coefficients to UV parameters

From Module 8, perturbing a UV parameter (e.g., $\lambda_{\text{UV}}$, $m_{\text{UV}}$) changes the matching conditions and thus the Wilson coefficients. The response is:
$$\delta c_i(\mu_{\text{match}}) = \frac{\partial c_i}{\partial g_{\text{UV}}} \delta g_{\text{UV}}$$
where $\partial c_i/\partial g_{\text{UV}}$ is computed from the matching calculation.

- Status: Approx (perturbative).

**N9.5.2:** Response of low-energy observables to Wilson coefficients

Once the Wilson coefficients are known, the low-energy observables (cross-sections, decay rates) depend on them. A change in $c_i$ propagates to observables:
$$\delta \mathcal{O}_{\text{obs}} = \sum_i \frac{\partial \mathcal{O}_{\text{obs}}}{\partial c_i} \delta c_i$$
This is a direct link to Module 8.

**N9.5.3:** Scale dependence of responses

The response of an observable to a UV parameter change is independent of the scale $\mu$ (if the RGE is used consistently). However, the response of the Wilson coefficients to $\mu$ is a scheme artifact.

---

## 9.6 UNRESOLVED ISSUES IN EFT

**N9.6.1:** Non-perturbative matching

Matching beyond perturbation theory is not well-defined; the exact relation between UV and effective theories is unknown in most cases.

**N9.6.2:** Operator mixing and completeness of basis

The operator basis may be infinite; truncation introduces errors. The full anomalous dimension matrix is not known.

**N9.6.3:** Power-counting violations

In some theories, operators with lower dimension can be generated through operator mixing (e.g., the $\theta$-term in QCD). These may require fine-tuning.

**N9.6.4:** Infrared divergences in matching

If the low-energy theory has massless particles, matching may be IR-sensitive; requires careful treatment.

**N9.6.5:** Existence of a Wilsonian cutoff

For non-perturbative theories (e.g., QCD), the Wilsonian effective action is defined on the lattice, but the continuum limit is not fully understood.

---

# RELATIONSHIP TABLE — MODULE 9

| Source Node | Target Node | Relationship Type | Mathematical Bridge | Required Assumptions | Direction | Local/Nonlocal | Exact/Approx | Gauge/Rep Dependence | Observable Consequence | Epistemic Status |
| :---------- | :---------- | :---------------- | :------------------ | :------------------- | :-------- | :------------- | :----------- | :------------------- | :--------------------- | :--------------- |
| N2.1.1 UV Action $S_{\text{UV}}$ | N9.1.1 Wilsonian $S_{\text{eff}}[\Lambda]$ | Integration | $e^{iS_{\text{eff}}[\phi_<]} = \int \mathcal{D}\phi_> e^{iS_{\text{UV}}[\phi_<+\phi_>]}$ | Momentum cutoff, separation of scales | Unidirectional | Nonlocal (functional) | Formal | Scheme-dependent (cutoff) | Effective dynamics | Conditional |
| N9.1.1 $S_{\text{eff}}$ | N9.1.5 $\mathcal{L}_{\text{eff}}$ | Expansion | $\mathcal{L}_{\text{eff}} = \sum_i c_i(\Lambda)\mathcal{O}_i$ | Locality at low energy | Unidirectional | Local | Approx (truncated) | Scheme-dependent | Effective Lagrangian | Conditional |
| N9.2.1 $c_i(\Lambda)$ | N9.2.2 Operator basis | Association | $c_i$ multiplies $\mathcal{O}_i$ | Operator basis complete | Unidirectional | Local | Exact (definition) | Scheme-dependent | Operator contribution | Definitional |
| N9.2.1 $c_i$ | N9.2.3 $d_i$ | Dimensional analysis | $[c_i] = d - d_i$ (in $d=4$: $[c_i] = 4 - d_i$) | Dimensional analysis | Unidirectional | Global | Exact | Independent | Operator relevance | Definitional |
| N9.2.1 $c_i$ | N9.2.4 Power counting | Suppression | $c_i$ scales as $\Lambda^{4-d_i}$ (up to logs) | Mass gap, hierarchy | Unidirectional | Global | Approx (leading order) | Scheme-dependent | EFT expansion | Derived |
| N9.3.1 Matching condition | N2.1.1 $S_{\text{UV}}$ and N9.1.1 $S_{\text{eff}}$ | Constraint | $S_{\text{eff}}[\phi; \mu_{\text{match}}] = S_{\text{UV}}[\phi] + O(\Lambda^{-n})$ | Perturbative matching | Unidirectional | Global | Approx (truncated) | Scheme-dependent | Equivalence at low energy | Conditional |
| N9.3.1 Matching | N9.2.1 $c_i$ | Determination | $c_i(\mu_{\text{match}})$ computed from UV amplitudes | Matching condition | Unidirectional | Global | Approx (loop expansion) | Scheme-dependent | Wilson coefficients at scale | Approx |
| N9.3.2 Decoupling theorem | N9.3.1 Matching | Consequence | For heavy mass $M$, $c_i$ suppressed by $1/M^{d_i-4}$ | Mass gap, renormalizable | Unidirectional | Global | Exact (asymptotic) | Scheme-independent (physical) | Heavy particles decouple | Supported |
| N9.4.1 RGE for $c_i$ | N9.2.1 $c_i$ | Differential | $\mu \frac{d}{d\mu} c_i = \gamma_{ji} c_j$ | RG invariance | Bidirectional | Global | Approx (perturbative) | Scheme-dependent (but physical combos invariant) | Scale dependence of Wilson coefficients | Derived |
| N9.4.2 Anomalous dimension $\gamma$ | N9.4.1 RGE | Definition | $\gamma_{ji} = \frac{\mu}{2} \frac{d}{d\mu} \ln Z_{\mathcal{O} j}$ (operator mixing) | Operator renormalization | Unidirectional | Global | Approx | Scheme-dependent | Mixing of operators | Derived |
| N9.4.3 RG evolution | N9.4.1 RGE | Integration | $c_i(\mu_{\text{low}}) = U_{ij}(\mu_{\text{low}},\mu_{\text{match}}) c_j(\mu_{\text{match}})$ | RGE solution | Unidirectional | Global | Approx (truncated) | Scheme-dependent | Low-energy coefficients | Derived |
| N9.5.1 Response of $c_i$ to UV params | Module 8 perturbations | Functional derivative | $\delta c_i(\mu_{\text{match}}) = \frac{\partial c_i}{\partial g_{\text{UV}}} \delta g_{\text{UV}}$ | Matching calculation | Unidirectional | Global | Approx (perturbative) | Scheme-dependent | Observable response | Conditional |
| N9.5.2 Response of observables | N9.2.1 $c_i$ | Chain rule | $\delta \mathcal{O}_{\text{obs}} = \sum_i \frac{\partial \mathcal{O}_{\text{obs}}}{\partial c_i} \delta c_i$ | EFT calculation | Unidirectional | Global | Approx | Scheme-independent (observables) | Physical effects | Derived |
| N9.5.3 Scale independence of observables | N9.4.1 RGE | Constraint | $\frac{d}{d\mu} \mathcal{O}_{\text{obs}} = 0$ (exact) | RGE consistency | Bidirectional | Global | Exact | Scheme-independent | Observables invariant | Derived |
| N9.1.1 $S_{\text{eff}}$ | N6.3.1 Callan–Symanzik | Relationship | The RGE for $c_i$ is equivalent to the Callan–Symanzik equation for the effective action | RG | Bidirectional | Global | Exact | Scheme-dependent | Scale dependence | Derived |
| N9.6.1 Non-perturbative matching | N9.3.1 Matching | Generalization | Unknown | Non-perturbative UV theory | — | — | Unresolved | — | — | Unresolved |
| N9.6.2 Operator mixing | N9.4.2 $\gamma$ | Incomplete | Operator basis infinite; mixing matrix truncated | Perturbative truncation | — | — | Approx | — | — | Unresolved |

---

# MODULE 9 SYNTHESIS

## Relationships Established

### Wilsonian Effective Action and Cutoff
1. **Effective Action via Integration**: $S_{\text{eff}}[\phi_<;\Lambda]$ is obtained by integrating out high-energy modes ($\phi_>$) in the path integral.
   - This is a **formal** construction; it requires a cutoff and a separation of scales.
   - The resulting $\mathcal{L}_{\text{eff}}$ is an infinite series of local operators: $\sum_i c_i(\Lambda) \mathcal{O}_i$.

2. **Wilson Coefficients**: $c_i(\Lambda)$ encode the effects of the integrated-out physics.
   - Their mass dimensions determine power counting: $[c_i] = 4 - d_i$ (in $d=4$).
   - Operators with $d_i > 4$ are irrelevant (suppressed by $1/\Lambda^{d_i-4}$); $d_i < 4$ are relevant (enhanced by $\Lambda^{4-d_i}$); $d_i = 4$ are marginal.

### Matching and Decoupling
3. **Matching Condition**: At the matching scale $\mu_{\text{match}}$ (often the heavy mass), the effective theory must reproduce the UV theory's low-energy physics up to power-suppressed corrections.
   - Wilson coefficients are computed by equating amplitudes (perturbatively).
   - The **decoupling theorem** states that heavy particles decouple at low energy; their effects are suppressed by powers of $E/M$.

### RG Evolution of Wilson Coefficients
4. **RGE for $c_i$**: $\mu \frac{d}{d\mu} c_i = \gamma_{ji} c_j$, where $\gamma_{ji}$ is the anomalous dimension matrix (including operator mixing).
   - This is derived from the requirement that the effective action is $\mu$-independent.
   - The evolution from $\mu_{\text{match}}$ to $\mu_{\text{low}}$ is given by the path-ordered exponential of $\gamma$.

### Connection to Module 8 (Perturbation Mapping)
5. **Response of $c_i$ to UV Parameters**: A change in a UV coupling or mass changes the matching conditions and thus $c_i$:
   - $\delta c_i(\mu_{\text{match}}) = \frac{\partial c_i}{\partial g_{\text{UV}}} \delta g_{\text{UV}}$.
   - This propagates to low-energy observables: $\delta \mathcal{O}_{\text{obs}} = \sum_i \frac{\partial \mathcal{O}_{\text{obs}}}{\partial c_i} \delta c_i$.
   - The physical observables are independent of $\mu$ (and $\Lambda$) exactly, providing a consistency check.

### Unresolved Issues
6. **Non-perturbative matching**: Beyond perturbation theory, the matching condition is not known.
7. **Operator mixing and infinite basis**: The operator basis may be infinite; truncation introduces errors. The full anomalous dimension matrix is not known.
8. **Power-counting violations**: Some theories generate lower-dimensional operators via mixing (e.g., the $\theta$-term), requiring fine-tuning.
9. **IR divergences**: Matching in massless theories is IR-sensitive, requiring careful treatment.

---

## Key Open Questions After Module 9

1. **Is the Wilsonian effective action unique?**
   - No; it depends on the choice of cutoff $\Lambda$, the choice of field variables, and the operator basis. However, physical observables are independent.

2. **How does the Wilsonian RG relate to the MS scheme?**
   - The Wilsonian RG integrates out modes (a change of $\Lambda$), while the MS scheme changes the renormalization scale $\mu$ without integrating out modes. The two are related but not identical; the Wilsonian action is non-local at $\Lambda$, while the MS effective action is local but has running couplings.

3. **Can all effects of heavy particles be captured by local operators?**
   - At low energy, yes (up to exponentially suppressed effects if there is a mass gap). Non-local effects (e.g., from massless particles) require a different treatment.

4. **How does operator mixing affect the EFT expansion?**
   - Mixing can generate lower-dimensional operators from higher-dimensional ones, altering the power counting. This requires a careful analysis.

5. **Is the decoupling theorem exact?**
   - In renormalizable theories with a mass gap, the decoupling theorem holds in the sense that heavy particles decouple up to power-suppressed terms. However, in theories with massless particles or scale invariance, decoupling may not hold.

---

## Dependencies Propagating from Module 9 to Module 10

- The Wilson coefficients $c_i$ are central nodes connecting UV parameters (Module 8) to low-energy observables (Module 7).
- The RGE for $c_i$ relates to the beta functions (Module 6) and the anomalous dimensions of operators.
- The matching condition provides a bridge between the full theory and the effective theory, which is essential for synthesizing the global dependency map.

---

# STATE OF MODULE 9

**Established:**
- Wilsonian effective action and cutoff.
- Wilson coefficients and operator expansion.
- Matching and decoupling.
- RGE for Wilson coefficients.
- Connection to perturbation responses.
- Unresolved issues explicitly listed.

**Not Established:**
- Non-perturbative matching.
- Full operator mixing and basis completeness.
- Rigorous definition of the Wilsonian effective action beyond perturbation theory.

**Mathematical Gaps:**
- The path integral over high-energy modes is not well-defined non-perturbatively.
- The locality of the effective action is assumed; may be violated by non-local effects.

---

# MODULE 10 — GLOBAL RELATIONSHIP AND DEPENDENCY SYNTHESIS

This module consolidates all established mathematical relationships from Modules 1–9 into a unified dependency system. The synthesis preserves the epistemic classifications and distinguishes universal, formulation-specific, model-specific, approximation-specific, and unresolved structures.

## 10.0 GRAPH ARCHITECTURE

The global map is not a single undifferentiated graph. It is a set of synchronized graph views over the same node and edge inventory.

| Graph View | Primary Question | Representative Path |
| :--------- | :--------------- | :------------------ |
| **ONTOLOGICAL GRAPH** | What objects, operators, equations, constraints, and states are present? | fields, states, operators |
| **MATHEMATICAL CONSTRUCTION GRAPH** | How is one object constructed from another? | $S\to\text{E-L}$, $Z[J]\to G_n$ |
| **CONSTRAINT GRAPH** | What restricts admissible structures? | unitarity $\to\mathcal S$, BRST $\to\mathcal H_{\rm phys}$ |
| **REPRESENTATION GRAPH** | Which formulations or descriptions encode the same structure? | canonical $\leftrightarrow$ path integral |
| **OBSERVABLE GRAPH** | How does formal structure reach measurable quantities? | $G_n\to$ LSZ $\to\mathcal M\to\sigma$ |
| **FEEDBACK GRAPH** | Where do directed paths return to upstream variables? | $\lambda\to\Sigma\to m_{\rm phys}\to\Sigma$ |
| **UNRESOLVED-BOUNDARY GRAPH** | Where does a dependency path terminate because existence or derivation remains unresolved? | path integral $\to$ nonperturbative boundary |

These are views of one dependency system, not independent theories. The same node may therefore appear in multiple views with different relation types.

### Canonical Backbone

The principal QFT dependency backbone represented across the modules is:

```text
spacetime / field structure
        |
        v
     action / formulation
        |
        +------> equations of motion
        |
        +------> quantization
                    |
                    +------> correlators / Green functions
                    |             |
                    |             +------> spectral structure ------> particle interpretation
                    |             |
                    |             +------> LSZ ------> amplitudes ------> observables
                    |
                    +------> symmetry / gauge structure ------> constraints
                    |
                    +------> renormalization ------> RG / scale structure
                                                       |
                                                       +------> EFT / matching
```

This backbone is a navigation view. The detailed module tables remain authoritative for the individual relationship records, preconditions, and epistemic classifications.

### Feedback Backbone

The principal feedback structures are:

```text
coupling λ  ---> self-energy Σ ---> physical mass ---> Σ
source J    <--> classical field φ_c <--> effective action Γ
scale μ     ---> running coupling g ---> β(g) ---> running coupling
thermal T   ---> thermal self-energy ---> thermal mass ---> thermal self-energy
operator η  ---> expectation value ---> Z-matrix ---> anomalous dimension ---> η
```

These are **cycles in the dependency graph**, not exceptions to a directed-graph representation. A graph may be directed while containing directed cycles; therefore the global system is not, in general, a directed acyclic graph.

### Universal / Formulation / Model / Approximation Hierarchy

A dependency belongs to the narrowest level that is justified by its prerequisites:

$$
\boxed{
\text{universal}
\supset
\text{formulation-specific}
\supset
\text{model-specific}
\supset
\text{approximation-specific}
}
$$

The inclusion symbols denote increasing specificity, not logical implication that every higher-level construction follows from every lower-level construction. A relationship must be promoted to a broader level only when its stated assumptions establish that promotion.

### Epistemic Path Composition

For an edge chain

$$
A \xrightarrow{e_1} B \xrightarrow{e_2} C \xrightarrow{e_3} Z,
$$

the final path label is the strongest status justified by the **weakest necessary edge, node, or precondition**. In particular:

- exact algebraic identities remain exact as identities even when their downstream physical use is conditional;
- formal functional relations remain formal when their defining functional measure or operator domain is not rigorously constructed;
- perturbative predictions remain approximation-specific even when the equations from which they are computed are exact;
- a path through an unresolved boundary cannot be promoted to an established prediction without an independent resolution of that boundary.

### Dependency Interruption Matrix

For major paths, the graph should identify what happens when a prerequisite is removed:

| Path Element | Removed Prerequisite | Result |
| :----------- | :------------------- | :----- |
| Correlator $\to$ LSZ $\to \mathcal S$ | asymptotic states | Standard LSZ scattering path unavailable |
| Källén-Lehmann positivity | positive-metric assumptions | Positive spectral-density conclusion unavailable in the standard form |
| Faddeev-Popov construction | declared gauge fixing | Gauge-fixed determinant representation must be reformulated |
| RG-improved observable | consistent running/matching | Residual scale dependence no longer represents a controlled RG cancellation |
| Perturbative prediction | perturbative truncation | The truncated result no longer specifies the exact theory |

The interruption result is itself a graph annotation: it identifies the dependency on the removed prerequisite without asserting that the entire theory becomes inconsistent.

---


## 10.1 COMPLETE RELATIONSHIP GRAPH (CATEGORICAL COMPILATION)

**Node Grouping:**

1. **Spacetime Primitives** (Module 1): \(M, x^\mu, d, g_{\mu\nu}, \eta_{\mu\nu}, \text{Poincaré}, \text{Causal Structure}\).  
2. **Field Primitives** (Module 1): \(\Phi_i(x), \psi(x), A_\mu(x), \hat{\Phi}(x)\), Classical vs Quantum.  
3. **State Space** (Module 1): \(\mathcal{H}, |\Psi\rangle, \rho, |0\rangle\).  
4. **Action & Variational** (Module 2): \(S[\Phi], \mathcal{L}, V(\Phi), \text{E-L Equations}, \Pi, H\).  
5. **Quantization** (Module 3): Canonical \([\,\,,\,\,]\), Path Integral \(Z[J]\), Schwinger-Dyson.  
6. **Correlation & Propagation** (Module 4): \(G_F, G_R, G_A, \mathcal{W}, \Sigma, \rho(s)\), Dyson Equation.  
7. **Symmetry & Gauge** (Module 5): Noether Current, Ward Identities, BRST, Anomalies.  
8. **Renormalization & Scale** (Module 6): \(\mu, \beta(g), \gamma_\Phi\), RG flow, Fixed Points.  
9. **Spectral & Scattering** (Module 7): LSZ, \(\mathcal{M}, \sigma, \Gamma\), Unitarity, Complex Poles.  
10. **Effective Theory** (Module 9): \(\Lambda, S_{\text{eff}}, c_i(\Lambda)\), Matching, Running of \(c_i\).

**Conditional Backbone Pathways (valid when the stated prerequisites hold):**
- Manifold \(\to\) Fields (as sections) \(\to\) Correlators (via states) is definitional.  
- If a Lagrangian exists \(\to\) Euler-Lagrange \(\to\) Green's functions (linearized) \(\to\) Propagators.  
- If Wightman axioms hold \(\to\) Källén–Lehmann spectral decomposition \(\to\) Particle poles.  
- If asymptotic states exist \(\to\) LSZ \(\to\) S-matrix \(\to\) Cross-sections.

---

## 10.2 DIRECT DEPENDENCY MAP (NON-NEGOTIABLE CHAINS)

| Chain ID | Source Node | Intermediate Node(s) | Target Node | Mathematical Bridge | Epistemic Status |
| :------- | :---------- | :------------------- | :---------- | :------------------- | :--------------- |
| **D1** | \(S[\Phi]\) (action) | Euler-Lagrange equations | Classical field equations | \(\frac{\delta S}{\delta \Phi}=0\) | Derived (conditional on Lagrangian) |
| **D2** | \(Z[J]\) (generating functional) | Functional derivatives | \(n\)-point correlators \(G_n\) | \(\frac{\delta^n Z}{\delta J^n} \propto \langle T\Phi^n \rangle\) | Formal/Conditional |
| **D3** | Connected \(W[J]\) | Functional derivatives | Connected \(G_n^c\) | \(\frac{\delta^n W}{\delta J^n}\) | Formal/Conditional |
| **D4** | Correlators \(G_n\) | LSZ Reduction (amputation + on-shell limit) | S-matrix element \(\mathcal{M}\) | \(\lim_{p^2\to m^2} (p^2-m^2) G_n\) | Conditional on asymptotic states |
| **D5** | Scattering amplitude \(\mathcal{M}\) | Phase space integration | Cross-section \(\sigma\) / Decay rate \(\Gamma\) | \(d\sigma \propto \|\mathcal{M}\|^2 d\Phi_n\) | Derived (relativistic QM) |
| **D6** | Canonical variables \(\Phi,\Pi\) | Commutator | Quantum Heisenberg eq. | \([\hat{\Phi},\hat{\Pi}]=i\hbar\delta\) | Conditional on canonical quantization |
| **D7** | Bare params \(g_0, m_0\) | Counterterms (\(Z\)-factors) | Renormalized params \(g_R, m_R\) | \(g_0 = \mu^{\Delta}Z_g g_R\) | Conditional on renormalization |
| **D8** | Renormalized params \(g_R\) | Beta function \(\beta(g)\) | Running coupling \(g(\mu)\) | \(\mu \partial_\mu g = \beta(g)\) | Derived (perturbative) |
| **D9** | Heavy field \(M\) | Matching at \(\mu_{\text{match}}\) | Wilson coefficient \(c_i(\mu)\) | Equate amplitudes | Conditional (EFT) |

---

## 10.3 INDIRECT DEPENDENCY MAP (VIA INTERMEDIATES)

| Chain ID | Source Perturbation | Intermediate Dependencies | Terminal Observable | Path Length | Epistemic Status |
| :------- | :------------------- | :------------------------- | :------------------ | :----------- | :--------------- |
| **I1** | UV coupling \(\lambda_{\text{UV}}\) | \(c_i(\mu_{\text{match}}) \to \text{RGE} \to c_i(\mu_{\text{low}}) \to \text{EFT amplitude}\) | Low-energy cross-section | 4 | Conditional/Approx |
| **I2** | Mass \(m_0\) | \(m_{\text{phys}} = m_0 + \Sigma(m_{\text{phys}}) \to \text{pole position} \to \text{LSZ}\) | S-matrix pole mass | 3 | Conditional/Formal |
| **I3** | Gauge parameter \(\xi\) (in gauge-fixing) | Propagator \(G_F^{\xi} \to \text{correlators} \to \text{amplitudes}\) | **No change** (cancellation) | 3 | Conditional/Exact |
| **I4** | Renormalization scale \(\mu\) | \(\lambda_R(\mu) \to G_R(p^2;\mu) \to \text{S-matrix}\) | **No change** (exact) | 3 | Conditional/Exact |

---

## 10.4 FEEDBACK LOOP MAP

| Loop ID | Nodes | Mathematical Relation | Type | Whether it returns to origin | Exact/Approx |
| :------ | :---- | :--------------------- | :--- | :--------------------------- | :----------- |
| **F1** | \(\lambda \to \Sigma \to m_{\text{phys}} \to \Sigma\) | \(m_{\text{phys}}^2 = m_R^2 + \Sigma(m_{\text{phys}}^2;\lambda)\) | Algebraic (gap equation) | Yes | Exact if \(\Sigma\) known; perturbative in practice |
| **F2** | \(J \to \phi_c \to \Gamma[\phi_c] \to J\) | \(J = -\delta \Gamma/\delta \phi_c\) ; Legendre transform | Functional (Legendre) | Yes | Exact (formal) |
| **F3** | \(\mu \to g(\mu) \to \beta(g) \to \partial_\mu g\) | \(\mu \partial_\mu g = \beta(g)\) | Differential (RG flow) | Yes | Approx (truncated) |
| **F4** | Thermal \(T \to \Sigma_T \to m_{\text{th}} \to \Sigma_T\) | \(m_{\text{th}}^2 = m^2 + \Sigma_T(m_{\text{th}}^2;T)\) | Algebraic (thermal gap) | Yes | Unresolved (non-perturbative) |
| **F5** | Operator insertion \(\eta \to \langle \mathcal{O} \rangle \to Z\)-factors | Composite operator renormalization mixes operators | Matrix (RG mixing) | Yes (via anomalous dims) | Approx |

**Distinction:**  
- **F1/F4** are *dynamical/statistical* feedback (mass depends on self-energy which depends on mass).  
- **F2** is *definitional* feedback (Legendre transform is self-consistent).  
- **F3** is *differential* feedback (slope depends on the value).  
- **F5** is *renormalization-mediated* feedback.

---

## 10.5 CONSTRAINT MAP

| Constraint Type | Nodes Involved | Mathematical Form | Imposes Restriction On | Epistemic Status |
| :-------------- | :------------- | :---------------- | :--------------------- | :--------------- |
| **Euler-Lagrange** | \(\Phi, S\) | \(\frac{\delta S}{\delta \Phi}=0\) | Field configurations (classical) | Derived (conditional) |
| **Gauss/Gauge** | \(A_\mu, \Pi\) | \(\nabla \cdot \mathbf{E} = \rho\) (QED) or \(G[A]=0\) | Gauge transformations | Conditional |
| **BRST physicality** | \(Q_B, |\Psi\rangle\) | \(Q_B|\Psi\rangle=0\) (mod \(Q_B\)) | Physical Hilbert space | Conditional |
| **Unitarity** | \(\mathcal{S}\) | \(\mathcal{S}^\dagger \mathcal{S} = 1\) | S-matrix elements | Conditional |
| **Spectral positivity** | \(\rho(s)\) | \(\rho(s) \ge 0\), \(\int \rho = 1\) | Källén-Lehmann measure | Derived (Wightman) |
| **Microcausality** | \(\mathcal{O}(x), \mathcal{O}(y)\) | \([\mathcal{O}(x),\mathcal{O}(y)]=0\) for spacelike | Operator support | Conditional |
| **Stability (vacuum)** | \(\Gamma[\phi], V_{\text{eff}}\) | \(\Gamma^{(2)} \ge 0\) (convexity) | Background perturbations | Conditional |
| **Renormalization** | \(g_0, g_R\) | \(d\mathcal{M}_{\text{phys}}/d\mu = 0\) | Scale variation of observables | Derived/Exact |
| **KMS (thermal)** | \(G_\beta(\tau)\) | \(G_\beta(\tau) = G_\beta(\tau-\beta)\) | Thermal states | Conditional |

---

## 10.6 GAUGE, FIELD-REDEFINITION, AND REPRESENTATION FILTER

| Quantity / Node | Gauge-Dependent? | Field-Redefinition Dependent? | Representation Dependent? | Scheme Dependent? | Physical/ Observable? |
| :-------------- | :--------------- | :---------------------------- | :------------------------- | :---------------- | :-------------------- |
| **Action \(S[\Phi]\)** | Yes (if gauge) | Yes (changes by boundary terms) | Yes | No | No |
| **Propagator \(G_F(x-y)\)** | Yes (gauge-variant fields) | Yes | Yes | Yes (MS vs OS) | No |
| **Effective action \(\Gamma[\phi]\)** | Yes (gauge-variant) | Yes | Yes | Yes | No |
| **S-matrix elements** | **No** | **No** (equivalence theorem) | **No** | **No** | **Yes** |
| **Pole mass \(m_{\text{phys}}\)** | **No** (gauge-invariant operator) | **No** | **No** | **No** | **Yes** |
| **Cross-section \(\sigma\)** | **No** | **No** | **No** | **No** | **Yes** |
| **Wilson coefficients \(c_i(\mu)\)** | Yes (if operators gauge-variant) | Yes | Yes | Yes | No |
| **Beta function \(\beta(g)\)** | Yes (scheme-dep beyond 2-loop) | No (physical combination) | No | Yes (higher orders) | No |
| **Anomalous dimension \(\gamma_\Phi\)** | Yes | Yes | Yes | Yes | No |
| **Vacuum expectation value \(\langle \Phi \rangle\)** | Yes (if \(\Phi\) gauge-variant) | Yes | Yes | Yes | Only if gauge-invariant combo |

---

## 10.7 OBSERVABLE MAP (TRACING BACK TO MATHEMATICS)

| Observable Quantity | Mathematical Construction Chain | Required Assumptions | Epistemic Status |
| :------------------ | :------------------------------- | :------------------- | :--------------- |
| **Particle Mass** | Pole of \(G_F(p^2)\) \(\to\) Källén-Lehmann \(\rho(s)\) \(\to\) Spectral decomposition | Wightman axioms + stable state | Derived/Supported |
| **Scattering Cross-section** | \(\mathcal{M}\) (from LSZ) \(\to\) \(|\mathcal{M}|^2\) \(\to\) Phase space \(d\Phi_n\) | Asymptotic states + perturbative computability | Derived/Supported |
| **Decay Width / Lifetime** | \(\Gamma = \frac{1}{2M} \int |\mathcal{M}|^2 d\Phi_n\) \(\to\) Complex pole: \(\Gamma = \text{Im}\Sigma/m\) | Unitarity + analytic continuation | Derived/Supported |
| **Vacuum Energy / Casimir** | \(\sum_n \frac{\omega_n}{2}\) (regularized) \(\to\) Renormalization | QFT + boundary conditions | Conditional/Tested |
| **Thermal masses** | \(m_{\text{th}}^2 = m^2 + \Sigma_T(m_{\text{th}}^2;T)\) \(\to\) KMS condition | Finite-temperature QFT | Conditional/Supported |
| **Anomalous processes** | \(\partial_\mu J^{5\mu} = \frac{g^2}{16\pi^2} F\tilde{F}\) \(\to\) Triangle diagrams | Chiral fermions | Model-Dependent/Supported |

---

## 10.8 RENORMALIZATION-DEPENDENCE MAP

| Quantity | Depends on \(\mu\)? | Depends on Scheme (OS vs MS)? | Physical Consequence? |
| :------- | :----------------- | :---------------------------- | :--------------------- |
| **Renormalized coupling \(g_R(\mu)\)** | Yes | Yes | No (intermediate) |
| **Renormalized mass \(m_R(\mu)\)** | Yes | Yes | No |
| **Bare parameters \(g_0, m_0\)** | No | No (but divergent) | No |
| **Pole mass \(m_{\text{phys}}\)** | **No** | **No** | Yes |
| **S-matrix / Cross-sections** | **No** | **No** | Yes |
| **Anomalous dimension \(\gamma(g)\)** | Yes | Yes (beyond 1-loop) | No |
| **Wilson coefficient \(c_i(\mu)\)** | Yes | Yes | No |
| **Effective potential \(V_{\text{eff}}(\phi)\)** | Yes | Yes | No (but minima may be scheme-independent) |

---

## 10.9 MODEL-DEPENDENT vs. UNIVERSAL RELATIONSHIPS

**Universal (Structural, independent of specific Lagrangian):**
1. **Causal structure**: Microcausality \([\mathcal{O}(x),\mathcal{O}(y)]=0\) for spacelike separation (if locality holds).
2. **Spectral decomposition**: \(G_F(p^2) = \int_0^\infty \frac{i\rho(s)}{p^2-s+i\epsilon} ds\) (under Wightman axioms).
3. **Unitarity**: \(\mathcal{S}^\dagger\mathcal{S} = 1\) (if asymptotic completeness holds).
4. **LSZ formalism**: The bridge from correlators to S-matrix (conditional on asymptotic states).
5. **RG invariance**: Physical observables independent of renormalization scale \(\mu\).
6. **Noether's theorem (if Lagrangian exists)**: Symmetry \(\to\) conserved current \(\to\) charge.

**Conditional or formulation-specific (requires specific assumptions):**
1. **Lorentz/Poincaré invariance**: Requires flat spacetime or a Killing vector.
2. **Lagrangian existence**: Required for EL equations and Noether's theorem.
3. **Gauge symmetry**: Requires local symmetry group and associated gauge fields.
4. **Renormalizability**: Requires operator dimensions \(\le d\).
5. **Particle interpretation**: Requires asymptotic states (mass gap or inclusive treatment).
6. **Spontaneous symmetry breaking**: Requires degenerate vacuum.

**Model-Dependent (Specific to QED, QCD, SM, \(\phi^4\), etc.):**
1. **Specific field content** (scalars, spinors, vectors in specific representations).
2. **Specific interaction terms** (Yukawa, gauge, quartic).
3. **Specific gauge group** (U(1), SU(3), etc.).
4. **Specific mass spectrum** and mixing angles.
5. **Specific anomaly coefficients**.

---

## 10.10 SYMBOLICALLY UNRESOLVED BOUNDARIES

| Unresolved Step | Module Reference | Reason for Unresolved Status |
| :-------------- | :--------------- | :--------------------------- |
| **Path-integral measure \(\mathcal{D}\Phi\)** | Module 3 | Not rigorously defined in \(d=4\) interacting QFT (requires lattice or constructive QFT). |
| **Haag's theorem** | Module 3 | Interaction picture not unitarily equivalent to free picture in infinite volume; perturbative expansion is formal. |
| **Existence of interacting QFT in \(d=4\)** | Module 3 | Millennium Problem; no rigorous non-perturbative construction (except trivial/super-renormalizable). |
| **Non-perturbative self-energy \(\Sigma\)** | Modules 4, 8 | Exact gap equation \(m_{\text{phys}}^2 = m^2 + \Sigma(m_{\text{phys}}^2)\) cannot be solved exactly in QCD/\(\phi^4\). |
| **Confinement (QCD)** | Module 7 | Asymptotic states are hadrons, not quarks/gluons; LSZ for quarks is invalid. |
| **Landau pole vs. triviality (\(\phi^4\))** | Module 6 | Perturbative beta function suggests Landau pole, but lattice suggests triviality (vanishing UV coupling). |
| **Non-perturbative matching (UV to EFT)** | Module 9 | Matching requires full UV theory; not known for QCD to ChPT beyond perturbation theory. |
| **Borel summability of perturbative series** | Module 6 | QFT perturbative series is asymptotic; relation to exact theory via Borel resummation is unproven for most cases. |
| **Thermal gap equation** | Module 8 | Non-perturbative solution of \(m_{\text{th}}^2 = m^2 + \Sigma_T(m_{\text{th}}^2;T)\) in QCD plasma is unresolved. |
| **Operator mixing basis completeness** | Module 9 | Infinite set of operators; truncation errors are uncontrolled. |
| **Gribov ambiguity** | Module 5 | Faddeev-Popov gauge fixing fails when gauge condition has multiple solutions (non-perturbative). |

---

## 10.11 EMPIRICALLY TESTED RELATIONSHIPS

| Relationship | Test/Evidence | Epistemic Status |
| :----------- | :------------ | :--------------- |
| **Propagator pole \(\to\) particle mass** | Measured masses of electron, Z boson, etc. | Supported (QED/EW) |
| **LSZ \(\to\) S-matrix \(\to\) cross-section** | QED \(e^+e^- \to \mu^+\mu^-\), QCD jets, Higgs decays | Supported (Standard Model) |
| **Optical theorem / Unitarity** | Total cross-sections; \(e^+e^- \to\) hadrons | Supported |
| **Chiral anomaly** | \(\pi^0 \to \gamma\gamma\) decay width | Supported (QCD) |
| **Scale anomaly / Running couplings** | Running of \(\alpha_s\) from DIS experiments | Supported |
| **Higgs mechanism / SSB** | Discovery of Higgs boson, \(W/Z\) masses | Supported |
| **Decoupling theorem** | Heavy quarks decouple in low-energy QCD | Supported (in MS with careful matching) |
| **Thermal masses in plasma** | Quark-gluon plasma phenomenology | Partially supported (lattice QCD) |

---

## 10.12 FINAL SYNTHESIS ANSWERS (A–J)

### **A. What is directly connected?**
Direct connections exist via **definitional operations** (functional derivatives, Legendre transforms, path integrals) and **differential equations** (Euler-Lagrange, Heisenberg, Schwinger-Dyson, RG flow).  
- **Example**: \(Z[J]\) directly connects to all \(n\)-point functions via \(\delta^n Z / \delta J^n\).  
- **Example**: \(S[\Phi]\) directly connects to field equations via \(\delta S=0\).  

### **B. What is only conditionally connected?**
- **Lagrangian \(\to\) Hamiltonian**: Requires a non-degenerate Legendre transform (no primary constraints).  
- **Classical symmetry \(\to\) quantum conservation**: Requires absence of anomalies.  
- **Correlators \(\to\) S-matrix**: Requires asymptotic states (LSZ) and stable external particles.  
- **UV parameters \(\to\) low-energy observables**: Requires matching and RG evolution (valid in perturbative EFT).  

### **C. What is independent?**
- **Physical observables** (S-matrix, pole masses, cross-sections) are **independent** of:  
  - Gauge choice (gauge invariance).  
  - Field redefinitions (equivalence theorem).  
  - Renormalization scale \(\mu\) and scheme (exact to all orders).  
- **The regularization procedure** is independent of the physical theory (it is an intermediate artifact).  

### **D. What is constrained?**
- **Gauge configurations** are constrained by Gauss's law / BRST cohomology (\(Q_B|\Psi\rangle=0\)).  
- **Background fields** are constrained by stability (\(\Gamma^{(2)} \ge 0\)).  
- **S-matrix elements** are constrained by unitarity (\(\mathcal{S}^\dagger\mathcal{S}=1\)) and crossing symmetry.  
- **Vacuum states** are constrained by positivity (\(\rho(s) \ge 0\)).  

### **E. What is gauge-dependent?**
- **Individual correlators** of gauge-variant fields (e.g., \(\langle A_\mu A_\nu \rangle\)).  
- **Propagator \(G_F\)** in covariant gauges.  
- **Effective action \(\Gamma[\phi]\)** (for gauge-variant \(\phi\)).  
- **Off-shell Green functions**.  
- **Ghost and gauge-fixing terms**.  

### **F. What is observable?**
- **S-matrix elements** (scattering amplitudes).  
- **Cross-sections** and **decay rates** (derived from \(|\mathcal{M}|^2\)).  
- **Pole masses** of gauge-invariant operators (physical spectrum).  
- **Anomalous effects** (e.g., \(\pi^0 \to \gamma\gamma\) from chiral anomaly).  
- **Thermal equilibrium properties** (pressure, energy density from thermal correlators).  

### **G. What propagates?**
Perturbations propagate through:  
- **Differential equations**: EOM (field response), Heisenberg (operator evolution), RG flow (coupling response).  
- **Functional equations**: Schwinger-Dyson (source response), Legendre transform (\(\phi_c\) response).  
- **Integral equations**: Dyson equation (self-energy response), Bethe-Salpeter (bound state response).  

### **H. What feeds back?**
Genuine feedback loops identified:  
1. **Self-energy loop**: \(\lambda \to \Sigma \to m_{\text{phys}} \to \Sigma\) (gap equation).  
2. **Effective action loop**: \(J \leftrightarrow \phi_c \leftrightarrow \Gamma\) (Legendre consistency).  
3. **RG loop**: \(\mu \to g \to \beta \to \partial_\mu g\) (differential flow).  
4. **Thermal loop**: \(T \to \Sigma_T \to m_{\text{th}} \to \Sigma_T\) (thermal gap).  
5. **Operator mixing loop**: \(\eta \to \langle \mathcal{O} \rangle \to Z\)-matrix \(\to \gamma \to \eta\) (RG of composite operators).  

### **I. What changes under scale?**
- **Renormalized couplings and masses** \(g_R(\mu), m_R(\mu)\).  
- **Field strengths / \(Z\)-factors** \(Z_\Phi(\mu)\).  
- **Wilson coefficients** \(c_i(\mu)\).  
- **Effective potential \(V_{\text{eff}}(\phi;\mu)\)**.  
- **Anomalous dimensions** \(\gamma(g)\).  
- **Physical observables** do **not** change with scale (exact constraint).  

### **J. What remains unresolved?**
1. **Rigorous mathematical definition** of interacting QFT in \(d=4\) (Millennium Problem).  
2. **Non-perturbative path-integral measure** \(\mathcal{D}\Phi\).  
3. **Haag's theorem** implications for the perturbative vacuum.  
4. **Non-perturbative solution of the gap equation** (self-energy).  
5. **Confinement mechanism** and hadronic spectrum from QCD.  
6. **Landau pole vs. triviality** of \(\phi^4\) in \(d=4\).  
7. **Non-perturbative matching** between UV and EFTs.  
8. **Borel summability / exact meaning** of asymptotic perturbative series.  
9. **Gribov ambiguity** in non-perturbative gauge fixing.  
10. **Thermal gap equation** in QCD plasma.  

---

## EPISTEMIC SUMMARY (ALL MODULES)

| Category | Number of Established Relationships | Key Examples |
| :------- | :---------------------------------- | :----------- |
| **Definitional** | ~35 | \(S = \int \mathcal{L}\), \(Z[J] = \int \mathcal{D}\Phi e^{iS}\), LSZ formula. |
| **Derived** | ~45 | E-L equations, Noether's theorem, Dyson equation, Optical theorem. |
| **Conditional** | ~55 | Path-integral/canonical equivalence, decoupling theorem, Ward identities. |
| **Approx/Perturbative** | ~18 | Beta functions, matching, Breit-Wigner. |
| **Formal/Unresolved** | ~15 | Path-integral measure, Haag's theorem, non-perturbative gap equation. |
| **Model-Dependent** | ~12 | Specific Lagrangians, gauge groups, field content. |
| **Supported/Tested** | ~8 | Running couplings, chiral anomaly, Higgs mechanism. |

---

## FINAL MATHEMATICAL GOVERNING PRINCIPLE

**The structure of QFT is a directed dependency graph containing acyclic dependency regions and explicit feedback cycles:**

- **Universal root nodes**: Spacetime manifold, fields as sections, states.  
- **Conditional branches**: Lagrangian vs. Algebraic; Canonical vs. Path-Integral; Perturbative vs. Non-perturbative.  
- **Converging observables**: All physical predictions (masses, cross-sections, decay rates) converge to the S-matrix and spectral functions via the **LSZ reduction** and **Källén-Lehmann** bridges.  
- **Gauge/Redundancy filter**: Gauge-variant intermediate quantities must cancel or combine into gauge-invariant structures along any path used to establish a physical observable.  
- **Scale filter**: All intermediate \(\mu\)-dependent quantities cancel in physical observables (RG invariance).  
- **Major unresolved attractor**: The non-perturbative regime (confinement, triviality, strong coupling) remains mathematically unresolved for \(d=4\), marking the boundary between well-defined perturbative expansions and the exact, unknown mathematical structure.

**Primary conclusion of the map:** The mathematical connections within perturbative QFT are extensively mapped and structurally coherent across the Dyson-Schwinger hierarchy, renormalization-group structure, LSZ reduction, and related bridges. Paths to non-perturbative predictions may terminate at explicitly identified unresolved nodes, indicating that the declared graph captures an extensive perturbative and formal dependency structure without constituting a complete non-perturbative mathematical construction of QFT.
