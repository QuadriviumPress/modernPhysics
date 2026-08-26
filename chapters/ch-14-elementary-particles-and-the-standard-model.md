---
title: Elementary Particles and the Standard Model
short_title: Chapter 14. Elementary Particles and the Standard Model
label: ch-elementary-particles-and-the-standard-model
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Classify particles as fermions or bosons and explain the physical distinction.
- Distinguish the four fundamental interactions by their relative strength, range, and mediating boson.
- Distinguish leptons and quarks as the two families of fundamental fermions, and state the generation structure of each.
- Explain quark confinement and construct the quark content of simple baryons and mesons.
- Apply conservation laws (charge, baryon number, lepton number) to determine whether a proposed particle reaction is allowed.
- Describe the role of the Higgs field in giving mass to fundamental particles.

## Introduction

Nuclear physics ([Chapter 13](#ch-nuclear-physics)) treated protons and neutrons as elementary building blocks, bound by the strong force into nuclei. This chapter goes one level deeper, to the particles and forces from which protons, neutrons, and indeed all matter are built. Over the course of the twentieth century, a rapidly growing zoo of "elementary" particles, discovered first in cosmic rays and then in purpose-built particle accelerators, was gradually organized into a coherent theoretical framework, the **Standard Model of particle physics**, which identifies a genuinely small set of truly fundamental particles and the forces (themselves mediated by particle exchange) that govern their interactions. This chapter surveys that framework: the classification of particles by spin and by the forces they feel, the substructure of protons and neutrons in terms of quarks, the conservation laws that govern which particle reactions can occur, and the mechanism by which most fundamental particles acquire mass at all.

## Classifying Particles: Fermions and Bosons

Every known particle carries an intrinsic spin angular momentum, quantized exactly as orbital angular momentum is ([Chapter 9](#ch-quantum-mechanics-in-three-dimensions)), $S = \sqrt{s(s+1)}\hbar$, but with $s$ either a half-integer ($\tfrac12, \tfrac32, \ldots$) or an integer ($0, 1, 2, \ldots$). This distinction is far more than bookkeeping: particles with half-integer spin, called **fermions**, obey the Pauli exclusion principle ([Chapter 11](#ch-many-electron-atoms)) and cannot occupy the same quantum state as an identical partner; particles with integer spin, called **bosons**, obey no such restriction and can occupy the same state in unlimited numbers (the basis, for photons, of the stimulated-emission cascade in a laser, [Chapter 11](#ch-many-electron-atoms)). Matter, in the Standard Model, is built from fermions (spin $\tfrac12$); the forces between them are mediated by the exchange of bosons.

## The Four Fundamental Interactions

All observed particle interactions are, to the precision of current experiments, accounted for by exactly four fundamental forces, each mediated by the exchange of a characteristic boson (a **gauge boson**, in the language of the quantum field theories underlying the Standard Model) and each with a distinct characteristic strength and range:

| Interaction | Relative strength | Range | Mediating boson(s) | Governs |
|---|---|---|---|---|
| Strong | $1$ | $\sim 1\ \text{fm}$ | gluon | quark binding; nuclear force (residual) |
| Electromagnetic | $\sim 10^{-2}$ | infinite | photon | charged-particle interactions |
| Weak | $\sim 10^{-6}$ | $\sim 10^{-3}\ \text{fm}$ | $W^\pm$, $Z^0$ | beta decay; some particle decays |
| Gravitational | $\sim 10^{-38}$ | infinite | graviton (hypothesized, not yet observed) | negligible for individual particles; dominant only for macroscopic masses |

The strong and weak interactions, both confined to nuclear-scale distances, are the reason their effects were unknown until nuclear and particle physics probed those scales directly; the electromagnetic and gravitational interactions, both infinite in range because their mediating boson is massless, dominate everyday, macroscopic experience. The relative strengths quoted are approximate and depend on the energy/distance scale at which the comparison is made, but the ordering — strong $\gg$ electromagnetic $\gg$ weak $\gg$ gravitational, at typical particle-physics scales — is robust. The strong force between nucleons discussed in [Chapter 13](#ch-nuclear-physics) is, in the Standard Model's deeper description, a residual effect of the strong force acting between the quarks confined inside each nucleon (analogous to the way the residual electromagnetic force between neutral atoms, the van der Waals force, is a residual effect of the more fundamental electromagnetic force between the charged constituents of each atom).

## Leptons and Quarks

The Standard Model's fundamental matter fermions fall into two families, **leptons** and **quarks**, each organized into three repeating **generations** of increasing mass, with (as far as current experiments show) identical properties within a generation apart from mass:

**Leptons** are fermions that do not feel the strong interaction. Each generation contains a charged lepton and a corresponding (essentially massless, electrically neutral) neutrino: the electron $e^-$ and electron neutrino $\nu_e$ (generation 1, the only stable charged lepton and the only leptons found in ordinary matter); the muon $\mu^-$ and muon neutrino $\nu_\mu$ (generation 2); and the tau $\tau^-$ and tau neutrino $\nu_\tau$ (generation 3). The muon and tau are, in essentially every respect apart from mass and consequent instability, heavier copies of the electron — the muon, for instance, decays via the weak interaction ($\mu^- \to e^- + \bar\nu_e + \nu_\mu$) with a mean lifetime of about $2.2\ \mu\text{s}$, far too short-lived to be found as a stable constituent of ordinary matter.

**Quarks** are fermions that do feel the strong interaction, and — unlike leptons — are never observed as free, isolated particles (a phenomenon called **confinement**, discussed further below). The three generations are: up ($u$) and down ($d$) (generation 1, the constituents of ordinary protons and neutrons); charm ($c$) and strange ($s$) (generation 2); and top ($t$) and bottom ($b$) (generation 3). Quarks carry fractional electric charge, $+\tfrac23 e$ ($u$, $c$, $t$) or $-\tfrac13 e$ ($d$, $s$, $b$), the only known particles to do so, and additionally carry a strong-interaction charge called **color** (in three varieties, whimsically named red, green, and blue, with no relation to visible color), which plays a role for the strong force directly analogous to the role electric charge plays for the electromagnetic force.

For every lepton and quark there exists a corresponding **antiparticle**, with identical mass and spin but opposite electric charge (and, for quarks, opposite color) — the electron's antiparticle, the positron, was introduced already in [Chapter 6](#ch-particle-properties-of-waves)'s discussion of pair production, and the same particle-antiparticle structure is universal across all Standard Model fermions.

## Hadrons and Confinement

Quarks are never seen individually; they are always found bound into composite particles called **hadrons**, a consequence of quark confinement: unlike the Coulomb or nuclear forces encountered so far, which weaken with distance, the strong force between two quarks does *not* weaken as they are pulled apart — instead, the energy stored in the strong-force field between them grows without bound, so that attempting to separate two quarks (e.g., in a high-energy collision) eventually supplies enough energy, via mass–energy equivalence, to spontaneously create a new quark-antiquark pair from the field energy itself, snapping the field into two shorter, separately confined pieces rather than yielding a single free quark. Hadrons are observed in exactly two configurations, both of which happen to have net integer electric charge and (color-)neutral total color charge, consistent with confinement always producing color-neutral bound states:

- **Baryons**: three quarks bound together (or three antiquarks, for antibaryons). The proton ($uud$) and neutron ($udd$) are the lightest, most familiar baryons; baryons are fermions (three half-integer spins combine to a net half-integer spin) and obey a conservation law, **baryon number** (discussed below).
- **Mesons**: a quark-antiquark pair. Mesons, such as the pion ($\pi^+ = u\bar d$, among others), are bosons (a half-integer spin combined with a half-integer spin gives an integer net spin) and carry baryon number zero.

## Conservation Laws

Not every combination of particles satisfying energy-momentum conservation is actually observed to occur; particle reactions additionally obey several conservation laws, some familiar from earlier chapters and some new to particle physics:

- **Electric charge** is conserved in every known interaction, without exception.
- **Baryon number** $B$ (defined as $+1$ for each baryon, $-1$ for each antibaryon, $0$ for all other particles, including mesons and leptons) is conserved in every observed reaction — this is why, for instance, the proton, the lightest baryon, is observed to be stable (or at least extremely long-lived: no proton decay has ever been observed, despite dedicated searches, placing its lifetime, if it decays at all, above $10^{34}$ years), since there is no lighter baryon for it to decay into consistent with $B$ conservation.
- **Lepton number**, separately for each generation ($L_e$, $L_\mu$, $L_\tau$, each $+1$ for the corresponding particle, $-1$ for its antiparticle, $0$ otherwise), is conserved to good approximation in essentially all observed reactions (this is why, for example, muon decay $\mu^- \to e^- + \bar\nu_e + \nu_\mu$ produces *both* an electron antineutrino and a muon neutrino, rather than either alone, to separately conserve $L_e$ and $L_\mu$: the initial state has $L_\mu = +1, L_e = 0$, and only the combination $\bar\nu_e + \nu_\mu$ on the right-hand side reproduces $L_e=0$, $L_\mu=+1$ on the left).

These conservation laws function exactly as energy, momentum, and angular momentum conservation do in earlier chapters: a proposed reaction consistent with all other physics can nonetheless be immediately ruled out if it violates one of these rules, and they provide a fast, purely bookkeeping-based check on whether an observed or hypothesized particle process is allowed.

## The Higgs Mechanism

A long-standing puzzle in the Standard Model was that the mathematical framework describing the weak and electromagnetic interactions in a unified way most naturally predicts that all fundamental particles, including the electron and quarks, should be massless — directly contradicted by experiment. The resolution, proposed independently by several theorists in 1964 (and associated most closely with the name of Peter Higgs), is that space is permeated by a nonzero background field, the **Higgs field**, and that fundamental particles acquire mass through their interaction with this field: a particle that couples strongly to the Higgs field behaves as though it has large inertia (large mass) as it moves through the field, while a particle that does not couple to it (the photon, for instance) remains exactly massless. Associated with the Higgs field, exactly as the electromagnetic field has an associated particle (the photon) representing its quantized excitations, is the **Higgs boson**, whose discovery at the Large Hadron Collider in 2012 — decades after it was first predicted, and requiring a purpose-built accelerator capable of reaching the multi-hundred-GeV collision energies needed to produce it directly — provided direct experimental confirmation of the mechanism and completed the last missing piece of the Standard Model's particle content.

## Summary

- Particles are classified by spin as **fermions** (half-integer spin, obey the exclusion principle; matter is built from these) or **bosons** (integer spin, no exclusion restriction; forces are mediated by these).
- Four fundamental interactions — **strong**, **electromagnetic**, **weak**, and **gravitational** — are distinguished by relative strength, range, and mediating gauge boson (gluon, photon, $W^\pm/Z^0$, and the hypothesized graviton, respectively).
- Matter fermions are **leptons** (no strong interaction; electron, muon, tau and their neutrinos, across three generations) and **quarks** (feel the strong interaction, carry fractional charge and color, never observed free due to **confinement**).
- Quarks bind into color-neutral **hadrons**: **baryons** (three quarks, e.g. proton $uud$, neutron $udd$) and **mesons** (quark-antiquark pairs).
- **Conservation laws** — electric charge, baryon number, and (approximately, per generation) lepton number — determine which proposed particle reactions are physically allowed.
- The **Higgs field**, and its associated **Higgs boson** (discovered 2012), is the mechanism by which most fundamental Standard Model particles acquire mass.

## Problems

1. Classify each of the following as a fermion or boson, based on its spin: photon ($s=1$), electron ($s=\tfrac12$), pion ($s=0$), proton ($s=\tfrac12$).

(ex-elementary-particles-and-the-standard-model-2)=
2. Determine the electric charge of a baryon composed of $uds$ (this particle is the $\Lambda^0$) using the quark charges $+\tfrac23 e$ for $u$, $-\tfrac13 e$ for $d$ and $s$, and check your result against the known charge of the $\Lambda^0$ (zero).

3. Determine whether each proposed reaction conserves charge, baryon number, and lepton number as required, and state which conservation law (if any) forbids the ones that are not allowed: (a) $p \to e^+ + \gamma$, (b) $n \to p + e^- + \bar\nu_e$, (c) $\mu^- \to e^- + \gamma$, (d) $p + p \to p + p + \pi^0$.

4. Using the known quark content of the proton ($uud$) and neutron ($udd$), and the quark charges given in [Problem 2](#ex-elementary-particles-and-the-standard-model-2), verify that the proton has charge $+e$ and the neutron has charge $0$.

5. The muon decays via $\mu^- \to e^- + \bar\nu_e + \nu_\mu$. Explain, using lepton-number conservation applied separately to the electron-generation number $L_e$ and muon-generation number $L_\mu$, why the decay $\mu^- \to e^- + \gamma$ alone (without the two neutrinos) is forbidden, even though it conserves charge, energy, and momentum.

6. Explain, in your own words, why quark confinement means that the constituent quarks of a proton can never be observed as free, isolated particles no matter how much energy is used to try to separate them, and contrast this with the behavior of the electromagnetic force between two separated electric charges, which weakens (rather than growing) with increasing separation.
