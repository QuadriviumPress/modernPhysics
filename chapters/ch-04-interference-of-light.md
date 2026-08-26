---
title: Interference of Light
short_title: Chapter 4. Interference of Light
label: ch-interference-of-light
numbering:
  enumerator: "4.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Describe light as an electromagnetic wave, relate its wavelength, frequency, and speed, and explain why detectors measure time-averaged intensity rather than the instantaneous field.
- Explain why interference and diffraction are invisible in everyday life, using the dimensionless ratio $\lambda/a$ and the correspondence between wave optics and ray optics.
- State Huygens's principle and use it to explain how a wavefront propagates and spreads after an aperture.
- Convert a path length difference into a phase difference, and use the result to decide whether two overlapping waves interfere constructively or destructively.
- Derive the path-difference conditions for Young's double-slit experiment, and calculate fringe angles, fringe positions, fringe spacing, and the highest observable order.
- Explain why two independent light sources do not produce a stable interference pattern; distinguish temporal from spatial coherence, and estimate coherence length from a source's spectral width.
- Derive the two-slit intensity pattern by phasor addition, show that the central maximum is four times a single slit's intensity, and explain why this does not violate energy conservation.
- Generalize the phasor method to $N$ equally spaced, idealized slits, and explain why the principal maxima sharpen as $1/N$ and brighten as $N^2$.
- Apply the thin-film interference conditions, correctly counting the $\pi$ phase shift on reflection from a higher-index medium, to soap films, antireflection coatings, air wedges, and Newton's rings.
- Describe the operation of the Michelson interferometer, convert a mirror displacement into a fringe count, and connect the instrument to the Michelson–Morley experiment of [Chapter 1](#ch-need-for-relativity).

## Introduction

Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) built special relativity from a single empirical fact: every inertial observer measures the same speed $c$ for light. That argument treated light purely as a *signal*, without asking what, physically, is doing the propagating. Maxwell's equations answer that question: light is an electromagnetic wave — a self-sustaining, traveling disturbance of the electric and magnetic fields. If that is right, then light must do what every other wave does. It must **interfere**: two overlapping light waves must be able to reinforce each other in some places and cancel each other in others. And it must **diffract**: it must bend around obstacles and spread out after passing through an aperture, instead of casting perfectly sharp geometric shadows.

Neither effect is part of ordinary experience. Shadows do look sharp. Light does seem to travel in straight lines. Two flashlights shone on the same wall produce a brighter patch, not a striped one. For most of the seventeenth and eighteenth centuries this was taken as decisive: Newton championed a *corpuscular* theory, in which light is a stream of tiny particles, and his enormous authority kept the wave theory of his contemporary Christiaan Huygens in the minority for over a century. A large part of this chapter's job is to explain why the wave effects hide so effectively — the answer, worked out below, is that the wavelength of visible light is a few hundred nanometers, some three orders of magnitude below the smallest object you handle in a day and six or more below a doorway — and then to show what happens when you shrink the apparatus until they can no longer hide.

Thomas Young did exactly that in 1801. He passed light from a single source through two closely spaced slits and found, on a distant screen, not two bright bands but a whole series of alternating bright and dark fringes. There is no way to get dark bands by adding light to light in a particle picture: two streams of corpuscles cannot cancel. In a wave picture the explanation is immediate, quantitative, and gives the wavelength of the light as a bonus. This chapter develops that treatment carefully, and the next takes up the closely related phenomenon of diffraction. Together they put the wave nature of light on the same firm experimental footing that Chapters [1](#ch-need-for-relativity)–[3](#ch-relativistic-dynamics) gave to the constancy of its speed — which makes it all the more startling when [Chapter 6](#ch-particle-properties-of-waves) shows that light *also* behaves as a stream of particle-like quanta, and that Newton was not simply wrong.

## Light as an Electromagnetic Wave

Everything in this chapter follows from one picture of what light is, so it is worth stating carefully before using it.

A monochromatic (single-wavelength) light wave traveling in the $+x$ direction consists of an electric field oscillating in a direction perpendicular to $x$,

$$
E(x,t) = E_0\sin(kx - \omega t + \varphi_0),
$$

accompanied by a magnetic field perpendicular to both. Here $E_0$ is the **amplitude**, $k = 2\pi/\lambda$ is the **wave number**, $\omega = 2\pi f$ is the **angular frequency**, and $\varphi_0$ is a constant that fixes where in its cycle the wave happens to be at $x = 0$, $t = 0$. The quantity in parentheses is the **phase**. Wavelength, frequency, and speed are linked in the usual way,

$$
c = f\lambda .
$$

Three consequences of this description are used constantly below.

**Detectors measure intensity, not field.** The **intensity** $I$ — the power per unit area carried by the wave — is proportional to the *time average of the square* of the electric field, and hence to the square of the amplitude:

$$
I \propto E_0^2 .
$$

This proportionality is the single most important fact in the chapter. It means amplitudes add, and *then* you square; it is emphatically not true that intensities add. Two waves whose fields cancel produce zero intensity even though each alone carries energy, and (as the phasor section shows) two waves whose fields reinforce produce four times a single wave's intensity, not twice.

Why the time average? Visible light has $f \approx 5\times10^{14}\ \text{Hz}$, so one oscillation takes about $2\times10^{-15}\ \text{s}$. No detector — no photodiode, no photographic emulsion, and certainly not the eye — responds anywhere near that fast. Every measurement is an average over an enormous number of cycles, and what survives that average is the intensity.

**Light slows down in matter, and its wavelength shrinks with it.** In a transparent medium of refractive index $n$, light travels at speed $v = c/n$. The frequency cannot change — the field at the boundary must oscillate in step on both sides — so the wavelength must:

$$
\lambda_n = \frac{\lambda}{n},
$$

where $\lambda$ is the vacuum wavelength. In water ($n = 1.33$), $550\ \text{nm}$ green light has a wavelength of only $414\ \text{nm}$.

**Optical path length is what counts.** Because interference depends on how many *wavelengths* fit into a path, and a medium packs more wavelengths into the same physical distance, the useful quantity is the **optical path length**: for a geometric distance $d$ traversed in a medium of index $n$,

$$
\text{optical path length} = nd .
$$

A phase advance is $2\pi$ per wavelength, so the phase accumulated over a physical distance $d$ in a medium of index $n$ is $(2\pi/\lambda)\,nd$ with $\lambda$ the *vacuum* wavelength. This idea reappears in the thin-film section and again in the Michelson interferometer, and it is the reason the thin-film formulas below carry a factor of $n$.

The picture behind all of this — a transverse electric field, a magnetic field perpendicular to it, and both perpendicular to the direction of travel — is drawn in three dimensions and set in motion in {numref}`Figure %s <fig:ch04-em-wave-sim>`. It is also the place to see what the phase constant $\varphi_0$ and the amplitude $E_0$ actually do, and what it means for a wave to be polarized: a direction of oscillation that plays no part in this chapter, where all the interfering beams share one, but that becomes the whole subject once a filter is put in the beam.

```{openphysics} LightPropagation
:label: fig:ch04-em-wave-sim

A monochromatic electromagnetic wave with its electric and magnetic fields drawn perpendicular to each other and to the direction of propagation. Later screens send the wave through polarizers and birefringent plates, where two components of one wave are given different optical paths — the same mechanism as the thin films of this chapter, applied to polarization rather than to geometry.
```

## Why Wave Effects Are So Hard to See

Before doing any interference calculation, it pays to understand why nobody notices these effects while walking around. The argument is a scaling argument, and it requires almost no algebra.

Suppose light of wavelength $\lambda$ passes through an aperture of width $a$ and spreads by some angle $\theta$. What can $\theta$ possibly depend on? The problem contains exactly two lengths, $\lambda$ and $a$, and $\theta$ is a pure number. A pure number cannot depend on a length, so it can only depend on the *ratio* of the two:

$$
\theta = (\text{some function of } \lambda/a).
$$

This is worth pausing on, because it says something strong. Shrink the wavelength and the aperture by the same factor and nothing changes — the whole pattern simply scales. It also means that experiments with water waves in a ripple tank, where wavelengths and apertures are both centimeters, are quantitatively informative about light, where both are tens of thousands of times smaller. What matters is never $\lambda$ alone; it is $\lambda/a$.

The next chapter shows that for a slit the answer is $\theta \approx \lambda/a$, with no large numerical factor. Take that on trust for a moment and put in numbers. For green light, $\lambda = 550\ \text{nm}$:

- Through a $1\ \text{mm}$ pinhole, $\lambda/a = 5.5\times10^{-4}\ \text{rad} \approx 0.03°$. Over a $2\ \text{m}$ throw the beam spreads by about $1\ \text{mm}$ — comparable to the pinhole itself, and easily mistaken for the geometric shadow.
- Through a gap the width of a human hair, $a \approx 70\ \mu\text{m}$, the spread is $\lambda/a = 7.9\times10^{-3}\ \text{rad}$, giving about $1.6\ \text{cm}$ at $2\ \text{m}$. That is unmistakable, and it is why you can see diffraction by looking at a distant streetlight through a narrow gap between two fingers.
- Through a doorway, $a \approx 1\ \text{m}$, the spread is $5.5\times10^{-7}\ \text{rad}$: about $1\ \mu\text{m}$ across a room. Utterly undetectable, which is why doorways cast sharp shadows.

So wave optics does not contradict the ray optics of an introductory course; it *contains* it. Ray optics is what wave optics becomes in the limit $\lambda/a \to 0$, and for everyday objects $\lambda/a \sim 10^{-4}$ or smaller. This is an instance of the **correspondence principle**, an idea that will recur throughout this book: a more general theory must reproduce the older, more limited one in the regime where the older one was tested. Relativity reduces to Newtonian mechanics when $v/c \to 0$ ([Chapter 2](#ch-special-relativity)); quantum mechanics reduces to classical mechanics in the limit of large quantum numbers ([Chapter 8](#ch-the-schrodinger-equation)); and wave optics reduces to ray optics when $\lambda/a \to 0$.

The practical lesson is simple: to see interference and diffraction, build apertures no more than a few hundred wavelengths across — that is, tenths of a millimeter or smaller. Young's achievement was in large part an achievement of craftsmanship.

## Huygens's Principle

**Huygens's principle** (1678) states that *every point on a wavefront may be treated as a source of secondary spherical wavelets, spreading out at the wave's speed; the wavefront at a later time is the envelope — the surface tangent to all of these wavelets.*

This is a purely geometrical recipe, proposed nearly two centuries before Maxwell's electromagnetic theory existed, and it is remarkably powerful. Applied to a plane wave in open space ({numref}`Figure %s <fig:ch04-huygens>`, panel a) it simply regenerates a plane wave, which is the least it must do. Applied at an interface it reproduces the laws of reflection and refraction. And applied at an aperture it makes a prediction that the ray picture cannot: the wavelets emitted near the edges have no neighbors to cancel their sideways spread, so the wave must bend into the geometric shadow. How much it bends depends, as the scaling argument above requires, on $\lambda/a$ (panels b and c).

```{figure} ../images/ch04-huygens-principle.svg
:label: fig:ch04-huygens
:alt: Three panels showing Huygens wavelets rebuilding a plane wavefront, a wide aperture where only the edges bend, and a narrow aperture where the transmitted wave spreads in all directions.

Huygens's construction. (a) Each point of a wavefront emits a spherical wavelet; the envelope of the wavelets is the wavefront an instant later. (b) At an aperture much wider than a wavelength, the wavelets in the middle rebuild a flat wavefront and only the edges bend, so the beam looks like a ray. (c) When the aperture is comparable to a wavelength, a single wavelet survives and the transmitted wave spreads over the whole region beyond the slit. Original schematic generated with matplotlib; see `scripts/figures/`.
```

Two honest caveats. First, taken literally the construction also predicts a backward-traveling wave, which does not exist; Fresnel and later Kirchhoff repaired this by attaching an *obliquity factor* to each wavelet that suppresses backward emission, and by insisting that the wavelets be added *with their phases* rather than merely enveloped. That upgraded version — the Huygens–Fresnel principle — is the tool of [Chapter 5](#ch-diffraction-of-light). Second, Huygens's principle by itself says nothing about intensity. To get intensities we need the superposition principle, which is where we turn next.

## Superposition: Turning Path Difference into Phase Difference

The **superposition principle** states that when two or more waves overlap, the resulting disturbance at each point and each instant is the *sum* of the individual disturbances. For light this is a consequence of the linearity of Maxwell's equations in vacuum and in ordinary transparent materials: fields add, and they add as vectors.

Consider two waves of the same frequency and the same amplitude $E_0$ arriving at some point $P$. Suppose they left a common source in step with each other but then traveled different distances, $r_1$ and $r_2$, to get to $P$. Each accumulates phase at a rate of $2\pi$ radians per wavelength traveled, so their **phase difference** at $P$ is

$$
\phi = \frac{2\pi}{\lambda}\,(r_2 - r_1) = \frac{2\pi}{\lambda}\,\Delta r .
$$

This one equation is the hinge of the whole chapter, and it is worth reading in both directions. A path difference of one whole wavelength corresponds to a phase difference of $2\pi$, which is no phase difference at all — the waves are back in step. A path difference of half a wavelength corresponds to a phase difference of $\pi$, which puts crest against trough. In general:

$$
\Delta r = m\lambda \quad (m = 0,\pm1,\pm2,\ldots) \qquad \Longrightarrow \qquad \phi = 2\pi m \qquad \textbf{constructive},
$$

$$
\Delta r = \left(m+\tfrac12\right)\lambda \qquad \Longrightarrow \qquad \phi = (2m+1)\pi \qquad \textbf{destructive}.
$$

Under constructive interference the fields add crest to crest, giving a resultant amplitude $2E_0$ and — since $I\propto E_0^2$ — an intensity *four* times that of either wave alone. Under destructive interference the resultant amplitude is $E_0 - E_0 = 0$ and the intensity vanishes. If the two amplitudes are unequal, the extremes are $E_1 + E_2$ and $|E_1 - E_2|$; complete darkness requires equal amplitudes, which is why interference fringes look best when the two slits are identical.

Three sources of phase difference will appear in this chapter, and it is worth naming them now so that they are not confused later:

1. **Path difference** in vacuum or air, $\phi = (2\pi/\lambda)\Delta r$ — the double slit.
2. **Optical path difference** when part of the path lies in a medium, $\phi = (2\pi/\lambda)\,\Delta(nd)$ — thin films, and gas cells in an interferometer.
3. **Phase shifts on reflection**, an abrupt $\pi$ acquired at certain boundaries — thin films again.

Every interference problem in this chapter is solved by totaling these three contributions and asking whether the total is an even or an odd multiple of $\pi$.

### Worked Example: From Path Difference to Brightness

Two identical, in-step sources emit light of wavelength $\lambda = 500\ \text{nm}$. At a particular point the waves have traveled distances differing by $\Delta r = 1.25\ \mu\text{m}$. Is that point bright or dark?

Count wavelengths in the path difference:

$$
\frac{\Delta r}{\lambda} = \frac{1.25\times10^{-6}\ \text{m}}{500\times10^{-9}\ \text{m}} = 2.5 .
$$

The path difference is two and a half wavelengths — a half-integer number — so $\phi = 2\pi(2.5) = 5\pi$, an odd multiple of $\pi$. The point is **dark**.

Now suppose the whole region between the sources and that point is filled with water, $n = 1.33$, without moving anything. The geometric path difference is unchanged, but the wavelength in the water is $\lambda_n = (500\ \text{nm})/1.33 = 376\ \text{nm}$, so the path difference is now $(1250\ \text{nm})/(376\ \text{nm}) = 3.32$ wavelengths and the point is neither fully bright nor fully dark. Immersing an interference experiment in a medium genuinely changes the pattern; it does not merely rescale the brightness.

## Young's Double-Slit Experiment

Young's arrangement is shown in {numref}`Figure %s <fig:ch04-double-slit>`. Light from a source passes first through a *single* narrow slit, then through *two* narrow slits separated by a distance $d$, and finally falls on a screen a distance $L$ away.

```{figure} ../images/ch04-double-slit-geometry.svg
:label: fig:ch04-double-slit
:alt: Left panel, the full double-slit apparatus with source, single slit, double slit, and fringed screen. Right panel, a magnified triangle showing the path difference d sine theta between two effectively parallel rays.

Young's double-slit experiment. (a) The first slit produces a single wavefront that illuminates both of the second pair, so $S_1$ and $S_2$ act as coherent sources. (b) For $L \gg d$ the two rays reaching a distant point are effectively parallel, and the ray from $S_2$ travels an extra distance $\Delta r = d\sin\theta$. Original schematic generated with matplotlib; see `scripts/figures/`.
```

The first slit is not decoration. Its job is to guarantee that a single wavefront reaches both of the following slits, so that whatever the source does — however erratically it flickers — it does the same thing at $S_1$ and at $S_2$ at the same moment. The two slits then behave as **coherent** sources with a fixed phase relationship. Without that first slit, different parts of an extended source illuminate the two slits independently, and the pattern washes out. (The coherence section below makes this precise; a modern laser has enough built-in coherence that the first slit can be omitted, which is why the classroom demonstration looks so much easier than Young's original.)

### The Path Difference

Consider a point $P$ on the screen, at angle $\theta$ from the central axis. Light reaching $P$ from $S_2$ has traveled farther than light from $S_1$. Because $L \gg d$ in any practical apparatus — $d$ is tens of micrometers, $L$ is a meter or more — the two rays heading for $P$ are very nearly parallel, and the geometry collapses to the small right triangle of {numref}`Figure %s(b) <fig:ch04-double-slit>`: drop a perpendicular from $S_1$ onto the ray from $S_2$, and the extra leg is

$$
\Delta r = d\sin\theta .
$$

Combining this with the constructive and destructive conditions of the previous section gives the **two-slit interference conditions**:

$$
d\sin\theta = m\lambda \qquad (\text{bright fringe}), \qquad m = 0,\pm1,\pm2,\ldots
$$

$$
d\sin\theta = \left(m+\tfrac12\right)\lambda \qquad (\text{dark fringe}).
$$

The integer $m$ is the **order** of the fringe. The $m = 0$ bright fringe sits on the axis, where the two paths are exactly equal; note that its position does not depend on $\lambda$, so in white light the central fringe is white while all the others are spread into little spectra.

### Fringe Positions on the Screen

For small angles — again, the usual case — $\sin\theta \approx \tan\theta \approx y/L$, where $y$ is measured on the screen from the central axis. The bright fringes then fall at

$$
y_m = \frac{m\lambda L}{d},
$$

evenly spaced, with **fringe spacing**

$$
\Delta y = \frac{\lambda L}{d}.
$$

Three features of this result deserve comment. First, measuring $\Delta y$, $L$, and $d$ determines $\lambda$ — this was historically one of the first accurate measurements of the wavelength of visible light, and the first evidence that different colors correspond to different, specific wavelengths. Second, the fringes get *farther apart* as the slits get *closer together*: squeezing the apparatus stretches the pattern. This reciprocal relationship between a wave's confinement and its spread is a hallmark of wave phenomena, and it returns as the uncertainty principle in [Chapter 7](#ch-wave-properties-of-particles). Third, the small-angle form is an approximation; when $d$ is only a few wavelengths the fringes are not evenly spaced and $d\sin\theta = m\lambda$ must be used directly.

The reciprocal relationship in $\Delta y = \lambda L/d$ is easy to state and easy to get backwards, so it is worth watching it happen. In {numref}`Figure %s <fig:ch04-double-slit-sim>` the slit separation is a slider and the pattern responds live: closing the slits together spreads the fringes apart, and raising the frequency — shortening $\lambda$ — packs them closer. The simulation runs the same geometry with water waves, sound, and light, which is a useful reminder that nothing in the derivation used any property of light beyond its being a wave with a wavelength.

```{phet} wave-interference
:screen: 3
:label: fig:ch04-double-slit-sim

Young's geometry with the slit separation, the slit width, and the wavelength under direct control. Switch between one slit and two: with one slit open the screen still shows structure, which is the diffraction of [Chapter 5](#ch-diffraction-of-light) intruding on the idealization used here, where the slits are treated as point sources.
```

Finally, since $\sin\theta$ can never exceed $1$, the condition $d\sin\theta = m\lambda$ has solutions only for

$$
|m| \le \frac{d}{\lambda},
$$

so a double slit produces a finite number of orders — a point that becomes important for diffraction gratings in [Chapter 5](#ch-diffraction-of-light).

### Worked Example: Wavelength from Fringe Spacing

Slits separated by $d = 0.200\ \text{mm}$ are illuminated by a laser, and the resulting fringes on a screen $L = 2.00\ \text{m}$ away are found to be spaced $\Delta y = 6.50\ \text{mm}$ apart. Find the laser wavelength.

Solving $\Delta y = \lambda L/d$ for $\lambda$:

$$
\lambda = \frac{\Delta y\, d}{L} = \frac{(6.50\times10^{-3}\ \text{m})(0.200\times10^{-3}\ \text{m})}{2.00\ \text{m}} = 6.50\times10^{-7}\ \text{m} = 650\ \text{nm},
$$

consistent with a red helium–neon or diode laser. Note the sizes of the quantities involved: a $650\ \text{nm}$ wavelength has been measured with a millimeter ruler, because the apparatus magnifies the wavelength by the factor $L/d = 10^4$.

### Worked Example: Fringe Angles, Positions, and Count

A double slit with $d = 0.100\ \text{mm}$ is illuminated with the green line of a mercury lamp, $\lambda = 546\ \text{nm}$, and the screen is $L = 1.20\ \text{m}$ away. (a) Find the angle to the third-order bright fringe. (b) Find the fringe spacing on the screen. (c) How many bright fringes appear on a screen $5.0\ \text{cm}$ wide, centered on the axis? (d) How many orders exist in principle?

**(a)** From $d\sin\theta = m\lambda$ with $m = 3$:

$$
\sin\theta_3 = \frac{3(546\times10^{-9}\ \text{m})}{1.00\times10^{-4}\ \text{m}} = 0.0164 \quad\Longrightarrow\quad \theta_3 = 0.939° .
$$

The angle is small, which retroactively justifies the small-angle work in (b).

**(b)**

$$
\Delta y = \frac{\lambda L}{d} = \frac{(546\times10^{-9}\ \text{m})(1.20\ \text{m})}{1.00\times10^{-4}\ \text{m}} = 6.55\times10^{-3}\ \text{m} = 6.55\ \text{mm}.
$$

**(c)** The screen extends from $y = -2.5\ \text{cm}$ to $+2.5\ \text{cm}$, so the highest order that lands on it satisfies $|m|\Delta y \le 25\ \text{mm}$, giving $|m| \le (25\ \text{mm})/(6.55\ \text{mm}) = 3.8$. Orders $m = -3$ through $m = +3$ appear: **seven bright fringes**.

**(d)** In principle, $|m| \le d/\lambda = (1.00\times10^{-4}\ \text{m})/(546\times10^{-9}\ \text{m}) = 183$. The far orders are useless in practice — they lie at large angles where the small-angle formula fails, and (as [Chapter 5](#ch-diffraction-of-light) shows) the finite width of real slits has long since dimmed them to nothing — but the counting matters for gratings.

### Worked Example: The Same Experiment Under Water

The apparatus of the previous example is submerged in water, $n = 1.33$, source and screen included. What happens to the fringe spacing?

The frequency of the light does not change, but its wavelength does: $\lambda_n = \lambda/n = (546\ \text{nm})/1.33 = 411\ \text{nm}$. Nothing in the derivation of $\Delta y = \lambda L/d$ referred to vacuum, so the same formula holds with the *local* wavelength:

$$
\Delta y_{\text{water}} = \frac{\lambda_n L}{d} = \frac{\Delta y}{n} = \frac{6.55\ \text{mm}}{1.33} = 4.93\ \text{mm}.
$$

The pattern contracts by the factor $n$. This is a genuinely useful check on understanding: it is the wavelength *where the interference happens* that sets the scale, and that is also why the thin-film formulas below carry a factor of $n_{\text{film}}$.

## Coherence

Young's experiment works only because both slits are carved out of the *same* wavefront, so the light leaving them keeps a fixed phase relationship. Try the experiment with two separate light bulbs and you see nothing but a uniformly lit screen. The reason is not that light bulbs are dim; it is that they are **incoherent**.

An ordinary thermal source — a filament, a flame, a fluorescent tube — emits light as an enormous number of independent atomic events. Each excited atom radiates a short burst, a **wave train** lasting perhaps $10^{-8}\ \text{s}$, and the next atom to radiate does so with no memory of the phase of the last. What emerges is therefore a chain of wave trains whose phase jumps randomly every few nanoseconds, as sketched in {numref}`Figure %s <fig:ch04-coherence>`.

```{figure} ../images/ch04-coherence.svg
:label: fig:ch04-coherence
:alt: Top, an unbroken sinusoid representing a perfectly coherent source. Bottom, a sinusoid whose phase jumps abruptly at regular intervals, representing a real source emitting short wave trains.

Coherence. An ideal source (top) maintains a predictable phase indefinitely. A real thermal source (bottom) emits short wave trains whose phase resets at random every coherence time $\tau_c$; any interference pattern formed by one train is replaced by a differently positioned pattern from the next, far faster than a detector can follow. Original schematic generated with matplotlib; see `scripts/figures/`.
```

Two independent sources therefore do produce an interference pattern — but a different one every few nanoseconds, in a random new position each time. Averaged over the nanoseconds to milliseconds that any real detector needs, the fringes wash out completely and the intensities simply add. The pattern is not weak; it is scrambled.

### Temporal Coherence, Coherence Time, and Coherence Length

Two quantities measure how long a source stays predictable:

- The **coherence time** $\tau_c$: roughly the duration of one uninterrupted wave train, the time over which the phase remains predictable.
- The **coherence length** $\ell_c = c\,\tau_c$: the corresponding path-length difference over which fringes survive. If the two arms of an interference experiment differ by much more than $\ell_c$, the light recombining at the screen comes from two *different*, unrelated wave trains, and there is nothing stable to interfere.

Coherence length is set by the spectral purity of the source. A wave train of finite duration $\tau_c$ cannot be perfectly monochromatic — Fourier analysis gives it a spread of frequencies $\Delta f \sim 1/\tau_c$ — and converting to wavelength gives the useful estimate

$$
\ell_c \approx \frac{\lambda^2}{\Delta\lambda}.
$$

The representative values in {numref}`Table %s <tab:ch04-coherence-lengths>` span an extraordinary range:

```{table} Representative coherence lengths for common light sources
:label: tab:ch04-coherence-lengths

| Source | $\lambda$ | $\Delta\lambda$ | $\ell_c \approx \lambda^2/\Delta\lambda$ |
|---|---|---|---|
| White light | $550\ \text{nm}$ | $\sim 300\ \text{nm}$ | $\sim 1\ \mu\text{m}$ (about two wavelengths) |
| Filtered sodium lamp | $589\ \text{nm}$ | $\sim 0.6\ \text{nm}$ | $\sim 0.6\ \text{mm}$ |
| Helium–neon laser | $633\ \text{nm}$ | $\sim 0.002\ \text{nm}$ | $\sim 20\ \text{cm}$ |
| Stabilized single-mode laser | $633\ \text{nm}$ | $\sim 10^{-6}\ \text{nm}$ | hundreds of meters |
```

A closely related way to say the same thing: the number of fringes you can count before the pattern fades is roughly

$$
N_{\text{fringes}} \approx \frac{\ell_c}{\lambda} \approx \frac{\lambda}{\Delta\lambda}.
$$

White light gives you two or three fringes — which is exactly what Young saw, and exactly why the colored fringes of a soap bubble are confined to a film only a few wavelengths thick. A helium–neon laser gives several hundred thousand.

### Spatial Coherence

Temporal coherence is about a single point in the beam staying predictable *over time*. **Spatial coherence** is about two *different* points across the beam having a fixed phase relationship *at the same time*, and it is what Young's first slit provides. An extended source — the Sun's disk, a broad filament — has poor spatial coherence, because light arriving at $S_1$ and light arriving at $S_2$ come from different, unrelated emitters. Passing the light through a pinhole first discards almost all of it but leaves what remains spatially coherent, since it all now originates from a region small enough to act as a single point.

A laser is coherent in both senses at once, which is why a laser pointer and a pair of razor-blade slits reproduce in seconds an experiment that took Young considerable ingenuity.

### Worked Example: Will the Fringes Survive?

A Michelson interferometer (below) has arms differing in length by $\Delta L = 5.0\ \text{cm}$, so the two recombining beams differ in path by $2\Delta L = 10\ \text{cm}$. Will fringes be visible with (a) a filtered sodium lamp, (b) a helium–neon laser?

**(a)** From {numref}`Table %s <tab:ch04-coherence-lengths>`, $\ell_c \approx 0.6\ \text{mm}$ for the sodium lamp. The path difference of $10\ \text{cm}$ exceeds this by a factor of about $170$, so the beams arriving together come from unrelated wave trains: **no fringes**.

**(b)** For the laser, $\ell_c \approx 20\ \text{cm}$, comfortably larger than the $10\ \text{cm}$ path difference: **fringes are visible**, though with reduced contrast since the path difference is a sizable fraction of $\ell_c$.

This is not a contrived exercise. Michelson had to keep his arms equal to within a fraction of a millimeter precisely because his sodium light had a coherence length of well under a millimeter — a serious experimental constraint in 1887, and one that vanished with the invention of the laser.

## Intensity: Adding Fields as Phasors

The conditions derived so far locate the bright and dark fringes but say nothing about the brightness in between. To get the full pattern we must add the two waves properly, and the most convenient bookkeeping for that is the **phasor**.

Because both waves have the same frequency, their relative phase does not change with time; only their common phase does. Represent each wave by a vector (a phasor) whose length is the wave's amplitude and whose direction gives its phase. The whole diagram rotates rigidly at the optical frequency, so we may freeze it at any instant; adding the waves is then just adding the vectors, and the length of the resultant vector is the amplitude of the combined wave.

```{figure} ../images/ch04-phasors.svg
:label: fig:ch04-phasors
:alt: Panel a, two equal phasors at angle phi with their resultant. Panel b, six phasors in a straight line for phase zero. Panel c, six phasors forming a closed hexagon.

Phasor addition. (a) Two equal phasors separated by $\phi$ form an isosceles triangle whose base is the resultant, $E = 2E_0\cos(\phi/2)$. (b) With $N$ slits and $\phi = 0$ all the phasors line up, giving $E = NE_0$ and hence $I = N^2I_1$. (c) When $\phi = 2\pi/N$ the chain closes on itself and the resultant vanishes — the first zero, at only $1/N$ of the way to the next principal maximum. Original schematic generated with matplotlib; see `scripts/figures/`.
```

### Two Slits

For the double slit, two phasors of equal length $E_0$ are separated by the angle

$$
\phi = \frac{2\pi}{\lambda}\,d\sin\theta .
$$

They form an isosceles triangle ({numref}`Figure %s(a) <fig:ch04-phasors>`). The resultant bisects the angle between them, and dropping a perpendicular gives immediately

$$
E = 2E_0\cos\!\left(\frac{\phi}{2}\right).
$$

Squaring, and writing $I_1 \propto E_0^2$ for the intensity one slit alone would produce,

$$
I(\theta) = 4I_1\cos^2\!\left(\frac{\phi}{2}\right) = I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right), \qquad I_0 \equiv 4I_1 .
$$

The result is plotted in {numref}`Figure %s <fig:ch04-two-slit-intensity>`. It reproduces everything derived earlier — $I = I_0$ whenever $d\sin\theta = m\lambda$, and $I = 0$ whenever $d\sin\theta = (m+\frac12)\lambda$ — and now fills in the smooth $\cos^2$ variation between.

```{figure} ../images/ch04-two-slit-intensity.svg
:label: fig:ch04-two-slit-intensity
:alt: A cosine-squared intensity curve versus path difference in wavelengths, with orders m labeled at the maxima, and a strip above showing the corresponding bright and dark fringes.

Two-slit intensity, $I = I_0\cos^2(\pi d\sin\theta/\lambda)$, with the corresponding fringe pattern above. All the maxima have the same height and the fringes are evenly spaced — a signature of ideal, infinitesimally narrow slits. Real slits impose the envelope derived in [Chapter 5](#ch-diffraction-of-light). Generated with matplotlib; see `scripts/figures/`.
```

### Where Does the Extra Light Come From?

The central maximum has intensity $I_0 = 4I_1$: four times what *one* slit would deliver, not twice. Students often find this alarming, and they should — until they check the energy budget.

The resolution is that $\cos^2$ averages to $\frac12$. Averaged across the pattern, the intensity is

$$
\langle I\rangle = 4I_1 \times \tfrac12 = 2I_1,
$$

which is exactly the two slits' worth of light that entered. Interference does not create or destroy energy; it **redistributes** it, taking light from the dark fringes and piling it into the bright ones. The factor of four at the peaks is paid for by the zeros in between.

This is worth stating sharply, because it is the cleanest possible refutation of a classical particle picture of light: opening a second slit makes some places on the screen *darker* than they were with one slit open. No stream of independent corpuscles can do that.

### Worked Example: Intensity Between the Fringes

For the mercury-lamp double slit above ($d = 0.100\ \text{mm}$, $\lambda = 546\ \text{nm}$, $L = 1.20\ \text{m}$), at what distance from the center of the pattern does the intensity fall to half its maximum?

Set $I = I_0/2$:

$$
\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right) = \frac12
\quad\Longrightarrow\quad
\frac{\pi d\sin\theta}{\lambda} = \frac{\pi}{4}
\quad\Longrightarrow\quad
d\sin\theta = \frac{\lambda}{4}.
$$

So the half-intensity point occurs at a quarter-wavelength path difference — one quarter of the way from a bright fringe to the next dark one. In small-angle terms $y = \Delta y/4$:

$$
y = \frac{6.55\ \text{mm}}{4} = 1.64\ \text{mm}.
$$

The full width at half maximum of each fringe is therefore $2y = 3.28\ \text{mm}$, exactly half the fringe spacing. Two-slit fringes are broad and sinusoidal — which, as the next section shows, is precisely what more slits fix.

## Three Slits, and Then $N$

Add a third identical slit, equally spaced. What changes?

The principal maxima do not move. At $d\sin\theta = m\lambda$, *every* slit is in step with every other, so all three phasors point the same way, the resultant is $3E_0$, and the intensity is $9I_1$. Adding slits at the same spacing can never shift these directions; it just adds more phasors to an already aligned stack.

What changes is where the *first zero* falls. With two slits, the resultant vanishes when the second phasor is antiparallel to the first: $\phi = \pi$. With three slits, the three phasors close into an equilateral triangle — and hence sum to zero — as soon as $\phi = 2\pi/3$, well before $\phi$ reaches $\pi$. The maximum has become narrower. With $N$ slits, the chain closes into a regular $N$-gon at $\phi = 2\pi/N$ ({numref}`Figure %s(c) <fig:ch04-phasors>`), so the first zero sits only $1/N$ of the way to the next principal maximum.

Summing the general chain is a geometric series. Writing each successive phasor as the previous one multiplied by $e^{i\phi}$, the total field is $E_0(1 + e^{i\phi} + e^{2i\phi} + \cdots + e^{i(N-1)\phi})$, whose magnitude works out to $E_0\,|\sin(N\phi/2)/\sin(\phi/2)|$. Squaring gives the **$N$-slit intensity pattern**

$$
I(\theta) = I_1\left[\frac{\sin(N\phi/2)}{\sin(\phi/2)}\right]^2, \qquad \phi = \frac{2\pi}{\lambda}d\sin\theta ,
$$

where $I_1$ is the intensity from a single slit. Setting $N = 2$ recovers the two-slit result, since $\sin\phi/\sin(\phi/2) = 2\cos(\phi/2)$.

{numref}`Figure %s <fig:ch04-n-slit>` collects the consequences:

- **Principal maxima** occur wherever $\phi$ is a multiple of $2\pi$, that is $d\sin\theta = m\lambda$ — the same directions as for two slits, for any $N$. Their height is $N^2I_1$.
- **Zeros** occur at $\phi = 2\pi p/N$ for every integer $p$ that is *not* a multiple of $N$. There are $N-1$ zeros between consecutive principal maxima, and hence $N-2$ much weaker **secondary maxima** squeezed between them.
- **Width.** Since the first zero is at $\phi = 2\pi/N$, the angular half-width of a principal maximum scales as $1/N$: doubling the number of illuminated slits halves the width of every line.

```{figure} ../images/ch04-n-slit-intensity.svg
:label: fig:ch04-n-slit
:alt: Four stacked intensity plots for N equal to 2, 3, 5 and 20 slits, showing principal maxima at the same positions becoming progressively narrower with weak secondary maxima between them.

Interference from $N$ equally spaced ideal slits. The principal maxima stay at $d\sin\theta = m\lambda$ regardless of $N$, but they grow taller (peak $\propto N^2$) and narrower (width $\propto 1/N$), and $N-2$ weak secondary maxima appear between them. Each panel is scaled to its own peak. Generated with matplotlib; see `scripts/figures/`.
```

The two scalings work together. The peak height grows as $N^2$ while the width shrinks as $1/N$, so the energy in each principal maximum grows only as $N$ — as it must, since $N$ slits admit $N$ times as much light. What you gain by adding slits is not more light in total but light concentrated into sharper and sharper spikes at precisely determined angles. Since those angles depend on $\lambda$, a device with very many slits becomes an extremely precise wavelength meter. That device is the **diffraction grating**, and it is taken up — together with the complication that real slits have finite width — in [Chapter 5](#ch-diffraction-of-light).

### Worked Example: Locating the Zeros of a Five-Slit Pattern

Five slits with $d = 2.00\ \mu\text{m}$ are illuminated at $\lambda = 500\ \text{nm}$. Find the directions of the principal maxima, and of the zeros lying between the central maximum and the first-order maximum.

Principal maxima: $\sin\theta = m\lambda/d = m(500\ \text{nm})/(2000\ \text{nm}) = 0.250\,m$, giving $m = 0,\pm1,\pm2,\pm3$ at $\sin\theta = 0, 0.250, 0.500, 0.750$, plus $m = \pm4$ exactly at $\sin\theta = 1$ (grazing, and not observable).

Zeros: $\phi = 2\pi p/5$ means $d\sin\theta = p\lambda/5$, so

$$
\sin\theta = \frac{p\lambda}{Nd} = \frac{p(500\ \text{nm})}{5(2000\ \text{nm})} = 0.0500\,p ,
$$

for $p = 1,2,3,4$ (the value $p = 5$ is excluded — it is the first-order principal maximum). The four zeros lie at $\sin\theta = 0.050, 0.100, 0.150, 0.200$, and between them sit $N - 2 = 3$ secondary maxima. Note that the first zero is at $\sin\theta = 0.050$, one fifth of the way to the first principal maximum at $0.250$: the central peak is five times narrower than the two-slit peak would be.

## Thin-Film Interference

The most familiar interference in everyday life needs no slits at all. The colors swirling on a soap bubble, the rainbow sheen of oil on a wet road, and the faint purple cast of a coated camera lens are all produced by light reflecting from the two surfaces of a very thin transparent layer.

{numref}`Figure %s <fig:ch04-thin-film-rays>` shows the situation. Light striking a film of thickness $t$ and refractive index $n_{\text{film}}$ partially reflects at the front surface (ray 1) and partially enters the film, reflects from the back surface, and re-emerges (ray 2). The two emerging beams are parallel, and the eye or a lens brings them together to interfere.

```{figure} ../images/ch04-thin-film-rays.svg
:label: fig:ch04-thin-film-rays
:alt: A ray striking a thin film, splitting into a front-surface reflection labeled with a pi phase shift and a back-surface reflection with no phase shift, and the extra optical path 2 n t marked.

Thin-film interference. Ray 1 reflects from the front surface, where the index increases, and picks up a $\pi$ phase shift. Ray 2 makes a round trip inside the film, acquiring an extra optical path $2n_{\text{film}}t$, and reflects from the back surface, where the index decreases, with no shift. The net phase difference is the sum of the two effects. Original schematic generated with matplotlib; see `scripts/figures/`.
```

### The Two Contributions

**Optical path.** At near-normal incidence, ray 2 travels an extra geometric distance $2t$, all of it inside the film. By the optical-path rule, this corresponds to a phase difference of

$$
\phi_{\text{path}} = \frac{2\pi}{\lambda}\,2n_{\text{film}}t ,
$$

with $\lambda$ the vacuum wavelength. The factor $n_{\text{film}}$ is not optional: the film packs more wavelengths into the same thickness.

**Phase shift on reflection.** Reflection at a boundary where the refractive index *increases* (light in a lower-index medium striking a higher-index one) flips the sign of the reflected field — an extra phase shift of exactly $\pi$. Reflection at a boundary where the index *decreases* produces no shift. The mechanical analog is a wave on a string: a pulse reflecting from a fixed end (a heavy string beyond, the "denser" case) comes back inverted, while a pulse reflecting from a free end (a light string beyond) comes back upright. "Higher refractive index" plays the role of "heavier string".

That analog is worth more than a sentence, because the sign is the one thing students reliably get wrong and it is not something to be memorized. {numref}`Figure %s <fig:ch04-reflection-sim>` launches a pulse down a chain of masses and springs terminated either rigidly or freely, and the inversion is not scripted into the simulation: it falls out of the boundary condition, exactly as the $\pi$ shift falls out of matching the electric field across an optical interface. A fixed end cannot move, so the reflected pulse must arrive with the opposite sign to cancel the incident one there; a free end has nothing to push against, and the pulse returns upright.

```{openphysics} StandingWaves
:screen: 1
:label: fig:ch04-reflection-sim

A pulse reflecting from a rigid termination and from a free one, side by side on the same clock. The rigid end inverts the pulse and the free end does not — the mechanical statement of the $0$-or-$\pi$ rule used throughout this section.
```

### Assembling the Conditions

Because the reflection shifts are either $0$ or $\pi$, the two reflections in {numref}`Figure %s <fig:ch04-thin-film-rays>` can only produce a *net* relative shift of $0$ or $\pi$. This gives a reliable three-step recipe:

1. Check the front reflection. Does the index increase going into the film? If so, that ray gets $\pi$.
2. Check the back reflection. Does the index increase going out of the film into whatever lies beyond? If so, that ray gets $\pi$.
3. If exactly one of the two picked up $\pi$, the net reflection shift is $\pi$; if both did or neither did, it is $0$.

**Case A — net shift of $\pi$** (exactly one reflection flips). This covers a soap film in air, an oil slick on water, and an air gap trapped between two glass plates. Bright reflection needs the path contribution to supply the missing half wavelength:

$$
2n_{\text{film}}t = \left(m+\tfrac12\right)\lambda \qquad (\text{constructive reflection}),
$$
$$
2n_{\text{film}}t = m\lambda \qquad (\text{destructive reflection}).
$$

**Case B — net shift of $0$** (both flip, or neither does). This covers any film whose index lies between those of the media on either side — an antireflection coating on glass, or an oil film on a denser substrate. The conditions are exactly reversed:

$$
2n_{\text{film}}t = m\lambda \qquad (\text{constructive reflection}),
$$
$$
2n_{\text{film}}t = \left(m+\tfrac12\right)\lambda \qquad (\text{destructive reflection}).
$$

Getting the case wrong swaps bright for dark everywhere, so it is worth the ten seconds it takes to check.

### Why Soap Films Are Colored — and Why They Go Black

Since the conditions involve $\lambda$, a film illuminated with white light reflects some wavelengths strongly and suppresses others, and the favored wavelength shifts as the thickness changes. {numref}`Figure %s <fig:ch04-thin-film-color>` shows the reflected intensity of red, green, and blue light as a function of the thickness of a soap film in air.

```{figure} ../images/ch04-thin-film-color.svg
:label: fig:ch04-thin-film-color
:alt: Reflected intensity versus film thickness for red, green and blue light from a soap film, three sine-squared curves of different periods, with a shaded region near zero thickness where all three vanish.

Reflected intensity from a soap film in air ($n = 1.33$) versus film thickness, for three visible wavelengths. Different colors peak at different thicknesses, which is why a draining soap film shows moving bands of color. As $t \to 0$ all three curves go to zero: the film turns black just before it bursts. Generated with matplotlib; see `scripts/figures/`.
```

Two features of the figure are worth dwelling on. First, the three curves peak at different thicknesses, so a soap film whose thickness varies from place to place — as it always does, since gravity drains it — shows bands of color that drift downward as the film thins. Second, and more striking: as $t\to0$ *all* the curves go to zero. A film very much thinner than $\lambda/4n_{\text{film}}$ contributes almost no path difference, so the two reflections are left with only the $\pi$ shift and cancel for every visible wavelength at once. The film goes **black** — a genuinely counterintuitive prediction, and one you can verify by watching a soap film held vertically in a wire loop: a black band appears at the top, spreads downward, and moments later the film bursts. Newton described this effect in the 1670s, without being able to explain it.

### Worked Example: The Color of a Soap Film

A soap film ($n = 1.33$) in air is $100\ \text{nm}$ thick. Which visible wavelength does it reflect most strongly, viewed at normal incidence?

This is Case A (air–film–air, so only the front reflection flips), and constructive reflection requires $2n_{\text{film}}t = (m + \frac12)\lambda$. Solving for $\lambda$:

$$
\lambda = \frac{2n_{\text{film}}t}{m + \frac12}.
$$

For $m = 0$: $\lambda = 2(1.33)(100\ \text{nm})/0.5 = 532\ \text{nm}$ — green. For $m = 1$: $\lambda = (266\ \text{nm})/1.5 = 177\ \text{nm}$, deep in the ultraviolet and invisible. So this film looks green, and only the $m = 0$ order matters. That is characteristic of thin films: they are thin enough that only the lowest one or two orders land in the visible, which is why their colors are broad and pastel rather than a sequence of sharp spectral lines.

### Worked Example: An Antireflection Coating

A camera lens ($n_{\text{glass}} = 1.52$) is coated with magnesium fluoride ($n_{\text{MgF}_2} = 1.38$) to minimize reflection at $\lambda = 550\ \text{nm}$, the middle of the visible spectrum where the eye is most sensitive. Light is incident from air. Find the minimum coating thickness.

Apply the recipe. Front reflection: air ($1.00$) into $\text{MgF}_2$ ($1.38$) — index increases, so $\pi$. Back reflection: $\text{MgF}_2$ ($1.38$) into glass ($1.52$) — index increases again, so $\pi$. Both flip: this is **Case B**, net shift $0$, and destructive reflection requires the odd-quarter-wave condition

$$
2n_{\text{MgF}_2}t = \left(m+\tfrac12\right)\lambda .
$$

The thinnest coating uses $m = 0$:

$$
t = \frac{\lambda}{4n_{\text{MgF}_2}} = \frac{550\ \text{nm}}{4(1.38)} = 99.6\ \text{nm} \approx 100\ \text{nm},
$$

the standard "quarter-wave" coating. Two remarks. First, the cancellation is not perfect even at $550\ \text{nm}$, because the two reflected beams have slightly different amplitudes; complete cancellation would require $n_{\text{coating}} = \sqrt{n_{\text{air}}n_{\text{glass}}} = 1.23$, and $\text{MgF}_2$ at $1.38$ is simply the closest durable material available. Second, the condition is wavelength-specific: at $450\ \text{nm}$ and $700\ \text{nm}$ the same coating still suppresses reflection, but only partially. The residual reflection is therefore richer in blue and red than in green, which is exactly the faint purple sheen you see on a coated lens.

### Wedges and Newton's Rings

A film need not have uniform thickness. Press two flat glass plates together and separate one edge with a thin spacer — a hair, a wire, a sheet of paper — and the air gap between them forms a **wedge** whose thickness grows linearly along the plates. This is Case A: at the glass-to-air surface the index *decreases*, so there is no shift, while at the air-to-glass surface below it increases, so that reflection flips. Exactly one flip, net shift $\pi$, and with $n_{\text{film}} = 1$ for air the dark fringes fall where $2t = m\lambda$ — including at $t = 0$, so the line of contact is dark. That dark contact line is a useful check that you have assigned the case correctly.

If the wedge has thickness $D$ at a distance $L$ from the contact line, then $t = Dx/L$ at position $x$, and successive dark fringes are separated by

$$
\Delta x = \frac{\lambda L}{2D}.
$$

Counting the fringes over the whole length gives $2D/\lambda$, so the wedge is a way of measuring a very small thickness by counting a large number.

Replace the top plate with a slightly convex lens resting on the flat and the fringes become concentric circles: **Newton's rings**. For a lens of radius of curvature $R$, geometry gives the gap at radius $r$ as $t \approx r^2/2R$, so the dark rings fall at

$$
r_m = \sqrt{m\lambda R}, \qquad m = 0, 1, 2,\ldots
$$

with a dark spot at the center. The rings crowd together as $m$ grows, since $r_m\propto\sqrt m$. Newton's rings remain a standard optical-shop test: any departure of the ring pattern from perfect circles reveals a departure of the surface from a perfect sphere, at a sensitivity of a fraction of a wavelength.

### Worked Example: Measuring a Wire with an Air Wedge

Two flat glass plates $10.0\ \text{cm}$ long are in contact at one end and separated at the other by a thin wire. Illuminated from above with sodium light ($\lambda = 589\ \text{nm}$), the plates show $170$ dark fringes between the contact line and the wire. Find the wire's diameter.

The wire's diameter is the wedge thickness $D$ at the far end. Dark fringes occur wherever $2t = m\lambda$, so the fringe count from $t = 0$ to $t = D$ is $m_{\max} = 2D/\lambda$:

$$
D = \frac{m_{\max}\lambda}{2} = \frac{170\,(589\times10^{-9}\ \text{m})}{2} = 5.01\times10^{-5}\ \text{m} = 50.1\ \mu\text{m}.
$$

The plate length never entered — it only sets the fringe *spacing*, $\Delta x = \lambda L/2D = 0.589\ \text{mm}$, which is what makes the fringes countable by eye. A $50\ \mu\text{m}$ wire has been measured to within a fraction of a micrometer using nothing but two pieces of glass, a sodium lamp, and patience.

## The Michelson Interferometer

The **Michelson interferometer** ({numref}`Figure %s <fig:ch04-michelson>`) is Young's two-path experiment rebuilt with mirrors, and it is the most consequential single instrument in this book.

```{figure} ../images/ch04-michelson.svg
:label: fig:ch04-michelson
:alt: Schematic of a Michelson interferometer with a source, beam splitter, compensator plate, a movable mirror and a fixed mirror on perpendicular arms, and circular fringes at the detector.

The Michelson interferometer. A beam splitter divides the incoming light into two perpendicular arms; each returns from a mirror and the two recombine at the splitter. Moving one mirror by $\delta$ changes that arm's round trip by $2\delta$ and sweeps $2\delta/\lambda$ fringes past the detector. The compensator plate equalizes the amount of glass traversed by the two beams. Original schematic generated with matplotlib; see `scripts/figures/`.
```

A beam splitter — a half-silvered mirror — divides an incoming beam into two perpendicular paths of lengths $L_1$ and $L_2$. Each path ends at a mirror that sends the light back, and the beam splitter recombines the two returning beams and sends them to a detector. The round-trip path difference is $2(L_1 - L_2)$, so the recombined beams interfere according to

$$
\Delta r = 2(L_1 - L_2).
$$

Now translate one mirror through a distance $\delta$. That arm's round trip changes by $2\delta$, and the fringe pattern shifts by

$$
\Delta N = \frac{2\delta}{\lambda} \qquad\text{fringes}.
$$ (eq:ch04-michelson-fringe-count)

One full fringe passes the detector for every *half* wavelength of mirror motion. Since $\lambda/2 \approx 300\ \text{nm}$ for visible light, and fringe positions can be interpolated to a small fraction of a fringe, the instrument measures displacements of a few nanometers. That is the whole reason for its importance: it converts a length comparison into a fringe count, and light's wavelength is a very fine ruler.

The small tilted plate in {numref}`Figure %s <fig:ch04-michelson>` is the **compensator**. Without it, the beam going to $M_2$ passes through the glass of the beam splitter three times while the beam going to $M_1$ passes through it once — a large and, worse, wavelength-dependent optical path difference. The compensator is an identical piece of uncoated glass placed in the other arm so that both beams traverse the same thickness. It is unnecessary with a laser but essential with white light.

Both arms, and the fringes they produce, can be manipulated directly in
{numref}`Figure %s <fig:ch04-interferometry-sim>`. Translating one mirror sweeps the fringe count
given by Equation {eq}`eq:ch04-michelson-fringe-count`; shortening the coherence length
washes the fringes out, which is the constraint of the next section made
visible.

```{openphysics} InterferometryLab
:label: fig:ch04-interferometry-sim

A physical-optics model of the Michelson interferometer, together with the
Mach–Zehnder and Fabry–Pérot geometries. Move a mirror and count fringes; change
the source's coherence length and watch the visibility collapse.
```

### Worked Example: Counting Fringes

In a Michelson interferometer illuminated with sodium light, $\lambda = 589\ \text{nm}$, one mirror is slowly translated and $1200$ fringes are counted passing a reference mark. How far did the mirror move?

$$
\delta = \frac{\Delta N\,\lambda}{2} = \frac{1200\,(589\times10^{-9}\ \text{m})}{2} = 3.53\times10^{-4}\ \text{m} = 0.353\ \text{mm}.
$$

Note the leverage: a third of a millimeter of motion, resolved into $1200$ countable events.

### Worked Example: The Refractive Index of Air

A transparent cell of length $L = 5.00\ \text{cm}$ is placed in one arm and slowly evacuated. As the air is pumped out, $49.7$ fringes are counted. Find the refractive index of air at $\lambda = 589\ \text{nm}$.

The light crosses the cell twice, so removing air of index $n$ changes the optical path by $2L(n-1)$, and the fringe count is

$$
\Delta N = \frac{2L(n-1)}{\lambda} \quad\Longrightarrow\quad n - 1 = \frac{\Delta N\,\lambda}{2L} = \frac{49.7\,(589\times10^{-9}\ \text{m})}{2(0.0500\ \text{m})} = 2.93\times10^{-4},
$$

so $n = 1.000293$ — the accepted value for dry air at standard conditions. The interferometer has measured a refractive index that differs from unity in the fourth decimal place, from a fringe count that a student can do by eye.

### What Interferometers Are For

- **The Michelson–Morley experiment.** As described in [Chapter 1](#ch-need-for-relativity), rotating the apparatus should have exchanged the roles of the arm parallel to Earth's motion through the ether and the arm perpendicular to it, shifting the fringes by about $0.4$ fringe against a sensitivity of $0.01$ fringe. No shift was ever seen, at any orientation or any time of year. The fringe-counting relation in Equation {eq}`eq:ch04-michelson-fringe-count` is exactly what converted a null optical measurement into a decisive statement about the structure of spacetime.
- **Fourier-transform spectroscopy.** Record the detector signal as a function of mirror position and you have the *autocorrelation* of the light; its Fourier transform is the spectrum. Nearly every infrared spectrometer in a modern chemistry laboratory is a Michelson interferometer operated this way.
- **Metrology.** Surface flatness, machine-tool calibration, and — until the 1983 redefinition of the meter in terms of $c$ — the international length standard itself.
- **Gravitational-wave detection.** LIGO and Virgo are Michelson interferometers with $4\ \text{km}$ arms, folded optically to an effective length of hundreds of kilometers, measuring mirror displacements of order $10^{-19}\ \text{m}$ — about one ten-thousandth of a proton's radius. The first detection, in September 2015, came from two merging black holes $1.3$ billion light-years away. The instrument that failed to find the ether became the instrument that found the ripples in spacetime that replaced it.

## Looking Ahead: Interference One Photon at a Time

Everything in this chapter treats light as a classical wave, and the treatment works. It is worth flagging now, though, that the story does not end here.

Turn the source in Young's experiment down. Not a little — down until the light is so faint that, on average, only one quantum of light is inside the apparatus at any moment. A $1\ \text{mW}$ helium–neon laser emits about $3\times10^{15}$ photons per second; light crosses a meter-long apparatus in about $3\ \text{ns}$; so a rate below roughly $10^{8}$ photons per second guarantees that each one arrives, passes the slits, and lands before the next is emitted. G. I. Taylor performed the experiment in 1909 using an attenuated gas flame and a three-month exposure, and it has been repeated countless times since with single-photon sources and imaging detectors.

The result is that the screen records individual, localized hits — dots, one at a time, apparently at random. But as the dots accumulate over hours, they build up precisely the $\cos^2$ fringe pattern derived in this chapter. Each photon interferes with itself; there is no second photon for it to interfere with. That fact cannot be accommodated by any picture in which the photon simply goes through one slit or the other, and it is the central puzzle that [Chapters 6](#ch-particle-properties-of-waves) and [7](#ch-wave-properties-of-particles) take up.

For now, the wave description stands on its own, and the next chapter completes it.

## Summary

- **Light is an electromagnetic wave.** Detectors measure the time-averaged intensity, $I \propto E_0^2$, so *amplitudes* superpose and the intensity is the square of the sum — never the sum of the intensities. In a medium of index $n$, the wavelength shrinks to $\lambda/n$, and what governs interference is the **optical path length** $nd$.
- **Wave effects hide behind a small number.** The only dimensionless quantity available is $\lambda/a$, and for everyday apertures it is $\sim10^{-4}$. Ray optics is wave optics in the limit $\lambda/a \to 0$ — an instance of the correspondence principle.
- **Huygens's principle** treats every point of a wavefront as a source of secondary wavelets whose envelope is the later wavefront; it predicts that waves spread after an aperture, by an amount governed by $\lambda/a$.
- **Path difference becomes phase difference** through $\phi = (2\pi/\lambda)\Delta r$. Constructive interference requires $\Delta r = m\lambda$, destructive requires $\Delta r = (m+\frac12)\lambda$.
- **Young's double slit** gives bright fringes at $d\sin\theta = m\lambda$ and dark fringes at $d\sin\theta = (m+\frac12)\lambda$; for $L \gg d$ and small angles, the fringes are evenly spaced with $\Delta y = \lambda L/d$. Only orders with $|m| \le d/\lambda$ exist.
- **Coherence** is required for a stable pattern. Real sources emit short wave trains with randomly resetting phase; the **coherence time** $\tau_c$ and **coherence length** $\ell_c = c\tau_c \approx \lambda^2/\Delta\lambda$ set the largest usable path difference, and $\lambda/\Delta\lambda$ estimates the number of visible fringes. Spatial coherence — supplied by Young's first slit, or built into a laser — is what lets two slits act as one source.
- **Phasor addition** gives the two-slit intensity $I = I_0\cos^2(\pi d\sin\theta/\lambda)$ with $I_0 = 4I_1$. The factor of four is offset by the zeros: the pattern *redistributes* energy, averaging back to $2I_1$.
- **$N$ equally spaced slits** give $I = I_1[\sin(N\phi/2)/\sin(\phi/2)]^2$. Principal maxima stay at $d\sin\theta = m\lambda$, rise as $N^2$, and narrow as $1/N$, with $N-2$ weak secondary maxima between them — the basis of the diffraction grating ([Chapter 5](#ch-diffraction-of-light)).
- **Thin films** interfere via the extra optical path $2n_{\text{film}}t$ plus any $\pi$ shift from reflection at a boundary where the index increases. Count the shifts first: one flip gives constructive reflection at $2n_{\text{film}}t = (m+\frac12)\lambda$; zero or two flips reverse the conditions. This explains soap-film colors, the black film, quarter-wave antireflection coatings, wedge fringes, and Newton's rings ($r_m = \sqrt{m\lambda R}$).
- **The Michelson interferometer** converts a mirror displacement $\delta$ into a fringe count $\Delta N = 2\delta/\lambda$, giving nanometer sensitivity. It produced the null result of [Chapter 1](#ch-need-for-relativity), and, scaled to kilometers, the first detection of gravitational waves.

## Conceptual Questions

1. Two flashlights are aimed at the same spot on a wall. Explain, in terms of coherence time, why no interference fringes appear, even though two light waves are certainly overlapping there.

2. In Young's experiment, what happens to the fringe spacing if (a) the slit separation $d$ is doubled, (b) the screen distance $L$ is doubled, (c) the light is changed from red to blue, (d) one slit is covered? Answer each in one sentence.

3. The central maximum in a double-slit pattern has four times the intensity that one slit alone would produce. Explain why this does not violate conservation of energy, and state where the extra energy comes from.

4. Explain why the $m = 0$ fringe is white when a double slit is illuminated with white light, while every other fringe is colored.

5. A soap film held vertically in a wire loop develops a black band at the top just before it bursts. Explain why the film appears black there rather than showing some color, and why the band appears at the *top*.

6. A camera lens with an antireflection coating still shows a faint purple reflection. Explain why the coating cannot eliminate reflection at all visible wavelengths at once.

7. Two glass plates in contact at one edge form an air wedge. Is the fringe at the line of contact bright or dark? Justify your answer by counting phase shifts on reflection, and explain what you would conclude if you observed the opposite.

8. Explain why a Michelson interferometer with arms differing by several centimeters shows fringes with a laser but not with a sodium lamp, even though the sodium lamp is far from white.

## Problems

1. Light of wavelength $633\ \text{nm}$ (a helium–neon laser) illuminates two slits separated by $d = 0.120\ \text{mm}$. Find the angle $\theta$ to (a) the third bright fringe and (b) the second dark fringe, measured from the central axis.

2. In a double-slit experiment with $d = 0.250\ \text{mm}$ and a screen at $L = 1.40\ \text{m}$, bright fringes are observed with spacing $\Delta y = 3.30\ \text{mm}$. Find the wavelength of the light used, and identify approximately its color.

3. A double slit with $d = 0.0800\ \text{mm}$ is illuminated at $\lambda = 480\ \text{nm}$ with the screen $2.50\ \text{m}$ away. (a) Find the fringe spacing. (b) How many bright fringes fall on a screen $8.0\ \text{cm}$ wide, centered on the axis? (c) What is the largest order that exists in principle?

4. Two identical in-step sources emit light of wavelength $620\ \text{nm}$. Find the smallest nonzero path difference that produces (a) a bright point, (b) a dark point, (c) a point whose intensity is half the maximum.

5. The double slit of Problem 3 is immersed, along with its source and screen, in a liquid of refractive index $n = 1.47$. Find the new fringe spacing, and explain in one sentence why the answer does not depend on where in the apparatus the liquid is.

6. A source has a central wavelength of $600\ \text{nm}$ and a wavelength spread $\Delta\lambda = 0.02\ \text{nm}$, typical of a good single-mode laser. (a) Estimate its coherence length. (b) Estimate the number of fringes visible before the pattern washes out. (c) Repeat both estimates for white light, $\lambda \approx 550\ \text{nm}$ with $\Delta\lambda \approx 300\ \text{nm}$, and comment on why Young's original experiment showed only a handful of fringes.

7. Starting from $I = I_0\cos^2(\phi/2)$ with $\phi = (2\pi/\lambda)d\sin\theta$, show that the full width at half maximum of each fringe is exactly half the fringe spacing, independent of $\lambda$, $d$, and $L$.

8. Using the $N$-slit intensity formula, evaluate $I(\theta = 0)$ for $N = 2$ and $N = 4$ slits with the same single-slit intensity $I_1$, and verify the scaling $I_{\max}\propto N^2$. Then show that the total light delivered by $N$ slits is proportional to $N$, not $N^2$, by combining the peak height with the peak width.

9. Six equally spaced slits with $d = 3.00\ \mu\text{m}$ are illuminated at $\lambda = 600\ \text{nm}$. (a) Find $\sin\theta$ for all the principal maxima. (b) Find the directions of the zeros between the central and first-order maxima. (c) How many secondary maxima lie between them?

10. A soap film ($n = 1.33$) in air is viewed at near-normal incidence with $\lambda = 500\ \text{nm}$ light. (a) Explain, by counting reflections, why only one of the two picks up a $\pi$ shift. (b) Find the two smallest nonzero thicknesses at which the film appears bright in reflection. (c) Find the smallest nonzero thickness at which it appears dark.

11. A thin layer of oil ($n = 1.45$) floats on water ($n = 1.33$). (a) Determine whether this is Case A or Case B in the classification of this chapter. (b) Find the minimum oil thickness that reflects $\lambda = 600\ \text{nm}$ light strongly. (c) Repeat parts (a) and (b) for the same oil film resting instead on a substrate of index $1.60$, and explain why the answer changes by a factor of two.

12. Design an antireflection coating of magnesium fluoride ($n = 1.38$) on glass ($n = 1.52$) that minimizes reflection at $\lambda = 600\ \text{nm}$ in air. (a) Find the minimum thickness. (b) Compute $2n_{\text{coating}}t/\lambda$ at $450\ \text{nm}$ and at $700\ \text{nm}$, and use the results to explain the residual purple reflection of coated optics.

13. A plano-convex lens with radius of curvature $R = 2.00\ \text{m}$ rests on a flat glass plate and is illuminated from above with $\lambda = 589\ \text{nm}$ light. (a) Find the radius of the tenth dark ring. (b) Explain why the center of the pattern is dark. (c) Explain why the rings crowd closer together as $m$ increases.

14. Two flat plates $15.0\ \text{cm}$ long touch at one end and are separated at the other by a sheet of foil. Illuminated at $\lambda = 546\ \text{nm}$, the plates show dark fringes spaced $0.750\ \text{mm}$ apart. Find the thickness of the foil.

15. In a Michelson interferometer illuminated at $\lambda = 546\ \text{nm}$, one mirror is translated by $0.200\ \text{mm}$. How many fringes pass a reference mark?

16. A gas cell $8.00\ \text{cm}$ long in one arm of a Michelson interferometer is filled with carbon dioxide at atmospheric pressure, and $122$ fringes are counted as it fills. Find the refractive index of carbon dioxide at $\lambda = 589\ \text{nm}$.

17. Explain, using the concept of optical path length, why the thin-film conditions use $2n_{\text{film}}t$ rather than $2t$, and estimate the error you would make in the predicted color of a $100\ \text{nm}$ soap film if you dropped the factor of $n$.

18. Revisit the Michelson–Morley experiment of [Chapter 1](#ch-need-for-relativity) using this chapter's fringe-shift relation. The predicted ether-wind path difference between the two arms was of order $Lv^2/c^2$ for arm length $L$ and Earth's orbital speed $v \approx 3\times10^4\ \text{m/s}$. Estimate the expected fringe shift for $L = 11\ \text{m}$ and $\lambda = 590\ \text{nm}$, and compare it with the experiment's sensitivity of about $0.01$ fringe.

19. LIGO measures mirror displacements of about $10^{-19}\ \text{m}$ using $\lambda = 1064\ \text{nm}$ light. (a) Using $\Delta N = 2\delta/\lambda$, find the corresponding fringe shift. (b) Your answer should be an absurdly small fraction of a fringe; explain what this implies about the additional techniques (optical cavities that fold the beam path, and averaging over enormous photon numbers) that a real detector must use.

20. A double slit is illuminated with light containing two wavelengths, $480\ \text{nm}$ and $600\ \text{nm}$, with $d = 0.150\ \text{mm}$ and $L = 2.00\ \text{m}$. Find the smallest nonzero distance from the center of the screen at which a bright fringe of one wavelength coincides exactly with a bright fringe of the other.
