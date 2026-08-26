---
title: Interference of Light
short_title: Chapter 4. Interference of Light
label: ch-interference-of-light
---

## Learning Objectives

By the end of this chapter, you should be able to:

- State Huygens's principle and the superposition principle, and explain how together they predict interference.
- Derive the path-difference conditions for constructive and destructive interference in Young's double-slit experiment, and calculate fringe positions and spacing.
- Explain why two independent light sources do not produce a stable interference pattern, and define coherence length and coherence time.
- Derive the intensity pattern of two-slit interference using phasor addition, and generalize the phasor method to $N$ equally spaced, idealized (zero-width) slits.
- Apply the thin-film interference conditions, accounting for the $\pi$ phase shift on reflection from a higher-index medium, to antireflection coatings and soap films.
- Describe the operation of the Michelson interferometer and connect it to the Michelson–Morley experiment of [Chapter 1](#ch-need-for-relativity).

## Introduction

Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) built special relativity from a single empirical fact: every inertial observer measures the same speed $c$ for light. That argument treated light purely as a *signal*, without asking what, physically, is doing the propagating. Maxwell's equations answer that question: light is an electromagnetic wave, and like any wave it should exhibit **interference** — the reinforcement or cancellation of two or more overlapping disturbances — and **diffraction** — the bending of a wave around obstacles and through apertures. Both effects are difficult to see with everyday light sources, for reasons this chapter will make precise, which is part of why light's wave nature took until the early nineteenth century to establish convincingly, long after Newton had championed a particle ("corpuscular") theory of light. Thomas Young's double-slit experiment of 1801 supplied the first decisive evidence: light from a single source, passed through two closely spaced slits, produces on a distant screen not two bright bands but a whole series of alternating bright and dark fringes — a pattern with no explanation in a purely particle picture, but an immediate and quantitative one once light is treated as a wave. This chapter develops that quantitative treatment, and the next takes up the closely related phenomenon of diffraction. Together they place the wave nature of light on the same firm experimental footing that Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) gave to its constancy of speed — which makes it all the more striking, in [Chapter 6](#ch-particle-properties-of-waves), that light also behaves as a stream of particle-like quanta.

## Huygens's Principle and the Superposition Principle

**Huygens's principle** states that every point on a wavefront can be treated as a source of secondary spherical wavelets, spreading out at the wave's speed; the wavefront at a later time is the envelope (the surface tangent to all of these wavelets). Huygens proposed this purely geometrical construction in 1678, well before Maxwell's electromagnetic theory existed, as a way of predicting how a wavefront of any shape propagates and bends around obstacles — and, applied to two nearby point sources, it immediately implies that the wavelets emitted from each source will overlap and combine at any point beyond them.

How wavelets combine is governed by the **superposition principle**: when two or more waves overlap in space, the resulting disturbance (electric field, for light) is the vector sum of the individual disturbances, at every point and at every instant. For two waves of the same frequency arriving at a point with some **phase difference** $\phi$ between them, the resulting intensity — proportional to the time-averaged square of the total field — depends critically on $\phi$:

- If $\phi = 0, 2\pi, 4\pi,\ldots$ (an integer multiple of $2\pi$), the waves arrive **in phase** and add crest-to-crest: **constructive interference**, with the resultant amplitude equal to the sum of the individual amplitudes.
- If $\phi = \pi, 3\pi, 5\pi,\ldots$ (an odd multiple of $\pi$), the waves arrive **exactly out of phase**, crest against trough: **destructive interference**, with the resultant amplitude equal to the *difference* of the individual amplitudes (zero, if the two amplitudes are equal).

Because $\phi$ generally depends on position, superposition of two overlapping waves produces a spatial pattern of alternating bright and dark regions wherever $\phi$ varies smoothly from point to point — exactly the fringe pattern Young observed.

## Young's Double-Slit Experiment

Consider two narrow slits, separated by a distance $d$, illuminated by a single monochromatic (single-wavelength) source so that the light emerging from each slit is a coherent, in-phase wavelet source (by Huygens's principle). A screen is placed a distance $L \gg d$ away. At a point on the screen located at angle $\theta$ from the line perpendicular to the slits (the *central axis*), light from the two slits travels along paths differing in length by

$$
\Delta r = d\sin\theta,
$$

the **path length difference**, obtained (for $L \gg d$) by treating the two rays reaching the observation point as effectively parallel and dropping a perpendicular from the near slit to the far ray. A path difference of a whole number of wavelengths brings the two waves back into phase; a path difference of a half-integer number of wavelengths brings them exactly out of phase. This gives the fundamental **two-slit interference conditions**:

$$
d\sin\theta = m\lambda \qquad (\text{constructive; bright fringe}), \qquad m = 0,\pm1,\pm2,\ldots
$$

$$
d\sin\theta = \left(m+\tfrac12\right)\lambda \qquad (\text{destructive; dark fringe}).
$$

The integer $m$ is the **order** of the fringe; $m=0$ labels the central bright fringe, on the axis, where the two paths are exactly equal regardless of $\lambda$.

For small angles (the usual case, since $d$ is typically tens of micrometers and $L$ is a meter or more), $\sin\theta \approx \tan\theta \approx y/L$, where $y$ is the position on the screen measured from the central axis. Substituting into the constructive-interference condition gives the position of the $m$-th bright fringe,

$$
y_m = \frac{m\lambda L}{d},
$$

so adjacent bright fringes are separated by a uniform **fringe spacing**

$$
\Delta y = \frac{\lambda L}{d}.
$$

Measuring $\Delta y$, $L$, and $d$ therefore gives a direct determination of $\lambda$ — historically, one of the first accurate wavelength measurements of visible light, and evidence that different colors correspond to different, specific wavelengths.

### Worked Example: Wavelength from Fringe Spacing

Slits separated by $d = 0.200\ \text{mm}$ are illuminated by a laser, and the resulting fringes on a screen $L = 2.00\ \text{m}$ away are found to be spaced $\Delta y = 6.50\ \text{mm}$ apart. Find the laser wavelength.

Solving $\Delta y = \lambda L/d$ for $\lambda$:

$$
\lambda = \frac{\Delta y\, d}{L} = \frac{(6.50\times10^{-3}\ \text{m})(0.200\times10^{-3}\ \text{m})}{2.00\ \text{m}} = 6.50\times10^{-7}\ \text{m} = 650\ \text{nm},
$$

consistent with a red helium–neon or diode laser.

## Coherence

Young's experiment works only because both slits are illuminated by the *same* wavefront from a single source, so that the phase relationship between the light leaving the two slits is fixed and stable in time — the two slit sources are **coherent**. Two independent, ordinary light sources (two separate light bulbs, for instance) do not produce a visible interference pattern: each source emits light as a rapid, random succession of short wave trains, each just a few nanoseconds long, with a phase that jumps randomly from one wave train to the next. Any interference pattern from one wave train is instantly washed out by the next, randomly-phased train arriving a few nanoseconds later — far faster than any detector (including the eye) can resolve — so the observed intensity is just the sum of the two independent intensities, with no fringes.

Two related length and time scales quantify how coherent a real (non-ideal, non-monochromatic) source is:

- The **coherence time** $\tau_c$, roughly the duration of a single, continuous wave train — the time over which the source's phase remains predictable.
- The **coherence length** $\ell_c = c\tau_c$, the corresponding path-length difference over which stable interference fringes can still be observed; path differences much larger than $\ell_c$ wash out the pattern because the two arms are then sampling *different*, independently-phased wave trains.

A source with a narrow range of wavelengths $\Delta\lambda$ around a central wavelength $\lambda$ has coherence length approximately $\ell_c \sim \lambda^2/\Delta\lambda$: a true single-frequency (monochromatic) source has $\Delta\lambda \to 0$ and hence $\ell_c \to \infty$, while ordinary "white" light, with $\Delta\lambda$ comparable to $\lambda$ itself, has a coherence length of only a few wavelengths. This is precisely why Young's original experiment — using ordinary sunlight passed first through a single pinhole (to create one coherent wavefront, spatially) before splitting it into the two slits — was a delicate and celebrated achievement, and why lasers, with extremely narrow $\Delta\lambda$ and correspondingly enormous coherence lengths (meters or more), make interference experiments dramatically easier to perform.

## Phasor Description and the Two-Slit Intensity Pattern

The interference conditions above locate the bright and dark fringes but say nothing about the *intensity* in between. This is found by adding the two slits' contributions as **phasors** — rotating vectors of length equal to each wave's amplitude $E_0$, rotating at the (common) optical frequency, with an angle between them equal to the phase difference $\phi$ corresponding to the path difference $\Delta r = d\sin\theta$:

$$
\phi = \frac{2\pi}{\lambda}\,d\sin\theta.
$$

Adding two equal-length phasors separated by angle $\phi$ (a standard vector-addition result, most easily seen from the law of cosines applied to the isosceles triangle the two phasors and their resultant form) gives a resultant amplitude $E = 2E_0\cos(\phi/2)$, and since intensity is proportional to the square of the amplitude,

$$
I(\theta) = I_0\cos^2\!\left(\frac{\phi}{2}\right) = I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right),
$$

where $I_0$ is the intensity at the central maximum ($\theta=0$, $\phi=0$), equal to *four* times the intensity from a single slit alone — not twice — because the amplitudes, not the intensities, add at a point of constructive interference: $E = 2E_0 \Rightarrow I \propto (2E_0)^2 = 4E_0^2$, four times a single slit's intensity $E_0^2$. This factor of four (rather than two) is itself a signature of wave interference, absent from any picture in which light energy simply adds like independent particles. The formula correctly reproduces bright fringes ($I=I_0$) whenever $\phi$ is a multiple of $2\pi$, i.e. $d\sin\theta = m\lambda$, and dark fringes ($I=0$) whenever $\phi$ is an odd multiple of $\pi$, i.e. $d\sin\theta = (m+\tfrac12)\lambda$, matching the conditions derived above.

### Multiple-Slit Interference

The phasor method generalizes immediately to $N$ equally spaced, idealized (zero-width) slits, each separated from its neighbor by $d$: the total field is the sum of $N$ equal-amplitude phasors, each successive one rotated by the same phase $\phi = (2\pi/\lambda)d\sin\theta$ relative to the last. Summing this geometric series of phasors gives the intensity pattern

$$
I(\theta) = I_1\left[\frac{\sin(N\phi/2)}{\sin(\phi/2)}\right]^2,
$$

where $I_1$ is the intensity from a single slit. Two features distinguish this from the two-slit case:

- **Principal maxima** still occur at exactly the same locations, $d\sin\theta = m\lambda$, since these are the angles at which *all* $N$ phasors point the same direction and add constructively no matter how many there are.
- The principal maxima become dramatically **narrower and more intense** as $N$ increases (their peak intensity scales as $N^2 I_1$, while their angular width scales as $1/N$), because slightly off the exact constructive-interference angle, the $N$ phasors — now pointing in $N$ slightly different directions — begin to cancel rather than reinforce, and this cancellation is more severe the more phasors there are. Between consecutive principal maxima, $N-2$ much weaker **secondary maxima** appear.

This sharpening with increasing $N$ is the physical basis of the diffraction grating, a device built from a very large number of closely, evenly spaced slits, taken up together with real (finite-width) slits in [Chapter 5](#ch-diffraction-of-light).

## Thin-Film Interference

A second everyday setting for interference is light reflecting from the two surfaces of a **thin film** — a soap bubble, an oil slick on water, or an engineered antireflection coating on a lens. Light striking the film partially reflects at the front surface and partially transmits into the film, reflects again at the back surface, and re-emerges to interfere with the light reflected at the front. For a film of thickness $t$ and refractive index $n_{\text{film}}$, viewed near-normal incidence, the beam reflecting off the back surface travels an extra round-trip distance $2t$ *inside* the film, corresponding to an extra optical path length $2n_{\text{film}}t$ (since a wave's wavelength inside a medium of index $n$ is $\lambda/n$, so the same physical distance corresponds to more wavelengths, and hence more phase, than the identical distance in vacuum).

A second, easily overlooked effect must be included: reflection off a boundary where the refractive index *increases* (light in a lower-index medium reflecting from a higher-index one) introduces an additional phase shift of exactly $\pi$ (equivalent to reflecting as if the wave flips upside-down), while reflection off a boundary where the index *decreases* introduces no such shift. This is directly analogous to a wave on a string reflecting from a fixed end (phase-inverted) versus a free end (not inverted), with "higher optical density" playing the role of "fixed end."

Combining the optical path difference $2n_{\text{film}}t$ with any phase shifts from the two reflections gives the thin-film interference conditions. For the common case of a film with $n_{\text{film}}$ greater than the medium on both sides (e.g., a soap film in air, or an oil film on water with $n_{\text{oil}} > n_{\text{water}}$ — so that only the *front* reflection, not the back one, picks up the extra $\pi$ shift, leaving a *net* relative phase shift of $\pi$ between the two reflected beams):

$$
2n_{\text{film}}t = \left(m+\tfrac12\right)\lambda \qquad (\text{constructive reflection}),
$$

$$
2n_{\text{film}}t = m\lambda \qquad (\text{destructive reflection}),
$$

with the roles of the two conditions exactly reversed (constructive at $m\lambda$, destructive at $(m+\tfrac12)\lambda$) if instead *both* reflections pick up a $\pi$ shift (or neither does), since the net relative shift is then $0$ rather than $\pi$. Because these conditions depend on $\lambda$, a film illuminated by white light reflects some wavelengths constructively and others destructively, producing the vividly colored, thickness-dependent bands seen in soap bubbles and oil slicks — colors that shift and swirl visibly as the film's thickness changes with time.

### Worked Example: An Antireflection Coating

A camera lens ($n_{\text{glass}} = 1.52$) is coated with a thin layer of magnesium fluoride ($n_{\text{MgF}_2} = 1.38$) to minimize reflection at $\lambda = 550\ \text{nm}$ (the middle of the visible spectrum, where the eye is most sensitive), for light incident from air ($n_{\text{air}}=1.00$).

Here $n_{\text{air}} < n_{\text{MgF}_2} < n_{\text{glass}}$, so *both* reflections (air-to-coating and coating-to-glass) occur at an interface where the index increases, and *both* therefore acquire the same $\pi$ phase shift — leaving a net relative phase shift of zero between them, exactly as in the "neither shifted" case above. Minimizing reflection (destructive interference between the two reflected beams) therefore requires the *odd-quarter-wavelength* condition,

$$
2n_{\text{MgF}_2}t = \left(m+\tfrac12\right)\lambda,
$$

and the thinnest such coating uses $m=0$:

$$
t = \frac{\lambda}{4n_{\text{MgF}_2}} = \frac{550\ \text{nm}}{4(1.38)} = 99.6\ \text{nm},
$$

a coating thickness of about $100\ \text{nm}$ — far thinner than a human hair, and a standard result quoted as the "quarter-wave" antireflection coating used throughout optics and photography. Because this cancellation condition depends on $\lambda$, such a coating minimizes reflection only near the design wavelength, which is why coated lenses still show a faint residual purplish tint (reflecting slightly more red and blue than green) under close inspection.

## The Michelson Interferometer

The **Michelson interferometer**, already encountered in [Chapter 1](#ch-need-for-relativity) as the instrument at the heart of the Michelson–Morley experiment, is in essence Young's two-path interference condensed into a single-source device using mirrors instead of two separate slits. A beam splitter divides an incoming beam into two perpendicular paths, each terminating in a mirror that reflects the light back to the beam splitter, where the two returning beams recombine and interfere; the observed fringe pattern depends on the difference in optical path length between the two arms. Displacing either mirror by a distance $\delta$ changes that arm's round-trip path length by $2\delta$, shifting the interference pattern by $2\delta/\lambda$ fringes — a shift precise enough to measure mirror displacements of a small fraction of a wavelength, i.e., tens of nanometers, making the interferometer one of the most sensitive length-measuring instruments available.

Recall from [Chapter 1](#ch-need-for-relativity) that this sensitivity is exactly what let Michelson and Morley set such a stringent limit on any ether-induced difference between the two perpendicular arms' round-trip light travel times: no rotation of the apparatus produced any fringe shift at all, to a precision that ruled out the expected ether-wind effect by more than an order of magnitude. The same operating principle — an extraordinarily sensitive comparison of two optical path lengths via interference fringes — underlies modern applications from precision engineering (measuring surface flatness to a fraction of a wavelength) to the gravitational-wave detectors LIGO and Virgo, which are, at heart, enormously scaled-up Michelson interferometers designed to detect mirror displacements many orders of magnitude smaller than a proton's radius.

## Summary

- **Huygens's principle** treats every point on a wavefront as a source of secondary wavelets; combined with the **superposition principle** (fields add; intensity depends on the resulting phase difference), it predicts interference wherever coherent waves overlap.
- **Young's double-slit experiment** gives bright fringes at $d\sin\theta = m\lambda$ and dark fringes at $d\sin\theta = (m+\tfrac12)\lambda$; for $L\gg d$, bright fringes are evenly spaced on the screen with spacing $\Delta y = \lambda L/d$.
- Stable interference requires **coherent** sources; two independent ordinary sources do not interfere because their random phase jumps, on a timescale set by the **coherence time** $\tau_c$, wash out any pattern faster than it can be observed. The **coherence length** $\ell_c = c\tau_c \sim \lambda^2/\Delta\lambda$ sets the maximum path difference over which fringes remain visible.
- Adding two slits' fields as **phasors** gives the two-slit intensity pattern $I(\theta) = I_0\cos^2(\pi d\sin\theta/\lambda)$; generalizing to $N$ idealized slits gives principal maxima at the same locations, $d\sin\theta=m\lambda$, growing sharper (width $\propto 1/N$) and more intense (peak $\propto N^2$) as $N$ increases — the basis of the diffraction grating ([Chapter 5](#ch-diffraction-of-light)).
- **Thin-film interference** depends on the extra optical path $2n_{\text{film}}t$ traveled inside the film, together with a $\pi$ phase shift for any reflection at a boundary where the refractive index increases; this explains both the iridescent colors of soap films and oil slicks and the design of quarter-wave antireflection coatings.
- The **Michelson interferometer** splits and recombines a single beam along two perpendicular paths, converting a path-length (or mirror-position) difference directly into an observable fringe shift; it is the instrument used in the Michelson–Morley experiment of [Chapter 1](#ch-need-for-relativity) and, scaled up enormously, in gravitational-wave detectors today.

## Problems

1. Light of wavelength $633\ \text{nm}$ (a helium–neon laser) illuminates two slits separated by $d = 0.120\ \text{mm}$. Find the angle $\theta$ to (a) the third bright fringe and (b) the second dark fringe, measured from the central axis.

2. In a double-slit experiment with $d = 0.250\ \text{mm}$ and a screen at $L = 1.40\ \text{m}$, bright fringes are observed with spacing $\Delta y = 3.30\ \text{mm}$. Find the wavelength of the light used, and identify (approximately) its color.

3. Explain, in terms of coherence time, why you do not see interference fringes when you look at two nearby incandescent light bulbs, but you readily see fringes from a laser passed through a double slit — even though both situations involve two overlapping light waves.

4. A source has a central wavelength of $600\ \text{nm}$ and a wavelength spread $\Delta\lambda = 0.02\ \text{nm}$ (typical of a good single-mode laser). Estimate its coherence length using $\ell_c \sim \lambda^2/\Delta\lambda$, and compare this to the $\sim\!1\ \mu\text{m}$ coherence length typical of an ordinary (non-laser) sodium lamp with $\Delta\lambda \approx 0.6\ \text{nm}$ (comment on the factor by which the laser's coherence length exceeds the sodium lamp's).

5. Starting from $I(\theta) = I_0\cos^2(\phi/2)$ with $\phi = (2\pi/\lambda)d\sin\theta$, verify that $I=I_0$ at $\theta=0$ and $I=0$ at the first dark fringe, and sketch (by hand or by evaluating a few points) the shape of $I(\theta)$ between the central maximum and the first two minima on either side.

6. Using the $N$-slit intensity formula, evaluate $I(\theta=0)$ for $N=2$ and $N=4$ slits (each with the same single-slit intensity $I_1$), and verify that the $N=4$ central maximum is $4\times$ as intense as the $N=2$ central maximum — consistent with the general scaling $I_{\max}\propto N^2$.

7. A soap film ($n=1.33$) in air is viewed at near-normal incidence. (a) Explain why only one of the two reflections (front or back surface) acquires a $\pi$ phase shift. (b) Find the two smallest nonzero thicknesses at which the film appears bright (constructive reflection) for $\lambda = 500\ \text{nm}$ light, and (c) the smallest thickness at which it appears completely dark.

8. Design an antireflection coating ($n=1.38$) for a glass lens ($n=1.52$) intended to minimize reflection at $\lambda = 600\ \text{nm}$ (in air). Find the minimum coating thickness, and explain why the coating will not perfectly eliminate reflection at other visible wavelengths, such as $450\ \text{nm}$ or $700\ \text{nm}$.

9. In a Michelson interferometer illuminated by $\lambda = 589\ \text{nm}$ light, one mirror is slowly moved, and $1200$ fringes are counted passing a reference point during the motion. Find the distance the mirror moved.

10. Explain, using the concept of optical path length, why the two-beam thin-film condition uses $2n_{\text{film}}t$ (rather than simply $2t$) for the extra path traveled inside the film, and why this matters for correctly locating the constructive and destructive reflection conditions.

11. Revisit the Michelson–Morley experiment of [Chapter 1](#ch-need-for-relativity) in light of this chapter's fringe-shift formula ($2\delta/\lambda$ fringes for a path-length change $\delta$). If the predicted ether-wind path-length difference between the two arms was of order $L v^2/c^2$ for an arm length $L$ and Earth's orbital speed $v\approx 3\times10^4\ \text{m/s}$, estimate the expected fringe shift for $L = 11\ \text{m}$ (achieved via multiple reflections in the original apparatus) and $\lambda = 590\ \text{nm}$, and compare it to the sub-hundredth-of-a-fringe precision of the null result.
