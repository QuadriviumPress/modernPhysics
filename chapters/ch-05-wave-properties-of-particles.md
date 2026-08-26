---
title: Wave Properties of Particles
short_title: Chapter 5. Wave Properties of Particles
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the de Broglie hypothesis and compute the de Broglie wavelength of a particle.
- Describe the Davisson–Germer experiment and explain why it confirms the de Broglie hypothesis.
- Explain wave–particle duality and why it applies to both light and matter.
- Construct a wave packet as a superposition of waves and relate its spatial and momentum spread.
- State, derive qualitatively, and apply the Heisenberg uncertainty principle for position–momentum and energy–time.
- Use the uncertainty principle to estimate minimum energies and to explain why electrons cannot exist inside a nucleus.

## Introduction

Chapter 4 established that light, long understood as a wave, also behaves as a stream of particle-like quanta in its interactions with matter. In 1924, Louis de Broglie proposed the converse: that matter, long understood as composed of particles, should also exhibit wave behavior. This was not an experimental discovery but a bold symmetry argument, made in de Broglie's doctoral thesis, and it proved correct. This chapter develops the de Broglie hypothesis, the experiments that confirmed it, and its most important consequence: because a particle with a well-defined wavelength is necessarily spread out in space, position and momentum cannot both be known with unlimited precision. That trade-off, the Heisenberg uncertainty principle, is not a statement about the limits of measurement technique but a fundamental feature of nature, and it sets the stage for the wave mechanics developed in Chapter 6.

## The de Broglie Hypothesis

Chapter 4 established that a photon carries momentum related to its wavelength by $p = h/\lambda$. De Broglie's proposal was to take this relation, turn it around, and apply it universally: **every material particle of momentum $p$ has an associated wavelength**

$$
\lambda = \frac{h}{p},
$$

now called the **de Broglie wavelength**. For a nonrelativistic particle of mass $m$ and speed $u$, $p = mu$, so $\lambda = h/mu$. Because $h$ is so small, the de Broglie wavelength of ordinary macroscopic objects is utterly negligible — a $1\ \text{g}$ mass moving at $1\ \text{m/s}$ has $\lambda \sim 10^{-31}\ \text{m}$, far too small to produce any observable wave effect — which is why matter waves went unnoticed until physicists deliberately looked for them in systems where $\lambda$ is not negligible, such as low-energy electrons, whose small mass makes $\lambda$ comparable to atomic and crystal-lattice spacings for accessible kinetic energies.

## The Davisson–Germer Experiment

Direct confirmation came in 1927, when Clinton Davisson and Lester Germer, studying electron scattering from a nickel crystal (originally for an unrelated purpose), observed that the intensity of electrons scattered from the crystal surface showed sharp maxima at specific angles, depending on the electrons' kinetic energy — exactly the pattern expected from **diffraction** of a wave by the regularly spaced planes of atoms in the crystal, analogous to X-ray diffraction from a crystal lattice (Bragg diffraction). Measuring the angles of the diffraction maxima and applying the same diffraction condition used for X-rays,

$$
d\sin\theta = n\lambda,
$$

(with $d$ the crystal's known interplanar spacing) allowed Davisson and Germer to extract an experimental wavelength for the electrons — and it agreed, to good precision, with the de Broglie wavelength $\lambda = h/p$ computed from the electrons' known kinetic energy. Electrons, unambiguously particles in every other respect (they have definite charge and mass, and leave localized tracks and point-like impacts on a detector), diffract like waves when their de Broglie wavelength is comparable to the spacing of the diffracting structure. The effect has since been confirmed for neutrons, atoms, and even large molecules, and is the operating principle of the electron microscope, whose resolution — set by the wavelength of the imaging "light," per ordinary diffraction limits — can be far finer than any visible-light microscope because electron de Broglie wavelengths can be made far shorter than visible wavelengths.

## Wave–Particle Duality

The picture that emerges from Chapters 4 and 5 together is symmetric: light, ordinarily described as a wave, exhibits particle-like behavior (photoelectric effect, Compton scattering); matter, ordinarily described as particles, exhibits wave-like behavior (electron diffraction). Neither description is simply "wrong" and replaced by the other; rather, **both light and matter possess both wave and particle aspects**, and which aspect is manifest depends on the experiment performed. This is **wave–particle duality**. It is tempting, but incorrect, to imagine that a photon or electron is "really" a tiny wave packet that sometimes behaves like a particle, or "really" a tiny particle that sometimes behaves like a wave; the two descriptions are complementary, and a full account of quantum behavior (developed starting in Chapter 6) requires a mathematical object — the wave function — that reduces to particle-like or wave-like predictions depending on what is measured, without being fully captured by either classical picture on its own.

## Wave Packets

To describe a localized particle in wave language, a single wave of definite wavelength $\lambda = h/p$ — which by its nature extends infinitely in space with constant amplitude — is not adequate, since it corresponds to a perfectly definite momentum but gives no information about *where* the particle is. A localized particle is instead represented by a **wave packet**: a superposition of many waves of slightly different wavelength (equivalently, different wave number $k = 2\pi/\lambda$), chosen so that they interfere constructively in some limited region $\Delta x$ and destructively (cancel) elsewhere. The mathematics of superposition (the same mathematics used for beats and Fourier synthesis of waveforms) requires that a packet localized to a narrow spatial region $\Delta x$ necessarily be built from a *broad* range of wave numbers $\Delta k$, and vice versa; the two spreads are inversely related, roughly

$$
\Delta x\, \Delta k \gtrsim 1,
$$

a purely mathematical fact about waves, true for sound pulses and water-wave packets just as much as for matter waves, with no quantum content yet. Quantum mechanics enters when this relation is combined with the de Broglie relation $p = hk/2\pi = \hbar k$ (where $\hbar \equiv h/2\pi$), converting spread in wave number into spread in momentum, $\Delta p = \hbar\,\Delta k$, and giving

$$
\Delta x\,\Delta p \gtrsim \hbar.
$$

## The Heisenberg Uncertainty Principle

Werner Heisenberg (1927) elevated this wave-packet relation to a fundamental principle governing all quantum systems, stated precisely as

$$
\Delta x\, \Delta p_x \geq \frac{\hbar}{2},
$$

where $\Delta x$ and $\Delta p_x$ are, more precisely, statistical spreads (standard deviations) in simultaneous measurements of position and momentum made on identically prepared systems. The **Heisenberg uncertainty principle** states that these two spreads cannot both be made arbitrarily small: the more precisely a particle's position is known, the less precisely its momentum can be known, and conversely. This is not a statement about the clumsiness of measuring instruments, correctable in principle by better technology — it is a consequence of the wave nature of matter itself, as the wave-packet argument above shows: a particle simply *does not possess* simultaneously well-defined position and momentum, in the same sense that a wave pulse of well-defined wavelength cannot also be localized to a point.

An analogous relation holds between energy and time,

$$
\Delta E\, \Delta t \geq \frac{\hbar}{2},
$$

where $\Delta t$ characterizes the time available to measure (or the lifetime of a state with) energy spread $\Delta E$. This relation, for instance, explains why an unstable state with a short lifetime $\Delta t$ (such as an excited atomic state, or an unstable particle) necessarily has an intrinsic spread, or "width," in its energy — and correspondingly in the frequency/wavelength of radiation it emits — that grows as its lifetime shrinks.

### Worked Example: Confining an Electron in a Nucleus

Could an electron exist bound inside an atomic nucleus, of radius $r \sim 5\times 10^{-15}\ \text{m}$? If so, the position uncertainty could be no larger than $\Delta x \sim r$, and the uncertainty principle then requires a momentum uncertainty of at least

$$
\Delta p \gtrsim \frac{\hbar}{2\,\Delta x} \approx \frac{1.055\times10^{-34}}{2(5\times10^{-15})}\ \text{kg}\cdot\text{m/s} \approx 1.1\times10^{-20}\ \text{kg}\cdot\text{m/s}.
$$

Converting to an energy via the (relativistic, since this momentum turns out to be large) relation $E \approx pc$ for $pc \gg mc^2$: $pc \approx (1.1\times10^{-20})(3.0\times10^8)\ \text{J} \approx 3.3\times10^{-12}\ \text{J} \approx 21\ \text{MeV}$. An electron confined to nuclear dimensions would need kinetic energy of tens of MeV — far larger than the few-MeV binding energies available in nuclei (Chapter 11) — so such an electron could not remain bound; this is one of the historical arguments (alongside others involving nuclear spin and magnetic moment) that electrons are not constituents of the nucleus, correctly anticipating that beta decay (Chapter 11) must *create* an electron at the moment of decay rather than releasing one that was previously confined inside.

## Summary

- The **de Broglie hypothesis** assigns every particle of momentum $p$ a wavelength $\lambda = h/p$, extending the photon relation of Chapter 4 to all matter.
- The **Davisson–Germer experiment** confirmed this directly: electrons diffract from a crystal lattice with a wavelength matching $\lambda = h/p$, exactly as X-rays do.
- **Wave–particle duality**: light and matter both show wave and particle behavior; which is manifest depends on the experiment, and neither classical picture alone is complete.
- A localized particle is represented by a **wave packet**, a superposition of waves over a range of wave numbers $\Delta k$; a narrower spatial spread $\Delta x$ requires a broader $\Delta k$ (and hence, via $p = \hbar k$, a broader momentum spread $\Delta p$).
- The **Heisenberg uncertainty principle**, $\Delta x\,\Delta p_x \geq \hbar/2$ (and analogously $\Delta E\,\Delta t \geq \hbar/2$), is a fundamental limit on the simultaneous precision of conjugate quantities, rooted in the wave nature of matter, not a limitation of measuring instruments.

## Problems

1. Find the de Broglie wavelength of (a) an electron with kinetic energy $54\ \text{eV}$ (as in the original Davisson–Germer experiment), (b) a proton with kinetic energy $1.0\ \text{MeV}$, and (c) a $0.145\ \text{kg}$ baseball moving at $40\ \text{m/s}$. Comment on which of these wavelengths could plausibly produce observable diffraction, and from what kind of structure.

2. In the Davisson–Germer experiment, a diffraction maximum for 54 eV electrons was observed at $\theta = 50°$ from a nickel crystal. Using $\lambda = h/p$ for the electrons' de Broglie wavelength and the diffraction condition $d\sin\theta = \lambda$ (first order, $n=1$), find the effective interplanar spacing $d$ of the nickel crystal consistent with this observation.

3. A proton is confined to a nucleus of diameter $1.0\times10^{-14}\ \text{m}$. Use the uncertainty principle to estimate the minimum kinetic energy the proton must have, and compare it (order of magnitude) to typical nuclear binding energies of several MeV per nucleon (Chapter 11).

4. An excited atomic state has a mean lifetime of $\Delta t = 1.0\times10^{-8}\ \text{s}$. (a) Use the energy–time uncertainty relation to estimate the minimum energy spread $\Delta E$ of this state, in eV. (b) If the state decays by emitting a photon of wavelength $500\ \text{nm}$, estimate the corresponding spread (linewidth) $\Delta\lambda$ in the emitted wavelength.

5. A beam of electrons is passed through a single slit of width $a$. Using the single-slit diffraction condition (first minimum at $\sin\theta \approx \lambda/a$ for small angles) together with the de Broglie relation, express the transverse momentum spread $\Delta p_y$ imparted to the electrons (estimated from $p\sin\theta$) in terms of the slit width $a$, and show that $\Delta y\,\Delta p_y \sim h$ if $\Delta y \sim a$, consistent with the uncertainty principle.

6. Explain, using the energy–time uncertainty relation, why a particle that is truly stable (infinite lifetime) can have a perfectly sharp rest energy $mc^2$, while an unstable particle cannot — and why particle physicists therefore quote both a mass and a "width" (in energy units) for unstable particles, a topic revisited in Chapter 12.
