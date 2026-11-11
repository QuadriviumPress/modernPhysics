# Simulation audit and implementation record

Updated 2026-11-11 after the approved additions. The initial review covered all
14 chapters and 54 embeds. The book now contains **76 embeds: 24 PhET HTML5,
45 OpenLyceum and 7 PhET Java/CheerpJ**.

## Approved scope

Added 22 focused simulation activities in chapters 4, 5, 6, 9, 11, 12 and 14.
Replaced the chapter 10 MRI embed with the forthcoming OpenLyceum Simplified
MRI, explicitly marked in progress. Existing figure labels and cross-references
were preserved. Quantum Scattering, discharge-lamp replacement and radioactive
dating replacement were not implemented, following the user's decisions.

## Implemented additions

All new activities include a prediction or observation prompt, an accessible
image description, and a screen-specific local PNG for PDF, Word and print.
The manifest and capture script record the source and screen selection.

| Chapter | Simulation | Screens | Activity |
| --- | --- | --- | --- |
| 4 | Diffraction Lab | 1 | N-slit phasors, maxima and zeros |
| 4 | Interferometry Lab | 2 | Complementary output ports, single photons and which-path information |
| 5 | Diffraction Lab | 1, 2, 3, 4 in four focused embeds | Gratings, spectral resolution, circular aperture and holography |
| 6 | Photon Interactions | 2; 1; 3–4 | X-ray tube, Compton scattering, pair production and annihilation |
| 9 | Quantum Atom 3D | 1, 3, 5 in three focused embeds | Spherical harmonics, angular momentum, oscillator degeneracy |
| 11 | Photon Interactions | 2 | Characteristic X-rays and Moseley plot |
| 11 | Interferometry Lab | 3 | Passive cavity resonance; gain remains in the separate Lasers simulation |
| 12 | Quantum Atom 3D | 2 | Hybrid-orbital superposition with an explicit hydrogenic-model limitation |
| 12 | Spectroscopy Lab | 3; 1 | Conjugated-molecule electronic absorption; HCl rovibrational structure |
| 12 | Quantum Potential | 2 | Harmonic and Morse level spacing; explicitly an electron-mass model, not a molecular-frequency prediction |
| 14 | Particle Zoo | 4; 1–2; 3 | Reaction vertices and conservation, hadrons and Eightfold Way, confinement |
| 14 | Collider Lab | 1–3 | Detector reconstruction, real CMS dimuon mass spectrum, collision energy |

## Legacy decisions and remaining gaps

| Topic | Decision |
| --- | --- |
| Simplified MRI | Include OpenLyceum's version ahead of completion. Chapter 10 labels it in progress, uses a local generic placeholder and links to the original PhET MRI. The new launch is not claimed to be complete or operational. Preserve `fig:ch10-mri-sim`. |
| Quantum tunneling | Retain PhET's Java Quantum Tunneling and Wave Packets. Do not introduce Quantum Scattering. |
| Discharge lamps | Retain PhET's Java model; defer Light and Atoms replacement. |
| Radioactive dating | Retain PhET's Java dating game and its carbon-14 worked-example references. Counting statistics and alpha decay do not replace dating. |
| Photoelectric effect | Retain Java; no equivalent public model found in the searched catalogs. |
| Davisson–Germer | Retain Java; optical diffraction and slit interference do not replace electron scattering from a crystal. |
| Lasers | Retain Java for pumping, population inversion and threshold. The added passive Fabry–Pérot cavity supplies only cavity resonance. |
| Nuclear fission | Retain Java; composition, stability and decay models do not replace chain reactions and reactor control. |

Alpha Decay, Beta Decay, Quantum Wave Interference, Quantum Bound States,
Particle in a Box, Bound State Superposition, Double Wells and Covalent Bonds,
and Band Structure were already embedded as HTML5 and needed no Java migration.

The MRI preview is the only intentional unfinished deployment. The remaining
models are public simulations. The source ledger in `SOURCES.md` was updated,
including its previously omitted Relativistic Dynamics activities in chapter 3.

## Source and capture references

- [PhET HTML5 catalog](https://phet.colorado.edu/en/simulations/filter?type=html)
- [PhET Java catalog](https://phet.colorado.edu/en/simulations/filter?sort=alpha&type=java)
- [OpenLyceum public catalog](https://www.openlyceum.com/)
- [OpenLyceum screen catalog](https://github.com/OpenLyceum/Baton/blob/main/structure/repos.json)
- [Capture manifest](images/simulations/manifest.json)
- [Capture script and usage](scripts/capture-simulation-fallbacks.mjs)

Feature comparisons were checked against the simulations' README/model
documentation and screen definitions. Local captures retain OpenLyceum credit
and AGPL-3.0 licensing as recorded in `SOURCES.md`. Refreshing screenshots from
a live deployment can change the images, so inspect them after regeneration.
Direct launch requests to PhET returned 403 in the research environment even
for known HTML5 titles; this was not interpreted as proof that a title is absent.

## Validation

- `npm run check`: project validation, 30 JavaScript tests, 5 Python tests and the strict HTML/link build.
- `npm run test:exports`: student/full PDF and Word export smoke tests passed.
- Chromium loaded all 20 selected screen combinations without JavaScript exceptions; five teaching presets were selected through keyboard controls before capture.
- The rendered diffraction, MRI and particle-physics pages were checked for their selected-screen iframe URLs, MRI progress notice and visible local print fallbacks.
- All previous figure labels were retained. The seven retained Java embeds and chapters 1, 2, 3, 7, 8 and 13 were verified unchanged.

## Current embed inventory

Line numbers refer to the source after this implementation.

| Chapter | Source line | Provider | Simulation | Selected screens | Figure label |
| --- | --- | --- | --- | --- | --- |
| 1 | [75](chapters/ch-01-the-need-for-relativity.md#L75) | `phet` | `waves-intro` | All / default | `fig:ch01-waves-sim` |
| 1 | [149](chapters/ch-01-the-need-for-relativity.md#L149) | `openlyceum` | `InterferometryLab` | All / default | `fig:ch01-interferometry-sim` |
| 2 | [111](chapters/ch-02-special-relativity.md#L111) | `openlyceum` | `SpecialRelativity` | 1 | `fig:ch02-light-clock-sim` |
| 2 | [301](chapters/ch-02-special-relativity.md#L301) | `openlyceum` | `DopplerEffect` | All / default | `fig:ch02-classical-doppler-sim` |
| 2 | [373](chapters/ch-02-special-relativity.md#L373) | `openlyceum` | `SpecialRelativity` | All / default | `fig:ch02-sr-sim` |
| 3 | [202](chapters/ch-03-relativistic-dynamics.md#L202) | `openlyceum` | `RelativisticDynamics` | 2 | `fig:ch03-energy-momentum-sim` |
| 3 | [239](chapters/ch-03-relativistic-dynamics.md#L239) | `phet` | `collision-lab` | All / default | `fig:ch03-collision-sim` |
| 3 | [247](chapters/ch-03-relativistic-dynamics.md#L247) | `openlyceum` | `RelativisticDynamics` | 3 | `fig:ch03-relativistic-collision-sim` |
| 3 | [291](chapters/ch-03-relativistic-dynamics.md#L291) | `openlyceum` | `RelativisticDynamics` | 4 | `fig:ch03-thresholds-sim` |
| 3 | [313](chapters/ch-03-relativistic-dynamics.md#L313) | `openlyceum` | `RelativisticDynamics` | 1 | `fig:ch03-accelerate-sim` |
| 4 | [95](chapters/ch-04-interference-of-light.md#L95) | `openlyceum` | `LightPropagation` | All / default | `fig:ch04-em-wave-sim` |
| 4 | [259](chapters/ch-04-interference-of-light.md#L259) | `phet` | `wave-interference` | 3 | `fig:ch04-double-slit-sim` |
| 4 | [542](chapters/ch-04-interference-of-light.md#L542) | `openlyceum` | `DiffractionLab` | 1 | `fig:ch04:n-slit-sim` |
| 4 | [581](chapters/ch-04-interference-of-light.md#L581) | `openlyceum` | `StandingWaves` | 1 | `fig:ch04-reflection-sim` |
| 4 | [733](chapters/ch-04-interference-of-light.md#L733) | `openlyceum` | `InterferometryLab` | All / default | `fig:ch04-interferometry-sim` |
| 4 | [782](chapters/ch-04-interference-of-light.md#L782) | `openlyceum` | `InterferometryLab` | 2 | `fig:ch04:single-photon-interferometer-sim` |
| 5 | [139](chapters/ch-05-diffraction-of-light.md#L139) | `phet` | `wave-interference` | 4 | `fig:ch05-diffraction-sim` |
| 5 | [299](chapters/ch-05-diffraction-of-light.md#L299) | `openlyceum` | `DiffractionLab` | 1 | `fig:ch05:gratings-sim` |
| 5 | [364](chapters/ch-05-diffraction-of-light.md#L364) | `openlyceum` | `DiffractionLab` | 2 | `fig:ch05:grating-resolution-sim` |
| 5 | [475](chapters/ch-05-diffraction-of-light.md#L475) | `openlyceum` | `DiffractionLab` | 3 | `fig:ch05:airy-resolution-sim` |
| 5 | [524](chapters/ch-05-diffraction-of-light.md#L524) | `openlyceum` | `CrystalLattice` | All / default | `fig:ch05-crystal-sim` |
| 5 | [575](chapters/ch-05-diffraction-of-light.md#L575) | `openlyceum` | `DiffractionLab` | 4 | `fig:ch05:holography-sim` |
| 6 | [60](chapters/ch-06-particle-properties-of-waves.md#L60) | `phet` | `blackbody-spectrum` | All / default | `fig:ch06-blackbody-sim` |
| 6 | [166](chapters/ch-06-particle-properties-of-waves.md#L166) | `phet-legacy` | `photoelectric` | All / default | `fig:ch06-photoelectric-sim` |
| 6 | [219](chapters/ch-06-particle-properties-of-waves.md#L219) | `openlyceum` | `RadioWaves` | All / default | `fig:ch06-radiating-charge-sim` |
| 6 | [235](chapters/ch-06-particle-properties-of-waves.md#L235) | `openlyceum` | `PhotonInteractions` | 2 | `fig:ch06:xray-tube-sim` |
| 6 | [315](chapters/ch-06-particle-properties-of-waves.md#L315) | `openlyceum` | `PhotonInteractions` | 1 | `fig:ch06:compton-sim` |
| 6 | [353](chapters/ch-06-particle-properties-of-waves.md#L353) | `openlyceum` | `PhotonInteractions` | 3,4 | `fig:ch06:pair-annihilation-sim` |
| 7 | [96](chapters/ch-07-wave-properties-of-particles.md#L96) | `phet-legacy` | `quantum-wave-interference/davisson-germer` | All / default | `fig:ch07-davisson-germer-sim` |
| 7 | [139](chapters/ch-07-wave-properties-of-particles.md#L139) | `openlyceum` | `StandingWaves` | 3 | `fig:ch07-standing-wave-sim` |
| 7 | [166](chapters/ch-07-wave-properties-of-particles.md#L166) | `phet` | `quantum-wave-interference` | 3 | `fig:ch07-single-particle-sim` |
| 7 | [223](chapters/ch-07-wave-properties-of-particles.md#L223) | `phet` | `fourier-making-waves` | 3 | `fig:ch07-wave-packet-sim` |
| 7 | [317](chapters/ch-07-wave-properties-of-particles.md#L317) | `openlyceum` | `WaveComposer` | All / default | `fig:ch07-bandwidth-sim` |
| 8 | [55](chapters/ch-08-the-schrodinger-equation.md#L55) | `phet` | `quantum-measurement` | All / default | `fig:ch08-measurement-sim` |
| 8 | [187](chapters/ch-08-the-schrodinger-equation.md#L187) | `phet` | `particle-in-a-box` | All / default | `fig:ch08-particle-in-a-box-sim` |
| 8 | [195](chapters/ch-08-the-schrodinger-equation.md#L195) | `phet` | `quantum-bound-states` | All / default | `fig:ch08-bound-states-sim` |
| 8 | [203](chapters/ch-08-the-schrodinger-equation.md#L203) | `phet` | `bound-state-superposition` | All / default | `fig:ch08-bound-superposition-sim` |
| 8 | [239](chapters/ch-08-the-schrodinger-equation.md#L239) | `phet-legacy` | `quantum-tunneling` | All / default | `fig:ch08-tunneling-sim` |
| 9 | [98](chapters/ch-09-quantum-mechanics-in-three-dimensions.md#L98) | `openlyceum` | `QuantumAtom3D` | 1 | `fig:ch09:spherical-harmonics-sim` |
| 9 | [162](chapters/ch-09-quantum-mechanics-in-three-dimensions.md#L162) | `openlyceum` | `QuantumAtom3D` | 3 | `fig:ch09:angular-momentum-sim` |
| 9 | [192](chapters/ch-09-quantum-mechanics-in-three-dimensions.md#L192) | `openlyceum` | `SternGerlach` | All / default | `fig:ch09-stern-gerlach-sim` |
| 9 | [223](chapters/ch-09-quantum-mechanics-in-three-dimensions.md#L223) | `openlyceum` | `Precession` | All / default | `fig:ch09-precession-sim` |
| 9 | [275](chapters/ch-09-quantum-mechanics-in-three-dimensions.md#L275) | `openlyceum` | `QuantumAtom3D` | 5 | `fig:ch09:oscillator-degeneracy-sim` |
| 10 | [72](chapters/ch-10-the-hydrogen-atom.md#L72) | `phet` | `models-of-the-hydrogen-atom` | All / default | `fig:ch10-hydrogen-models-sim` |
| 10 | [181](chapters/ch-10-the-hydrogen-atom.md#L181) | `openlyceum` | `QuantumAtom3D` | 1 | `fig:ch10-quantum-atom-3d-sim` |
| 10 | [246](chapters/ch-10-the-hydrogen-atom.md#L246) | `openlyceum` | `LightAndAtoms` | 2 | `fig:ch10-light-and-atoms-sim` |
| 10 | [321](chapters/ch-10-the-hydrogen-atom.md#L321) | `openlyceum` | `QuantumAtom3D` | 4 | `fig:ch10-zeeman-atom-sim` |
| 10 | [378](chapters/ch-10-the-hydrogen-atom.md#L378) | `openlyceum` | `SimplifiedMRI` | All / default | `fig:ch10-mri-sim` |
| 11 | [123](chapters/ch-11-many-electron-atoms.md#L123) | `phet` | `build-an-atom` | All / default | `fig:ch11-build-atom-sim` |
| 11 | [131](chapters/ch-11-many-electron-atoms.md#L131) | `openlyceum` | `ElectronConfiguration` | All / default | `fig:ch11-electron-config-sim` |
| 11 | [190](chapters/ch-11-many-electron-atoms.md#L190) | `openlyceum` | `PeriodicTrends` | All / default | `fig:ch11-periodic-trends-sim` |
| 11 | [244](chapters/ch-11-many-electron-atoms.md#L244) | `openlyceum` | `PhotonInteractions` | 2 | `fig:ch11:moseley-sim` |
| 11 | [271](chapters/ch-11-many-electron-atoms.md#L271) | `phet-legacy` | `discharge-lamps` | All / default | `fig:ch11-discharge-sim` |
| 11 | [292](chapters/ch-11-many-electron-atoms.md#L292) | `phet-legacy` | `lasers` | All / default | `fig:ch11-laser-sim` |
| 11 | [318](chapters/ch-11-many-electron-atoms.md#L318) | `openlyceum` | `InterferometryLab` | 3 | `fig:ch11:laser-cavity-sim` |
| 12 | [47](chapters/ch-12-molecular-structure.md#L47) | `phet` | `molecule-polarity` | All / default | `fig:ch12-polarity-sim` |
| 12 | [90](chapters/ch-12-molecular-structure.md#L90) | `phet` | `molecule-shapes` | All / default | `fig:ch12-shapes-sim` |
| 12 | [96](chapters/ch-12-molecular-structure.md#L96) | `openlyceum` | `QuantumAtom3D` | 2 | `fig:ch12:hybrid-orbitals-sim` |
| 12 | [154](chapters/ch-12-molecular-structure.md#L154) | `phet` | `double-wells-and-covalent-bonds` | All / default | `fig:ch12-double-well-sim` |
| 12 | [162](chapters/ch-12-molecular-structure.md#L162) | `phet` | `band-structure` | All / default | `fig:ch12-band-structure-sim` |
| 12 | [182](chapters/ch-12-molecular-structure.md#L182) | `openlyceum` | `SpectroscopyLab` | 3 | `fig:ch12:electronic-spectra-sim` |
| 12 | [307](chapters/ch-12-molecular-structure.md#L307) | `phet` | `atomic-interactions` | All / default | `fig:ch12-interatomic-sim` |
| 12 | [323](chapters/ch-12-molecular-structure.md#L323) | `phet` | `molecules-and-light` | All / default | `fig:ch12-molecules-light-sim` |
| 12 | [382](chapters/ch-12-molecular-structure.md#L382) | `openlyceum` | `SpectroscopyLab` | 1 | `fig:ch12:rovibrational-sim` |
| 12 | [402](chapters/ch-12-molecular-structure.md#L402) | `openlyceum` | `QuantumPotential` | 2 | `fig:ch12:morse-potential-sim` |
| 13 | [45](chapters/ch-13-nuclear-physics.md#L45) | `phet` | `isotopes-and-atomic-mass` | All / default | `fig:ch13-isotopes-sim` |
| 13 | [77](chapters/ch-13-nuclear-physics.md#L77) | `phet` | `rutherford-scattering` | All / default | `fig:ch13-rutherford-sim` |
| 13 | [236](chapters/ch-13-nuclear-physics.md#L236) | `phet-legacy` | `nuclear-physics/radioactive-dating-game` | All / default | `fig:ch13-decay-sim` |
| 13 | [314](chapters/ch-13-nuclear-physics.md#L314) | `phet` | `alpha-decay` | All / default | `fig:ch13-alpha-decay-sim` |
| 13 | [334](chapters/ch-13-nuclear-physics.md#L334) | `phet` | `build-a-nucleus` | All / default | `fig:ch13-nucleus-sim` |
| 13 | [370](chapters/ch-13-nuclear-physics.md#L370) | `phet-legacy` | `nuclear-physics/nuclear-fission` | All / default | `fig:ch13-fission-sim` |
| 14 | [87](chapters/ch-14-elementary-particles-and-the-standard-model.md#L87) | `phet` | `beta-decay` | All / default | `fig:ch14-beta-decay-sim` |
| 14 | [133](chapters/ch-14-elementary-particles-and-the-standard-model.md#L133) | `openlyceum` | `ParticleZoo` | 4 | `fig:ch14:reaction-court-sim` |
| 14 | [172](chapters/ch-14-elementary-particles-and-the-standard-model.md#L172) | `openlyceum` | `ColliderLab` | 1,2,3 | `fig:ch14:collider-lab-sim` |
| 14 | [274](chapters/ch-14-elementary-particles-and-the-standard-model.md#L274) | `openlyceum` | `ParticleZoo` | 1,2 | `fig:ch14:hadron-builder-sim` |
| 14 | [308](chapters/ch-14-elementary-particles-and-the-standard-model.md#L308) | `openlyceum` | `ParticleZoo` | 3 | `fig:ch14:confinement-sim` |
