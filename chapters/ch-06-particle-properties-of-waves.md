---
title: Particle Properties of Waves
short_title: Chapter 6. Particle Properties of Waves
label: ch-particle-properties-of-waves
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain the ultraviolet catastrophe and how Planck's quantization hypothesis resolves it.
- State and apply Planck's radiation law and Wien's displacement law.
- Describe the photoelectric effect and explain why classical (wave) theory fails to account for its observed features.
- Apply Einstein's photon model, $E = hf$, to the photoelectric effect and interpret the stopping-potential and work-function data it predicts.
- Derive and apply the Compton scattering formula, and explain why Compton scattering demonstrates that photons carry momentum.
- Explain pair production and pair annihilation as further evidence for the particle nature of light.

## Introduction

Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) dismantled the ether and rebuilt kinematics and dynamics on Einstein's postulates, but light itself — a wave, according to Maxwell's equations, which special relativity leaves intact — remained conceptually untouched. Chapters [4](#ch-interference-of-light)–[5](#ch-diffraction-of-light) then developed that wave picture in full quantitative detail: interference and diffraction, both direct, precise confirmations that light obeys a wave equation. This chapter takes up a second, independent crisis of classical physics, one concerning not the *kinematics* of light but its very *nature*. Three phenomena — blackbody radiation, the photoelectric effect, and Compton scattering — each show, in a different experimental setting, that electromagnetic radiation exchanges energy with matter not continuously, as a wave should, but in discrete packets. The concept that emerges, the **photon**, carries energy $E = hf$ and momentum $p = h/\lambda$, and behaves in each of these experiments like a particle, even though light indisputably also shows the wave behavior of Chapters [4](#ch-interference-of-light)–[5](#ch-diffraction-of-light) in other settings. Reconciling these two faces of light is the beginning of quantum mechanics.

## Blackbody Radiation and Planck's Hypothesis

Any object at temperature $T$ emits electromagnetic radiation across a continuous range of wavelengths, with an intensity distribution depending on $T$. An idealized perfect absorber and emitter is called a **blackbody**; its emitted spectral distribution, the blackbody spectrum, depends only on temperature, not on the material.

Late-nineteenth-century classical physics, applying the equipartition theorem to the electromagnetic field modes inside a cavity, predicted a spectral energy density that grows without bound at short wavelengths — the **ultraviolet catastrophe** — sharply contradicted by the observed spectrum, which rises from zero at short wavelength, peaks, and falls off at long wavelength.

Max Planck resolved this in 1900 by a hypothesis with no classical justification: the oscillators making up the cavity walls cannot exchange energy with the field continuously, but only in discrete multiples of a fundamental quantum,

$$
E_n = nhf, \qquad n = 0, 1, 2, \ldots,
$$

where $f$ is the oscillator's frequency and $h$ is a new fundamental constant (**Planck's constant**), $h = 6.626\times 10^{-34}\ \text{J}\cdot\text{s}$. With this assumption, the average energy of a mode at frequency $f$ in thermal equilibrium at temperature $T$ is not $k_BT$ (the equipartition value, independent of $f$, which causes the catastrophe) but

$$
\langle E \rangle = \frac{hf}{e^{hf/k_BT} - 1},
$$

which suppresses high-frequency (short-wavelength) modes because at high $f$, $hf \gg k_BT$ makes a single quantum too "expensive" to be thermally excited. This leads to **Planck's radiation law** for the spectral radiance,

$$
u(\lambda, T) = \frac{8\pi hc}{\lambda^5}\, \frac{1}{e^{hc/\lambda k_B T} - 1},
$$

which matches the observed blackbody spectrum at all wavelengths and temperatures, and reduces to the classical (catastrophic) prediction in the limit $hf \ll k_BT$, i.e. at long wavelength, where quantization effects become negligible. Differentiating $u(\lambda,T)$ with respect to $\lambda$ and setting the result to zero gives **Wien's displacement law** for the wavelength of peak emission,

$$
\lambda_{\max} T = 2.898\times 10^{-3}\ \text{m}\cdot\text{K},
$$

which is why hotter objects glow at shorter (bluer) wavelengths — from the deep red of a heating element to the blue-white of a hot star.

Planck himself regarded the quantization of oscillator energy as a mathematical device rather than a physical claim about light. It was Einstein who, five years later, proposed taking it literally.

## The Photoelectric Effect

When light of sufficiently short wavelength strikes a metal surface, electrons are ejected — the **photoelectric effect**. A typical apparatus measures the photocurrent as a function of a retarding voltage $V$ applied between the emitting surface and a collector; the voltage at which the current just reaches zero, the **stopping potential** $V_0$, gives the maximum kinetic energy of the ejected electrons, $K_{\max} = eV_0$.

Three experimental features of this effect resist any explanation in terms of classical electromagnetic waves, in which energy is delivered continuously and is proportional to intensity:

1. **$K_{\max}$ is independent of light intensity.** Classically, a more intense wave delivers more energy per unit time to an electron and should eject electrons with more kinetic energy. Experimentally, increasing intensity increases the *number* of photoelectrons (the current) but not $K_{\max}$.
2. **$K_{\max}$ depends linearly on frequency**, and there exists a sharp **threshold frequency** $f_0$, characteristic of the metal, below which no photoelectrons are emitted at all, regardless of intensity or exposure time. Classically, a wave of any frequency should eventually eject electrons if given enough time to deliver sufficient energy, so a hard threshold — and one depending on frequency rather than intensity — has no classical explanation.
3. **Emission is (essentially) instantaneous**, with no observable time lag even at very low intensity. Classically, a dim wave should take a measurable time to deliver enough energy to an electron to free it; no such delay is observed.

Einstein resolved all three in 1905 by proposing that light itself is quantized: it consists of discrete packets, **photons**, each carrying energy

$$
E = hf,
$$

with $h$ the same constant Planck introduced. In the photoelectric effect, a single photon transfers its entire energy to a single electron in one interaction. If $\phi$ (the metal's **work function**) is the minimum energy needed to remove an electron from the metal, conservation of energy gives

$$
K_{\max} = hf - \phi,
$$

the **photoelectric equation**. This immediately explains all three observations: $K_{\max}$ depends on $f$ (through the photon energy $hf$) but not on intensity, since intensity only changes the *number* of photons per second, not the energy of each one; the threshold frequency is $f_0 = \phi/h$, below which a single photon simply does not carry enough energy to free an electron, no matter how many photons arrive; and emission is instantaneous because each electron absorbs one photon's energy all at once, not gradually. A plot of $K_{\max}$ (equivalently, $eV_0$) versus $f$ is a straight line of slope $h$ and $y$-intercept $-\phi$, and Millikan's precise measurement of exactly this line (1916) provided both a direct experimental value of $h$ and strong confirmation of Einstein's photon hypothesis — for which, not for relativity, Einstein received the 1921 Nobel Prize in Physics.

## Compton Scattering

Even after the photoelectric effect, one could imagine "photon-like" energy exchange as a property specific to bound electrons in a metal, without light itself consisting of localized particles carrying momentum. Arthur Compton's 1923 experiment removed this loophole by showing that photons scattering from a *free* electron transfer momentum exactly as a particle collision would.

In Compton's experiment, X-rays of a single wavelength $\lambda$ are directed at a target of loosely bound (effectively free) electrons, and the wavelength $\lambda'$ of the scattered X-rays is measured as a function of scattering angle $\theta$. Classically, an electromagnetic wave incident on a charge should simply drive that charge to oscillate at the incident frequency and re-radiate at the *same* frequency (Thomson scattering); no wavelength shift is expected. Compton observed a systematic *increase* in wavelength, $\lambda' > \lambda$, growing with scattering angle $\theta$ and independent of the target material — a signature of a two-body collision, not wave re-radiation.

Treating the photon as a particle with energy $E = hf = hc/\lambda$ and momentum $p = E/c = h/\lambda$ (consistent with the massless-particle limit of the energy–momentum relation from [Chapter 3](#ch-relativistic-dynamics)), and applying conservation of relativistic energy and momentum to an elastic collision between the photon and an initially free, stationary electron of mass $m_e$, gives the **Compton scattering formula**:

$$
\lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta).
$$

The constant $h/m_ec = 2.426\times 10^{-12}\ \text{m}$ is the **Compton wavelength** of the electron. The formula correctly predicts zero shift at $\theta = 0$ (forward, undeflected "scattering") and maximum shift $2h/m_ec$ at $\theta = 180°$ (photon backscattered), matches the observed angular dependence precisely, and — crucially — is independent of the incident wavelength $\lambda$ itself, matching experiment. Compton scattering is direct, quantitative confirmation that a photon carries momentum $p = h/\lambda$ and transfers it to a free electron exactly as one particle colliding with another.

## Pair Production and Annihilation

A further, still more dramatic demonstration of the particle nature of light is **pair production**: a sufficiently energetic photon, passing near a nucleus (needed to conserve momentum), can convert entirely into an electron–positron pair,

$$
\gamma \rightarrow e^- + e^+,
$$

requiring a photon energy of at least $2m_ec^2 = 1.022\ \text{MeV}$ (twice the electron rest energy) — a direct manifestation of mass–energy equivalence ([Chapter 3](#ch-relativistic-dynamics)), converting a massless particle's energy into the rest mass of two massive particles. The reverse process, **pair annihilation**, $e^- + e^+ \to 2\gamma$ (two photons are required, rather than one, to conserve momentum in the electron-positron center-of-momentum frame — see [Chapter 3](#ch-relativistic-dynamics), [Problem 3](#ex-relativistic-dynamics-3)), converts rest mass entirely back into photon energy and is used, for example, in positron-emission tomography (PET) imaging.

## Summary

- The blackbody spectrum cannot be explained by classical equipartition (the ultraviolet catastrophe); Planck's hypothesis that oscillator energy is quantized in units of $hf$ yields a radiation law matching observation and leads to Wien's displacement law $\lambda_{\max}T = 2.898\times10^{-3}\ \text{m}\cdot\text{K}$.
- The photoelectric effect — $K_{\max}$ independent of intensity, a sharp threshold frequency, and instantaneous emission — cannot be explained by classical wave theory but follows directly from Einstein's photon hypothesis, $E = hf$, via $K_{\max} = hf - \phi$.
- Compton scattering — the angle-dependent wavelength shift of X-rays scattered from free electrons, $\lambda' - \lambda = (h/m_ec)(1-\cos\theta)$ — shows that photons carry momentum $p = h/\lambda$ and interact with electrons as particles in an elastic collision, consistent with the relativistic energy–momentum relation for a massless particle.
- Pair production ($\gamma \to e^- + e^+$, requiring $hf \ge 2m_ec^2$) and pair annihilation ($e^-+e^+ \to 2\gamma$) further confirm that photons are quanta of energy and momentum interconvertible with massive particles.

## Problems

1. The peak of the Sun's blackbody emission spectrum occurs near $\lambda_{\max} \approx 500\ \text{nm}$. Use Wien's displacement law to estimate the Sun's surface temperature.

2. Light of wavelength $400\ \text{nm}$ strikes a sodium surface with work function $\phi = 2.28\ \text{eV}$. (a) Find the photon energy in eV. (b) Find the maximum kinetic energy of the ejected photoelectrons. (c) Find the stopping potential $V_0$. (d) Find the threshold wavelength for sodium.

3. A photoelectric-effect experiment on a certain metal gives a stopping potential of $0.65\ \text{V}$ for light of wavelength $450\ \text{nm}$, and $1.28\ \text{V}$ for light of wavelength $360\ \text{nm}$. Use these two data points (rather than assuming a value of $h$) to determine (a) Planck's constant and (b) the work function of the metal from this data, treating $K_{\max}=eV_0=hf-\phi$ as a linear equation in $f$.

4. X-rays of wavelength $\lambda = 0.0711\ \text{nm}$ are Compton-scattered at $\theta = 90°$. (a) Find the wavelength shift. (b) Find the wavelength and energy of the scattered photon. (c) Find the kinetic energy given to the recoiling electron.

5. Show that, for a photon Compton-scattered directly backward ($\theta = 180°$) by a free electron, the wavelength shift is $2h/m_ec$, and evaluate this numerically. For an incident photon of very short wavelength ($\lambda \ll h/m_ec$, i.e. a very energetic photon), find the approximate fraction of the incident photon's energy that is transferred to the electron in a $180°$ collision.

6. Find the minimum photon energy required for pair production of an electron-positron pair, and convert this to a wavelength. Explain why pair production cannot occur for an isolated photon in empty space (i.e., why a nearby nucleus or other particle is required), using conservation of momentum and energy together.
