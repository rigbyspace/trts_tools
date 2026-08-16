# GR NUMERIC CONSTANTS AND MEASURED-PARAMETER ADDENDUM

## 1. Purpose and scope

This addendum is the numerical companion to `gr_relationship_mapping.md`.

The GR relationship map is intentionally structural and symbolic. It defines and relates mathematical objects, operators, equations, constraints, formulations, and dependency paths. It does not attempt to embed measured numerical values into those structures.

This addendum records numerical instantiations that are relevant to the GR map while preserving the distinction between:

1. exact defining constants;
2. experimentally recommended constants with uncertainty;
3. model-dependent inferred cosmological parameters;
4. derived quantities calculated from other entries;
5. bounds and limits;
6. formulation-, convention-, or model-dependent quantities.

A numerical entry is therefore not itself evidence that the corresponding symbolic relationship is empirically established. The numerical registry and the structural graph are separate layers linked by stable identifiers.

## 2. Numeric-node schema

Each numeric record uses the following fields.

| Field | Meaning |
|---|---|
| Numeric ID | Stable identifier for the numerical record. |
| Quantity | Human-readable name. |
| Symbol | Mathematical symbol. |
| Value | Central numerical value, exact value, interval, or limit. |
| Uncertainty / limit | Standard uncertainty, confidence statement, or bound when applicable. |
| Units | Unit system and units used for the reported value. |
| Numeric status | Exact, measured, inferred, derived, bound, scheme-dependent, scale-dependent, model-dependent, or approximate. |
| Definition / context | What the number represents and under what assumptions it is meaningful. |
| Source | Primary data source or authoritative compilation. |
| Reference vintage | Adjustment, release, or data year. |
| Map linkage | Related structural-map node(s), or `external parameter` when no explicit node exists in the current map. |
| Notes | Qualification necessary to avoid conflating the numerical entry with a universal structural statement. |

## 3. Numeric status taxonomy

- **Exact:** fixed by definition or an exact defining relation within the stated unit system.
- **Measured:** experimentally determined with an uncertainty.
- **Inferred:** obtained from observations through a stated theoretical/model framework.
- **Derived:** calculated from other registered quantities.
- **Bound:** an upper, lower, or interval constraint rather than a central measurement.
- **Scheme-dependent:** numerical value depends on renormalization or related convention.
- **Scale-dependent:** numerical value depends on a declared scale.
- **Model-dependent:** numerical inference depends materially on a specified physical model.
- **Approximate:** numerical value is an approximation to a more general quantity or relation.

## 4. Baseline fundamental and gravitational constants

The numerical values in this section use the 2022 CODATA recommended values, the latest CODATA set currently available from NIST as of this addendum. NIST notes that the next regularly scheduled CODATA adjustment is 2026. The tables below therefore preserve the source vintage explicitly rather than treating the values as timeless constants-data. citeturn936054search0turn936054search2

| Numeric ID | Quantity | Symbol | Value | Uncertainty / limit | Units | Numeric status | Definition / context | Source / vintage | Map linkage |
|---|---|---|---:|---|---|---|---|---|---|
| NUM-GR-0001 | Speed of light in vacuum | \(c\) | 299 792 458 | exact | m s\(^{-1}\) | Exact | SI defining constant | NIST/CODATA 2022 | External parameter; relevant to N25 and spacetime units |
| NUM-GR-0002 | Newtonian gravitational constant | \(G\) | 6.67430 × 10\(^{-11}\) | 0.00015 × 10\(^{-11}\) m\(^3\) kg\(^{-1}\) s\(^{-2}\) | m\(^3\) kg\(^{-1}\) s\(^{-2}\) | Measured/recommended | Gravitational coupling measured through experiments | NIST/CODATA 2022 | External parameter; determines N25 under SI conventions |
| NUM-GR-0003 | Planck constant | \(h\) | 6.62607015 × 10\(^{-34}\) | exact | J Hz\(^{-1}\) | Exact | SI defining constant | NIST/CODATA 2022 | External parameter |
| NUM-GR-0004 | Reduced Planck constant | \(\hbar\) | 1.054571817… × 10\(^{-34}\) | exact in SI-defining terms | J s | Exact/derived | \(h/(2\pi)\) | NIST/CODATA 2022 | External parameter |
| NUM-GR-0005 | Elementary charge | \(e\) | 1.602176634 × 10\(^{-19}\) | exact | C | Exact | SI defining constant | NIST/CODATA 2022 | External parameter |
| NUM-GR-0006 | Planck length | \(\ell_P\) | 1.616255 × 10\(^{-35}\) | 0.000018 × 10\(^{-35}\) m | m | Derived | \((\hbar G/c^3)^{1/2}\) | NIST/CODATA 2022 | External parameter; related to geometric scale in N1–N4 |
| NUM-GR-0007 | Planck time | \(t_P\) | 5.391247 × 10\(^{-44}\) | 0.000060 × 10\(^{-44}\) s | s | Derived | \(\ell_P/c\) | NIST/CODATA 2022 | External parameter |
| NUM-GR-0008 | Planck mass | \(m_P\) | 2.176434 × 10\(^{-8}\) | 0.000024 × 10\(^{-8}\) kg | kg | Derived | \((\hbar c/G)^{1/2}\) | NIST/CODATA 2022 | External parameter |

NIST's 2022 tables report the exact value of \(c\), \(h\), and \(e\), and report \(G=6.67430(15)\times10^{-11}\) m\(^3\) kg\(^{-1}\) s\(^{-2}\); the same tables provide the corresponding Planck scales. citeturn936054search36turn936054search37

## 5. Einstein coupling and derived numerical forms

The structural GR map defines

\[
\kappa = \frac{8\pi G}{c^4}.
\]

The numerical addendum treats \(\kappa\) as a derived parameter rather than an independent measured constant.

| Numeric ID | Quantity | Symbol | Value | Units | Numeric status | Derivation | Map linkage |
|---|---|---|---:|---|---|---|---|
| NUM-GR-0009 | Einstein gravitational coupling | \(\kappa\) | 2.0766… × 10\(^{-43}\) | m J\(^{-1}\) | Derived | \(8\pi G/c^4\) using NUM-GR-0001 and NUM-GR-0002 | N25 |

The numerical value above is intentionally not promoted to an independently measured quantity: N25 is defined structurally in the GR map by the relation between \(G\), \(c\), and \(\kappa\). fileciteturn1file0L213-L220

## 6. Cosmological parameters: explicitly model-dependent numerical layer

Cosmological parameters must not be placed in the same epistemic class as defining constants. They are inferred from observations through a specified cosmological model and data combination.

For example, the Planck 2018 base-\(\Lambda\)CDM analysis reports \(H_0=(67.4\pm0.5)\) km s\(^{-1}\) Mpc\(^{-1}\), \(\Omega_m=0.315\pm0.007\), and \(\sigma_8=0.811\pm0.006\). These are model-dependent inferred parameters, not universal constants of the structural GR equations. citeturn241844search0

| Numeric ID | Quantity | Symbol | Value | Uncertainty / limit | Units | Numeric status | Model / context | Source / vintage | Map linkage |
|---|---|---|---:|---|---|---|---|---|---|
| NUM-GR-0010 | Hubble constant | \(H_0\) | 67.4 | ±0.5 | km s\(^{-1}\) Mpc\(^{-1}\) | Inferred / model-dependent | Planck base-\(\Lambda\)CDM | Planck 2018 | External parameter; relevant to cosmological applications of N2, N17, N19 |
| NUM-GR-0011 | Matter density parameter | \(\Omega_m\) | 0.315 | ±0.007 | dimensionless | Inferred / model-dependent | Planck base-\(\Lambda\)CDM | Planck 2018 | External parameter |
| NUM-GR-0012 | Matter fluctuation amplitude | \(\sigma_8\) | 0.811 | ±0.006 | dimensionless | Inferred / model-dependent | Planck base-\(\Lambda\)CDM | Planck 2018 | External parameter |
| NUM-GR-0013 | Spatial curvature parameter | \(\Omega_K\) | 0.0007 | ±0.0019 | dimensionless | Inferred / model-dependent | Planck 2018, combined data context | Planck 2018 | External parameter; relevant to metric/cosmological solutions |
| NUM-GR-0014 | Effective number of relativistic degrees of freedom | \(N_{\rm eff}\) | 2.99 | ±0.17 | dimensionless | Inferred / model-dependent | Planck + BAO | Planck 2018 | External parameter; matter/radiation sector |
| NUM-GR-0015 | Sum of neutrino masses | \(\sum m_\nu\) | < 0.12 | 95% upper limit | eV | Bound / model-dependent | Planck + BAO | Planck 2018 | External parameter; matter sector |

These entries intentionally preserve their observational/model context. A value such as \(H_0\) must not be represented in the structural graph as though GR itself determines a unique numerical value for it.

## 7. Numeric values that should remain external to the structural graph

The following classes are explicitly maintained as addendum-only information unless the structural map is later expanded to include the associated observational or model-specific nodes:

- cosmological best-fit parameters;
- observationally inferred dark-energy parameters;
- measured astrophysical masses or distances;
- laboratory values of matter-sector parameters;
- dataset-specific confidence intervals;
- numerical solutions of particular GR spacetimes;
- simulation-dependent or coordinate-dependent numerical quantities.

This separation prevents an inferred parameter from being mistaken for a mathematical consequence of an equation.

## 8. Numeric-to-structural linkage rules

1. A numeric record may point to a structural node without changing that node's mathematical definition.
2. A derived numeric quantity inherits the units, uncertainty, assumptions, and epistemic qualifications of its inputs.
3. A model-dependent numerical value must retain its model label.
4. A value with competing measurements must not be collapsed to a single unlabeled scalar.
5. Exact constants may be used in derived numerical calculations without introducing an empirical uncertainty.
6. Numerical values do not alter structural closure. The structural map remains closed or open according to its symbolic node/edge rules, not according to whether numerical data exist.

## 9. Recommended extension fields for future records

For future numerical records, the following fields should be added when applicable:

- confidence level;
- covariance/correlation reference;
- dataset identifier;
- instrument/experiment;
- calibration status;
- coordinate or gauge convention;
- unit-system convention;
- cosmological-model identifier;
- numerical method;
- reproducibility reference;
- date of last verification.

## 10. Source registry

1. NIST, CODATA 2022 Recommended Values of the Fundamental Physical Constants. https://physics.nist.gov/cuu/Constants/index.html
2. NIST, CODATA 2022 recommended-value tables. https://physics.nist.gov/cuu/pdf/wall_2022.pdf
3. Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astronomy & Astrophysics 641, A6 (2020), DOI: 10.1051/0004-6361/201833910.

## 11. Numerical registry status

This addendum is a controlled baseline registry, not an assertion of numerical completeness. Its purpose is to establish the schema, provenance discipline, structural cross-linking, and epistemic separation required for a complete numerical companion to the GR relationship map.
