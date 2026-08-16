# QFT NUMERIC CONSTANTS, PARAMETERS, AND MEASURED-QUANTITY ADDENDUM

## 1. Purpose and scope

This addendum is the numerical companion to `qft_relationship_map.md`.

The QFT relationship map is intentionally structural and symbolic. It maps fields, states, actions, quantization procedures, correlators, symmetries, gauge structure, renormalization, spectral objects, scattering, perturbations, feedback, and effective-theory relationships. It does not embed measured numerical values into those symbolic structures.

This addendum provides a separately versioned numerical layer for quantities that instantiate the structures in the map. The numerical layer preserves the distinction among exact defining constants, measured quantities, fitted parameters, scale-dependent parameters, scheme-dependent parameters, derived quantities, and bounds.

## 2. Numeric-node schema

| Field | Meaning |
|---|---|
| Numeric ID | Stable identifier for the numerical record. |
| Quantity | Human-readable name. |
| Symbol | Mathematical symbol. |
| Value | Central value, exact value, interval, or bound. |
| Uncertainty / confidence | Standard uncertainty, confidence statement, or limit. |
| Units | Unit system and units. |
| Numeric status | Exact, measured, inferred, derived, bound, scheme-dependent, scale-dependent, model-dependent, or approximate. |
| Scale | Renormalization or physical scale when relevant. |
| Scheme | Renormalization/parameter convention when relevant. |
| Definition / context | Precise meaning and applicability. |
| Source | Primary data source or authoritative compilation. |
| Reference vintage | Release or edition. |
| Map linkage | Structural-map node(s) to which the quantity connects. |
| Notes | Qualifications required to interpret the value correctly. |

## 3. Numeric status taxonomy

- **Exact:** fixed by definition or an exact defining relation within the stated convention.
- **Measured:** directly constrained by experiment with an uncertainty.
- **Inferred:** obtained from data through a stated theory/model fit.
- **Derived:** calculated from other registered values.
- **Bound:** upper/lower/interval constraint rather than a central measurement.
- **Scheme-dependent:** depends on renormalization prescription.
- **Scale-dependent:** depends on a declared energy/momentum scale.
- **Model-dependent:** numerical inference depends on a specified physical model or fit.
- **Approximate:** approximation to an exact or more general quantity.

## 4. Fundamental constants used by QFT

The NIST/CODATA 2022 values are the current CODATA set available in the NIST database as of this addendum; NIST identifies the next regularly scheduled adjustment as the 2026 CODATA adjustment. citeturn936054search0turn936054search2

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Numeric status | Map linkage |
|---|---|---|---:|---|---|---|---|
| NUM-QFT-0001 | Speed of light in vacuum | \(c\) | 299 792 458 | exact | m s\(^{-1}\) | Exact | External parameter; N1 and spacetime layer |
| NUM-QFT-0002 | Planck constant | \(h\) | 6.62607015 × 10\(^{-34}\) | exact | J Hz\(^{-1}\) | Exact | External parameter; N2 action/quantum layer |
| NUM-QFT-0003 | Reduced Planck constant | \(\hbar\) | 1.054571817… × 10\(^{-34}\) | exact | J s | Exact/derived | N3 quantization layer |
| NUM-QFT-0004 | Elementary charge | \(e\) | 1.602176634 × 10\(^{-19}\) | exact | C | Exact | Gauge/electromagnetic structures |
| NUM-QFT-0005 | Fine-structure constant | \(\alpha\) | 7.2973525643 × 10\(^{-3}\) | 0.0000000011 × 10\(^{-3}\) | dimensionless | Measured/recommended | Gauge-coupling and observable layers |
| NUM-QFT-0006 | Inverse fine-structure constant | \(\alpha^{-1}\) | 137.035999177 | ±0.000000021 | dimensionless | Measured/recommended | Gauge-coupling layer |
| NUM-QFT-0007 | Newtonian gravitational constant | \(G_N\) | 6.67430 × 10\(^{-11}\) | 0.00015 × 10\(^{-11}\) | m\(^3\) kg\(^{-1}\) s\(^{-2}\) | Measured/recommended | External gravity parameter; not an intrinsic QFT gauge coupling |

NIST reports the 2022 values of \(c\), \(h\), \(e\), and \(\alpha\), including their exact/uncertain status. citeturn936054search36turn936054search37

## 5. Standard Model particle masses and electroweak quantities

Particle masses and widths are numerical physical quantities rather than universal structural primitives of the QFT map. The values below use the 2024 Particle Data Group Review of Particle Physics as the source vintage. PDG provides both summary tables and machine-readable data resources. citeturn333983search7turn333983search9turn333983search1

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Numeric status | Map linkage | Source / vintage |
|---|---|---|---:|---|---|---|---|---|
| NUM-QFT-0008 | Electron mass | \(m_e\) | 0.51099895000 | ±0.00000000015 | MeV | Measured/recommended | N7.1.5 physical mass; spectral pole layer | PDG 2024 |
| NUM-QFT-0009 | Muon mass | \(m_\mu\) | 105.6583755 | ±0.0000023 | MeV | Measured/recommended | N7.1.5 | PDG 2024 |
| NUM-QFT-0010 | Z-boson mass | \(m_Z\) | 91.1880 | ±0.0020 | GeV | Measured/recommended | N7.1.5; electroweak observable layer | PDG 2024 |
| NUM-QFT-0011 | W-boson mass | \(m_W\) | 80.3692 | ±0.0133 | GeV | Measured/recommended | N7.1.5; electroweak observable layer | PDG 2024 |
| NUM-QFT-0012 | Higgs-boson mass | \(m_H\) | 125.20 | ±0.11 | GeV | Measured/recommended | N7.1.5; SSB/Higgs layer | PDG 2024 |
| NUM-QFT-0013 | Fermi constant | \(G_F\) | 1.1663788 × 10\(^{-5}\) | ±0.0000006 × 10\(^{-5}\) | GeV\(^{-2}\) | Measured/recommended | Weak-interaction coupling; observable layer |
| NUM-QFT-0014 | Weak mixing angle, \(\overline{\mathrm{MS}}\) | \(\sin^2\hat\theta_W(M_Z)\) | 0.23129 | ±0.00004 | dimensionless | Inferred / scheme-dependent | N5 gauge structure; renormalization layer | PDG 2024 |

The PDG 2024 constants tables report \(\alpha_s(M_Z)=0.1180(9)\), \(m_Z=91.1880(20)\) GeV, \(m_W=80.3692(133)\) GeV, and \(G_F=1.1663788(6)\times10^{-5}\) GeV\(^{-2}\). citeturn333983search12 The PDG Higgs listing gives \(m_H=125.20\pm0.11\) GeV. citeturn333983search14 The PDG 2024 electroweak review lists \(\sin^2\hat\theta_W(M_Z)=0.23129(4)\) in the stated \(\overline{\mathrm{MS}}\) convention. citeturn333983search13 The electron and muon values are given in the PDG 2024 lepton tables. citeturn963544search26

## 6. Strong coupling and running-parameter entries

A QFT numeric registry must not record a running coupling as a bare scalar without its scale and convention.

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Scale / scheme | Numeric status | Map linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-QFT-0015 | Strong coupling | \(\alpha_s(M_Z)\) | 0.1180 | ±0.0009 | \(\mu=M_Z\); PDG convention | Scale-dependent / measured-recommended | N6.3.2 beta function; N6.3.4 running coupling; N9.4 RGE | PDG 2024 |

PDG explicitly identifies this quantity as \(\alpha_s(m_Z)=0.1180(9)\). citeturn333983search12

The structural map therefore treats

\[
\alpha_s=\alpha_s(\mu;\,\text{scheme},\,\text{definition})
\]

rather than identifying the number 0.1180 with an invariant constant of QCD.

## 7. Selected critical and anomalous quantities

Critical exponents and anomalous dimensions require a much stricter provenance convention than ordinary constants because they may depend on universality class, model, dimension, normalization, renormalization convention, perturbative order, or numerical method.

The registry therefore uses the following schema for such entries even when a value is not yet populated:

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Theory / model | Dimension | Method | Scheme / normalization | Status | Map linkage |
|---|---|---|---:|---|---|---:|---|---|---|---|
| NUM-QFT-0016 | Critical exponent | \(\nu\) | registry entry required | — | specified model required | specified | specified | specified | Model-dependent | N6.3.7 critical exponent |
| NUM-QFT-0017 | Critical exponent | \(\eta\) | registry entry required | — | specified model required | specified | specified | specified | Model-dependent | N6.3.7; N6.3.3 anomalous dimension |
| NUM-QFT-0018 | Field anomalous dimension | \(\gamma_\Phi\) | registry entry required | — | specified QFT | specified | perturbative/nonperturbative method required | scheme required | Scheme- and model-dependent | N6.3.3 |

These records deliberately require the theory/model, dimension, computational method, and normalization to be specified before a numerical value can be considered admissible. The structural map defines \(\theta=\beta'(g^*)\) and \(\gamma_\Phi\) symbolically; the numerical value belongs to the addendum only when the corresponding universality class or renormalization convention is identified. fileciteturn4file0L164-L181

## 8. Numerical quantities associated with the perturbation map

Module 8 uses massive real scalar \(\phi^4\) theory in \(d=4\), dimensional regularization, and the \(\overline{\mathrm{MS}}\) scheme. fileciteturn4file0L812-L842

A numerical instantiation of that module must therefore record the complete baseline tuple:

\[
(\text{field content},d,m_R^2,\lambda_R,\mu,\text{regulator},\text{scheme},\text{perturbative order}).
\]

The addendum should not accept a numerical value for \(\lambda_R\), \(m_R\), or \(\mu\) without these qualifiers.

| Numeric ID | Quantity | Symbol | Value | Required context | Numeric status | Map linkage |
|---|---|---|---:|---|---|---|
| NUM-QFT-0019 | Renormalized quartic coupling | \(\lambda_R\) | no universal value | \(\phi^4\), \(d=4\), \(\mu\), scheme required | Scale-/scheme-dependent | Module 8; N6.2.4, N6.3.4 |
| NUM-QFT-0020 | Renormalized mass | \(m_R\) or \(m_R^2\) | no universal value | theory, \(\mu\), scheme required | Scale-/scheme-dependent | Module 8; N6.2.4 |
| NUM-QFT-0021 | Renormalization scale | \(\mu\) | no universal value | chosen calculation scale | Scheme/context parameter | Module 6; Module 8 |

These are intentionally not populated with arbitrary numbers. A numerical value without the complete context would falsely suggest universality.

## 9. Observable numerical quantities

Observable quantities should be recorded separately from the intermediate theoretical parameters that predict them.

| Numeric ID | Observable class | Symbol | Numeric requirements | Map linkage |
|---|---|---|---|---|
| NUM-QFT-0022 | Particle mass | \(m_{\rm phys}\) | pole definition; state identification; experimental source | N7.1.5 |
| NUM-QFT-0023 | Decay width | \(\Gamma\) | particle, channel set, pole/Breit-Wigner convention where relevant | N7.4.5, N7.6.3 |
| NUM-QFT-0024 | Cross-section | \(\sigma\) | process, kinematics, beam conditions, cuts, radiative-order definition | N7.4.3–N7.4.4 |
| NUM-QFT-0025 | Branching ratio | \(\mathrm{Br}\) | parent particle and channel definition | N7.4.6 |

A numerical observable must remain linked to the corresponding experimental definition. For example, a cross-section value is not a pure property of the symbolic amplitude \(\mathcal M\); it also depends on the process, kinematic domain, phase-space definition, and experimental/theoretical treatment.

## 10. Numeric-to-structural linkage rules

1. A numeric record instantiates a symbolic quantity; it does not alter the symbolic definition.
2. A numerical value must inherit every assumption necessary to define the quantity being instantiated.
3. A running parameter requires an explicit scale.
4. A scheme-dependent parameter requires an explicit scheme.
5. A fitted quantity requires the data/model combination used for the fit.
6. A derived quantity retains provenance to every upstream numerical input.
7. A measured quantity must not be substituted for a theoretical parameter when the relation between them contains a nontrivial matching or renormalization step.
8. A bound must remain distinguishable from a measurement.
9. Correlated numerical inputs should retain their covariance reference rather than being represented as independent scalars.
10. Numerical values do not change structural closure of the QFT graph. They are instantiations of the graph, not new structural edges.

## 11. Numerical uncertainty propagation

For derived quantity \(Y=f(X_1,\ldots,X_n)\), the addendum should preserve covariance information whenever available. In linear approximation,

\[
\sigma_Y^2 \approx \sum_{i,j}
\frac{\partial f}{\partial X_i}
\frac{\partial f}{\partial X_j}
\operatorname{Cov}(X_i,X_j).
\]

The registry therefore distinguishes:

- independent uncertainty;
- correlated uncertainty;
- theoretical/systematic uncertainty;
- experimental statistical uncertainty;
- model uncertainty;
- scheme/scale variation.

These categories should not be silently combined.

## 12. Numeric epistemic propagation

For a structural path

\[
A\rightarrow B\rightarrow C,
\]

the numerical instantiation of \(C\) must preserve any upstream qualification that is essential to the path.

Examples:

\[
\text{data}\rightarrow\text{fit}\rightarrow g(\mu)
\]

produces a model- and scheme-qualified numerical parameter.

\[
\text{measured spectrum}\rightarrow\text{pole extraction}\rightarrow m_{\rm phys}
\]

produces a quantity tied to the pole definition and experimental extraction method.

\[
\beta(g)\rightarrow g(\mu)
\]

produces a scale-dependent quantity even if the underlying physical theory is scale-invariant in its observable predictions.

## 13. Source registry

1. NIST, CODATA 2022 Recommended Values of the Fundamental Physical Constants. https://physics.nist.gov/cuu/Constants/index.html
2. NIST, CODATA 2022 value tables. https://physics.nist.gov/cuu/pdf/wall_2022.pdf
3. Particle Data Group, Review of Particle Physics 2024, Phys. Rev. D 110, 030001 (2024). https://pdg.lbl.gov/2024/
4. Particle Data Group, 2024 physical constants and summary tables. https://pdg.lbl.gov/2024/download/db2024.pdf
5. Particle Data Group, 2024 Higgs-boson listing. https://pdg.lbl.gov/2024/listings/rpp2024-list-higgs-boson.pdf
6. Particle Data Group, 2024 electroweak review. https://pdg.lbl.gov/2024/reviews/rpp2024-rev-standard-model.pdf

## 14. Numerical registry status

This addendum establishes the numerical-layer schema and a provenance-controlled baseline registry. It is not a claim that every experimentally relevant QFT number has been entered. Numerical expansion should proceed by structural node coverage: each quantitative node in the relationship map should acquire a corresponding numerical record only when a value, bound, fit, or derived quantity can be assigned with complete contextual metadata.
