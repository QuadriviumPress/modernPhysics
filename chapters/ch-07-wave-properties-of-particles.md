---
title: Wave Properties of Particles
short_title: Chapter 7. Wave Properties of Particles
label: ch-wave-properties-of-particles
numbering:
  enumerator: "7.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State the de Broglie hypothesis and compute the de Broglie wavelength of a particle.
- Explain how the de Broglie hypothesis reinterprets the Bohr model's angular-momentum quantization condition as a standing-wave requirement.
- Describe the Davisson–Germer and G. P. Thomson experiments and explain why they confirm the de Broglie hypothesis, and describe how matter-wave interference has since been extended to atoms and large molecules.
- Explain wave–particle duality and complementarity, and describe how "which-path" information destroys interference.
- Construct a wave packet as a superposition of waves and relate its spatial and momentum spread; distinguish phase velocity from group velocity and show that group velocity equals particle velocity.
- State, derive qualitatively, and apply the Heisenberg uncertainty principle for position–momentum and energy–time.
- Use the uncertainty principle to estimate minimum energies and to explain why electrons cannot exist inside a nucleus.

## Introduction

[Chapter 6](#ch-particle-properties-of-waves) established that light, long understood as a wave, also behaves as a stream of particle-like quanta in its interactions with matter. In 1924, Louis de Broglie proposed the converse: that matter, long understood as composed of particles, should also exhibit wave behavior. This was not an experimental discovery but a bold symmetry argument, made in de Broglie's doctoral thesis, and it proved correct. This chapter develops the de Broglie hypothesis, the experiments that confirmed it, and its most important consequence: because a particle with a well-defined wavelength is necessarily spread out in space, position and momentum cannot both be known with unlimited precision. That trade-off, the Heisenberg uncertainty principle, is not a statement about the limits of measurement technique but a fundamental feature of nature, and it sets the stage for the wave mechanics developed in [Chapter 8](#ch-the-schrodinger-equation).

## The de Broglie Hypothesis

[Chapter 6](#ch-particle-properties-of-waves) established that a photon carries momentum related to its wavelength by $p = h/\lambda$. De Broglie's proposal was to take this relation, turn it around, and apply it universally: **every material particle of momentum $p$ has an associated wavelength**

$$
\lambda = \frac{h}{p},
$$

now called the **de Broglie wavelength**. For a nonrelativistic particle of mass $m$ and speed $u$, $p = mu$, so $\lambda = h/mu$; more generally, for a particle accelerated from rest through a potential difference $V$, $K = eV = p^2/2m$ gives $p = \sqrt{2meV}$ and hence $\lambda = h/\sqrt{2meV}$. Because $h$ is so small, the de Broglie wavelength of ordinary macroscopic objects is utterly negligible — a $1\ \text{g}$ mass moving at $1\ \text{m/s}$ has $\lambda \sim 10^{-31}\ \text{m}$, far too small to produce any observable wave effect — which is why matter waves went unnoticed until physicists deliberately looked for them in systems where $\lambda$ is not negligible, such as low-energy electrons, whose small mass makes $\lambda$ comparable to atomic and crystal-lattice spacings for accessible kinetic energies.

### Worked Example: De Broglie Wavelength of an Accelerated Electron

An electron is accelerated from rest through a potential difference of $V = 100\ \text{V}$, a typical value in early electron-diffraction experiments. Its nonrelativistic momentum is

$$
p = \sqrt{2m_eeV} = \sqrt{2(9.11\times10^{-31}\ \text{kg})(1.60\times10^{-19}\ \text{C})(100\ \text{V})} = 5.40\times10^{-24}\ \text{kg}\cdot\text{m/s},
$$

so the de Broglie wavelength is

$$
\lambda = \frac{h}{p} = \frac{6.626\times10^{-34}\ \text{J}\cdot\text{s}}{5.40\times10^{-24}\ \text{kg}\cdot\text{m/s}} = 1.23\times10^{-10}\ \text{m} = 0.123\ \text{nm}.
$$

This convenient combination is often written $\lambda[\text{nm}] \approx 1.226/\sqrt{V[\text{volts}]}$ for nonrelativistic electrons. The result, $0.123\ \text{nm}$, is comparable to the spacing between atomic planes in a crystal ($\sim 0.1$–$0.3\ \text{nm}$) — exactly the condition needed for the crystal to act as a diffraction grating for the electrons, as the next section describes.

### A Consistency Check: The Relativistic Origin of $\lambda = h/p$

De Broglie did not simply guess $\lambda = h/p$; he arrived at it by demanding consistency between the photon relations of [Chapter 6](#ch-particle-properties-of-waves) and the relativistic energy–momentum relation of [Chapter 3](#ch-relativistic-dynamics). A wave of frequency $f$ and phase speed $u_p$ has wavelength $\lambda = u_p/f$. Associating a particle of energy $E$ with a wave of frequency $f=E/h$ (the Planck–Einstein relation, extended by hypothesis to matter) and demanding that the resulting phase velocity be consistent with the particle's momentum $p$ via $E=pc^2/u$ (the relativistic relation between energy, momentum, and velocity established in [Chapter 3](#ch-relativistic-dynamics)) leads, after eliminating $f$ and $u_p$ in favor of $E$, $p$, and the particle's actual velocity $u$, directly to $\lambda = h/p$ — the same relation obtained by simply carrying the photon formula over to matter, but now derived from relativistic energy–momentum consistency rather than asserted by analogy alone. This is one reason de Broglie's hypothesis, though speculative, was taken seriously immediately: it was not an arbitrary guess but the unique relation consistent with treating matter and light on the same relativistic footing.

## The Davisson–Germer and G. P. Thomson Experiments

Direct confirmation came in 1927, when Clinton Davisson and Lester Germer, studying electron scattering from a nickel crystal (originally for an unrelated purpose), observed that the intensity of electrons scattered from the crystal surface showed sharp maxima at specific angles, depending on the electrons' kinetic energy — exactly the pattern expected from **diffraction** of a wave by the regularly spaced planes of atoms in the crystal, analogous to X-ray diffraction from a crystal lattice (Bragg diffraction). Measuring the angles of the diffraction maxima and applying the same diffraction condition used for X-rays,

$$
d\sin\theta = n\lambda,
$$

(with $d$ the crystal's known interplanar spacing) allowed Davisson and Germer to extract an experimental wavelength for the electrons — and it agreed, to good precision, with the de Broglie wavelength $\lambda = h/p$ computed from the electrons' known kinetic energy.

The experiment is reconstructed in {numref}`Figure %s <fig:ch07-davisson-germer-sim>`, where both sides of $d\sin\theta = n\lambda$ are under control: the electron gun's accelerating voltage, which fixes $p$ and hence $\lambda = h/p$, and the spacing of the target atoms, which fixes $d$. Raising the voltage shortens the wavelength and pulls the scattering maxima to smaller angles; widening the atomic spacing pushes them back out. Neither response is available to a stream of particles bouncing off a surface, and observing both is what settled the question.

```{phet-legacy} quantum-wave-interference/davisson-germer
:sim-name: Davisson–Germer: Electron Diffraction
:label: fig:ch07-davisson-germer-sim

Electrons scattering from a crystal surface, with the beam energy and the atomic spacing under control. What is drawn is the electron's wave; where it is detected is a single point.
```

That same year, working independently in Britain, George Paget Thomson fired higher-energy electrons through thin polycrystalline metal foils and observed concentric diffraction rings on a photographic plate — the electron analog of the ring patterns produced by X-ray diffraction through a powdered crystalline sample — providing an independent confirmation using a completely different experimental geometry. Thomson's result carries a particular irony: his father, J. J. Thomson, had won the 1906 Nobel Prize for discovering the electron and demonstrating that it is a particle with a definite charge-to-mass ratio; the son shared the 1937 Nobel Prize (with Davisson) for demonstrating that the very same particle also behaves as a wave — both experiments correct, neither in conflict with the other, once wave–particle duality is properly understood.

Electrons, unambiguously particles in every other respect (they have definite charge and mass, and leave localized tracks and point-like impacts on a detector), diffract like waves when their de Broglie wavelength is comparable to the spacing of the diffracting structure. The effect has since been confirmed for neutrons, atoms, and — in experiments beginning in the late 1990s — even large molecules: neutron diffraction is now a standard tool for probing crystal and magnetic structure (complementing X-ray diffraction, since neutrons, being uncharged, scatter primarily from nuclei rather than electron clouds), and a landmark 1999 experiment by Arndt, Zeilinger, and collaborators observed diffraction of $C_{60}$ "buckyball" molecules — each containing 60 carbon atoms, with a mass some $10^5$ times that of a single electron — through a microfabricated grating, with a measured de Broglie wavelength of only a few picometers, far smaller than the molecule itself, yet still large enough to produce a measurable diffraction pattern. Matter-wave interference is not a special property of electrons; it is a universal feature of quantum objects, observable whenever a system can be prepared with a de Broglie wavelength comparable to some accessible length scale. The same phenomenon is the operating principle of the electron microscope, whose resolution — set by the wavelength of the imaging "light," per ordinary diffraction limits ([Chapter 5](#ch-diffraction-of-light)) — can be far finer than any visible-light microscope because electron de Broglie wavelengths, as the worked example above shows, can be made far shorter than visible wavelengths simply by choosing a sufficiently large accelerating voltage.

### Neutron Interferometry

Because neutrons are electrically neutral, they can be split into two coherent beams and recombined using **neutron interferometers** built from a single, precisely machined crystal of silicon, without the beam-steering complications that an electron's charge would introduce in a magnetic or electric field. A landmark 1975 experiment by Colella, Overhauser, and Werner (the "COW experiment") used exactly this technique to observe a measurable phase shift between the two arms of a neutron interferometer when one arm was raised slightly in the Earth's gravitational field relative to the other — a direct demonstration that a quantum matter wave, not merely a mathematical bookkeeping device, is affected by gravity precisely as its de Broglie wavelength and the classical gravitational potential energy predict. Neutron interferometry has since been used to test the sign and magnitude of gravitational, and even rotational (Sagnac), phase shifts on matter waves with high precision, extending the reach of wave–particle duality from crystal diffraction to macroscopic-scale sensitivity to gravity itself.

### The Bohr Quantization Condition Revisited

The de Broglie hypothesis retroactively explains a feature of the 1913 Bohr model of the hydrogen atom (developed further in [Chapter 10](#ch-the-hydrogen-atom)) that Bohr himself had simply postulated without justification: that an orbiting electron's angular momentum is quantized in integer multiples of $\hbar$, $L = n\hbar$. If the electron in a circular orbit of radius $r$ is described by a de Broglie wave of wavelength $\lambda = h/p$, that wave can only form a consistent, single-valued standing pattern around the orbit if the orbit's circumference contains a whole number of wavelengths,

$$
2\pi r = n\lambda = \frac{nh}{p}, \qquad n = 1, 2, 3, \ldots,
$$

since otherwise the wave would interfere destructively with itself on successive trips around the loop and no stable pattern could persist. Rearranging, $pr = n\hbar$ — exactly Bohr's angular-momentum quantization condition, $L = n\hbar$, now derived (rather than assumed) from the requirement that an electron's matter wave close consistently on itself. This does not yet constitute a full theory (that requires the Schrödinger equation of Chapters [8](#ch-the-schrodinger-equation)–[9](#ch-quantum-mechanics-in-three-dimensions), applied to the hydrogen atom in [Chapter 10](#ch-the-hydrogen-atom)), but it shows that de Broglie's hypothesis was not an isolated curiosity: it directly explains why atomic angular momentum comes only in discrete multiples of $\hbar$, years before Schrödinger's wave equation made the connection rigorous.

Quantization by a closure condition is not a quantum idea, and it is easier to trust once it has been seen somewhere unmysterious. {numref}`Figure %s <fig:ch07-standing-wave-sim>` drives a column of air and sweeps the frequency: almost every frequency produces nothing, and at a discrete set of them the tube suddenly resonates, because only there does the wave returning from the far end arrive back in step with itself. Nothing is quantized about air. What is discrete is the set of wavelengths that a boundary condition permits — an integer count fitting into the available length — and de Broglie's contribution was to notice that an electron's wave going around an orbit is subject to a closure condition of exactly the same kind.

```{openphysics} StandingWaves
:screen: 3
:label: fig:ch07-standing-wave-sim

Standing waves in a pipe. Sweep the drive frequency and the response is a set of sharp resonances at which a whole number of half-wavelengths fits between the ends; between them, the returning wave arrives out of step and cancels itself. The Bohr condition $2\pi r = n\lambda$ is the same statement for a wave that closes on a loop instead of between two ends.
```

### Worked Example: Checking the Standing-Wave Condition for Hydrogen's Ground State

The Bohr model (developed further in [Chapter 10](#ch-the-hydrogen-atom)) gives the electron in hydrogen's $n=1$ orbit a radius $a_0 = 5.29\times10^{-11}\ \text{m}$ (the **Bohr radius**) and an orbital speed $v = 2.19\times10^6\ \text{m/s}$. Its de Broglie wavelength is

$$
\lambda = \frac{h}{m_ev} = \frac{6.626\times10^{-34}\ \text{J}\cdot\text{s}}{(9.11\times10^{-31}\ \text{kg})(2.19\times10^6\ \text{m/s})} = 3.32\times10^{-10}\ \text{m},
$$

while the orbit's circumference is $2\pi a_0 = 2\pi(5.29\times10^{-11}\ \text{m}) = 3.32\times10^{-10}\ \text{m}$ — the two agree to three significant figures, exactly confirming the standing-wave condition $2\pi r = n\lambda$ for $n=1$: the ground-state orbit's circumference is precisely one de Broglie wavelength.

## Wave–Particle Duality

The picture that emerges from Chapters [6](#ch-particle-properties-of-waves) and [7](#ch-wave-properties-of-particles) together is symmetric: light, ordinarily described as a wave, exhibits particle-like behavior (photoelectric effect, Compton scattering); matter, ordinarily described as particles, exhibits wave-like behavior (electron diffraction). Neither description is simply "wrong" and replaced by the other; rather, **both light and matter possess both wave and particle aspects**, and which aspect is manifest depends on the experiment performed. This is **wave–particle duality**, and its sharpest expression is Niels Bohr's **principle of complementarity**: the wave and particle descriptions are both necessary for a complete account of quantum behavior, both cannot be exhibited in full simultaneously by the same experimental arrangement, and neither alone is sufficient.

The double-slit experiment ([Chapter 4](#ch-interference-of-light)) makes this concrete. Even when electrons (or photons) are sent through the apparatus one at a time — far too infrequently for any two particles to interact or "interfere with each other" in transit — the individual, localized detection events recorded on a screen accumulate, after many particles, into the same interference fringe pattern predicted for a wave. Each particle arrives as a single, point-like click, exactly as a particle should; yet the *statistical distribution* of many such clicks builds up the wave-interference pattern, meaning each individual particle's behavior is governed by the same wave mathematics used for light, even though no two particles are present in the apparatus at once to "interfere" with each other in any classical sense. This experiment has been performed with electrons (originally by Claus Jönsson in 1961, and in a particularly clean single-particle-at-a-time form by Akira Tonomura and collaborators in 1989) and confirms the interference pattern exactly as quantum mechanics predicts.

That accumulation is the thing to watch, and it is what {numref}`Figure %s <fig:ch07-single-particle-sim>` reproduces. Fire particles one at a time and the screen records isolated, point-like hits in what looks at first like a random scatter; leave it running and the fringes emerge from the statistics of hits that were never anything but individual. The simulation also carries the which-path apparatus discussed next: a detector placed in the path of the wave function collapses it on each measurement, and the fringes go with it, while the individual hits go on looking exactly the same.

```{phet-legacy} quantum-wave-interference
:label: fig:ch07-single-particle-sim

Single particles sent through a double slit, one at a time, with the detection screen accumulating hits. The wave function is displayed alongside the record of impacts: one object, propagating as a wave and detected as a particle.
```

Crucially, if a measurement is added to the apparatus that determines *which* slit each particle actually passed through — "which-path" information — the interference pattern disappears entirely, replaced by the simple sum of the two single-slit patterns, exactly as if the particles were classical objects going through one slit or the other. Acquiring which-path information is not a matter of clumsy experimental technique that could, with sufficient care, be avoided while preserving the fringes; the loss of interference is a direct, unavoidable consequence of the uncertainty principle (developed later in this chapter), since determining which slit a particle used necessarily disturbs its momentum by an amount sufficient to wash out the fringe spacing. It is tempting, but incorrect, to imagine that a photon or electron is "really" a tiny wave packet that sometimes behaves like a particle, or "really" a tiny particle that sometimes behaves like a wave; the two descriptions are complementary, and a full account of quantum behavior (developed starting in [Chapter 8](#ch-the-schrodinger-equation)) requires a mathematical object — the wave function — that reduces to particle-like or wave-like predictions depending on what is measured, without being fully captured by either classical picture on its own.

### Delayed Choice and the Quantum Eraser

A particularly striking variant, proposed by John Wheeler in 1978 and since realized experimentally, asks whether the decision to measure which-path information can be postponed until *after* a particle has, in some naive classical sense, "already passed" through the slits. In a **delayed-choice experiment**, the choice of whether to record which-path information (destroying the interference pattern) or to erase it before the particle is detected (restoring the interference pattern) is made only at the very last possible moment — in some realizations, only after the particle has already traversed the region of the slits. Experiments of this kind confirm quantum mechanics' prediction exactly: interference reappears whenever which-path information is unavailable (or erased before it can be extracted) at the time of final detection, regardless of when in the experiment that choice is made. A related arrangement, the **quantum eraser**, first correlates each particle with a "marker" that could in principle reveal which path it took, then either reads that marker (destroying the interference pattern in the corresponding subset of detection events) or "erases" the marker's which-path information before it is read (restoring interference in that subset). Neither experiment allows sending a signal backward in time or violates causality; both instead show that the loss or restoration of interference tracks strictly whether which-path information is, at the moment of detection, available anywhere in the universe in principle — not whether a human experimenter has looked at it, and not whether the "choice" is made before or after the particle has traversed the apparatus. These results reinforce the same lesson as the ordinary double-slit experiment: a quantum system does not carry a hidden, predetermined trajectory waiting to be revealed, and complementarity is a statement about what information can coexist, not merely about the limits of measurement technology.

## Wave Packets

To describe a localized particle in wave language, a single wave of definite wavelength $\lambda = h/p$ — which by its nature extends infinitely in space with constant amplitude — is not adequate, since it corresponds to a perfectly definite momentum but gives no information about *where* the particle is. A localized particle is instead represented by a **wave packet**: a superposition of many waves of slightly different wavelength (equivalently, different wave number $k = 2\pi/\lambda$), chosen so that they interfere constructively in some limited region $\Delta x$ and destructively (cancel) elsewhere. The mathematics of superposition (the same mathematics used for beats and Fourier synthesis of waveforms) requires that a packet localized to a narrow spatial region $\Delta x$ necessarily be built from a *broad* range of wave numbers $\Delta k$, and vice versa; the two spreads are inversely related, roughly

$$
\Delta x\, \Delta k \gtrsim 1,
$$

The trade-off can be watched directly. {numref}`Figure %s <fig:ch07-wave-packet-sim>` builds a packet out of harmonic components whose amplitudes follow an adjustable envelope, and prints both widths as you work: narrow the spread $\sigma_k$ of contributing wave numbers and the packet in $x$ stretches out toward the infinite sinusoid of definite momentum; widen $\sigma_k$ and the packet contracts toward a spike, with the panel reporting $\sigma_x = 1/\sigma_k$ throughout. Switching the display from a function of space to a function of time turns the same relation into the energy–time form used later in this section.

```{phet} fourier-making-waves
:sim-name: Fourier: Making Waves
:screen: 3
:label: fig:ch07-wave-packet-sim

A wave packet and the Fourier components that build it, with the width in $k$ and the width in $x$ both displayed. Their product cannot be reduced: this is the classical wave theorem that becomes the uncertainty principle once $p = \hbar k$ is imposed.
```

a purely mathematical fact about waves, true for sound pulses and water-wave packets just as much as for matter waves, with no quantum content yet. Quantum mechanics enters when this relation is combined with the de Broglie relation $p = hk/2\pi = \hbar k$ (where $\hbar \equiv h/2\pi$), converting spread in wave number into spread in momentum, $\Delta p = \hbar\,\Delta k$, and giving

$$
\Delta x\,\Delta p \gtrsim \hbar.
$$

### Phase Velocity and Group Velocity

A wave packet built from components of angular frequency $\omega(k)$ spread over a narrow range of $k$ can be shown, by adding two nearby component waves $\cos(kx-\omega t)$ and $\cos[(k+\Delta k)x - (\omega+\Delta \omega)t]$, to have an overall envelope that moves at the **group velocity**

$$
v_g = \frac{d\omega}{dk},
$$

which is, in general, different from the **phase velocity** $v_p = \omega/k$ at which the individual wave crests inside the envelope move. For a nonrelativistic free particle, the de Broglie relations $p = \hbar k$ and $E = \hbar\omega$, combined with the nonrelativistic kinetic-energy relation $E = p^2/2m$, give

$$
\omega(k) = \frac{\hbar k^2}{2m},
$$ (eq:ch07-dispersion)

so that

$$
v_g = \frac{d\omega}{dk} = \frac{\hbar k}{m} = \frac{p}{m} = u,
$$

exactly the classical particle velocity — the wave packet's envelope, the physically observable, localized "blob" of probability, moves at precisely the speed a classical particle with the same momentum would have. The phase velocity, by contrast, is $v_p = \omega/k = \hbar k/2m = u/2$, exactly *half* the particle's actual speed: the individual crests inside the packet move at a different, less physically meaningful speed than the envelope itself, a reminder that it is the group velocity, not the phase velocity, that corresponds to the motion of the particle (and, for a light pulse in a dispersive medium, to the speed at which energy and information actually travel).

### Wave Packet Spreading

The nonrelativistic dispersion relation in Equation {eq}`eq:ch07-dispersion` is not linear in $k$ (unlike the dispersion relation $\omega = ck$ for light in vacuum), which has a further consequence beyond fixing the group velocity: different Fourier components of a wave packet, corresponding to different momenta, travel at slightly different group velocities $v_g(k) = \hbar k/m$, since a component with larger $k$ (larger momentum) simply moves faster. A packet initially localized to a narrow width $\Delta x_0$ therefore does not maintain its shape as it propagates; because it necessarily contains a spread $\Delta k \sim 1/\Delta x_0$ of wave numbers (the same uncertainty relation used earlier in this section), and each component travels at a slightly different speed, the packet's spatial width grows with time — it **spreads**. A careful calculation shows the spreading time scale is of order $\tau \sim m(\Delta x_0)^2/\hbar$: a light particle (small $m$) confined to a very small initial region (small $\Delta x_0$) spreads apart quickly, while a macroscopic object's wave packet spreads on a time scale so astronomically long that the effect is entirely unobservable — one more reason, alongside the negligible de Broglie wavelength itself, that ordinary macroscopic objects appear to follow sharp, well-defined classical trajectories rather than visibly diffusing.

## The Heisenberg Uncertainty Principle

Werner Heisenberg (1927) elevated the wave-packet relation above to a fundamental principle governing all quantum systems, stated precisely as

$$
\Delta x\, \Delta p_x \geq \frac{\hbar}{2},
$$

where $\Delta x$ and $\Delta p_x$ are, more precisely, statistical spreads (standard deviations) in simultaneous measurements of position and momentum made on identically prepared systems. The **Heisenberg uncertainty principle** states that these two spreads cannot both be made arbitrarily small: the more precisely a particle's position is known, the less precisely its momentum can be known, and conversely. This is not a statement about the clumsiness of measuring instruments, correctable in principle by better technology — it is a consequence of the wave nature of matter itself, as the wave-packet argument above shows: a particle simply *does not possess* simultaneously well-defined position and momentum, in the same sense that a wave pulse of well-defined wavelength cannot also be localized to a point.

An analogous relation holds between energy and time,

$$
\Delta E\, \Delta t \geq \frac{\hbar}{2},
$$

where $\Delta t$ characterizes the time available to measure (or the lifetime of a state with) energy spread $\Delta E$. This relation, for instance, explains why an unstable state with a short lifetime $\Delta t$ (such as an excited atomic state, or an unstable particle) necessarily has an intrinsic spread, or "width," in its energy — and correspondingly in the frequency/wavelength of radiation it emits — that grows as its lifetime shrinks.

Stripped of $\hbar$, this is a theorem about signals rather than about quantum mechanics, and it applies to any wave one cares to measure — including the sound of one's own voice. {numref}`Figure %s <fig:ch07-bandwidth-sim>` runs a live spectrum of whatever the microphone hears: a sustained vowel, going on for a long $\Delta t$, resolves into sharp harmonic lines with small $\Delta f$, while a clipped consonant lasting a few milliseconds has no sharp lines at all, only a broad smear across the spectrum. No better microphone would fix this. A short signal does not *have* a well-defined frequency, exactly as a short-lived excited state does not have a well-defined energy.

```{openphysics} WaveComposer
:label: fig:ch07-bandwidth-sim

Real-time spectrum analysis of a microphone signal. The duration of a sound and the sharpness of its spectrum trade off against each other, which is $\Delta E\,\Delta t \gtrsim \hbar/2$ with the $\hbar$ removed and the quantum mechanics along with it.
```

### Worked Example: Confining an Electron in a Nucleus

Could an electron exist bound inside an atomic nucleus, of radius $r \sim 5\times 10^{-15}\ \text{m}$? If so, the position uncertainty could be no larger than $\Delta x \sim r$, and the uncertainty principle then requires a momentum uncertainty of at least

$$
\Delta p \gtrsim \frac{\hbar}{2\,\Delta x} \approx \frac{1.055\times10^{-34}\ \text{J}\cdot\text{s}}{2(5\times10^{-15}\ \text{m})} \approx 1.1\times10^{-20}\ \text{kg}\cdot\text{m/s}.
$$

Converting to an energy via the (relativistic, since this momentum turns out to be large) relation $E \approx pc$ for $pc \gg mc^2$: $pc \approx (1.1\times10^{-20}\ \text{kg}\cdot\text{m/s})(3.0\times10^8\ \text{m/s}) \approx 3.3\times10^{-12}\ \text{J} \approx 21\ \text{MeV}$. An electron confined to nuclear dimensions would need kinetic energy of tens of MeV — far larger than the few-MeV binding energies available in nuclei ([Chapter 13](#ch-nuclear-physics)) — so such an electron could not remain bound; this is one of the historical arguments (alongside others involving nuclear spin and magnetic moment) that electrons are not constituents of the nucleus, correctly anticipating that beta decay ([Chapter 13](#ch-nuclear-physics)) must *create* an electron at the moment of decay rather than releasing one that was previously confined inside.

### Worked Example: The Scale of Atomic Energies

The uncertainty principle also correctly predicts the *order of magnitude* of atomic binding energies, without needing to solve the Schrödinger equation at all. An electron confined to an atom of radius $r \sim a_0 = 5.3\times10^{-11}\ \text{m}$ (the Bohr radius, derived properly in [Chapter 10](#ch-the-hydrogen-atom)) has, by the same reasoning as above, a minimum momentum uncertainty

$$
\Delta p \gtrsim \frac{\hbar}{2\,\Delta x} \approx \frac{1.055\times10^{-34}\ \text{J}\cdot\text{s}}{2(5.3\times10^{-11}\ \text{m})} \approx 1.0\times10^{-24}\ \text{kg}\cdot\text{m/s}.
$$

Since this is small enough that the electron remains nonrelativistic, its kinetic energy is $K \sim (\Delta p)^2/2m_e \approx (1.0\times10^{-24}\ \text{kg}\cdot\text{m/s})^2/[2(9.11\times10^{-31}\ \text{kg})] \approx 5.5\times10^{-19}\ \text{J} \approx 3.4\ \text{eV}$ — the right order of magnitude for atomic binding and ionization energies (a few to a few tens of eV), even though the precise numerical value requires the full machinery of Chapters [9](#ch-quantum-mechanics-in-three-dimensions)–[10](#ch-the-hydrogen-atom). This is a recurring pattern in quantum mechanics: the uncertainty principle alone, applied as an order-of-magnitude estimate, correctly anticipates the characteristic energy scale of a confined system, well before an exact calculation is carried out.

## Summary

- The **de Broglie hypothesis** assigns every particle of momentum $p$ a wavelength $\lambda = h/p$, extending the photon relation of [Chapter 6](#ch-particle-properties-of-waves) to all matter, and for an electron accelerated through voltage $V$ gives $\lambda \approx 1.226\ \text{nm}/\sqrt{V[\text{volts}]}$.
- Requiring an electron's de Broglie wave to form a consistent standing pattern around a circular orbit, $2\pi r = n\lambda$, reproduces the Bohr model's angular-momentum quantization $L = n\hbar$, previously an unexplained postulate.
- The **Davisson–Germer** and **G. P. Thomson** experiments confirmed matter waves directly: electrons diffract from a crystal lattice with a wavelength matching $\lambda = h/p$, exactly as X-rays do; matter-wave interference has since been observed for neutrons, atoms, and large molecules such as $C_{60}$.
- **Wave–particle duality** and Bohr's **complementarity principle**: light and matter both show wave and particle behavior; which is manifest depends on the experiment (as the single-particle double-slit experiment and the loss of fringes upon acquiring which-path information both show), and neither classical picture alone is complete.
- A localized particle is represented by a **wave packet**, a superposition of waves over a range of wave numbers $\Delta k$; its envelope moves at the **group velocity** $v_g = d\omega/dk$, which equals the particle's classical velocity, distinct from the **phase velocity** $v_p = \omega/k$ of the individual wave crests.
- The **Heisenberg uncertainty principle**, $\Delta x\,\Delta p_x \geq \hbar/2$ (and analogously $\Delta E\,\Delta t \geq \hbar/2$), is a fundamental limit on the simultaneous precision of conjugate quantities, rooted in the wave nature of matter, not a limitation of measuring instruments, and correctly predicts the order of magnitude of confinement energies from nuclear to atomic scales.

## Problems

:::{exercise}
:label: ex-wave-properties-of-particles-1

Find the de Broglie wavelength of (a) an electron with kinetic energy $54\ \text{eV}$ (as in the original Davisson–Germer experiment), (b) a proton with kinetic energy $1.0\ \text{MeV}$, and (c) a $0.145\ \text{kg}$ baseball moving at $40\ \text{m/s}$. Comment on which of these wavelengths could plausibly produce observable diffraction, and from what kind of structure.
:::

:::{solution} ex-wave-properties-of-particles-1
:label: sol-wave-properties-of-particles-1
:class: dropdown

For nonrelativistic particles, $\lambda=h/\sqrt{2mK}$.  For $54\ \text{eV}$ electrons, $\lambda=1.226/\sqrt{54}=0.167\ \text{nm}$.  For a $1.0\ \text{MeV}$ proton, $\lambda=2.86\times10^{-14}\ \text{m}=0.0286\ \text{pm}$.  For the baseball,

$$\lambda=\frac{6.626\times10^{-34}\ \text{J s}}{(0.145\ \text{kg})(40\ \text{m/s})}=1.14\times10^{-34}\ \text{m}.$$

Therefore, electron waves can diffract from atomic crystal planes, proton waves need nuclear-scale structure, and the baseball wavelength is far too small to observe diffraction.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-2

In the Davisson–Germer experiment, a diffraction maximum for 54 eV electrons was observed at $\theta = 50°$ from a nickel crystal. Using $\lambda = h/p$ for the electrons' de Broglie wavelength and the diffraction condition $d\sin\theta = \lambda$ (first order, $n=1$), find the effective interplanar spacing $d$ of the nickel crystal consistent with this observation.
:::

:::{solution} ex-wave-properties-of-particles-2
:label: sol-wave-properties-of-particles-2
:class: dropdown

The $54\ \text{eV}$ electron wavelength from Problem 1 is $0.167\ \text{nm}$.  First-order diffraction gives

$$d=\frac{\lambda}{\sin50^\circ}=\frac{0.167\ \text{nm}}{0.766}=0.218\ \text{nm}.$$

Therefore, the observed Davisson--Germer maximum corresponds to an effective nickel-plane spacing of $0.218\ \text{nm}$.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-3

Using the worked-example formula $\lambda \approx 1.226\ \text{nm}/\sqrt{V[\text{volts}]}$, find the accelerating voltage needed to give electrons a de Broglie wavelength of exactly $0.0500\ \text{nm}$, comparable to a typical X-ray wavelength used in crystallography.
:::

:::{solution} ex-wave-properties-of-particles-3
:label: sol-wave-properties-of-particles-3
:class: dropdown

From $\lambda=1.226\ \text{nm}/\sqrt{V}$,

$$V=\left(\frac{1.226\ \text{nm}}{0.0500\ \text{nm}}\right)^2=6.01\times10^2\ \text{V}.$$

Therefore, electrons require an accelerating voltage of about $601\ \text{V}$ to have a $0.0500\ \text{nm}$ de Broglie wavelength.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-4

A beam of thermal neutrons (kinetic energy $\approx k_BT$ at room temperature, $T \approx 300\ \text{K}$) is used for neutron diffraction studies of crystal structure. (a) Estimate the neutrons' typical kinetic energy in eV. (b) Find their de Broglie wavelength, given the neutron mass $m_n = 1.675\times10^{-27}\ \text{kg}$, and compare it to typical interatomic spacings.
:::

:::{solution} ex-wave-properties-of-particles-4
:label: sol-wave-properties-of-particles-4
:class: dropdown

The thermal energy is $K\sim k_BT=(1.381\times10^{-23}\ \text{J/K})(300\ \text{K})=4.14\times10^{-21}\ \text{J}=0.0259\ \text{eV}$.  Then

$$\lambda=\frac{h}{\sqrt{2m_nK}}=\frac{6.626\times10^{-34}}{\sqrt{2(1.675\times10^{-27})(4.14\times10^{-21})}}=1.78\times10^{-10}\ \text{m}=0.178\ \text{nm}.$$

Therefore, room-temperature neutrons have about $0.026\ \text{eV}$ energy and $0.18\ \text{nm}$ wavelength, comparable to interatomic spacings and ideal for crystal diffraction.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-5

Verify the claim in the text that a $C_{60}$ molecule (mass $\approx 1.2\times10^{-24}\ \text{kg}$) moving at a typical thermal beam speed of $200\ \text{m/s}$ has a de Broglie wavelength of a few picometers, and comment on why such a short wavelength, far smaller than the molecule's own diameter ($\approx 1\ \text{nm}$), can nonetheless produce an observable diffraction pattern from a grating with a period of order $100\ \text{nm}$.
:::

:::{solution} ex-wave-properties-of-particles-5
:label: sol-wave-properties-of-particles-5
:class: dropdown

The molecular momentum is $p=mv=(1.2\times10^{-24}\ \text{kg})(200\ \text{m/s})=2.4\times10^{-22}\ \text{kg m/s}$.  Thus

$$\lambda=\frac hp=\frac{6.626\times10^{-34}}{2.4\times10^{-22}}=2.76\times10^{-12}\ \text{m}=2.76\ \text{pm}.$$

The grating period is much larger than this wavelength, but diffraction angles can still be measured and the molecule's center-of-mass wave can interfere.  Therefore, $C_{60}$ has a few-picometer de Broglie wavelength and can diffract from a nanostructured grating despite being physically larger than its wavelength.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-6

Using the de Broglie standing-wave argument, show that an electron in a circular Bohr orbit with $n=1$ has an orbital circumference equal to exactly one de Broglie wavelength, and explain qualitatively (without calculation) why this is consistent with such an orbit being the atom's lowest-energy (ground) state.
:::

:::{solution} ex-wave-properties-of-particles-6
:label: sol-wave-properties-of-particles-6
:class: dropdown

The standing-wave condition is $2\pi r=n\lambda$.  For $n=1$, $2\pi r=\lambda$: exactly one de Broglie wavelength fits around the orbit.  A shorter circumference would not close in phase, and the one-wavelength state has the smallest allowed momentum and kinetic energy.  Therefore, the Bohr ground orbit corresponds to the lowest closed standing matter wave.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-7

A proton is confined to a nucleus of diameter $1.0\times10^{-14}\ \text{m}$. Use the uncertainty principle to estimate the minimum kinetic energy the proton must have, and compare it (order of magnitude) to typical nuclear binding energies of several MeV per nucleon ([Chapter 13](#ch-nuclear-physics)).
:::

:::{solution} ex-wave-properties-of-particles-7
:label: sol-wave-properties-of-particles-7
:class: dropdown

Taking $\Delta x\sim10^{-14}\ \text{m}$ gives $\Delta p\sim h/\Delta x=6.63\times10^{-20}\ \text{kg m/s}$.  The minimum kinetic energy is

$$K\sim\frac{(\Delta p)^2}{2m_p}=\frac{(6.63\times10^{-20})^2}{2(1.673\times10^{-27})}=1.31\times10^{-12}\ \text{J}=8.2\ \text{MeV}.$$

Therefore, nuclear confinement requires proton kinetic energies of order several MeV, comparable to nuclear binding energies.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-8

An excited atomic state has a mean lifetime of $\Delta t = 1.0\times10^{-8}\ \text{s}$. (a) Use the energy–time uncertainty relation to estimate the minimum energy spread $\Delta E$ of this state, in eV. (b) If the state decays by emitting a photon of wavelength $500\ \text{nm}$, estimate the corresponding spread (linewidth) $\Delta\lambda$ in the emitted wavelength.
:::

:::{solution} ex-wave-properties-of-particles-8
:label: sol-wave-properties-of-particles-8
:class: dropdown

The energy--time uncertainty estimate is

$$\Delta E\sim\frac{\hbar}{2\Delta t}=\frac{1.055\times10^{-34}\ \text{J s}}{2(1.0\times10^{-8}\ \text{s})}=5.28\times10^{-27}\ \text{J}=3.29\times10^{-8}\ \text{eV}.$$

Since $E=hc/\lambda$, $|\Delta\lambda|\simeq\lambda^2\Delta E/(hc)$, giving $\Delta\lambda=(500\ \text{nm})^2(3.29\times10^{-8}\ \text{eV})/(1240\ \text{eV nm})=6.6\times10^{-6}\ \text{nm}$.  Therefore, the lifetime implies a minimum width of about $3.3\times10^{-8}\ \text{eV}$ or $6.6\times10^{-6}\ \text{nm}$.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-9

A beam of electrons is passed through a single slit of width $a$. Using the single-slit diffraction condition (first minimum at $\sin\theta \approx \lambda/a$ for small angles) together with the de Broglie relation, express the transverse momentum spread $\Delta p_y$ imparted to the electrons (estimated from $p\sin\theta$) in terms of the slit width $a$, and show that $\Delta y\,\Delta p_y \sim h$ if $\Delta y \sim a$, consistent with the uncertainty principle.
:::

:::{solution} ex-wave-properties-of-particles-9
:label: sol-wave-properties-of-particles-9
:class: dropdown

At the first minimum, $\sin\theta\simeq\lambda/a$.  Thus

$$\Delta p_y\sim p\sin\theta=\frac h\lambda\frac\lambda a=\frac ha.$$

With $\Delta y\sim a$, $\Delta y\Delta p_y\sim a(h/a)=h$.  Therefore, single-slit diffraction gives the same position--momentum uncertainty scale required by the uncertainty principle.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-10

Explain, using the energy–time uncertainty relation, why a particle that is truly stable (infinite lifetime) can have a perfectly sharp rest energy $mc^2$, while an unstable particle cannot — and why particle physicists therefore quote both a mass and a "width" (in energy units) for unstable particles, a topic revisited in [Chapter 14](#ch-elementary-particles-and-the-standard-model).
:::

:::{solution} ex-wave-properties-of-particles-10
:label: sol-wave-properties-of-particles-10
:class: dropdown

For an infinite lifetime, $\Delta t\to\infty$, so the uncertainty lower bound $\Delta E\gtrsim\hbar/(2\Delta t)$ tends to zero.  An unstable state has finite lifetime and therefore nonzero energy width.  Therefore, stable particles can have sharp rest energies, while unstable particles must be described by both a central mass and a finite decay width.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-11

Verify the group-velocity calculation in the text: starting from $\omega(k) = \hbar k^2/2m$ (the nonrelativistic free-particle dispersion relation), compute $d\omega/dk$ explicitly and confirm that it equals $\hbar k/m = p/m$.
:::

:::{solution} ex-wave-properties-of-particles-11
:label: sol-wave-properties-of-particles-11
:class: dropdown

Differentiate directly:

$$v_g=\frac{d\omega}{dk}=\frac{d}{dk}\left(\frac{\hbar k^2}{2m}\right)=\frac{2\hbar k}{2m}=\frac{\hbar k}{m}=\frac pm.$$

Therefore, the nonrelativistic matter-wave group velocity equals the particle velocity.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-12

A relativistic free particle has energy $E = \sqrt{(pc)^2+(mc^2)^2}$ ([Chapter 3](#ch-relativistic-dynamics)). Using $E = \hbar\omega$ and $p = \hbar k$, show that the group velocity $v_g = d\omega/dk$ equals $pc^2/E$, and confirm that this reduces to the particle's actual (relativistic) velocity $u$ using the relation $u = pc^2/E$ established in [Chapter 3](#ch-relativistic-dynamics).
:::

:::{solution} ex-wave-properties-of-particles-12
:label: sol-wave-properties-of-particles-12
:class: dropdown

With $E=\hbar\omega$ and $p=\hbar k$,

$$v_g=\frac{d\omega}{dk}=\frac{dE}{dp}=\frac{d}{dp}\sqrt{p^2c^2+m^2c^4}=\frac{pc^2}{E}.$$

The relativistic momentum and energy relations give the same identity $u=pc^2/E$.  Therefore, the group velocity of a relativistic matter wave is exactly the particle's physical velocity $u$.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-13

Estimate, using the uncertainty principle in the same manner as the atomic-scale worked example, the characteristic kinetic energy of an electron confined to a quantum dot (a nanoscale semiconductor structure) of diameter $10\ \text{nm}$, and compare it in order of magnitude to the atomic-scale estimate found in the text.
:::

:::{solution} ex-wave-properties-of-particles-13
:label: sol-wave-properties-of-particles-13
:class: dropdown

For confinement to $L=10\ \text{nm}=10^{-8}\ \text{m}$, take $p\sim h/L$.  Then

$$K\sim\frac{h^2}{2m_eL^2}=\frac{(6.626\times10^{-34})^2}{2(9.109\times10^{-31})(10^{-8})^2}=2.41\times10^{-21}\ \text{J}=0.015\ \text{eV}.$$

An atom-scale $0.1\ \text{nm}$ confinement is $10^2$ smaller in length and therefore $10^4$ larger in energy.  Therefore, a $10\ \text{nm}$ quantum dot has a characteristic confinement energy of order $10^{-2}\ \text{eV}$, far below atomic-scale energies.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-14

A double-slit experiment is performed with electrons at a rate of one electron at a time, with a detector placed at one slit to determine which slit each electron passes through. (a) Explain, in terms of the uncertainty principle, why this which-path measurement necessarily disturbs the electron's momentum. (b) Estimate the momentum disturbance needed to determine, to within the slit width $a$, which of two slits separated by distance $d$ an electron passed through, and explain qualitatively why a disturbance of this size is enough to wash out an interference pattern with fringe spacing set by $d$.
:::

:::{solution} ex-wave-properties-of-particles-14
:label: sol-wave-properties-of-particles-14
:class: dropdown

Determining a slit position to uncertainty $\Delta y\sim a$ necessarily gives a transverse momentum disturbance $\Delta p_y\gtrsim\hbar/(2a)$ (of order $h/a$).  This random transverse kick changes the relative phase between paths; when its associated angular spread is comparable with the interference angle $\lambda/d$, the fringe correlation is lost.  Therefore, a sufficiently precise which-path measurement necessarily supplies enough momentum uncertainty to wash out the two-slit interference pattern.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-15

Explain why the phase velocity $v_p = \omega/k$ of a nonrelativistic free-particle matter wave, found in the text to be $u/2$, is not the speed of anything physically observable (in contrast with the group velocity), and why this is not a paradox.
:::

:::{solution} ex-wave-properties-of-particles-15
:label: sol-wave-properties-of-particles-15
:class: dropdown

For a nonrelativistic free particle, phase velocity is $v_p=\omega/k=(\hbar k/2m)=u/2$, while the wave packet and all information move at $v_g=d\omega/dk=u$.  Individual phase crests are not localized objects and cannot carry a signal.  Therefore, the phase velocity is not an observable propagation speed, so its difference from the group velocity is not paradoxical.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-16

Using the spreading time scale $\tau \sim m(\Delta x_0)^2/\hbar$ quoted in the text, estimate $\tau$ for (a) an electron initially localized to $\Delta x_0 = 1.0\times10^{-10}\ \text{m}$ (roughly an atomic diameter), and (b) a $1.0\ \text{mg}$ dust grain initially localized to $\Delta x_0 = 1.0\times10^{-6}\ \text{m}$. Comment on which of these spreading times could plausibly be observed in a laboratory measurement lasting a few seconds.
:::

:::{solution} ex-wave-properties-of-particles-16
:label: sol-wave-properties-of-particles-16
:class: dropdown

For the electron,

$$\tau\sim\frac{m(\Delta x_0)^2}{\hbar}=\frac{(9.109\times10^{-31}\ \text{kg})(10^{-10}\ \text{m})^2}{1.055\times10^{-34}\ \text{J s}}=8.6\times10^{-17}\ \text{s}.$$

For the dust grain, $\tau=(10^{-6}\ \text{kg})(10^{-6}\ \text{m})^2/\hbar=9.5\times10^{15}\ \text{s}\approx3\times10^8\ \text{yr}$.  Therefore, electron spreading is extremely rapid, whereas dust-grain spreading is unobservable during a seconds-long laboratory measurement.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-17

In a delayed-choice or quantum-eraser experiment, explain why the disappearance and reappearance of the interference pattern cannot be used to send information backward in time, even though the "choice" of whether which-path information is available may be made after the particle has passed through the slit region. (Hint: consider what an experimenter examining only the particles that land in a single, fixed detector region can and cannot know without also consulting the marker/eraser results.)
:::

:::{solution} ex-wave-properties-of-particles-17
:label: sol-wave-properties-of-particles-17
:class: dropdown

Without consulting the marker result, detections in any one output channel form an ordinary interference-free mixture; no observer can tell whether a later eraser choice was made.  Interference reappears only after sorting the already-recorded events into correlated subensembles using classical information from the marker/eraser measurement.  Therefore, quantum erasure changes conditional correlations, not past detection outcomes, and cannot transmit information backward in time.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-18

A beam of electrons, each with the same de Broglie wavelength $\lambda = h/p$, is used in a Davisson–Germer-type experiment. Explain, using the standing-wave condition of the "Bohr Quantization Condition Revisited" subsection as an analogy, why a diffraction condition $d\sin\theta = n\lambda$ (rather than an arbitrary relation between $\theta$ and $\lambda$) is required for a diffraction maximum, drawing the parallel between constructive interference around a crystal lattice and constructive interference around a closed atomic orbit.
:::

:::{solution} ex-wave-properties-of-particles-18
:label: sol-wave-properties-of-particles-18
:class: dropdown

Waves from successive crystal planes differ in path by $d\sin\theta$.  They reinforce only when this difference is an integer number of wavelengths, $d\sin\theta=n\lambda$; otherwise their phases cancel in the sum.  This is directly analogous to an atomic orbit, where a matter wave survives only when its circumference contains an integer number of wavelengths.  Therefore, a diffraction maximum is a standing-wave condition imposed across the periodic crystal lattice.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-19

Verify the claim in the "Consistency Check" subsection that $E=pc^2/u$ for a relativistic particle, using $E=\gamma mc^2$ and $p=\gamma mu$ from [Chapter 3](#ch-relativistic-dynamics), and show that combining this with $E=hf$ and $\lambda = u_p/f$ (with $u_p$ the wave's phase velocity) gives a phase velocity $u_p = c^2/u$ greater than $c$ — then explain why this superluminal *phase* velocity does not violate relativity, referring to your answer to Problem 15 about which velocity is physically observable.
:::

:::{solution} ex-wave-properties-of-particles-19
:label: sol-wave-properties-of-particles-19
:class: dropdown

From $E=\gamma mc^2$ and $p=\gamma mu$,

$$\frac{pc^2}{u}=\frac{(\gamma mu)c^2}{u}=\gamma mc^2=E.$$

Combining $E=hf$ with $\lambda=u_p/f$ gives $E=hu_p/\lambda=pu_p$, so $u_p=E/p=c^2/u$.  This can exceed $c$ because phase velocity carries neither a particle nor usable information; the group velocity remains $u<c$.  Therefore, superluminal phase velocity does not violate relativity.
:::

:::{exercise}
:label: ex-wave-properties-of-particles-20

The neutron interferometry (COW) experiment detects a gravitationally induced phase shift between two paths of different height $\Delta h$ in a neutron interferometer of horizontal path length $L$. Explain qualitatively, using the de Broglie relation $\lambda = h/p$ and the fact that a neutron's kinetic energy (and hence its momentum and wavelength) changes very slightly with height in a gravitational field, why raising one arm of the interferometer changes the phase accumulated along that arm relative to the other.
:::

:::{solution} ex-wave-properties-of-particles-20
:label: sol-wave-properties-of-particles-20
:class: dropdown

Raising a neutron increases its gravitational potential energy and decreases its kinetic energy by the same small amount.  Its momentum therefore decreases and its de Broglie wavelength $\lambda=h/p$ increases slightly; over a finite path this changes the accumulated phase $2\pi L/\lambda$.  Therefore, paths at different heights acquire a measurable relative gravitational phase shift even though the energy change is very small.
:::
