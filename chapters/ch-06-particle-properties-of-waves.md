---
title: Particle Properties of Waves
short_title: Chapter 6. Particle Properties of Waves
label: ch-particle-properties-of-waves
numbering:
  enumerator: "6.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain the ultraviolet catastrophe and how Planck's quantization hypothesis resolves it.
- State and apply Planck's radiation law, Wien's displacement law, and the Stefan–Boltzmann law.
- Describe the photoelectric effect and explain why classical (wave) theory fails to account for its observed features.
- Apply Einstein's photon model, $E = hf$, to the photoelectric effect and interpret the stopping-potential and work-function data it predicts.
- Explain X-ray production (bremsstrahlung) as, in effect, the inverse of the photoelectric effect, and apply the Duane–Hunt relation for the minimum X-ray wavelength.
- Derive and apply the Compton scattering formula, and explain why Compton scattering demonstrates that photons carry momentum.
- Explain pair production and pair annihilation as further evidence for the particle nature of light, and use conservation of energy and momentum to find threshold conditions for each.

## Introduction

Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) dismantled the ether and rebuilt kinematics and dynamics on Einstein's postulates, but light itself — a wave, according to Maxwell's equations, which special relativity leaves intact — remained conceptually untouched. Chapters [4](#ch-interference-of-light)–[5](#ch-diffraction-of-light) then developed that wave picture in full quantitative detail: interference and diffraction, both direct, precise confirmations that light obeys a wave equation. This chapter takes up a second, independent crisis of classical physics, one concerning not the *kinematics* of light but its very *nature*. Four phenomena — blackbody radiation, the photoelectric effect, X-ray production, and Compton scattering — each show, in a different experimental setting, that electromagnetic radiation exchanges energy with matter not continuously, as a wave should, but in discrete packets. The concept that emerges, the **photon**, carries energy $E = hf$ and momentum $p = h/\lambda$, and behaves in each of these experiments like a particle, even though light indisputably also shows the wave behavior of Chapters [4](#ch-interference-of-light)–[5](#ch-diffraction-of-light) in other settings. A final phenomenon, pair production, shows that a photon's energy can be converted entirely into matter, tying the particle nature of light directly to the mass–energy equivalence of [Chapter 3](#ch-relativistic-dynamics). Reconciling these two faces of light is the beginning of quantum mechanics.

## Blackbody Radiation and Planck's Hypothesis

Any object at temperature $T$ emits electromagnetic radiation across a continuous range of wavelengths, with an intensity distribution depending on $T$. An idealized perfect absorber and emitter is called a **blackbody**; its emitted spectral distribution, the blackbody spectrum, depends only on temperature, not on the material. A good laboratory approximation is a small hole in the wall of an otherwise closed, heated cavity: radiation entering the hole is absorbed and re-emitted many times by the cavity walls before any of it can escape, so the radiation leaking out through the hole is, to excellent approximation, in thermal equilibrium with the cavity walls and independent of what the walls are made of.

### The Ultraviolet Catastrophe

Late-nineteenth-century classical physics attempted to compute this spectrum by treating the electromagnetic field inside the cavity as a superposition of standing-wave modes, each behaving as an independent harmonic oscillator, and invoking the equipartition theorem — every such oscillator, in thermal equilibrium at temperature $T$, should carry average energy $k_BT$, independent of its frequency. Counting the number of standing-wave modes per unit volume in a wavelength interval $d\lambda$ (a purely geometric problem, fixed by the cavity's size) and multiplying by $k_BT$ per mode gives the **Rayleigh–Jeans law**,

$$
u(\lambda,T) = \frac{8\pi k_BT}{\lambda^4},
$$

for the spectral energy density. This matches the observed spectrum reasonably well at long wavelength, but diverges as $\lambda \to 0$: since the number of short-wavelength modes grows without bound and each is assigned the same energy $k_BT$, the predicted radiated energy — obtained by integrating $u(\lambda,T)$ over all $\lambda$ — is *infinite*. This absurd prediction, sharply contradicted by the observed spectrum (which rises from zero at short wavelength, peaks, and falls off at long wavelength), became known as the **ultraviolet catastrophe**: not a small discrepancy to be patched, but a qualitative failure of classical statistical mechanics applied to the electromagnetic field.

{numref}`Figure %s <fig:ch06-blackbody-sim>` plots both curves against each other. Raising the
temperature moves the peak and lifts the total area, as the next section's
displacement and Stefan–Boltzmann laws require; the classical curve, plotted
alongside, runs off the top of the graph at short wavelength no matter what
temperature is chosen.

```{phet} blackbody-spectrum
:label: fig:ch06-blackbody-sim

The blackbody spectrum as a function of temperature, with the Rayleigh–Jeans
prediction available for comparison. The gap between the two at short wavelength
is the ultraviolet catastrophe.
```

### Planck's Quantization Hypothesis

Max Planck resolved this in 1900 by a hypothesis with no classical justification: the oscillators making up the cavity walls cannot exchange energy with the field continuously, but only in discrete multiples of a fundamental quantum,

$$
E_n = nhf, \qquad n = 0, 1, 2, \ldots,
$$

where $f$ is the oscillator's frequency and $h$ is a new fundamental constant (**Planck's constant**), $h = 6.626\times 10^{-34}\ \text{J}\cdot\text{s}$. With this assumption, the average energy of a mode at frequency $f$ in thermal equilibrium at temperature $T$ is not $k_BT$ (the equipartition value, independent of $f$, which causes the catastrophe) but

$$
\langle E \rangle = \frac{hf}{e^{hf/k_BT} - 1},
$$

which suppresses high-frequency (short-wavelength) modes because at high $f$, $hf \gg k_BT$ makes a single quantum too "expensive" to be thermally excited: the Boltzmann factor $e^{-hf/k_BT}$ governing how likely a mode is to hold even one quantum falls off exponentially, cutting off the ultraviolet divergence entirely. This leads to **Planck's radiation law** for the spectral radiance,

$$
u(\lambda, T) = \frac{8\pi hc}{\lambda^5}\, \frac{1}{e^{hc/\lambda k_B T} - 1},
$$

which matches the observed blackbody spectrum at all wavelengths and temperatures, and reduces to the Rayleigh–Jeans law in the limit $hf \ll k_BT$, i.e. at long wavelength, where $e^{hf/k_BT}-1 \approx hf/k_BT$ and quantization effects become negligible — exactly the regime in which the classical calculation had already succeeded. Planck himself regarded the quantization of oscillator energy as a mathematical device rather than a physical claim about light. It was Einstein who, five years later, proposed taking it literally.

### Wien's Displacement Law and the Stefan–Boltzmann Law

Differentiating $u(\lambda,T)$ with respect to $\lambda$ and setting the result to zero gives **Wien's displacement law** for the wavelength of peak emission,

$$
\lambda_{\max} T = 2.898\times 10^{-3}\ \text{m}\cdot\text{K},
$$

which is why hotter objects glow at shorter (bluer) wavelengths — from the deep red of a heating element to the blue-white of a hot star. Integrating $u(\lambda,T)$ over all wavelengths gives the total power radiated per unit surface area of an ideal blackbody, the **Stefan–Boltzmann law**,

$$
\frac{P}{A} = \sigma T^4, \qquad \sigma = 5.670\times 10^{-8}\ \text{W}\cdot\text{m}^{-2}\cdot\text{K}^{-4},
$$

with $\sigma$ the **Stefan–Boltzmann constant**. The steep $T^4$ dependence means that radiated power is extremely sensitive to temperature: doubling an object's absolute temperature increases its radiated power per unit area sixteenfold. Real objects are not perfect blackbodies; a surface's actual radiated power is $P/A = \varepsilon\sigma T^4$, where the **emissivity** $\varepsilon \le 1$ measures how closely the surface approximates an ideal absorber and emitter ($\varepsilon = 1$ for a true blackbody).

### Worked Example: The Sun as a Blackbody

The Sun's surface (photosphere) has an effective temperature of $T \approx 5778\ \text{K}$ and radius $R_\odot = 6.96\times10^8\ \text{m}$. Treating it as an ideal blackbody, Wien's law gives the wavelength of peak emission,

$$
\lambda_{\max} = \frac{2.898\times10^{-3}\ \text{m}\cdot\text{K}}{5778\ \text{K}} = 5.01\times10^{-7}\ \text{m} = 501\ \text{nm},
$$

squarely in the green part of the visible spectrum — the Sun's spectrum actually peaks near the middle of the range of wavelengths the human eye evolved to detect, though scattering in Earth's atmosphere and the eye's overall spectral response make sunlight appear white or yellow rather than green. The Stefan–Boltzmann law gives the power radiated per unit area, $P/A = \sigma T^4 = (5.670\times10^{-8}\ \text{W}\cdot\text{m}^{-2}\cdot\text{K}^{-4})(5778\ \text{K})^4 \approx 6.32\times10^7\ \text{W/m}^2$. Multiplying by the Sun's surface area, $A = 4\pi R_\odot^2 \approx 6.09\times10^{18}\ \text{m}^2$, gives a total radiated power (luminosity)

$$
P = \frac{P}{A}\cdot A \approx (6.32\times10^7\ \text{W/m}^2)(6.09\times10^{18}\ \text{m}^2) \approx 3.85\times10^{26}\ \text{W},
$$

in close agreement with the Sun's independently measured luminosity of $3.828\times10^{26}\ \text{W}$ — the same figure used in [Chapter 3, Problem 6](#ex-relativistic-dynamics-6) to estimate the Sun's rate of mass loss via $E=mc^2$. That two completely independent lines of physics (blackbody radiation here, and mass–energy equivalence there) connect so tightly to the same measured number is a testament to how well both theories describe the physical world.

### Historical Context: Lenard's Puzzle

Planck's quantization hypothesis was aimed narrowly at the blackbody spectrum, and Planck himself did not initially believe that light itself came in discrete packets. Evidence pointing in that direction had, in fact, already been gathering independently. In 1902, three years before Einstein's photon paper, Philipp Lenard studied the photoelectric effect using an arc lamp and a retarding-voltage apparatus much like the one described below, and found — to general puzzlement at the time — that the stopping voltage (and hence the photoelectrons' maximum kinetic energy) did not increase with the lamp's intensity, contrary to every expectation from Maxwell's wave theory of light, in which a more intense wave carries proportionally more energy to whatever absorbs it. Lenard had no explanation; the result simply sat as an unresolved anomaly in the physics literature for three years, alongside blackbody radiation, until Einstein showed that both puzzles have the same root cause: light exchanges energy with matter in discrete quanta, not continuously.

## The Photoelectric Effect

When light of sufficiently short wavelength strikes a metal surface, electrons are ejected — the **photoelectric effect**. A typical apparatus measures the photocurrent as a function of a retarding voltage $V$ applied between the emitting surface and a collector; the voltage at which the current just reaches zero, the **stopping potential** $V_0$, gives the maximum kinetic energy of the ejected electrons, $K_{\max} = eV_0$. Plotting the measured photocurrent against retarding voltage traces out a curve that falls smoothly to zero at $V_0$ rather than dropping abruptly, because the ejected electrons are emitted with a distribution of kinetic energies up to $K_{\max}$, not a single sharp value; $V_0$ marks where even the *fastest* electrons are turned back.

Three experimental features of this effect resist any explanation in terms of classical electromagnetic waves, in which energy is delivered continuously and is proportional to intensity:

1. **$K_{\max}$ is independent of light intensity.** Classically, a more intense wave delivers more energy per unit time to an electron and should eject electrons with more kinetic energy. Experimentally, increasing intensity increases the *number* of photoelectrons (the current) but not $K_{\max}$.
2. **$K_{\max}$ depends linearly on frequency**, and there exists a sharp **threshold frequency** $f_0$, characteristic of the metal, below which no photoelectrons are emitted at all, regardless of intensity or exposure time. Classically, a wave of any frequency should eventually eject electrons if given enough time to deliver sufficient energy, so a hard threshold — and one depending on frequency rather than intensity — has no classical explanation.
3. **Emission is (essentially) instantaneous**, with no observable time lag even at very low intensity. Classically, a dim wave should take a measurable time to deliver enough energy to an electron to free it; a rough classical estimate for a very weak source predicts delays of minutes to hours, yet no such delay is ever observed.

Einstein resolved all three in 1905 by proposing that light itself is quantized: it consists of discrete packets, **photons**, each carrying energy

$$
E = hf,
$$

with $h$ the same constant Planck introduced. In the photoelectric effect, a single photon transfers its entire energy to a single electron in one interaction. If $\phi$ (the metal's **work function**) is the minimum energy needed to remove an electron from the metal, conservation of energy gives

$$
K_{\max} = hf - \phi,
$$

the **photoelectric equation**. This immediately explains all three observations: $K_{\max}$ depends on $f$ (through the photon energy $hf$) but not on intensity, since intensity only changes the *number* of photons per second, not the energy of each one; the threshold frequency is $f_0 = \phi/h$, below which a single photon simply does not carry enough energy to free an electron, no matter how many photons arrive; and emission is instantaneous because each electron absorbs one photon's energy all at once, not gradually. A plot of $K_{\max}$ (equivalently, $eV_0$) versus $f$ is a straight line of slope $h$ and $y$-intercept $-\phi$, and Millikan's precise measurement of exactly this line (1916) provided both a direct experimental value of $h$ and strong confirmation of Einstein's photon hypothesis — for which, not for relativity, Einstein received the 1921 Nobel Prize in Physics.

The three stubborn facts are best met in the order Lenard and Millikan met them, with the apparatus in front of you. In {numref}`Figure %s <fig:ch06-photoelectric-sim>` the light's intensity, its wavelength, the target metal, and the retarding voltage are all under control, and the photocurrent and stopping potential are read off directly. Turn the intensity up at fixed wavelength: the current rises and the stopping potential does not move. Shorten the wavelength instead: the stopping potential climbs, and a plot of $eV_0$ against $f$ — the simulation will accumulate one for you — is a straight line whose slope is $h$ and whose intercept names the metal. Cross the threshold from the long-wavelength side and the current stops altogether, at full intensity.

```{phet-legacy} photoelectric
:sim-name: Photoelectric Effect
:label: fig:ch06-photoelectric-sim

The photoelectric apparatus: a photocathode, an adjustable light source, and a retarding voltage. (This is one of PhET's original Java simulations, run in the browser by CheerpJ; it downloads a Java runtime before it starts, so give it a few seconds on first load.)
```

### Worked Example: The Photoelectric Effect in Cesium

Cesium has one of the lowest work functions of any metal, $\phi = 2.14\ \text{eV}$, which is why it is used in the photocathodes of photomultiplier tubes and early photoelectric light meters. Ultraviolet light of wavelength $\lambda = 250\ \text{nm}$ illuminates a cesium surface. Using the convenient combination $hc = 1240\ \text{eV}\cdot\text{nm}$,

$$
E_{\text{photon}} = \frac{hc}{\lambda} = \frac{1240\ \text{eV}\cdot\text{nm}}{250\ \text{nm}} = 4.96\ \text{eV}.
$$

The maximum kinetic energy of the photoelectrons is $K_{\max} = E_{\text{photon}} - \phi = 4.96\ \text{eV} - 2.14\ \text{eV} = 2.82\ \text{eV}$, so the stopping potential is $V_0 = 2.82\ \text{V}$. The threshold wavelength — the longest wavelength that can still eject an electron — follows from $\phi = hc/\lambda_0$:

$$
\lambda_0 = \frac{hc}{\phi} = \frac{1240\ \text{eV}\cdot\text{nm}}{2.14\ \text{eV}} = 579\ \text{nm},
$$

which falls in the visible (yellow) part of the spectrum. Cesium is therefore photoelectrically sensitive to ordinary visible light, unlike most metals, whose work functions of $4$–$5\ \text{eV}$ push their threshold wavelengths into the ultraviolet.

### Applications: Photomultipliers and Photovoltaic Cells

The photoelectric effect underlies two technologies central to modern experimental physics and everyday life. A **photomultiplier tube** exploits a low-work-function photocathode (often a cesium compound, as in the worked example above) to convert a single incoming photon into a single ejected photoelectron, then accelerates that electron into a series of intermediate electrodes (**dynodes**), each of which is struck hard enough to eject several additional electrons via ordinary (non-photoelectric) collisional ionization; the resulting cascade, doubling in size at each of perhaps ten dynode stages, converts the arrival of a single photon into a macroscopic, easily measured current pulse containing millions of electrons. This single-photon sensitivity makes photomultiplier tubes essential wherever extremely faint light must be detected and counted, including the gamma-ray detectors used in PET scanners (discussed later in this chapter) and in nuclear and particle-physics experiments generally.

A closely related but distinct effect, the **photovoltaic effect**, underlies solar cells: rather than ejecting an electron entirely from the material, an absorbed photon in a semiconductor promotes an electron across the material's band gap (the semiconductor analog of the work function, examined further in solid-state contexts), and a built-in electric field at a junction between two differently doped semiconductor layers then separates the resulting electron and the vacancy (hole) it leaves behind before they can recombine, driving a current through an external circuit. As in the ordinary photoelectric effect, only photons with energy exceeding a threshold (the band-gap energy) contribute usable electrons, which is why solar-cell efficiency depends sensitively on matching the semiconductor's band gap to the solar spectrum.

## X-Ray Production: The Inverse Photoelectric Effect

The photoelectric effect converts a photon into an energetic electron; the reverse process — an energetic electron converted (at least partly) into a photon — occurs whenever fast electrons are abruptly decelerated in matter, and is the standard laboratory and industrial method of producing X-rays. In an X-ray tube, electrons are accelerated from rest through a large potential difference $V$ (typically tens to hundreds of kilovolts) and strike a dense metal target (commonly tungsten). As each electron decelerates within the target — a process called **bremsstrahlung**, German for "braking radiation" — it radiates part or all of its kinetic energy as one or more photons.

Because an individual electron can, in principle, lose its *entire* kinetic energy $eV$ in a single deceleration event (converting essentially all its kinetic energy into one photon, the exact time-reversed counterpart of the photoelectric effect, where one photon gives up its entire energy to one electron), there is a sharply defined **maximum** photon energy — and correspondingly a **minimum** wavelength — that the tube can produce, set by

$$
eV = \frac{hc}{\lambda_{\min}} \quad \Longrightarrow \quad \lambda_{\min} = \frac{hc}{eV},
$$

known as the **Duane–Hunt limit**. Most electrons instead lose their energy gradually over many collisions, radiating photons of smaller energy at each step and producing a continuous spectrum of wavelengths longer than $\lambda_{\min}$ — but no photon in the entire spectrum can have a wavelength shorter than $\lambda_{\min}$, since no single electron carries more than $eV$ of kinetic energy to begin with. Superimposed on this continuous bremsstrahlung spectrum are sharp **characteristic X-ray lines**, produced when an incident electron knocks an inner-shell electron out of a target atom and an outer electron falls down to fill the vacancy, emitting a photon of energy fixed by the target element's inner-shell energy levels (Moseley's law for these characteristic energies is developed in [Chapter 11](#ch-many-electron-atoms)). Unlike the continuous bremsstrahlung background, the characteristic lines depend on the target material, not on the accelerating voltage (once $V$ is large enough to eject the inner-shell electron in the first place).

Bremsstrahlung is worth separating into its classical and its quantum halves, because only the second is new here. The classical half — that a charge which accelerates radiates, and that the radiation carries energy away — is already in Maxwell's equations, and {numref}`Figure %s <fig:ch06-radiating-charge-sim>` is that statement on its own: shake a charge and kinks in its field propagate outward at $c$, taking energy with them. Stopping a charge dead is an acceleration like any other, so an electron slamming into a tungsten anode must radiate. What classical physics cannot supply is the sharp edge at $\lambda_{\min}$: a continuous field theory sets no floor on the wavelength radiated in a single event, and the Duane–Hunt limit exists only because the radiated energy comes in quanta $hf$ and one electron brings only $eV$ to spend.

```{openphysics} RadioWaves
:label: fig:ch06-radiating-charge-sim

An accelerating charge and the field it radiates. Move the charge by hand and watch the disturbance propagate outward at $c$ — the classical mechanism behind bremsstrahlung, and the one the electron in an X-ray tube obeys on its way to producing a photon of energy up to $eV$.
```

### Worked Example: Minimum Wavelength from a Diagnostic X-Ray Tube

A medical diagnostic X-ray tube is operated at an accelerating voltage of $V = 80.0\ \text{kV}$. The Duane–Hunt limit gives

$$
\lambda_{\min} = \frac{hc}{eV} = \frac{1240\ \text{eV}\cdot\text{nm}}{8.00\times10^{4}\ \text{eV}} = 1.55\times10^{-2}\ \text{nm} = 15.5\ \text{pm}.
$$

This is comparable to, and somewhat shorter than, typical interatomic spacings in crystals ($\sim 0.1$–$0.3\ \text{nm}$), which is why X-rays of this energy scale are useful for crystallographic diffraction ([Chapter 5](#ch-diffraction-of-light)) as well as medical imaging, where their short wavelength (and correspondingly high photon energy) allows them to penetrate soft tissue while being partially absorbed by denser bone.

## Compton Scattering

Even after the photoelectric effect, one could imagine "photon-like" energy exchange as a property specific to bound electrons in a metal, without light itself consisting of localized particles carrying momentum. Arthur Compton's 1923 experiment removed this loophole by showing that photons scattering from a *free* electron transfer momentum exactly as a particle collision would.

In Compton's experiment, X-rays of a single wavelength $\lambda$ are directed at a target of loosely bound (effectively free) electrons, and the wavelength $\lambda'$ of the scattered X-rays is measured as a function of scattering angle $\theta$. Classically, an electromagnetic wave incident on a charge should simply drive that charge to oscillate at the incident frequency and re-radiate at the *same* frequency (Thomson scattering); no wavelength shift is expected. Compton observed a systematic *increase* in wavelength, $\lambda' > \lambda$, growing with scattering angle $\theta$ and independent of the target material — a signature of a two-body collision, not wave re-radiation.

### Deriving the Compton Formula

Treat the photon as a particle with energy $E = hc/\lambda$ and momentum $p = E/c = h/\lambda$ (consistent with the massless-particle limit of the energy–momentum relation from [Chapter 3](#ch-relativistic-dynamics)), and apply conservation of relativistic energy and momentum to an elastic collision between the photon and an initially free, stationary electron of mass $m_e$. Let the photon scatter through angle $\theta$, emerging with wavelength $\lambda'$, while the electron recoils with momentum $p_e$ and (relativistic) energy $E_e$. The three momentum components entering the collision — incident photon momentum $h/\lambda$ along the initial direction, and zero for the electron — must balance the two outgoing momenta, whose vector sum (photon momentum $h/\lambda'$ at angle $\theta$, electron momentum $p_e$ at some recoil angle) forms a triangle. The law of cosines applied to that triangle gives

$$
(p_ec)^2 = \left(\frac{hc}{\lambda}\right)^2 + \left(\frac{hc}{\lambda'}\right)^2 - 2\left(\frac{hc}{\lambda}\right)\left(\frac{hc}{\lambda'}\right)\cos\theta. \tag{i}
$$

Conservation of energy, with the electron initially at rest ($E_e^{(0)} = m_ec^2$), gives

$$
E_e = \frac{hc}{\lambda} - \frac{hc}{\lambda'} + m_ec^2. \tag{ii}
$$

Squaring (ii) and using the energy–momentum invariant $E_e^2 = (p_ec)^2 + (m_ec^2)^2$ from [Chapter 3](#ch-relativistic-dynamics) to eliminate $E_e$ in favor of $p_ec$, then substituting (i) for $(p_ec)^2$, produces (after the $\left(\frac{hc}{\lambda}\right)^2$, $\left(\frac{hc}{\lambda'}\right)^2$, and $(m_ec^2)^2$ terms cancel identically between the two sides) the much simpler relation

$$
m_ec^2\left(\frac{hc}{\lambda} - \frac{hc}{\lambda'}\right) = \frac{hc}{\lambda}\cdot\frac{hc}{\lambda'}\,(1-\cos\theta).
$$

Dividing through by $hc$, multiplying both sides by $\lambda\lambda'/m_ec^2$, and simplifying $\lambda\left(\frac1\lambda-\frac1{\lambda'}\right)\lambda' = \lambda'-\lambda$ yields the **Compton scattering formula**:

$$
\lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta).
$$

The constant $h/m_ec = 2.426\times 10^{-12}\ \text{m}$ is the **Compton wavelength** of the electron. The formula correctly predicts zero shift at $\theta = 0$ (forward, undeflected "scattering") and maximum shift $2h/m_ec$ at $\theta = 180°$ (photon backscattered), matches the observed angular dependence precisely, and — crucially — is independent of the incident wavelength $\lambda$ itself, matching experiment. Compton scattering is direct, quantitative confirmation that a photon carries momentum $p = h/\lambda$ and transfers it to a free electron exactly as one particle colliding with another.

### Worked Example: Compton-Scattered Molybdenum X-Rays

X-rays of wavelength $\lambda = 0.100\ \text{nm}$ (comparable to characteristic molybdenum $K_\alpha$ X-rays used in crystallography) Compton-scatter off free electrons at $\theta = 60°$. The wavelength shift is

$$
\Delta\lambda = \frac{h}{m_ec}(1-\cos 60°) = (2.426\times10^{-12}\ \text{m})(1 - 0.500) = 1.21\times10^{-12}\ \text{m} = 1.21\ \text{pm},
$$

so the scattered wavelength is $\lambda' = 101.2\ \text{pm}$. In photon-energy terms, the incident photon carries $E = hc/\lambda = (1240\ \text{eV}\cdot\text{nm})/(0.100\ \text{nm}) = 12.40\ \text{keV}$, while the scattered photon carries $E' = hc/\lambda' = (1240\ \text{eV}\cdot\text{nm})/(0.1012\ \text{nm}) = 12.25\ \text{keV}$. The energy transferred to the recoiling electron is therefore $\Delta E = E - E' \approx 0.15\ \text{keV} = 150\ \text{eV}$ — a small but entirely measurable fraction of the incident photon's energy, exactly the kind of energy loss Compton measured to confirm the formula.

### The Compton Edge

In a real gamma-ray or X-ray detector, photons scatter through the full range of angles $0 \le \theta \le 180°$ available inside the detector material, and the detector records the energy $\Delta E(\theta) = E - E'(\theta)$ actually deposited by the recoiling electron for each scattering event. Because $\Delta E(\theta)$ increases monotonically with $\theta$ (least energy transfer for forward scattering, most for backscattering), there is a sharply defined *maximum* possible energy deposit, occurring at $\theta = 180°$ — the **Compton edge** — beyond which no Compton-scattered electron can deposit more energy in a single scattering event, no matter how many photons are examined. A photon that instead deposits its *entire* energy in one interaction (via the photoelectric effect on a bound atomic electron, rather than Compton scattering a free one) produces a separate, sharp peak at the full incident photon energy, the **photopeak**. Gamma-ray spectroscopists routinely distinguish these two features — a sharp photopeak plus a broad continuum of Compton-scattered energies cut off abruptly at the Compton edge — when interpreting a detector's measured energy spectrum, since both are simultaneous, competing ways the same photon can interact with the detector material.

## Pair Production and Annihilation

A further, still more dramatic demonstration of the particle nature of light is **pair production**: a sufficiently energetic photon, passing near a nucleus, can convert entirely into an electron–positron pair,

$$
\gamma \rightarrow e^- + e^+,
$$

requiring a photon energy of at least $2m_ec^2 = 1.022\ \text{MeV}$ (twice the electron rest energy) — a direct manifestation of mass–energy equivalence ([Chapter 3](#ch-relativistic-dynamics)), converting a massless particle's energy into the rest mass of two massive particles.

A nearby massive third body — typically an atomic nucleus — is required to conserve momentum. This can be seen directly from the energy–momentum four-vector formalism of [Chapter 3](#ch-relativistic-dynamics): an isolated photon of energy $E_\gamma$ has momentum $p_\gamma = E_\gamma/c$, but a resulting electron–positron pair with the *same* total energy $E_\gamma$ (by energy conservation) necessarily has total momentum strictly *less* than $E_\gamma/c$, because each massive particle satisfies $E^2 = (pc)^2+(mc^2)^2 > (pc)^2$, so $pc < E$ for each — the pair's combined momentum cannot match the photon's original momentum at the same total energy. A nucleus nearby can absorb the small difference in momentum (recoiling with negligible kinetic energy, because its mass is so much larger than $m_e$) while barely affecting the energy balance, resolving the mismatch; in a vacuum with no such third body available, momentum conservation alone forbids the process outright, regardless of how much energy the lone photon carries.

The reverse process, **pair annihilation**, $e^- + e^+ \to 2\gamma$ (two photons are required, rather than one, to conserve momentum in the electron–positron center-of-momentum frame — see [Chapter 3](#ch-relativistic-dynamics), [Problem 3](#ex-relativistic-dynamics-3)), converts rest mass entirely back into photon energy and is used, for example, in positron-emission tomography (PET) imaging, where each annihilation of an injected positron-emitting tracer with a nearby atomic electron produces two back-to-back $511\ \text{keV}$ gamma rays that a ring of detectors uses to reconstruct the tracer's location.

### Worked Example: Sharing Energy Above Pair-Production Threshold

A photon of energy $E_\gamma = 3.00\ \text{MeV}$, well above the $1.022\ \text{MeV}$ threshold, undergoes pair production near a heavy nucleus. Because the nucleus is far more massive than the electron or positron, it absorbs essentially none of the available kinetic energy (a large mass can supply whatever small momentum balance is needed while carrying away almost no energy, exactly analogous to how a wall barely recoils, and gains almost no kinetic energy, when it reflects a ball). The energy left over after paying the $2m_ec^2$ rest-mass cost is therefore shared, to good approximation, between the electron and positron as kinetic energy:

$$
K_{e^-} + K_{e^+} \approx E_\gamma - 2m_ec^2 = 3.00\ \text{MeV} - 1.022\ \text{MeV} = 1.978\ \text{MeV}.
$$

If the pair shares this energy symmetrically (not required by any conservation law, but a common simplifying assumption and, on average, the most probable outcome), each particle carries about $0.989\ \text{MeV}$ of kinetic energy — comparable to its own rest energy, so each is produced at a substantial fraction of the speed of light.

## The Photon: A Unified Picture

Four seemingly unrelated phenomena — blackbody radiation, the photoelectric effect, X-ray production, and Compton scattering — together with pair production and annihilation, are all consequences of a single underlying fact: electromagnetic radiation exchanges energy and momentum with matter in discrete, particle-like quanta, $E=hf$ and $p=h/\lambda$, rather than continuously. Blackbody radiation shows that an oscillator can only *emit or absorb* energy in these units; the photoelectric effect shows that a photon transfers its *entire* energy to a single electron in one step; X-ray production shows the same process run in reverse, with a sharply bounded maximum photon energy set by the incident electron's kinetic energy; Compton scattering shows that a photon carries not just energy but momentum, exchanged with a free electron exactly as in a two-body collision; and pair production and annihilation show that a photon's energy is, via $E=mc^2$, interconvertible with the rest mass of matter itself. None of these five phenomena has any classical explanation in terms of a continuous electromagnetic wave; all five are explained, quantitatively and without exception, by the same photon concept. Yet, as Chapters [4](#ch-interference-of-light)–[5](#ch-diffraction-of-light) demonstrated, light also produces interference and diffraction patterns with no possible explanation in a naive particle picture. [Chapter 7](#ch-wave-properties-of-particles) confronts this apparent contradiction directly, and shows that it is resolved not by choosing one description over the other, but by recognizing that matter, too, has a wave nature — and that wave and particle descriptions are two complementary faces of a single, more complete quantum picture.

## Summary

- The blackbody spectrum cannot be explained by the classical **Rayleigh–Jeans law**, $u(\lambda,T) = 8\pi k_BT/\lambda^4$, which diverges at short wavelength (the ultraviolet catastrophe); Planck's hypothesis that oscillator energy is quantized in units of $hf$ yields a radiation law matching observation at all wavelengths and reduces to the Rayleigh–Jeans law at long wavelength.
- **Wien's displacement law**, $\lambda_{\max}T = 2.898\times10^{-3}\ \text{m}\cdot\text{K}$, and the **Stefan–Boltzmann law**, $P/A = \sigma T^4$, follow from Planck's radiation law and together determine both the color and total radiated power of a thermal source from its temperature alone.
- The photoelectric effect — $K_{\max}$ independent of intensity, a sharp threshold frequency, and instantaneous emission — cannot be explained by classical wave theory but follows directly from Einstein's photon hypothesis, $E = hf$, via $K_{\max} = hf - \phi$.
- X-ray production (bremsstrahlung) is, in effect, the inverse of the photoelectric effect: decelerating electrons in an X-ray tube produce a continuous spectrum bounded by a sharp minimum wavelength, the **Duane–Hunt limit**, $\lambda_{\min} = hc/eV$, since no photon can carry more energy than a single electron's kinetic energy $eV$.
- Compton scattering — the angle-dependent wavelength shift of X-rays scattered from free electrons, $\lambda' - \lambda = (h/m_ec)(1-\cos\theta)$, derivable directly from conservation of relativistic energy and momentum — shows that photons carry momentum $p = h/\lambda$ and interact with electrons as particles in an elastic collision.
- Pair production ($\gamma \to e^- + e^+$, requiring $hf \ge 2m_ec^2$ and a nearby massive body to conserve momentum) and pair annihilation ($e^-+e^+ \to 2\gamma$) further confirm that photons are quanta of energy and momentum interconvertible with massive particles.

## Problems

:::{exercise}
:label: ex-particle-properties-of-waves-1

The peak of the Sun's blackbody emission spectrum occurs near $\lambda_{\max} \approx 500\ \text{nm}$. Use Wien's displacement law to estimate the Sun's surface temperature, and compare your answer to the value $T=5778\ \text{K}$ used in the worked example.
:::

:::{solution} ex-particle-properties-of-waves-1
:label: sol-particle-properties-of-waves-1
:class: dropdown

Wien's law gives

$$T=\frac{2.898\times10^{-3}\ \text{m K}}{500\times10^{-9}\ \text{m}}=5.80\times10^3\ \text{K}.$$

The difference from $5778\ \text{K}$ is $18\ \text{K}$, or $0.3\%$.  Therefore, the peak wavelength estimates the solar surface temperature as about $5800\ \text{K}$, in excellent agreement with the stated value.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-2

A tungsten filament in an incandescent bulb operates at $T = 2900\ \text{K}$. (a) Find the wavelength of peak emission and identify the region of the spectrum (visible, infrared, etc.) in which it lies. (b) Explain, using your answer to (a), why incandescent bulbs are inefficient sources of visible light. (c) Find the power radiated per unit area, assuming ideal blackbody behavior.
:::

:::{solution} ex-particle-properties-of-waves-2
:label: sol-particle-properties-of-waves-2
:class: dropdown

Wien's law gives $\lambda_{\max}=(2.898\times10^{-3}\ \text{m K})/(2900\ \text{K})=9.99\times10^{-7}\ \text{m}=999\ \text{nm}$, which is infrared.  The blackbody flux is

$$\frac PA=\sigma T^4=(5.670\times10^{-8}\ \text{W m}^{-2}\text{K}^{-4})(2900\ \text{K})^4=4.01\times10^6\ \text{W/m}^2.$$

Therefore, the filament peaks near $1.00\ \mu\text{m}$ in the infrared and radiates $4.01\times10^6\ \text{W/m}^2$ ideally; most of its power is invisible infrared rather than useful visible light.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-3

A red giant star has surface temperature $3200\ \text{K}$ and radius $500\,R_\odot$, where $R_\odot = 6.96\times10^8\ \text{m}$ is the Sun's radius. Using the Stefan–Boltzmann law, find the star's total luminosity, and compare it (as a ratio) to the Sun's luminosity of $3.83\times10^{26}\ \text{W}$ found in the worked example.
:::

:::{solution} ex-particle-properties-of-waves-3
:label: sol-particle-properties-of-waves-3
:class: dropdown

The radius is $R=500(6.96\times10^8\ \text{m})=3.48\times10^{11}\ \text{m}$.  Thus

$$P=4\pi R^2\sigma T^4=4\pi(3.48\times10^{11}\ \text{m})^2(5.670\times10^{-8})(3200\ \text{K})^4=9.05\times10^{30}\ \text{W}.$$

The ratio is $9.05\times10^{30}/(3.83\times10^{26})=2.36\times10^4$.  Therefore, the red giant radiates about $9.1\times10^{30}\ \text{W}$, or $2.4\times10^4$ times the Sun's luminosity.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-4

Light of wavelength $400\ \text{nm}$ strikes a sodium surface with work function $\phi = 2.28\ \text{eV}$. (a) Find the photon energy in eV. (b) Find the maximum kinetic energy of the ejected photoelectrons. (c) Find the stopping potential $V_0$. (d) Find the threshold wavelength for sodium.
:::

:::{solution} ex-particle-properties-of-waves-4
:label: sol-particle-properties-of-waves-4
:class: dropdown

Using $hc=1240\ \text{eV nm}$,

$$E_\gamma=\frac{1240\ \text{eV nm}}{400\ \text{nm}}=3.10\ \text{eV},\qquad K_{\max}=3.10\ \text{eV}-2.28\ \text{eV}=0.82\ \text{eV}.$$

Since $eV_0=K_{\max}$, $V_0=0.82\ \text{V}$.  At threshold, $\phi=hc/\lambda_0$, so $\lambda_0=1240/2.28=544\ \text{nm}$.  Therefore, the photon energy is $3.10\ \text{eV}$, the largest electron kinetic energy is $0.82\ \text{eV}$, the stopping potential is $0.82\ \text{V}$, and the threshold wavelength is $544\ \text{nm}$.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-5

A photoelectric-effect experiment on a certain metal gives a stopping potential of $0.65\ \text{V}$ for light of wavelength $450\ \text{nm}$, and $1.28\ \text{V}$ for light of wavelength $360\ \text{nm}$. Use these two data points (rather than assuming a value of $h$) to determine (a) Planck's constant and (b) the work function of the metal from this data, treating $K_{\max}=eV_0=hf-\phi$ as a linear equation in $f$.
:::

:::{solution} ex-particle-properties-of-waves-5
:label: sol-particle-properties-of-waves-5
:class: dropdown

The frequencies are $f_1=c/(450\ \text{nm})=6.67\times10^{14}\ \text{Hz}$ and $f_2=c/(360\ \text{nm})=8.33\times10^{14}\ \text{Hz}$.  Subtracting $eV_0=hf-\phi$ for the two data points gives

$$h=\frac{e(1.28-0.65)\ \text{V}}{f_2-f_1}=3.78\times10^{-15}\ \text{eV s}=6.05\times10^{-34}\ \text{J s}.$$

Then $\phi=hf_1-eV_1=(3.78\times10^{-15})(6.67\times10^{14})-0.65=1.87\ \text{eV}$.  Therefore, the data give $h=6.05\times10^{-34}\ \text{J s}$ and a work function of $1.87\ \text{eV}$.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-6

A photocell with a platinum surface (work function $\phi = 6.35\ \text{eV}$) is illuminated with light of wavelength $150\ \text{nm}$. (a) Show that this wavelength is above the threshold for photoemission and find $K_{\max}$. (b) Find the longest wavelength of light that could eject photoelectrons from platinum, and explain why ordinary visible or near-UV light sources cannot do so.
:::

:::{solution} ex-particle-properties-of-waves-6
:label: sol-particle-properties-of-waves-6
:class: dropdown

The incident photon energy is $E=1240/150=8.27\ \text{eV}$, which exceeds $\phi=6.35\ \text{eV}$.  Thus $K_{\max}=8.27-6.35=1.92\ \text{eV}$.  The threshold wavelength is

$$\lambda_0=\frac{1240\ \text{eV nm}}{6.35\ \text{eV}}=195\ \text{nm}.$$

Therefore, $150\ \text{nm}$ ultraviolet light ejects electrons with up to $1.92\ \text{eV}$ kinetic energy, while visible and near-UV wavelengths longer than $195\ \text{nm}$ cannot overcome platinum's work function.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-7

An X-ray tube is operated at an accelerating voltage of $120\ \text{kV}$. (a) Find the Duane–Hunt minimum wavelength $\lambda_{\min}$. (b) Find the corresponding maximum photon energy, in keV. (c) If the accelerating voltage is doubled, by what factor does $\lambda_{\min}$ change?
:::

:::{solution} ex-particle-properties-of-waves-7
:label: sol-particle-properties-of-waves-7
:class: dropdown

An electron accelerated through $120\ \text{kV}$ gains $eV=120\ \text{keV}$.  Hence

$$\lambda_{\min}=\frac{hc}{eV}=\frac{1240\ \text{eV nm}}{120000\ \text{eV}}=0.0103\ \text{nm}.$$

Therefore, the minimum wavelength is $0.0103\ \text{nm}$ and the maximum photon energy is $120\ \text{keV}$; doubling the voltage halves $\lambda_{\min}$.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-8

Explain, in your own words and using conservation of energy, why the bremsstrahlung spectrum from an X-ray tube is continuous (a range of wavelengths) even though each individual electron carries the same, sharply defined kinetic energy $eV$ upon striking the target.
:::

:::{solution} ex-particle-properties-of-waves-8
:label: sol-particle-properties-of-waves-8
:class: dropdown

Each incident electron begins with energy $eV$, but it can lose any fraction of that energy in one encounter and can lose the rest in subsequent collisions, target excitation, or heat.  A photon made in one braking event can therefore have any energy from nearly zero up to $eV$, with $E_\gamma=hc/\lambda$.  Therefore, the many allowed energy shares produce a continuous bremsstrahlung spectrum, even though the endpoint energy and minimum wavelength are sharp.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-9

X-rays of wavelength $\lambda = 0.0711\ \text{nm}$ are Compton-scattered at $\theta = 90°$. (a) Find the wavelength shift. (b) Find the wavelength and energy of the scattered photon. (c) Find the kinetic energy given to the recoiling electron.
:::

:::{solution} ex-particle-properties-of-waves-9
:label: sol-particle-properties-of-waves-9
:class: dropdown

At $90^\circ$, $\Delta\lambda=h/(m_ec)=2.426\ \text{pm}=0.002426\ \text{nm}$.  Thus

$$\lambda'=0.0711\ \text{nm}+0.002426\ \text{nm}=0.073526\ \text{nm},$$

$$E'=\frac{1240\ \text{eV nm}}{0.073526\ \text{nm}}=16.86\ \text{keV}.$$

The incident energy is $1240/0.0711=17.44\ \text{keV}$, so the electron receives $17.44-16.86=0.58\ \text{keV}$.  Therefore, the shift is $2.426\ \text{pm}$, the scattered photon has wavelength $0.07353\ \text{nm}$ and energy $16.86\ \text{keV}$, and the electron receives about $0.58\ \text{keV}$.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-10

Show that, for a photon Compton-scattered directly backward ($\theta = 180°$) by a free electron, the wavelength shift is $2h/m_ec$, and evaluate this numerically. For an incident photon of very short wavelength ($\lambda \ll h/m_ec$, i.e. a very energetic photon), find the approximate fraction of the incident photon's energy that is transferred to the electron in a $180°$ collision.
:::

:::{solution} ex-particle-properties-of-waves-10
:label: sol-particle-properties-of-waves-10
:class: dropdown

Putting $\theta=180^\circ$ into $\Delta\lambda=(h/m_ec)(1-\cos\theta)$ gives

$$\Delta\lambda=\frac{h}{m_ec}[1-(-1)]=\frac{2h}{m_ec}=4.852\times10^{-12}\ \text{m}=4.852\ \text{pm}.$$

For $\lambda\ll h/(m_ec)$, $\lambda'=\lambda+2h/(m_ec)\approx2h/(m_ec)$, so $E'/E=\lambda/\lambda'\ll1$ and $(E-E')/E\approx1$.  Therefore, backscattering shifts the wavelength by $4.852\ \text{pm}$ and transfers nearly $100\%$ of a sufficiently energetic photon's energy to the electron.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-11

Fill in the algebraic step omitted in the text: starting from equations (i) and (ii) in the derivation of the Compton formula, substitute (i) into the squared version of (ii) combined with $E_e^2=(p_ec)^2+(m_ec^2)^2$, and verify explicitly that the terms $(hc/\lambda)^2$, $(hc/\lambda')^2$, and $(m_ec^2)^2$ cancel between the two sides, leaving the simplified relation quoted in the text.
:::

:::{solution} ex-particle-properties-of-waves-11
:label: sol-particle-properties-of-waves-11
:class: dropdown

Let $A=hc/\lambda$, $B=hc/\lambda'$, and $M=m_ec^2$.  Equations (i) and (ii) give

$$E_e^2=(A-B+M)^2=A^2+B^2+M^2-2AB+2AM-2BM,$$

$$E_e^2=(p_ec)^2+M^2=A^2+B^2-2AB\cos\theta+M^2.$$

Cancelling $A^2$, $B^2$, and $M^2$ leaves $-2AB+2M(A-B)=-2AB\cos\theta$, or $M(A-B)=AB(1-\cos\theta)$.  Therefore, explicit cancellation gives exactly the simplified relation quoted in the text.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-12

A beam of visible-light photons ($\lambda = 600\ \text{nm}$) is Compton-scattered from free electrons at $\theta = 90°$. (a) Compute the fractional wavelength shift $\Delta\lambda/\lambda$. (b) Explain, using your numerical result, why the Compton effect is essentially undetectable with visible light and was only discovered using X-rays.
:::

:::{solution} ex-particle-properties-of-waves-12
:label: sol-particle-properties-of-waves-12
:class: dropdown

At $90^\circ$, $\Delta\lambda=2.426\ \text{pm}$.  Therefore,

$$\frac{\Delta\lambda}{\lambda}=\frac{2.426\times10^{-12}\ \text{m}}{600\times10^{-9}\ \text{m}}=4.04\times10^{-6}.$$

Therefore, visible light shifts by only four parts per million, far below ordinary spectral resolution, whereas the same fixed Compton shift is a measurable fraction of an X-ray wavelength.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-13

Find the minimum photon energy required for pair production of an electron-positron pair, and convert this to a wavelength. Explain why pair production cannot occur for an isolated photon in empty space (i.e., why a nearby nucleus or other particle is required), using conservation of momentum and energy together.
:::

:::{solution} ex-particle-properties-of-waves-13
:label: sol-particle-properties-of-waves-13
:class: dropdown

At minimum, the photon supplies two electron rest energies:

$$E_{\min}=2m_ec^2=2(0.511\ \text{MeV})=1.022\ \text{MeV},$$

$$\lambda=\frac{1240\ \text{eV nm}}{1.022\times10^6\ \text{eV}}=0.00121\ \text{nm}=1.21\ \text{pm}.$$

An isolated photon has $p=E/c$, but two massive particles with the same total energy have total momentum less than $E/c$; energy and momentum cannot both be conserved.  Therefore, pair production requires at least $1.022\ \text{MeV}$ photons of wavelength about $1.21\ \text{pm}$ and a nearby nucleus to absorb recoil momentum.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-14

A $2.50\ \text{MeV}$ photon undergoes pair production near a heavy nucleus, which recoils with negligible kinetic energy. If the electron and positron share the available kinetic energy equally, find the kinetic energy and the total (kinetic plus rest) energy of each particle.
:::

:::{solution} ex-particle-properties-of-waves-14
:label: sol-particle-properties-of-waves-14
:class: dropdown

The rest-energy cost is $2m_ec^2=1.022\ \text{MeV}$, leaving

$$K_{\rm available}=2.50\ \text{MeV}-1.022\ \text{MeV}=1.478\ \text{MeV}.$$

Equal sharing gives $K_e=K_{e^+}=0.739\ \text{MeV}$ and total energy $0.739+0.511=1.250\ \text{MeV}$ for each.  Therefore, each particle has $0.739\ \text{MeV}$ kinetic energy and $1.250\ \text{MeV}$ total energy.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-15

In positron-emission tomography, a positron emitted by a radioactive tracer travels a short distance, loses its kinetic energy through collisions, and then annihilates with an atomic electron essentially at rest. (a) Using conservation of energy and momentum (as in [Chapter 3, Problem 3](#ex-relativistic-dynamics-3)), find the energy of each of the two emitted gamma rays. (b) Find the wavelength of each gamma ray. (c) Explain, physically, why PET scanners are built as a ring of detectors surrounding the patient rather than a single detector.
:::

:::{solution} ex-particle-properties-of-waves-15
:label: sol-particle-properties-of-waves-15
:class: dropdown

At rest the electron and positron have total energy $2m_ec^2=1.022\ \text{MeV}$ and total momentum zero.  The two photons must have equal, opposite momenta and equal energies, so each has $0.511\ \text{MeV}$.  Its wavelength is

$$\lambda=\frac{1240\ \text{eV nm}}{511000\ \text{eV}}=0.00243\ \text{nm}=2.43\ \text{pm}.$$

Therefore, annihilation produces two opposite $511\ \text{keV}$ gamma rays of wavelength $2.43\ \text{pm}$; a detector ring records their coincident, back-to-back directions to localize the annihilation line through the patient.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-16

Estimate the minimum photon energy needed to produce a proton–antiproton pair ($p + \bar p$) instead of an electron–positron pair, given the proton rest energy $m_pc^2 = 938\ \text{MeV}$, and compare the required photon wavelength to that found for electron–positron pair production in Problem 13.
:::

:::{solution} ex-particle-properties-of-waves-16
:label: sol-particle-properties-of-waves-16
:class: dropdown

The threshold is $2m_pc^2=2(938\ \text{MeV})=1876\ \text{MeV}=1.876\ \text{GeV}$.  Its wavelength is

$$\lambda=\frac{1240\ \text{eV nm}}{1.876\times10^9\ \text{eV}}=6.61\times10^{-7}\ \text{nm}=0.661\ \text{fm}.$$

Compared with the electron-pair threshold wavelength $1.21\ \text{pm}$, this is smaller by about $1836$, the proton-to-electron mass ratio.  Therefore, proton--antiproton production needs about $1.88\ \text{GeV}$ photons with a $0.661\ \text{fm}$ wavelength.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-17

A $0.662\ \text{MeV}$ gamma ray (a characteristic energy emitted by the common radioactive source cesium-137) Compton-scatters inside a detector. (a) Find the maximum possible energy, $\Delta E_{\max}$, that can be deposited by a single Compton-scattering event (i.e., the location of the Compton edge), using the $\theta=180°$ result from Problem 10. (b) Find the photopeak energy, i.e., the energy deposited if the photon instead undergoes full photoelectric absorption. (c) Explain, in one or two sentences, why a real detector's measured spectrum for this source shows both features.
:::

:::{solution} ex-particle-properties-of-waves-17
:label: sol-particle-properties-of-waves-17
:class: dropdown

For $180^\circ$ scattering, $E'=E/[1+2E/(m_ec^2)]$.  Hence

$$E'=\frac{0.662\ \text{MeV}}{1+2(0.662/0.511)}=0.184\ \text{MeV},$$

$$\Delta E_{\max}=0.662\ \text{MeV}-0.184\ \text{MeV}=0.478\ \text{MeV}.$$

Full photoelectric absorption deposits $0.662\ \text{MeV}$.  Therefore, the Compton edge is $0.478\ \text{MeV}$ and the photopeak is $0.662\ \text{MeV}$; both appear because photons can either scatter incompletely or be fully absorbed.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-18

Explain, using the discussion of photomultiplier tubes, why a single visible-light photon (energy of order a few eV) can trigger a measurable macroscopic current pulse, even though a single electron's charge ($1.6\times10^{-19}\ \text{C}$) is far too small to detect directly with ordinary circuitry; estimate the number of electrons that must reach the final dynode stage to constitute a charge pulse of $1.0\times10^{-12}\ \text{C}$ (a typical minimum detectable pulse), and comment on whether a cascade of ten dynode stages, each multiplying the electron count by a factor of $4$, is sufficient to produce a pulse of this size starting from one photoelectron.
:::

:::{solution} ex-particle-properties-of-waves-18
:label: sol-particle-properties-of-waves-18
:class: dropdown

The charge needed is $Q=1.0\times10^{-12}\ \text{C}$, so

$$N=\frac Qe=\frac{1.0\times10^{-12}\ \text{C}}{1.602\times10^{-19}\ \text{C}}=6.24\times10^6\ \text{electrons}.$$

Ten stages multiplying by four give $4^{10}=1.05\times10^6$ electrons, or $1.68\times10^{-13}\ \text{C}$, below the stated threshold.  Therefore, a photomultiplier makes a photon detectable by multiplying one photoelectron into millions, but ten factor-four stages alone are short of a $1.0\times10^{-12}\ \text{C}$ pulse.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-19

Explain why the ultraviolet catastrophe (Rayleigh–Jeans law) and Lenard's photoelectric puzzle are, at first glance, very different experimental problems (one about the color and intensity of thermal glow, the other about ejected electrons), yet both are resolved by exactly the same hypothesis. Identify precisely which physical assumption is shared by both classical (failed) treatments, and which single quantization postulate replaces it in both cases.
:::

:::{solution} ex-particle-properties-of-waves-19
:label: sol-particle-properties-of-waves-19
:class: dropdown

Classical treatments assume electromagnetic energy is continuously divisible: cavity modes can receive the continuous equipartition energy $k_BT$, and a brighter wave can transfer energy continuously to an electron.  Planck and Einstein replace that assumption with $E=hf$ quanta: high-frequency cavity modes are rarely excited because quanta cost too much energy, and one electron receives one photon's energy at a time.  Therefore, both puzzles are resolved by the same photon-energy quantization postulate.
:::

:::{exercise}
:label: ex-particle-properties-of-waves-20

Silicon, used in most solar cells, has a band gap of about $1.1\ \text{eV}$. (a) Find the longest wavelength of light that can produce a usable electron–hole pair in a silicon photovoltaic cell, and identify the region of the spectrum in which it lies. (b) Explain, using the photoelectric equation as a guide, why photons with much *more* than the band-gap energy do not produce proportionally more usable electrical energy per photon, even though they carry more energy each.
:::

:::{solution} ex-particle-properties-of-waves-20
:label: sol-particle-properties-of-waves-20
:class: dropdown

The threshold condition is $E_\gamma\ge E_g$, so

$$\lambda_{\max}=\frac{1240\ \text{eV nm}}{1.1\ \text{eV}}=1.13\times10^3\ \text{nm}=1.13\ \mu\text{m}.$$

This lies in the near infrared.  Photon energy above the band gap first creates an electron--hole pair; excess energy is rapidly lost to lattice vibrations rather than producing proportional electrical work.  Therefore, silicon can use wavelengths up to about $1.13\ \mu\text{m}$, and photons far above the $1.1\ \text{eV}$ gap waste much of their extra energy as heat.
:::
