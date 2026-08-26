---
title: Diffraction of Light
short_title: Chapter 5. Diffraction of Light
label: ch-diffraction-of-light
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain diffraction as a consequence of the Huygens–Fresnel principle applied to a finite-width aperture, and distinguish it conceptually from the idealized (zero-width-slit) interference of [Chapter 4](#ch-interference-of-light).
- Derive and apply the single-slit diffraction minimum condition, and describe the resulting intensity pattern.
- Explain how a real double slit's pattern combines two-slit interference with single-slit diffraction, including the phenomenon of missing orders.
- Describe how a diffraction grating produces sharp spectral lines, and apply its resolving power to spectroscopic problems.
- Apply the Rayleigh criterion to determine the angular resolution limit of a circular aperture, and use it to evaluate the resolving power of telescopes, microscopes, and the eye.
- State Bragg's law and use it to relate X-ray diffraction angles to interatomic spacing in a crystal.

## Introduction

[Chapter 4](#ch-interference-of-light) developed interference for idealized, infinitesimally narrow slits: point-like Huygens sources whose emitted wavelets combine according to their path-length differences alone. A real slit, however, has a finite width $a$, and every point across that width, not just its two edges, emits Huygens wavelets that must be summed. This chapter takes up the resulting phenomenon, **diffraction**: the way waves spread out and produce their own characteristic interference pattern after passing through a finite aperture or around an obstacle — most famously, the way a single narrow slit alone, with no second slit needed at all, produces a pattern of bright and dark bands. Diffraction is not a fundamentally different phenomenon from the interference of [Chapter 4](#ch-interference-of-light); both follow from exactly the same Huygens-wavelet superposition, applied now to a continuum of sources across a finite aperture rather than to a discrete set of idealized point sources. The distinction is one of bookkeeping, not physics — but it has an inescapable practical consequence: diffraction imposes a fundamental limit on the resolution of every optical instrument, from the human eye to the largest telescope, a limit no amount of engineering improvement can circumvent.

## The Huygens–Fresnel Principle Applied to an Aperture

Augustin-Jean Fresnel extended Huygens's geometrical construction ([Chapter 4](#ch-interference-of-light)) into a quantitative theory by treating every point across an open aperture as a source of secondary wavelets of equal amplitude, and computing the resulting field at any observation point by summing (integrating) the contributions from every such point, with their appropriate phases. This **Huygens–Fresnel principle** correctly predicts both the interference patterns of [Chapter 4](#ch-interference-of-light) (in the limit of vanishingly narrow slits, where only a discrete handful of point sources need be summed) and the diffraction patterns of this chapter (where a continuum of sources across a finite-width aperture must be summed). The distant-screen case relevant to most of this chapter — where the aperture is small and the screen is far enough away that the diffracted wavefronts arriving at the screen are effectively planar — is called **Fraunhofer diffraction**, and it is the case treated throughout this chapter.

## Single-Slit Diffraction

Consider a single slit of width $a$ illuminated by a plane wave of wavelength $\lambda$, with a screen far away ($L\gg a$). To find the directions of zero intensity, divide the slit conceptually into two equal halves, each of width $a/2$. Light from the top half and the corresponding point in the bottom half (a distance $a/2$ apart) will be exactly out of phase — and hence cancel — whenever their path difference is $\lambda/2$:

$$
\frac{a}{2}\sin\theta = \frac{\lambda}{2} \quad \Longrightarrow \quad a\sin\theta = \lambda.
$$

The same pairing argument, applied by dividing the slit into $2, 4, 6,\ldots$ equal strips instead of $2$, generalizes this to the full set of **single-slit diffraction minima**:

$$
a\sin\theta = m\lambda, \qquad m = \pm1,\pm2,\pm3,\ldots \qquad (\text{diffraction minima}),
$$

with $m=0$ conspicuously *excluded*: unlike double-slit interference, where $m=0$ locates a bright central fringe, here the central region ($\theta=0$) is a broad **central maximum**, and the pairwise-cancellation argument only ever produces minima, never a formula for maxima (the maxima between successive minima must instead be found from the full intensity pattern below, and do not fall at simple fractional positions). The central maximum is bounded by the two first-order minima at $\sin\theta = \pm\lambda/a$, giving it an angular half-width $\theta_1 \approx \lambda/a$ (for $\lambda \ll a$) and making it, notably, *twice as wide* as any of the smaller secondary maxima that follow on either side.

### Worked Example: Central Maximum Width

A slit of width $a = 0.0400\ \text{mm}$ is illuminated by light of wavelength $\lambda = 580\ \text{nm}$, with a screen $L=2.00\ \text{m}$ away. Find the width of the central diffraction maximum.

The first minima occur at $\sin\theta_1 = \lambda/a = (580\times10^{-9})/(0.0400\times10^{-3}) = 0.0145$, so $\theta_1 \approx 0.0145\ \text{rad}$ (small-angle approximation). The corresponding position on the screen is $y_1 = L\tan\theta_1 \approx L\theta_1 = (2.00)(0.0145) = 0.0290\ \text{m}$, so the full central maximum, spanning from $-y_1$ to $+y_1$, has width

$$
w = 2y_1 = 5.80\ \text{cm}.
$$

Notice that a *narrower* slit ($a$ smaller) produces a *wider* central maximum — diffraction spreads light out more, not less, as the aperture shrinks, the opposite of the naive geometric-shadow intuition that a narrower opening should produce a narrower, sharper-edged beam.

## Intensity in Single-Slit Diffraction

Carrying out the Huygens–Fresnel phasor sum across the continuum of point sources spanning the slit width $a$ (a calculation that becomes an integral rather than a discrete sum, but is conceptually the same phasor-addition procedure used for the discrete slits of [Chapter 4](#ch-interference-of-light)) gives the single-slit intensity pattern

$$
I(\theta) = I_0\left[\frac{\sin(\beta/2)}{\beta/2}\right]^2, \qquad \beta \equiv \frac{2\pi}{\lambda}a\sin\theta,
$$

often written using the normalized $\mathrm{sinc}$ function, $I(\theta) = I_0\,\mathrm{sinc}^2(\beta/2)$. This correctly reproduces the minima found above: $I=0$ whenever $\beta/2 = m\pi$ for nonzero integer $m$, i.e. $a\sin\theta = m\lambda$, while at $\theta=0$, $\beta\to0$ and $\sin(\beta/2)/(\beta/2)\to1$ (the removable-singularity limit of $\sin x/x$ as $x\to0$), giving the maximum possible intensity $I_0$. The secondary maxima, located approximately (but not exactly) midway between successive minima, fall off rapidly in intensity moving away from the center: the first secondary maximum reaches only about $4.5\%$ of $I_0$, the second about $1.6\%$, and so on — which is why, to the eye, a single-slit diffraction pattern appears as one dominant bright central band with faint, rapidly fading side bands, rather than a series of comparably bright fringes.

## Double-Slit Diffraction: Interference and Diffraction Combined

A *real* double slit — two slits, each of finite width $a$, separated center-to-center by $d$ — exhibits both effects of the preceding two sections simultaneously: the two-slit interference pattern of [Chapter 4](#ch-interference-of-light) (governed by $d$), multiplied by the single-slit diffraction envelope of this chapter (governed by $a$):

$$
I(\theta) = I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right)\left[\frac{\sin(\beta/2)}{\beta/2}\right]^2, \qquad \beta = \frac{2\pi}{\lambda}a\sin\theta.
$$

The rapidly-oscillating $\cos^2$ factor produces the closely-spaced interference fringes (spacing set by the *larger* length scale $d$), while the more slowly-varying $\mathrm{sinc}^2$ factor modulates their overall intensity, suppressing fringes that fall near a diffraction minimum. This produces the characteristic feature of real double-slit patterns: **missing orders**, in which an interference maximum predicted by $d\sin\theta = m\lambda$ is suppressed to essentially zero intensity because it happens to coincide with a diffraction minimum $a\sin\theta = m'\lambda$ for some integer $m'$ — which occurs whenever $d/a$ is itself an integer, since then every $(d/a)$-th interference order is silently erased by a coincident diffraction minimum. Observing which interference orders are missing, and at what spacing, is in fact a practical way to measure the ratio $d/a$ for a given double-slit apparatus without independently measuring $a$ and $d$ directly.

## Diffraction Gratings

The idealized $N$-slit interference pattern of [Chapter 4](#ch-interference-of-light) assumed each slit was infinitesimally narrow. A real **diffraction grating** — thousands of parallel slits (or, in a reflection grating, finely ruled reflective grooves) per millimeter, spaced a distance $d$ apart — combines the same $N$-slit sharpening effect with the finite-width diffraction envelope of this chapter, but because $N$ is so enormous (typically $10^3$–$10^4$ slits illuminated at once), the principal maxima predicted by $d\sin\theta = m\lambda$ become extraordinarily narrow, sharp spectral lines, easily resolved and precisely measurable even though a small number of orders may be suppressed as "missing" in the same manner as the double slit.

The most important practical property of a grating is its **resolving power**: its ability to distinguish two closely spaced wavelengths, $\lambda$ and $\lambda + \Delta\lambda$, as separate spectral lines rather than a single blurred line. Two lines are considered *just* resolved, by the (same) Rayleigh-type criterion developed below for imaging systems, when the principal maximum of one coincides with the first zero of intensity of the other. Working through this condition for an $N$-slit grating gives the simple result

$$
R \equiv \frac{\lambda}{\Delta\lambda} = mN,
$$

where $m$ is the diffraction order being used. This shows that resolving power improves both by using more illuminated grating lines $N$ and by working at a higher diffraction order $m$ — which is why precision spectroscopy uses gratings ruled with as many lines as practically possible, and why, for a given grating, the second- or third-order spectrum resolves closely spaced spectral lines (such as the sodium doublet) that the first-order spectrum cannot.

### Worked Example: Resolving the Sodium Doublet

The well-known **sodium doublet** consists of two closely spaced yellow spectral lines at $\lambda_1 = 589.0\ \text{nm}$ and $\lambda_2 = 589.6\ \text{nm}$, so $\Delta\lambda = 0.6\ \text{nm}$ and $\lambda/\Delta\lambda \approx 982$. Find the minimum number of illuminated grating lines $N$ needed to resolve this doublet in first order ($m=1$).

From $R = mN$,

$$
N = \frac{R}{m} = \frac{982}{1} \approx 982\ \text{lines},
$$

so a grating illuminated over a width containing at least about $1000$ lines will just resolve the two sodium lines in first order — a modest requirement easily met by any standard laboratory grating, which typically has many thousands of lines per centimeter.

## Circular Apertures and the Rayleigh Criterion

Every real optical instrument — the eye's pupil, a camera lens, a telescope's primary mirror — collects light through a *circular* aperture of diameter $D$, not a slit, so its diffraction pattern is the circularly symmetric analog of the single-slit pattern: a bright central spot (the **Airy disk**) surrounded by faint concentric rings. The mathematics of a circular aperture (an integral over a disk rather than a line segment) is more involved than the single-slit case, but the result is structurally the same, with a numerical factor $1.22$ arising from the specific geometry of a circular opening: the angle to the first minimum (the edge of the Airy disk) is

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D}.
$$

Lord Rayleigh proposed that two point sources (two stars, or two nearby features on a microscope slide) should be considered *just barely resolvable* — distinguishable as two separate objects rather than one blurred blob — when the angular separation between them equals this $\theta_{\min}$: that is, when the center of one source's Airy disk falls exactly on the first dark ring of the other's. This **Rayleigh criterion**,

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D},
$$

sets an absolute lower limit on the angular resolution of *any* optical instrument with aperture diameter $D$, regardless of the quality of its lenses or mirrors: no amount of optical engineering can resolve two objects separated by less than $\theta_{\min}$, because the limitation is diffraction itself, a direct consequence of light's finite wavelength passing through a finite aperture, not a correctable manufacturing imperfection. This is why larger telescopes resolve finer angular detail (larger $D$, smaller $\theta_{\min}$) even when built from mirrors of comparable optical quality, and why microscopy is fundamentally limited in the finest detail it can resolve using visible light, motivating the shorter-wavelength probes (electron beams; see [Chapter 7](#ch-wave-properties-of-particles)) used in electron microscopy to push past this limit.

### Worked Example: Resolving Two Stars

The Hubble Space Telescope has a primary mirror of diameter $D = 2.4\ \text{m}$. Estimate its diffraction-limited angular resolution for visible light ($\lambda = 550\ \text{nm}$), and find the minimum separation of two features on the Moon (distance $3.84\times10^8\ \text{m}$) that it could just resolve.

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D} = 1.22\,\frac{550\times10^{-9}\ \text{m}}{2.4\ \text{m}} = 2.80\times10^{-7}\ \text{rad},
$$

an angle of about $0.058$ arcseconds. At the Moon's distance, this corresponds to a linear separation of

$$
s = \theta_{\min} \times (3.84\times10^8\ \text{m}) = 108\ \text{m},
$$

illustrating both the remarkable resolving power such a large aperture affords and the fact that even a diffraction-limited space telescope cannot resolve arbitrarily fine detail — a fundamental, not merely technological, limit.

## X-Ray Diffraction and Bragg's Law

Visible-light diffraction gratings have line spacings ($d\sim$ micrometers) comparable to visible wavelengths, which is precisely the condition needed to produce well-separated diffraction orders. The regularly repeating planes of atoms in a crystalline solid, spaced by only a few tenths of a nanometer, are far too closely spaced for visible light to resolve via diffraction — but that same spacing is comparable to the wavelength of **X-rays**, making crystals natural three-dimensional diffraction gratings for X-ray wavelengths, first demonstrated by Max von Laue in 1912.

W. L. Bragg and W. H. Bragg gave the simplest quantitative treatment: model the crystal as a stack of parallel atomic planes spaced by a distance $d$ (a different, crystallographic $d$ from the grating-line spacing above, though playing an analogous role), and consider X-rays reflecting specularly off successive planes. Two rays reflecting off adjacent planes, at a grazing angle $\theta$ measured from the plane itself (not from the normal, by crystallographic convention), travel an extra path length $2d\sin\theta$ (twice the distance $d\sin\theta$ each ray effectively penetrates deeper before "reflecting"). Constructive interference between rays reflected from successive planes therefore requires

$$
n\lambda = 2d\sin\theta \qquad (\textbf{Bragg's law}), \qquad n = 1,2,3,\ldots,
$$

with $n$ the diffraction order. Measuring the angles $\theta$ at which strong reflected X-ray intensity is observed, for X-rays of known wavelength $\lambda$, directly yields the interplanar spacing $d$ — the basic technique of **X-ray crystallography**, responsible for determining the atomic structure of everything from table salt to (via the diffraction pattern obtained by Rosalind Franklin and Raymond Gosling) the double-helix structure of DNA.

### Worked Example: Interplanar Spacing from a Bragg Reflection

X-rays of wavelength $\lambda = 0.154\ \text{nm}$ (a standard copper $K_\alpha$ laboratory source) produce a first-order ($n=1$) Bragg reflection at $\theta = 22.5°$ from a crystal sample. Find the spacing between the reflecting atomic planes.

$$
d = \frac{n\lambda}{2\sin\theta} = \frac{(1)(0.154\ \text{nm})}{2\sin(22.5°)} = \frac{0.154\ \text{nm}}{2(0.383)} = 0.201\ \text{nm},
$$

a spacing consistent with typical interatomic distances in a crystal lattice, and exactly the kind of measurement used to determine crystal structures from a series of such reflections at different angles and orientations.

Bragg diffraction is not restricted to X-rays: any wave with a wavelength comparable to the interatomic spacing will diffract from a crystal lattice in the same way, including the electron matter-waves taken up in [Chapter 7](#ch-wave-properties-of-particles) — Davisson and Germer's 1927 observation of exactly this kind of diffraction pattern, using electrons reflected from a nickel crystal, provided the first direct experimental confirmation that matter itself has wave properties.

## Summary

- Diffraction and interference both follow from the same Huygens–Fresnel superposition principle; diffraction refers to the pattern produced by summing contributions across a *finite-width* aperture rather than a discrete set of idealized point sources.
- **Single-slit diffraction** produces minima at $a\sin\theta = m\lambda$ ($m$ a nonzero integer) and an intensity pattern $I(\theta) = I_0[\sin(\beta/2)/(\beta/2)]^2$ with $\beta = (2\pi/\lambda)a\sin\theta$; the central maximum is twice as wide as the secondary maxima and dominates the pattern, since secondary maxima fall off rapidly (the first reaches only about $4.5\%$ of $I_0$).
- A real double slit's pattern is the two-slit interference pattern (period set by $d$) multiplied by the single-slit diffraction envelope (width set by $a$); coincidence of an interference maximum with a diffraction minimum produces a **missing order**.
- A **diffraction grating**'s many slits sharpen the interference principal maxima into narrow spectral lines; its resolving power, $R = \lambda/\Delta\lambda = mN$, improves with more illuminated lines $N$ and higher order $m$.
- A circular aperture of diameter $D$ produces an Airy pattern with first minimum at $\theta_{\min} = 1.22\lambda/D$; the **Rayleigh criterion** takes this as the angular resolution limit of any optical instrument with that aperture, a fundamental diffraction limit independent of optical quality.
- **Bragg's law**, $n\lambda = 2d\sin\theta$, describes constructive interference of waves reflecting from successive planes in a crystal lattice; applied to X-rays, it is the basis of X-ray crystallography, and applies equally to any wave — including, as Davisson and Germer showed, electron matter waves ([Chapter 7](#ch-wave-properties-of-particles)) — with a wavelength comparable to the lattice spacing.

## Problems

1. A single slit of width $a = 0.0250\ \text{mm}$ is illuminated by light of wavelength $633\ \text{nm}$. Find the angles to the first and second diffraction minima.

2. A slit of unknown width produces a central diffraction maximum $4.00\ \text{cm}$ wide on a screen $1.50\ \text{m}$ away, using light of wavelength $520\ \text{nm}$. Find the slit width.

3. Explain, using the pairwise-cancellation argument, why $\theta=0$ is never a diffraction minimum for a single slit, no matter how the slit is divided into pairs of strips.

4. A double slit has slit width $a = 0.020\ \text{mm}$ and slit separation $d = 0.100\ \text{mm}$. (a) Find the ratio $d/a$. (b) Determine which interference orders $m$ (if any, up to $m=6$) are "missing" because they coincide with a single-slit diffraction minimum.

5. A diffraction grating has $5000$ lines per centimeter. (a) Find the line spacing $d$. (b) Find the angle of the first-order maximum for light of wavelength $500\ \text{nm}$. (c) Find the highest order $m$ observable for this wavelength (recall that $\sin\theta$ cannot exceed $1$).

6. A grating with $N = 4000$ illuminated lines is used in second order ($m=2$). Find the smallest wavelength difference $\Delta\lambda$ it can resolve near $\lambda = 600\ \text{nm}$, and compare this resolving power to the same grating used in first order.

(ex-diffraction-of-light-7)=
7. The human eye has a pupil diameter of about $D = 4.0\ \text{mm}$ in typical lighting. Using the Rayleigh criterion with $\lambda = 550\ \text{nm}$, estimate the smallest angular separation the eye can resolve, and the corresponding minimum separation of two objects viewed at a distance of $25\ \text{cm}$ (a comfortable reading distance).

8. A car's two headlights are separated by $1.3\ \text{m}$. Using the eye's diffraction limit from [Problem 7](#ex-diffraction-of-light-7), estimate the maximum distance at which an observer could, in principle, resolve them as two separate points of light rather than one, and comment on whether atmospheric conditions or the eye's actual optical imperfections might set a more restrictive limit in practice.

9. X-rays of wavelength $\lambda = 0.0709\ \text{nm}$ produce a first-order Bragg reflection at $\theta = 15.0°$ from a set of crystal planes. Find the spacing between the planes, and find the angle at which the second-order ($n=2$) reflection from the same planes occurs.

10. A crystal has an interplanar spacing of $d = 0.282\ \text{nm}$ (close to the value for table salt, NaCl). Find the X-ray wavelength that would produce a first-order Bragg reflection at $\theta = 20.0°$, and state whether this wavelength lies in the X-ray part of the electromagnetic spectrum.

11. Explain physically why a narrower single slit produces a *wider* central diffraction maximum, using the relationship $\theta_1 \approx \lambda/a$, and contrast this with the (opposite) way a *wider* aperture improves a telescope's angular resolution via the Rayleigh criterion. Are these two statements in tension? Explain why or why not.

12. A telescope's objective diameter is doubled while keeping the observing wavelength fixed. By what factor does its diffraction-limited angular resolution (the smallest resolvable angle) improve? By what factor would the resolution improve instead if the diameter were kept fixed but observations were switched from visible light ($\lambda \approx 550\ \text{nm}$) to near-ultraviolet light ($\lambda \approx 275\ \text{nm}$)?
