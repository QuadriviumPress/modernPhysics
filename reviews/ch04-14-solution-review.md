# Solution Correctness Review — Chapters 4–14

Review of every worked solution in the textbook from Chapter 4 (Interference of Light) through Chapter 14 (Elementary Particles and the Standard Model). Each problem was independently re-derived (formula choice, algebra, numeric substitution, units, order-of-magnitude) rather than just proofread. Confirmed errors were fixed directly in the chapter source files.

If this review is resumed in a new session: read the status table below and continue from the first chapter marked `N`.

## Status

| Ch | File | # Problems | Reviewed? | Issues found | Fixed |
|---|---|---|---|---|---|
| 4 | ch-04-interference-of-light.md | 20 | Y | 0 | 0 |
| 5 | ch-05-diffraction-of-light.md | 20 | Y | 0 | 0 |
| 6 | ch-06-particle-properties-of-waves.md | 20 | Y | 1 | 1 |
| 7 | ch-07-wave-properties-of-particles.md | 20 | Y | 0 | 0 |
| 8 | ch-08-the-schrodinger-equation.md | 20 | Y | 0 | 0 |
| 9 | ch-09-quantum-mechanics-in-three-dimensions.md | 19 | Y | 0 | 0 |
| 10 | ch-10-the-hydrogen-atom.md | 10 | Y | 0 | 0 |
| 11 | ch-11-many-electron-atoms.md | 12 | Y | 0 | 0 |
| 12 | ch-12-molecular-structure.md | 10 | Y | 0 | 0 |
| 13 | ch-13-nuclear-physics.md | 10 | Y | 1 | 1 |
| 14 | ch-14-elementary-particles-and-the-standard-model.md | 11 | Y | 0 | 0 |

## Chapter details

### Chapter 4 — Interference of Light (20/20 checked, 0 issues)

All 20 solutions independently re-derived and confirmed correct: fringe-angle geometry, small-angle fringe spacing, coherence length/coherence-fringe-count estimates, N-slit intensity scaling ($I_{\max}\propto N^2$, total flux $\propto N$), thin-film/Newton's-ring phase-reversal bookkeeping (Case A vs. Case B), Michelson interferometer fringe counting, gas-cell refractometry, Michelson–Morley fringe-shift estimate, LIGO fringe-shift estimate, and two-wavelength coincidence order. No arithmetic, formula, or cross-reference errors found.

- sol-interference-of-light-1 through sol-interference-of-light-20: Correct.

### Chapter 5 — Diffraction of Light (20/20 checked, 0 issues)

All 20 solutions independently re-derived and confirmed correct: single-slit minima/central-maximum width, sinc-squared intensity comparison to true secondary maximum, Fresnel number estimate, double-slit missing orders and fringe counting inside the envelope, grating dispersion and resolving power ($R=mN$), grating order overlap, Rayleigh-criterion resolution (eye, headlights, telescope scaling, microscope NA vs. electron wavelength), Bragg diffraction (spacing, higher orders, $\lambda\le 2d$ cutoff), slit-width/momentum-uncertainty estimate, and EHT/CD/DVD resolution examples. No arithmetic, formula, or cross-reference errors found.

- sol-diffraction-of-light-1 through sol-diffraction-of-light-20: Correct.

### Chapter 6 — Particle Properties of Waves (20/20 checked, 1 issue, 1 fixed)

All 20 solutions independently re-derived (Wien's law, Stefan–Boltzmann luminosity, photoelectric effect incl. two-point $h$/work-function determination, Duane–Hunt limit, Compton scattering incl. the symbolic derivation in Problem 11, pair production thresholds for $e^+e^-$ and $p\bar p$, PET annihilation photons, Compton edge vs. photopeak, photomultiplier gain, band-gap absorption).

- **sol-particle-properties-of-waves-1 — Fixed.** The precise Wien's-law temperature is $T=2.898\times10^{-3}/500\times10^{-9}=5796\ \text{K}$ (correctly rounded to $5.80\times10^3\ \text{K}$ in the text), but the solution then computed the difference from the example's $5778\ \text{K}$ using the *rounded* $5800\ \text{K}$, stating "$22\ \text{K}$, or $0.4\%$." The correct difference using the unrounded value is $5796-5778=18\ \text{K}$ ($0.3\%$). Corrected the text to $18\ \text{K}$, $0.3\%$.
- sol-particle-properties-of-waves-2 through -20: Correct.

### Chapter 7 — Wave Properties of Particles (20/20 checked, 0 issues)

All 20 solutions independently re-derived and confirmed correct: de Broglie wavelengths (electron/proton/baseball/neutron/$C_{60}$), Davisson–Germer spacing, accelerating-voltage-to-wavelength relation, Bohr standing-wave orbit condition, uncertainty-principle estimates (nuclear confinement, atomic linewidth, quantum dot, which-path disturbance, wavepacket spreading time), nonrelativistic and relativistic group-velocity derivations, phase-velocity/superluminality discussion, delayed-choice/quantum-eraser reasoning, and the COW gravitational phase-shift argument. No arithmetic, formula, or cross-reference errors found.

- sol-wave-properties-of-particles-1 through -20: Correct.

### Chapter 8 — The Schrödinger Equation (20/20 checked, 0 issues)

All 20 solutions independently re-derived and confirmed correct: infinite square well energies/wavefunction verification/node counting, potential-step reflection/transmission ($R+T=1$ proof), barrier tunneling (proton vs. alpha, STM current vs. gap, alpha-decay half-life sensitivity), harmonic oscillator ground-state verification, zero-point energy/spread (macroscopic vs. H$_2$), selection rules, correspondence principle, and large-$n$ classical-limit estimate. No arithmetic, formula, or cross-reference errors found.

- sol-the-schrodinger-equation-1 through -20: Correct.

### Chapter 9 — Quantum Mechanics in Three Dimensions (19/19 checked, 0 issues)

All 19 solutions independently re-derived and confirmed correct: 3D box degeneracies (cubic and anisotropic quantum dot), orbital angular momentum quantization ($L$, $m_\ell$, cone angle vs. $\ell$), angular-momentum commutation relations, isotropic 3D harmonic oscillator degeneracies and nuclear shell-model magic numbers, central-potential separation of variables and centrifugal barrier, spherical harmonics/$p_z$ shape, Zeeman-type orbital splitting count, and the Stern–Gerlach orbital-vs-spin argument. No arithmetic, formula, or cross-reference errors found.

- sol-quantum-mechanics-in-three-dimensions-1 through -19: Correct.

### Chapter 10 — The Hydrogen Atom (10/10 checked, 0 issues)

All 10 solutions independently re-derived and confirmed correct: Lyman series wavelengths, $n=3$ state counting, $\Delta\ell=\pm1$ selection rule, orbital angular momentum/magnetic moment, Stern–Gerlach silver-vs-helium reasoning, radial probability maximization, hydrogenic $Z$-scaling for Li$^{2+}$, Stern–Gerlach spot-separation kinematics, Zeeman splitting (energy/frequency/wavelength), and fine-structure scaling with $n$. No arithmetic, formula, or cross-reference errors found.

- sol-the-hydrogen-atom-1 through -10: Correct.

### Chapter 11 — Many-Electron Atoms (12/12 checked, 0 issues)

All 12 solutions independently re-derived and confirmed correct: ground-state electron configurations, Hund's rule, penetration/screening argument for $4s$ vs. $3d$, Moseley's law (single-point and two-point fits, incl. the Cu/Mo/Ag numeric chain), exclusion-principle reactivity argument, metastable-state laser argument, Slater's-rules $Z_\text{eff}$ for Mg $3s$, exchange-energy ionization-energy reversal (P vs. S), He–Ne laser photon-rate calculation, Hartree self-consistent-field explanation, and the K/Ar atomic-radius anomaly. No arithmetic, formula, or cross-reference errors found.

- sol-many-electron-atoms-1 through -12: Correct.

### Chapter 12 — Molecular Structure (10/10 checked, 0 issues)

All 10 solutions independently re-derived and confirmed correct: VSEPR hybridization/geometry (NH$_3$, CO$_2$, SF$_6$, SF$_4$), MO bond-order diagrams (N$_2$, He$_2^+$, O$_2^\pm$, F$_2$/F$_2^+$ incl. paramagnetism), HCl reduced mass and zero-point vibrational energy, CO moment of inertia and rotational transition energy, HCl rotational constant/line spacing/missing-Q-branch gap, and the halogen boiling-point/London-dispersion trend. No arithmetic, formula, or cross-reference errors found.

- sol-molecular-structure-1 through -10: Correct.

### Chapter 13 — Nuclear Physics (10/10 checked, 1 issue, 1 fixed)

All 10 solutions independently re-derived (nuclear radius $A^{1/3}$ scaling, radioactive decay kinetics, alpha/beta decay energetics, fission energy budgeting, semi-empirical mass formula, secular equilibrium, radiocarbon dating, D-T fusion momentum sharing).

- **sol-nuclear-physics-2 — Fixed.** The solution computed $\Delta m$ by directly subtracting the *atomic* mass $M(^4_2\text{He})=4.002602\ \text{u}$ (which includes two orbital electrons) from $2m_p+2m_n$ built from the *bare* proton mass, without correcting for the two electron rest masses. This understates the binding energy by $2m_ec^2\approx1.02\ \text{MeV}$, giving $27.28\ \text{MeV}$ ($6.82\ \text{MeV/nucleon}$) instead of the correct $28.30\ \text{MeV}$ ($7.07\ \text{MeV/nucleon}$) — the latter matches the well-known accepted value for $^4\text{He}$. Corrected the text to remove $2m_e$ from the atomic mass before differencing.
- sol-nuclear-physics-1, 3–10: Correct.

### Chapter 14 — Elementary Particles and the Standard Model (11/11 checked, 0 issues)

All 11 solutions independently re-derived and confirmed correct: fermion/boson classification, quark-model charge assignments ($\Lambda^0$, proton, neutron, $K^-$/$K^+$), conservation-law checks (charge, baryon number, lepton number incl. separate $L_e$/$L_\mu$, strangeness) across several reactions, quark confinement explanation, $K^-p\to\Lambda^0\pi^0$ strong-interaction check, a two-vertex muon-decay Feynman diagram with per-vertex conservation, relativistic muon decay-length kinematics, and the electron-pair gravity/electromagnetism force-ratio calculation. No arithmetic, formula, or cross-reference errors found.

- sol-elementary-particles-and-the-standard-model-1 through -11: Correct.

## Summary

Reviewed all 172 problem/solution pairs across chapters 4–14. Found and fixed **2 issues**, both in Chapter 6 and Chapter 13:

1. **Ch. 6, Problem 1** (Wien's law): a rounding-order slip made the stated temperature difference from the Sun's example value off by 4 K (22 K/0.4% stated vs. correct 18 K/0.3%). Fixed.
2. **Ch. 13, Problem 2** (He-4 binding energy): the calculation mixed an atomic mass (includes 2 electrons) with the bare nuclear proton mass without correcting for the 2 electron rest masses, understating the binding energy by about 1 MeV (27.28 MeV / 6.82 MeV per nucleon, instead of the correct 28.30 MeV / 7.07 MeV per nucleon — the well-known accepted value). Fixed.

All other 170 solutions (chapters 4, 5, 7, 8, 9, 10, 11, 12, 14 in full, and the other 19 problems each in chapters 6 and 13) were independently re-derived from scratch and confirmed correct — no other arithmetic, formula, unit, or cross-reference errors were found.
