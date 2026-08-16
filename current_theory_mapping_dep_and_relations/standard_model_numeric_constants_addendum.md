# STANDARD MODEL — NUMERIC CONSTANTS AND MEASURED-PARAMETER ADDENDUM

## 1. Purpose and scope

This document is the numerical companion to `standard_model_dependency_map.md`.

The Standard Model dependency map is intentionally structural and symbolic. This addendum supplies numerical instantiations of quantities that appear in, or are derived from, that structure. Numerical values are kept separate from the dependency graph so that experimental updates do not alter the symbolic definitions or dependency relations.

This addendum is restricted to the minimal renormalizable Standard Model described by the dependency map:

\[
SU(3)_C\times SU(2)_L\times U(1)_Y,
\]

with three fermion generations, one Higgs doublet, and no right-handed neutrinos. Consequently, neutrino masses and PMNS parameters are not included as Standard Model parameters here; they belong to an extension of the minimal model.

The numerical registry distinguishes exact defining constants, measured quantities, inferred parameters, derived quantities, scheme-dependent parameters, scale-dependent parameters, and model-dependent quantities.

The current Particle Data Group reference edition is the 2026 Review of Particle Physics. The 2026 edition includes revised QCD, electroweak, Higgs, CKM, W-mass, quark-mass, and top-quark reviews. [1]

## 2. Numeric-record schema

| Field | Meaning |
|---|---|
| Numeric ID | Stable identifier for the numerical record. |
| Quantity | Human-readable quantity name. |
| Symbol | Mathematical symbol. |
| Value | Central value, exact value, interval, or bound. |
| Uncertainty / limit | Experimental or inferred uncertainty, confidence limit, or other qualification. |
| Units | Units of the reported quantity. |
| Numeric status | Exact, measured, inferred, derived, bound, scheme-dependent, scale-dependent, model-dependent, or approximate. |
| Scale | Renormalization or physical scale when relevant. |
| Scheme / convention | Renormalization, mass, coupling, or parameter convention when relevant. |
| Context | Definition and applicability of the value. |
| Structural linkage | Standard Model map node or module to which the quantity corresponds. |
| Source / vintage | Authoritative source and edition/year. |

## 3. Numeric status taxonomy

- **Exact:** fixed by definition rather than measurement.
- **Measured:** experimentally determined quantity with an associated uncertainty.
- **Inferred:** extracted through a global fit or model-dependent interpretation of observations.
- **Derived:** calculated from other registered values using an explicitly stated relation.
- **Bound:** an upper, lower, or interval constraint rather than a central value.
- **Scheme-dependent:** depends on a renormalization or parameter-definition convention.
- **Scale-dependent:** depends on a declared energy or momentum scale.
- **Model-dependent:** depends materially on a specified theoretical or phenomenological model.
- **Approximate:** numerical approximation to an exact or more general expression.

## 4. Exact physical constants used by the Standard Model

The following SI values are exact by definition where the SI fixes them exactly. They are not free Standard Model parameters.

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0001 | Speed of light in vacuum | \(c\) | 299 792 458 | exact | m s\(^{-1}\) | Exact | N1.1–N1.3 spacetime layer | NIST/CODATA 2022 [2] |
| NUM-SM-0002 | Planck constant | \(h\) | 6.62607015 × 10\(^{-34}\) | exact | J s | Exact | quantum normalization | NIST/CODATA 2022 [2] |
| NUM-SM-0003 | Reduced Planck constant | \(\hbar\) | 1.054571817… × 10\(^{-34}\) | exact in SI definition | J s | Exact/derived | quantization layer | NIST/CODATA 2022 [2] |
| NUM-SM-0004 | Elementary charge | \(e\) | 1.602176634 × 10\(^{-19}\) | exact | C | Exact | electromagnetic coupling normalization | NIST/CODATA 2022 [2] |

These constants define units and normalization conventions; they are not, by themselves, the free dynamical parameters of the Standard Model.

## 5. Minimal Standard Model parameter count

For the minimal three-generation, renormalizable Standard Model with massless neutrinos, a conventional physical parameterization contains 19 independent parameters:

\[
3\ \text{gauge couplings}
+2\ \text{Higgs-sector parameters}
+9\ \text{charged-fermion Yukawa eigenvalues}
+4\ \text{CKM parameters}
+1\ \theta_{\rm QCD}
=19.
\]

The equivalent choice of numerical coordinates is convention-dependent. The structural map defines the underlying nodes; this addendum records commonly used physical or renormalized parameterizations of them.

## 6. Electroweak input quantities and Higgs vacuum scale

### 6.1 Fermi constant and electroweak vacuum expectation value

The Fermi constant is measured from muon decay. In the tree-level Standard Model relation,

\[
G_F=\frac{1}{\sqrt2\,v^2},
\]

so

\[
v=(\sqrt2 G_F)^{-1/2}.
\]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source / context |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0005 | Fermi constant | \(G_F\) | 1.1663787… × 10\(^{-5}\) | experimental uncertainty at the few ×10\(^{-12}\) relative level | GeV\(^{-2}\) | Measured | electroweak/Yukawa sectors | PDG electroweak inputs; value conventionally quoted near 1.1663787 × 10\(^{-5}\) GeV\(^{-2}\) [3] |
| NUM-SM-0006 | Higgs vacuum expectation value | \(v\) | ≈ 246.2197 | derived from \(G_F\) | GeV | Derived | Higgs sector; EWSB; N3–N4 | from NUM-SM-0005 |

The value of \(v\) is not an independently fitted fifth electroweak coupling; it is a derived parameter once the Fermi constant convention and radiative-correction treatment are specified.

### 6.2 Z-boson mass

The 2024/2025 PDG electroweak treatment quotes

\[
M_Z=91.1876\pm0.0021\ \mathrm{GeV}
\]

for the conventional LEP lineshape definition. The 2026 PDG edition retains dedicated Z-boson and electroweak reviews; the exact numerical definition must always be retained with the mass convention. [4,5]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source / vintage |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0007 | Z-boson mass | \(M_Z\) | 91.1876 | ±0.0021 | GeV | Measured | electroweak breaking; N4 mass eigenstates | PDG 2024/2025 electroweak review [4] |

## 7. W boson and W width — current 2026 update

The 2026 PDG W-boson review quotes the May 2026 LHC–Tevatron working-group combination as the current world average:

\[
M_W=80.3625\pm0.0077\ \mathrm{GeV},
\]

with the combination excluding the 2022 CDF result from the world average because the full combination is highly inconsistent. The same review quotes

\[
\Gamma_W=2.14\pm0.05\ \mathrm{GeV}.
\]

The distinction between the direct measured world average and the indirect Standard Model electroweak-fit prediction is retained explicitly: the same 2026 review quotes an SM-fit prediction of \(M_W=80.357\pm0.006\) GeV when the measured \(M_W\) and \(\Gamma_W\) inputs are excluded. [6]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Context | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|---|
| NUM-SM-0008 | W-boson mass | \(M_W\) | 80.3625 | ±0.0077 | GeV | Measured/world average | May 2026 combination; Breit–Wigner mass definition | electroweak breaking; N4 | PDG 2026 [6] |
| NUM-SM-0009 | W-boson total width | \(\Gamma_W\) | 2.14 | ±0.05 | GeV | Measured/world average | error scaled for combination tension | unstable-particle/observable layer | PDG 2026 [6] |
| NUM-SM-0010 | SM electroweak-fit W mass | \(M_W^{\rm SM,fit}\) | 80.357 | ±0.006 | GeV | Inferred/derived | fit excludes direct \(M_W,\Gamma_W\) input | electroweak precision loop structure | PDG 2026 [6] |

## 8. Higgs boson

The PDG 2025 listing quotes the combined Higgs mass value

\[
m_H=125.20\pm0.11\ \mathrm{GeV}.
\]

The 2026 PDG edition contains a substantially revised Higgs review, incorporating additional measurements and constraints. The historical numerical baseline below therefore preserves the 2025 PDG value explicitly rather than silently replacing it with an unverified number. [1,7]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source / vintage |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0011 | Higgs-boson mass | \(m_H\) | 125.20 | ±0.11 | GeV | Measured | Higgs potential; EWSB; physical scalar | PDG 2025 [7] |
| NUM-SM-0012 | Higgs VEV | \(v\) | ≈246.2197 | derived | GeV | Derived | EWSB and fermion/gauge mass generation | from \(G_F\) |
| NUM-SM-0013 | Tree-level Higgs quartic | \(\lambda\) | ≈0.129 | derived/approximate | dimensionless | Derived/Approximate | N3 Higgs potential | \(\lambda\approx m_H^2/(2v^2)\), tree-level relation |

The numerical value of the renormalized Higgs quartic is scale- and scheme-dependent beyond tree level. The entry above is therefore a tree-level derived quantity, not a scheme-independent invariant coupling.

## 9. Gauge couplings

The structural map defines three independent gauge couplings \(g_s,g_2,g_1\). Their numerical values are not invariant without specifying the normalization and renormalization convention.

A common electroweak parameterization uses an electromagnetic coupling and a weak mixing angle. In an \(\overline{\mathrm{MS}}\) convention near the Z pole, PDG electroweak fits quote approximately

\[
\sin^2\hat\theta_W(M_Z)\approx0.23129,
\]

while the strong coupling is commonly quoted as

\[
\alpha_s(M_Z)=0.1180\pm0.0009
\]

in the PDG convention. [4,8]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Scale / scheme | Status | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0014 | Strong coupling | \(\alpha_s(M_Z)\) | 0.1180 | ±0.0009 | \(\mu=M_Z\), conventional \(\overline{\mathrm{MS}}\) usage | Scale-dependent | QCD gauge coupling; N2, RG module | PDG 2024/2025 [8] |
| NUM-SM-0015 | Weak mixing angle | \(\sin^2\hat\theta_W(M_Z)\) | 0.23129 | ±0.00004 | \(\overline{\mathrm{MS}}\), Z-pole | Scheme-dependent | electroweak mixing N4 | PDG 2024/2025 [4] |
| NUM-SM-0016 | Fine-structure constant at low energy | \(\alpha^{-1}(0)\) | 137.035999177 | ±0.000000021 | Thomson-limit definition | Measured | electromagnetic sector | NIST/CODATA 2022 [2] |

The addendum deliberately does not treat \(g_1,g_2,g_3\) as universal fixed numbers. They run with scale and depend on normalization/scheme conventions. They may be reconstructed from a specified set of renormalized inputs.

## 10. Fermion masses and Yukawa eigenvalues

In the minimal SM, charged-fermion masses arise from Yukawa couplings after electroweak symmetry breaking:

\[
m_f=\frac{y_f v}{\sqrt2}
\]

at tree level in the diagonal mass basis. Therefore

\[
y_f=\frac{\sqrt2\,m_f}{v}
\]

is a derived tree-level relation, while the running Yukawa coupling is scale- and scheme-dependent.

### 10.1 Charged leptons

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0017 | Electron mass | \(m_e\) | 0.51099895 | ≈0.00000000015 | MeV | Measured/recommended | charged-lepton Yukawa; N5–N6 | PDG 2024/2025 [9] |
| NUM-SM-0018 | Muon mass | \(m_\mu\) | 105.6583755 | ±0.0000023 | MeV | Measured/recommended | charged-lepton Yukawa; N5–N6 | PDG 2024/2025 [9] |
| NUM-SM-0019 | Tau mass | \(m_\tau\) | 1776.93 | ±0.09 | MeV | Measured/recommended | charged-lepton Yukawa; N5–N6 | PDG 2024/2025 [9] |

### 10.2 Quark masses

Quark masses must not be represented as one undifferentiated list. Light-quark values are conventionally quoted as \(\overline{\mathrm{MS}}\) running masses at \(\mu=2\) GeV, while heavy-quark values use different standard conventions. The top-quark mass has an additional distinction between direct/Monte-Carlo determinations and field-theoretic mass schemes. [10,11]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Scale / scheme | Status | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0020 | Up-quark mass | \(m_u\) | 2.16 | ±0.07 | MeV, \(\overline{\mathrm{MS}}\), \(\mu=2\) GeV | Measured/inferred | up-type Yukawa matrix | PDG 2024 [10] |
| NUM-SM-0021 | Down-quark mass | \(m_d\) | 4.70 | ±0.07 | MeV, \(\overline{\mathrm{MS}}\), \(\mu=2\) GeV | Measured/inferred | down-type Yukawa matrix | PDG 2024 [10] |
| NUM-SM-0022 | Strange-quark mass | \(m_s\) | 93.5 | ±0.8 | MeV, \(\overline{\mathrm{MS}}\), \(\mu=2\) GeV | Measured/inferred | down-type Yukawa matrix | PDG 2024 [10] |
| NUM-SM-0023 | Charm-quark mass | \(m_c(m_c)\) | 1.2730 | ±0.0046 | GeV, \(\overline{\mathrm{MS}}\) at \(\mu=m_c\) | Measured/inferred | up-type Yukawa matrix | PDG 2024 [10] |
| NUM-SM-0024 | Bottom-quark mass | \(m_b(m_b)\) | 4.183 | ±0.007 | GeV, \(\overline{\mathrm{MS}}\) at \(\mu=m_b\) | Measured/inferred | down-type Yukawa matrix | PDG 2024 [10] |
| NUM-SM-0025 | Top-quark mass | \(m_t^{\rm direct}\) | 172.52 | ±0.33 | GeV; direct collider determination | Measured | top Yukawa; N5–N6 | PDG 2026 review [11] |
| NUM-SM-0026 | Top-quark \(\overline{\mathrm{MS}}\) mass | \(m_t^{\overline{\mathrm{MS}}}(m_t)\) | 162.69 | ≈0.006 in the quoted perturbative conversion | GeV, \(\overline{\mathrm{MS}}\) | Derived / scheme-dependent | top Yukawa; RG module | PDG 2026 illustrative conversion [11] |

The PDG 2026 top-quark review explicitly emphasizes that the direct collider mass is not itself a scheme-independent Lagrangian mass parameter and quotes the conversion \(m_t^{\rm pole}\approx172.5\) GeV \(\rightarrow m_t^{\overline{\mathrm{MS}}}(m_t)=162.69\) GeV using the stated perturbative relation. [11]

## 11. Derived Yukawa eigenvalues

Using the tree-level relation

\[
y_f=\sqrt2\,m_f/v,
\]

and \(v\approx246.2197\) GeV gives the following approximate physical-basis Yukawa scales. These are derived tree-level numbers, not renormalized \(\overline{\mathrm{MS}}\) couplings.

| Numeric ID | Fermion | Symbol | Approx. derived Yukawa | Status | Context |
|---|---|---|---:|---|---|
| NUM-SM-0027 | Electron | \(y_e\) | 2.94 × 10\(^{-6}\) | Derived/Approximate | tree-level pole-mass relation |
| NUM-SM-0028 | Muon | \(y_\mu\) | 6.07 × 10\(^{-4}\) | Derived/Approximate | tree-level pole-mass relation |
| NUM-SM-0029 | Tau | \(y_\tau\) | 1.02 × 10\(^{-2}\) | Derived/Approximate | tree-level pole-mass relation |
| NUM-SM-0030 | Up | \(y_u\) | 1.24 × 10\(^{-5}\) | Derived/Approximate | mass convention must be retained |
| NUM-SM-0031 | Down | \(y_d\) | 2.70 × 10\(^{-5}\) | Derived/Approximate | mass convention must be retained |
| NUM-SM-0032 | Strange | \(y_s\) | 5.37 × 10\(^{-4}\) | Derived/Approximate | mass convention must be retained |
| NUM-SM-0033 | Charm | \(y_c\) | 7.31 × 10\(^{-3}\) | Derived/Approximate | mass convention must be retained |
| NUM-SM-0034 | Bottom | \(y_b\) | 2.40 × 10\(^{-2}\) | Derived/Approximate | mass convention must be retained |
| NUM-SM-0035 | Top | \(y_t\) | ≈0.99 | Derived/Approximate | direct-mass scale; true running Yukawa is scheme/scale dependent |

The approximate top Yukawa value is therefore close to unity, consistent with the 2026 PDG top review's characterization of the top mass as \(m_t\sim v/\sqrt2\). [11]

## 12. CKM quark-mixing parameters

The quark Yukawa matrices are not themselves directly observable. Their mismatch under the separate diagonalizations of the up- and down-type mass matrices generates the CKM matrix.

A standard Wolfenstein parameterization uses four independent physical parameters. The following values are retained from the PDG-era global-fit parameterization used in the Standard Model literature; the 2026 PDG edition contains a revised CKM review and should be treated as the current source for subsequent registry updates. [1,12]

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Status | Structural linkage | Source / vintage |
|---|---|---|---:|---|---|---|---|
| NUM-SM-0036 | Wolfenstein parameter | \(\lambda\) | 0.22453 | ±0.00044 | Inferred/global fit | CKM mixing; flavor module | PDG-era global CKM fit [12] |
| NUM-SM-0037 | Wolfenstein parameter | \(A\) | 0.836 | ±0.015 | Inferred/global fit | CKM mixing | PDG-era global CKM fit [12] |
| NUM-SM-0038 | Rescaled Wolfenstein parameter | \(\bar\rho\) | 0.122 | \(^{+0.018}_{-0.017}\) | Inferred/global fit | CKM CP structure | PDG-era global CKM fit [12] |
| NUM-SM-0039 | Rescaled Wolfenstein parameter | \(\bar\eta\) | 0.355 | \(^{+0.012}_{-0.011}\) | Inferred/global fit | CKM CP violation | PDG-era global CKM fit [12] |

The addendum does not silently convert these into a unique numerical CKM matrix because the chosen parameterization and truncation must also be recorded.

## 13. QCD vacuum angle

The renormalizable Standard Model permits a strong CP parameter

\[
\mathcal L_\theta=\theta_{\rm QCD}\,\frac{g_s^2}{32\pi^2}G^A_{\mu\nu}\widetilde G^{A\mu\nu}.
\]

Its numerical value is not a precision measurement. A small value is constrained by the experimental non-observation of a neutron electric dipole moment, but the exact numerical bound depends on the hadronic matrix element used to convert the EDM limit into a bound on \(\theta_{\rm QCD}\). Therefore the registry records the parameter as a bound-class quantity rather than fabricating a central value.

| Numeric ID | Quantity | Symbol | Value | Status | Context | Structural linkage |
|---|---|---|---|---|---|---|
| NUM-SM-0040 | Strong CP angle | \(\theta_{\rm QCD}\) | \(\lvert\theta_{\rm QCD}\rvert\ll1\); numerical bound requires hadronic matrix-element convention | Bound / model-dependent | neutron EDM interpretation | QCD/topological term |

## 14. Derived electroweak relations

At tree level,

\[
M_W=\frac{gv}{2},
\qquad
M_Z=\frac{v}{2}\sqrt{g^2+g'^2},
\qquad
e=g\sin\theta_W=g'\cos\theta_W.
\]

Therefore, once a conventionally defined set \((G_F,M_Z,\alpha,\sin^2\theta_W)\) or an equivalent input scheme is chosen, the corresponding renormalized electroweak couplings can be calculated. Beyond tree level, the numerical values depend on the renormalization scheme and loop corrections.

For the same reason, the relation

\[
\sin^2\theta_W=1-\frac{M_W^2}{M_Z^2}
\]

should be labeled an on-shell scheme definition when used beyond tree-level shorthand, rather than being treated as a universally scheme-independent identity. [4]

## 15. Observable particle widths

Widths are numerical observables, but their reported values depend on the mass/width convention and resonance definition. The following registry records selected current values explicitly.

| Numeric ID | Quantity | Symbol | Value | Uncertainty | Units | Status | Structural linkage | Source |
|---|---|---|---:|---|---|---|---|---|
| NUM-SM-0041 | W-boson width | \(\Gamma_W\) | 2.14 | ±0.05 | GeV | Measured/world average | unstable gauge boson | PDG 2026 [6] |
| NUM-SM-0042 | Top-quark width, reference SM prediction | \(\Gamma_t\) | 1.326 | calculation value at \(m_t=172.5\) GeV | GeV | Derived/theory prediction | top decay and CKM sector | PDG 2026 [11] |

The top width entry is explicitly a Standard Model prediction at a stated reference point, not a direct world-average measurement.

## 16. Quantities intentionally excluded from this addendum

The following are excluded from the minimal-SM numerical registry unless a future extension of the structural map changes the scope:

- neutrino masses;
- PMNS mixing angles and phases;
- sterile-neutrino parameters;
- dark-matter masses/couplings not present in the minimal SM;
- gravitational parameters as dynamical SM parameters;
- beyond-SM Wilson coefficients;
- SMEFT coefficients;
- arbitrary detector-specific cross sections or event yields unless tied to a precisely defined SM observable record;
- hadronic matrix elements unless explicitly linked to a Standard Model observable and a declared lattice/QCD convention.

## 17. Numeric-to-structural linkage rules

1. A numeric record instantiates a symbolic quantity; it does not redefine the corresponding structural node.
2. Every running parameter must carry its scale.
3. Every scheme-dependent parameter must carry its scheme.
4. Every inferred value must carry its fit/model context.
5. Every derived value must retain its upstream numerical provenance.
6. A pole mass, running mass, Monte-Carlo mass, and short-distance mass must never be treated as interchangeable numerical labels.
7. Numerical values do not change the dependency graph's structural closure.
8. Experimental disagreement must remain visible when it materially affects the reported world average.
9. A theory prediction must not be placed in the same numeric-status class as a direct experimental measurement.
10. A dimensionless number is not automatically a universal constant; its definition, scale, scheme, or normalization may be essential.

## 18. Numerical uncertainty and covariance

For a derived quantity \(Y=f(X_1,\ldots,X_n)\), the registry should retain covariance information whenever it exists. In linear approximation,

\[
\sigma_Y^2\approx
\sum_{i,j}
\frac{\partial f}{\partial X_i}
\frac{\partial f}{\partial X_j}
\operatorname{Cov}(X_i,X_j).
\]

The registry distinguishes statistical uncertainty, systematic uncertainty, theoretical uncertainty, parameter-fit uncertainty, model uncertainty, and scale/scheme variation. These sources should not be silently combined.

## 19. Source registry

1. Particle Data Group, *Review of Particle Physics 2026*, F. Takahashi et al., current 2026 edition and online reviews/listings. [1]
2. NIST/CODATA, Recommended Values of the Fundamental Physical Constants 2022. [2]
3. Particle Data Group, electroweak-model review and Fermi-constant input documentation. [3,4]
4. Particle Data Group, *Electroweak Model and Constraints on New Physics*, 2024/2025 update; used here for the explicitly stated \(M_Z\) and \(\overline{\mathrm{MS}}\) electroweak inputs where the 2026 numerical table was not directly exposed in the retrieved text. [4]
5. Particle Data Group, 2026 Z-boson review/listing. [1]
6. Particle Data Group, *Mass and Width of the W Boson*, revised May 2026. [6]
7. Particle Data Group, Higgs-boson listing, 2025 update, \(m_H=125.20\pm0.11\) GeV; the 2026 edition contains a revised Higgs review. [7]
8. Particle Data Group, QCD/electroweak reviews, \(\alpha_s(M_Z)\) reference value. [8]
9. Particle Data Group, charged-lepton listings. [9]
10. Particle Data Group, quark-mass summary and listings. [10]
11. Particle Data Group, *Top Quark*, revised 2026; direct combination \(m_t=172.52\pm0.33\) GeV and stated pole/MS conversion. [11]
12. Particle Data Group, CKM quark-mixing review and global-fit parameterization. [12]

## 20. Registry status

This is a provenance-controlled baseline numerical companion to the Standard Model dependency map, not a claim of numerical completeness. Numerical entries are deliberately accompanied by definitions, source vintage, uncertainty status, scale/scheme context, and structural linkage. Values from older PDG vintages are retained only where the current 2026 source was not directly numerically recoverable from the available public text and are explicitly labeled as such.

The structural dependency map remains symbolic. This addendum supplies numerical instantiations without altering the underlying Standard Model graph.
