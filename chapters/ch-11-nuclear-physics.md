---
title: Nuclear Physics
short_title: Chapter 11. Nuclear Physics
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Describe the composition of the nucleus and use standard notation for nuclides and isotopes.
- Compute nuclear radius, density, binding energy, and binding energy per nucleon, and interpret the binding-energy-per-nucleon curve.
- Explain the qualitative form of the strong nuclear force and the semi-empirical (liquid-drop) mass formula.
- Apply the exponential radioactive decay law, including half-life, mean lifetime, and activity.
- Distinguish alpha, beta, and gamma decay, explain tunneling's role in alpha decay, and apply conservation laws to each.
- Explain nuclear fission and fusion in terms of the binding-energy curve and compute energy released in representative reactions.

## Introduction

Chapters 8–10 treated the nucleus as a structureless positive point charge, a fixed source of the Coulomb potential binding atomic electrons. This chapter looks inside the nucleus itself: a bound system of protons and neutrons, held together not by the electromagnetic force (which, among the mutually repelling protons, would tend to blow the nucleus apart) but by a new fundamental interaction, the strong nuclear force, with a strength and range entirely different from anything encountered so far in this book. The same quantum-mechanical ideas developed for atoms — quantized energy levels, tunneling, exponential decay driven by fixed transition probabilities — reappear here on a length scale roughly $10^5$ times smaller and an energy scale roughly $10^6$ times larger, and account for radioactivity, nuclear stability, and the energy-release mechanisms (fission and fusion) that make the nucleus, unlike the atom, a practical source of usable energy.

## Nuclear Composition and Notation

A nucleus consists of $Z$ protons and $N$ neutrons, collectively called **nucleons**, with mass number $A = Z + N$. A given nuclear species (**nuclide**) is denoted $^A_Z X$, where $X$ is the chemical symbol determined by $Z$ (since $Z$ alone fixes the number of atomic electrons in the neutral atom, and hence its chemistry). Nuclides sharing the same $Z$ but different $N$ (and hence different $A$) are **isotopes** of the same element — chemically near-identical but differing in mass and, often, nuclear stability. Protons and neutrons have nearly equal mass ($m_p c^2 = 938.3\ \text{MeV}$, $m_nc^2 = 939.6\ \text{MeV}$), and because a proton's charge is exactly opposite an electron's, the notation $^AZX$ carries the atom's full identity without needing $N$ written explicitly ($N = A - Z$).

## Nuclear Size, Density, and the Strong Force

Scattering experiments (extending Rutherford's original alpha-scattering method, now generally using higher-energy electron or nucleon probes to resolve the nuclear interior itself) show that nuclear radius grows with mass number as

$$
R = R_0 A^{1/3}, \qquad R_0 \approx 1.2\ \text{fm} \ (1\ \text{fm} = 10^{-15}\ \text{m}),
$$

so nuclear *volume* is proportional to $A$ — each nucleon occupies, on average, the same volume regardless of the size of the nucleus it belongs to, exactly as one would expect for an (nearly) incompressible fluid of tightly packed, closely spaced constituents. This is the empirical basis of the **liquid-drop model** of the nucleus, in which the nucleus is treated, for many purposes, as a droplet of incompressible nuclear fluid.

Nuclear stability is not explained by electromagnetism — the Coulomb force between two protons at nuclear separations, $\sim 1\ \text{fm}$, is enormously repulsive and would fly the nucleus apart if the electromagnetic force between nucleons were the whole story. Nuclei are held together by the **strong nuclear force**, an attractive interaction between nucleons (proton-proton, proton-neutron, and neutron-neutron alike, largely independent of charge) that is far stronger than the Coulomb repulsion at nuclear distances, but has an extremely short range (roughly $1$–$2\ \text{fm}$), falling off essentially to zero beyond a few fermis. This short range explains why nuclear binding, unlike Coulomb binding, saturates: a given nucleon interacts strongly only with its immediate neighbors, not with every other nucleon in the nucleus (unlike the long-range Coulomb repulsion, which every proton feels from every other proton, growing roughly as $Z^2$) — a key qualitative fact used below to explain both the shape of the binding-energy curve and, ultimately, nuclear fission and fusion.

## Binding Energy

The mass of a bound nucleus is always *less* than the sum of the masses of its separated constituent protons and neutrons — a direct manifestation of mass–energy equivalence (Chapter 3): energy must be supplied to pull the nucleus apart into free nucleons, so the bound system, having lower total energy, has correspondingly lower total mass. The **binding energy** is defined as

$$
E_B = \left[Zm_p + Nm_n - M(^A_ZX)\right]c^2,
$$

where $M(^A_ZX)$ is the measured nuclear mass (in practice, atomic masses, which include electrons, are tabulated and used consistently on both sides of this equation, since the electron masses and atomic binding energies very nearly cancel). It is generally more informative to consider the **binding energy per nucleon**, $E_B/A$, since this measures how tightly, on average, an individual nucleon is bound, independent of the nucleus's overall size.

Plotting $E_B/A$ against $A$ for all known nuclides gives one of the most important curves in nuclear physics: $E_B/A$ rises sharply from very light nuclei, peaks at around $E_B/A \approx 8.7\ \text{MeV}$ near $A \approx 56$ (iron and its neighbors), and then decreases slowly for heavier nuclei. Two competing effects, both traceable to the short range of the strong force versus the long range of the Coulomb force, explain this shape: for light nuclei, a growing fraction of nucleons sit at or near the nuclear surface, with fewer strong-force neighbors than an interior nucleon has (a **surface term**, reducing $E_B/A$ for small $A$, since surface-to-volume ratio falls as $A$ grows), while for heavy nuclei, the number of proton pairs, and hence the total Coulomb repulsion energy, grows roughly as $Z^2$ — much faster than the (short-range, saturating) strong-force binding, which grows only as $A$ — progressively weakening binding per nucleon as $A$ increases (a **Coulomb term**). Together with a bulk (volume) term that would alone give constant $E_B/A$, and additional smaller terms accounting for the extra stability of nuclei with $N=Z$ (a symmetry term) and of nuclei with even numbers of protons and neutrons (a pairing term), these considerations make up the **semi-empirical mass formula** (also called the Weizsäcker or liquid-drop mass formula), which reproduces the observed binding energy of essentially every known nuclide to good accuracy using only five fitted terms with a clear physical origin apiece.

The location of the peak at $A\approx56$ has an immediate and far-reaching consequence, developed further below: **energy can be released either by combining light nuclei into heavier ones (fusion) or by splitting heavy nuclei into lighter ones (fission)**, in each case moving the participating nucleons toward the peak of the curve, where they are more tightly bound (lower mass) than before — with the energy released equal to the resulting decrease in total rest mass, via $E = \Delta m\, c^2$.

## Radioactive Decay

An unstable nuclide decays into a different nuclide (or a lower energy state of the same nuclide) at a rate governed, as with any quantum system undergoing a transition, by a fixed, per-nucleus **decay constant** $\lambda$ (units of inverse time), independent of the nucleus's history or environment (with rare, small exceptions for certain electron-capture processes sensitive to chemical environment). If $N(t)$ is the number of undecayed nuclei present at time $t$, the rate of decay is proportional to the number remaining, $dN/dt = -\lambda N$, giving the **exponential decay law**:

$$
N(t) = N_0\, e^{-\lambda t}.
$$

The **half-life** $T_{1/2}$, the time for half of an initial sample to decay, and the **mean lifetime** $\tau$, the average lifetime of an individual nucleus, are related to $\lambda$ by

$$
T_{1/2} = \frac{\ln 2}{\lambda}, \qquad \tau = \frac{1}{\lambda} = \frac{T_{1/2}}{\ln 2}.
$$

The **activity**, $\mathcal{A} \equiv -dN/dt = \lambda N(t) = \mathcal{A}_0 e^{-\lambda t}$, is the physically measured decay rate (in decays per second, or the traditional unit the curie), and decays with the same exponential form and the same $T_{1/2}$ as $N(t)$ itself, since $\mathcal A$ is simply proportional to $N$ at every instant.

## Modes of Decay

Three principal decay modes connect unstable nuclides to more stable ones:

**Alpha decay** ($^A_ZX \to {}^{A-4}_{Z-2}Y + \alpha$, where $\alpha = {}^4_2\text{He}$) occurs predominantly among heavy nuclei, where it is energetically favorable (the parent's mass exceeds the combined daughter-plus-alpha mass) largely because of the Coulomb term discussed above. Classically, the alpha particle is confined within the nucleus by a potential well combining the short-range attractive strong force and, outside the nuclear radius, the repulsive Coulomb barrier — a barrier typically well above the alpha particle's actual kinetic energy once emitted, so classically the particle could never escape. Alpha decay is understood, quantitatively, as **quantum tunneling** (Chapter 6) of the alpha particle through this Coulomb barrier: the measured strong sensitivity of half-life to alpha particle energy (the **Geiger–Nuttall relation**, an empirical pattern in which small changes in emitted alpha energy correspond to enormous changes in half-life, spanning many orders of magnitude across known alpha emitters) is explained quantitatively by the exponential dependence of the tunneling probability on barrier height and width worked out in Chapter 6, making alpha decay one of the most direct large-scale confirmations of quantum tunneling.

**Beta decay** occurs in three related forms — $\beta^-$ decay ($n \to p + e^- + \bar\nu_e$, converting a neutron to a proton within the nucleus), $\beta^+$ decay ($p \to n + e^+ + \nu_e$), and electron capture ($p + e^- \to n + \nu_e$) — each mediated by the weak nuclear interaction (Chapter 12) and each moving a nucleus toward the more stable $N/Z$ ratio for its mass number. The **neutrino** ($\nu_e$) and **antineutrino** ($\bar\nu_e$) are required, not merely as bookkeeping devices, by conservation of energy, momentum, and angular momentum: without a third emitted particle, a two-body decay ($n \to p + e^-$ alone) would force the emitted electron to have one single, fixed energy for a given parent-daughter pair, but the observed electron energy spectrum in beta decay is continuous, spread over a range up to a fixed maximum — direct evidence (first argued by Pauli in 1930, on exactly these grounds) that a third, initially unobserved particle carries away the missing energy and momentum event by event.

**Gamma decay** ($^A_ZX^* \to {}^A_ZX + \gamma$, where the asterisk denotes an excited nuclear state) is the nuclear analog of atomic photon emission (Chapter 8): a nucleus left in an excited state, often as the immediate product of a preceding alpha or beta decay, drops to a lower-energy (often the ground) state by emitting a photon, with energy set by the spacing between nuclear energy levels — typically keV to MeV, far larger than atomic transition energies, because the nuclear scale of confinement is so much smaller than the atomic scale (an application of the same uncertainty-principle confinement argument used in Chapter 5).

## Fission

**Nuclear fission** is the splitting of a heavy nucleus (typically after absorbing a neutron, which excites the nucleus into oscillation, distorting the initially spherical liquid drop) into two lighter, roughly comparable-mass fragments, plus several free neutrons. Because the binding-energy-per-nucleon curve rises steeply from heavy $A$ toward the $A\approx56$ peak, the fragments are individually more tightly bound (per nucleon) than the original heavy nucleus was, and the reaction releases a large amount of energy, typically around $200\ \text{MeV}$ per fission event for a nucleus such as $^{235}_{92}\text{U}$ — overwhelmingly larger than typical chemical reaction energies (electron-volts per bond, versus roughly $10^8$ times more energy per fission event), directly reflecting the vastly greater strength of the nuclear force compared to the electromagnetic forces governing chemical bonding.

Because each fission event releases, on average, more than one free neutron, and each of those neutrons can potentially induce a further fission event in a neighboring nucleus, a **chain reaction** is possible if enough fissile material is present (a **critical mass**) to sustain, on average, at least one neutron-induced fission per neutron released — the basis of both controlled fission (nuclear power reactors, where the reaction rate is regulated, e.g. via neutron-absorbing control rods) and uncontrolled fission (fission weapons).

## Fusion

**Nuclear fusion**, the combination of two light nuclei into a single heavier one, releases energy for exactly the mirror-image reason: moving from very light $A$ toward the peak of the binding-energy curve increases $E_B/A$, so the fused product is more tightly bound (per nucleon) than the separate light nuclei were. Fusion is the energy source that powers stars, where sequences of fusion reactions (in the Sun, predominantly the **proton-proton chain**, ultimately converting four protons into a helium-4 nucleus plus positrons, neutrinos, and gamma rays) release the energy that balances gravitational collapse and produces the Sun's luminosity (Chapter 3, Problem 6). Because fusion requires two positively charged nuclei to approach to within the range of the strong force ($\sim 1\ \text{fm}$) against their mutual Coulomb repulsion, it requires very high temperatures (tens of millions of kelvin or more, as in stellar cores) to proceed at an appreciable rate even with the assistance of quantum tunneling through the Coulomb barrier — the same tunneling mechanism responsible for alpha decay, now working in reverse to allow two light nuclei to fuse despite insufficient classical kinetic energy to overcome their mutual repulsion.

## Summary

- A nucleus $^A_ZX$ contains $Z$ protons and $N=A-Z$ neutrons; nuclear radius scales as $R = R_0A^{1/3}$, consistent with a roughly incompressible liquid-drop model of tightly packed nucleons.
- The short-range, charge-independent **strong nuclear force** overcomes Coulomb repulsion to bind the nucleus; **binding energy**, $E_B = [Zm_p+Nm_n-M]c^2$, and **binding energy per nucleon**, peaking near $A\approx56$ (iron), summarize nuclear stability and are captured by the semi-empirical mass formula's volume, surface, Coulomb, symmetry, and pairing terms.
- Radioactive decay follows the exponential law $N(t)=N_0e^{-\lambda t}$, with half-life $T_{1/2}=\ln2/\lambda$ and activity $\mathcal A = \lambda N$.
- **Alpha decay** proceeds by quantum tunneling through the Coulomb barrier; **beta decay** ($\beta^-$, $\beta^+$, electron capture) proceeds via the weak interaction and requires a neutrino/antineutrino to conserve energy, momentum, and angular momentum, as shown by the continuous beta-electron energy spectrum; **gamma decay** is photon emission between nuclear energy levels.
- **Fission** (heavy nucleus splits) and **fusion** (light nuclei combine) both release energy by moving nucleons toward the binding-energy peak near $A\approx56$; fission chain reactions require a critical mass, and fusion requires overcoming the Coulomb barrier, typically via high temperature and tunneling, as in stellar interiors.

## Problems

1. Estimate the nuclear radius of $^{238}_{92}\text{U}$ and of $^{4}_{2}\text{He}$ using $R = R_0A^{1/3}$, and compute the ratio of their radii. Comment on whether this ratio is consistent with $A^{1/3}$ scaling given the ratio of their mass numbers.

2. Compute the binding energy and binding energy per nucleon of $^{4}_{2}\text{He}$, given $M(^4_2\text{He}) = 4.002602\ \text{u}$, $m_p = 1.007276\ \text{u}$, $m_n=1.008665\ \text{u}$, and using $1\ \text{u}\,c^2 = 931.5\ \text{MeV}$ (you may neglect the small correction from atomic electron binding energies).

3. A radioactive sample of $^{131}_{53}\text{I}$ (half-life $8.02$ days) initially contains $N_0 = 1.00\times10^{18}$ nuclei. (a) Find the decay constant $\lambda$. (b) Find the number of nuclei remaining after $24$ days. (c) Find the initial activity, in becquerels (decays/s).

4. $^{238}_{92}\text{U}$ undergoes alpha decay to $^{234}_{90}\text{Th}$. Write the full decay equation, and explain, using the shape of the binding-energy-per-nucleon curve, why alpha decay (rather than, say, single-proton emission) is the energetically favored decay mode for very heavy nuclei.

5. In beta-minus decay of a free neutron, $n \to p + e^- + \bar\nu_e$, use $m_nc^2 = 939.57\ \text{MeV}$, $m_pc^2 = 938.27\ \text{MeV}$, $m_ec^2 = 0.511\ \text{MeV}$ (and treat the antineutrino as massless) to find the total kinetic energy shared among the three decay products. Explain why the electron's kinetic energy alone is not fixed at this value, but instead varies continuously up to it.

6. In the fission of $^{235}_{92}\text{U}$ (via neutron absorption to $^{236}_{92}\text{U}$, then fission), roughly $200\ \text{MeV}$ is released per event. Estimate the mass (in kg) of $^{235}\text{U}$ that would need to fission completely to release $1.0\times10^{14}\ \text{J}$ (order of magnitude of a small commercial reactor's daily output), using Avogadro's number and the molar mass of $^{235}\text{U}$.
