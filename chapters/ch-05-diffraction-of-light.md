---
title: Diffraction of Light
short_title: Chapter 5. Diffraction of Light
label: ch-diffraction-of-light
numbering:
  enumerator: "5.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain diffraction as the Huygens–Fresnel principle applied to a continuum of sources across a finite aperture, and say precisely how it differs — and does not differ — from the interference of [Chapter 4](#ch-interference-of-light).
- Distinguish Fresnel (near-field) from Fraunhofer (far-field) diffraction, and decide which applies in a given geometry.
- Derive the single-slit minimum condition by the pairwise-cancellation argument, and explain why $m = 0$ is excluded.
- Sketch and use the single-slit intensity pattern, including the width of the central maximum and the rapid decline of the secondary maxima.
- Explain how a real double slit's pattern is the product of a two-slit interference factor and a single-slit envelope, and locate missing orders.
- Apply the grating equation, compute angular dispersion, and use the resolving power $R = mN$ in spectroscopic problems.
- Apply the Rayleigh criterion for a circular aperture to telescopes, microscopes, and the eye, and distinguish the diffraction limit from practical limits such as atmospheric seeing.
- State Bragg's law, use it to extract interplanar spacings from measured X-ray diffraction angles, and explain why the same argument applies to electron and neutron beams.
- Describe how a hologram records and reconstructs a wavefront, and explain why it requires a coherent source.
- Use single-slit diffraction to make a first, order-of-magnitude argument for the uncertainty principle of [Chapter 7](#ch-wave-properties-of-particles).

## Introduction

In 1818 the French Academy of Sciences held a prize competition on the nature of light. Augustin-Jean Fresnel submitted a wave theory. Siméon Denis Poisson, a member of the judging committee and a convinced supporter of Newton's particle theory, worked through Fresnel's mathematics and triumphantly produced what he took to be its refutation: if Fresnel were right, then the shadow of a small circular disk, illuminated by a point source, would have a *bright spot at its exact center* — light would diffract around the rim, arrive at the axis having traveled equal distances from every point of that rim, and interfere constructively. The prediction was patently ridiculous.

A member of that committee, François Arago, went and looked. The spot was there.

That bright point — now called the Poisson spot, or the Arago spot, depending on whose role in the story one prefers to emphasize — is a fair emblem for this chapter. **Diffraction** is what waves do when they encounter an obstacle or a finite aperture: they bend into the geometric shadow, and they interfere with themselves in the process, producing patterns of light and dark that no ray-tracing argument can generate.

[Chapter 4](#ch-interference-of-light) worked with idealized slits: point-like Huygens sources, infinitesimally narrow, contributing one wavelet apiece. A real slit has a finite width $a$, and *every* point across that width emits a wavelet. Summing those contributions is the whole subject of this chapter. Three results follow, in increasing order of consequence. First, a single slit, all by itself, produces a pattern of bright and dark bands. Second, real multiple-slit devices — above all the diffraction grating — combine the sharp interference maxima of [Chapter 4](#ch-interference-of-light) with a diffraction envelope that decides how bright each of those maxima actually is. Third, and most importantly, because every real optical instrument gathers light through an aperture of finite size, diffraction sets an absolute limit on the fineness of detail any instrument can resolve — a limit that no improvement in polishing, alignment, or manufacture can evade, because it is imposed by the wavelength of light itself.

## Diffraction Versus Interference: A Note on Words

It is worth settling a piece of vocabulary that causes more confusion than it should.

There is no physical distinction between interference and diffraction. Both are the same thing: coherent waves from different places arriving at a common point and adding as fields. The words differ only in bookkeeping convention. When the sources are a small, discrete set — two slits, five slits — the custom is to say *interference* and to write a sum. When the sources form a continuum across an aperture, the custom is to say *diffraction* and to write an integral. Richard Feynman put it bluntly: "no one has ever been able to define the difference between interference and diffraction satisfactorily. It is just a question of usage, and there is no specific, important physical difference between them."

The reason the distinction survives is practical. In a real double slit there are two length scales — the slit separation $d$ and the slit width $a$, with $d > a$ — and they produce structure on two very different angular scales. Calling the fine structure "interference" and the coarse envelope "diffraction" is a convenient way to keep track of which is which. That is all it is.

## The Huygens–Fresnel Principle

Fresnel's contribution was to make Huygens's construction quantitative. Where Huygens drew an envelope of wavelets, Fresnel insisted on *adding the wavelets as waves, with their phases*, and then squaring the result to get an intensity. Stated for an aperture:

> Every point of an open aperture acts as a source of secondary wavelets of equal amplitude and of the same phase as the incoming wave at that point. The field at any observation point is the sum, over the whole aperture, of these wavelets, each with the phase it has accumulated on its journey.

This **Huygens–Fresnel principle** reproduces the results of [Chapter 4](#ch-interference-of-light) when the aperture is a set of very narrow slits, and everything in this chapter when it is not. The sum becomes an integral, but the physics — add fields, account for phase, then square — is unchanged.

### Near Field and Far Field

Whether the sum is easy or hard depends on the geometry, and the distinction matters enough to have names.

If the screen is far enough away that the rays converging on any observation point are effectively parallel, the phase of each wavelet is a *linear* function of its position in the aperture, and the integral is elementary. This is **Fraunhofer diffraction**, or far-field diffraction, and it is the case treated throughout this chapter.

If the screen is close, the rays are noticeably non-parallel, the phase varies *quadratically* across the aperture, and the pattern depends in a complicated way on distance. This is **Fresnel diffraction**, or near-field diffraction. The Poisson spot of the introduction is a Fresnel phenomenon; so are the fine bright and dark bands you can see just inside the edge of a sharp shadow cast by a small bright source.

The dividing line is set by the **Fresnel number**

$$
F = \frac{a^2}{L\lambda},
$$

:::{margin}
$F$ is dimensionless — $a^2$ and $L\lambda$ are both areas — so it can be compared directly to $1$ regardless of what length unit $a$, $L$, and $\lambda$ happen to be quoted in, as long as all three use the same one.
:::

where $a$ is the aperture size and $L$ the aperture-to-screen distance. Fraunhofer diffraction applies when $F \ll 1$; Fresnel diffraction when $F \gtrsim 1$. For a $0.05\ \text{mm}$ slit, $550\ \text{nm}$ light, and a screen $2\ \text{m}$ away, $F = (5\times10^{-5}\ \text{m})^2/[(2\ \text{m})(5.5\times10^{-7}\ \text{m})] = 2\times10^{-3}$, comfortably in the far field. Conveniently, a lens converts the far field into something you can put on a bench: any lens placed after the aperture brings the parallel bundles to a focus in its focal plane, so the Fraunhofer pattern appears there no matter how short the bench.

:::{note}
Joseph von Fraunhofer, the optician whose name now labels the entire far-field regime, made his most consequential discovery almost as a side effect. Testing prism spectrometers around 1814, he noticed that the Sun's spectrum was crossed by hundreds of sharp dark lines at fixed wavelengths — the Fraunhofer lines — and went on to rule some of the first precision diffraction gratings by hand, specifically to measure those wavelengths accurately. Decades later, Gustav Kirchhoff and Robert Bunsen explained the lines as absorption by specific elements in the Sun's outer atmosphere, founding the science of spectroscopy that the diffraction grating, later in this chapter, still serves.
:::

## Single-Slit Diffraction

Consider a slit of width $a$ illuminated by a plane wave of wavelength $\lambda$, with a distant screen. The clever step, due to Fresnel, is not to attempt the whole sum at once but to ask a narrower question: *in which directions does everything cancel?*

Divide the slit conceptually into two equal halves, each of width $a/2$, as in {numref}`Figure %s(a) <fig:ch05-pairing>`. Pair up the topmost point of the upper half with the topmost point of the lower half; they are a distance $a/2$ apart. Pair the second point of the upper half with the second point of the lower half; also $a/2$ apart. Every point in the upper half has a partner in the lower half exactly $a/2$ below it. If the light heading off at angle $\theta$ from each pair is exactly out of phase — path difference $\lambda/2$ — then *every* pair cancels, and so does the whole slit:

$$
\frac{a}{2}\sin\theta = \frac{\lambda}{2} \qquad\Longrightarrow\qquad a\sin\theta = \lambda .
$$

```{figure} ../images/ch05-single-slit-pairing.svg
:label: fig:ch05-pairing
:alt: Two panels showing a slit divided into two halves and into four quarters, with a highlighted pair of source points separated by a over 2 and a over 4 and the extra path each pair accumulates.

Canceling the slit against itself. Dividing the slit into two strips pairs each point with a partner $a/2$ away; when those pairs are a half wavelength out of step, the whole slit cancels, giving $a\sin\theta = \lambda$. Dividing into four strips pairs points $a/4$ apart and gives $a\sin\theta = 2\lambda$, and so on. Original schematic generated with matplotlib; see `scripts/figures/`.
```

Repeat the argument with four strips ({numref}`Figure %s(b) <fig:ch05-pairing>`): now partners are $a/4$ apart, each pair cancels when $(a/4)\sin\theta = \lambda/2$, and the whole slit cancels at $a\sin\theta = 2\lambda$. With $2m$ strips the condition is $a\sin\theta = m\lambda$. The complete set of **single-slit minima** is therefore

$$
a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \pm3, \ldots \qquad (\text{diffraction minima}).
$$

Two things about this formula regularly trip people up, and both are worth stating explicitly.

**It locates minima, not maxima.** Compare with the double-slit condition $d\sin\theta = m\lambda$, which locates *maxima*. The two formulas look almost identical and mean opposite things. The distinction is not a convention: it comes from the fact that the pairing argument can only ever demonstrate cancellation.

**$m = 0$ is excluded.** At $\theta = 0$ every point of the slit is in phase with every other, so the wavelets add rather than cancel — there is nothing to pair against. The center of the pattern is a broad, bright **central maximum**, not a minimum. Formally, the pairing argument demands a path difference of $\lambda/2$ within each pair, and $\theta = 0$ supplies a path difference of zero.

### The Width of the Central Maximum

The central maximum is bounded by the first minima on either side, at $\sin\theta = \pm\lambda/a$. Its angular half-width is therefore

$$
\theta_1 = \arcsin\frac{\lambda}{a} \approx \frac{\lambda}{a} \quad (\text{for } \lambda \ll a),
$$

exactly the $\lambda/a$ scaling that the dimensional argument of [Chapter 4](#ch-interference-of-light) demanded. Note that in $\sin\theta$ the central maximum runs from $-\lambda/a$ to $+\lambda/a$, while every other maximum spans only $\lambda/a$: the central peak is **twice as wide** as the rest, in addition to being far brighter.

The most important qualitative consequence is that *narrowing the slit widens the pattern*, as {numref}`Figure %s <fig:ch05-scaling>` shows.

```{figure} ../images/ch05-slit-width-scaling.svg
:label: fig:ch05-scaling
:alt: Four stacked intensity curves for slits of width one, two, five and twenty wavelengths, showing the diffraction pattern narrowing dramatically as the slit widens.

Single-slit patterns for four slit widths. The central maximum spans $\sin\theta = \pm\lambda/a$, so it narrows as the slit widens: a slit $20\lambda$ across concentrates the light into a beam, while a slit only $1\lambda$ across has no minimum at all and radiates almost like a single point source. Generated with matplotlib; see `scripts/figures/`.
```

This is the opposite of the naive expectation that a narrower opening should produce a narrower beam, and it is a genuinely wave-like signature. It also gives the correct picture of the limiting case: when $a \le \lambda$, the condition $\sin\theta = \lambda/a \ge 1$ has no solution, there are no minima anywhere, and the slit radiates into the entire forward hemisphere — behaving, exactly as [Chapter 4](#ch-interference-of-light) assumed, like a single Huygens point source. That is the justification, after the fact, for treating the slits of the double-slit experiment as points.

The inverse relationship between the aperture and its pattern is worth seeing rather than reading about, and {numref}`Figure %s <fig:ch05-diffraction-sim>` shows the two side by side: the aperture on the left, the far-field pattern it produces on the right, with the aperture's size and the wavelength both on sliders. Shrinking the opening spreads the pattern, and by exactly the ratio $\lambda/a$ derived above. Two further controls make the point sharper than a single slit can. Squashing the round aperture into an ellipse produces an elliptical pattern elongated along the *other* axis, so the reciprocity holds direction by direction and not just on average; and the non-circular shapes on offer produce patterns of matching symmetry — an anticipation of the circular-aperture section below, where a round hole is found to give rings rather than a row of bands, and of the crystal lattices at the end of the chapter, where a periodic array of holes gives a periodic array of spots.

```{phet} wave-interference
:screen: 4
:label: fig:ch05-diffraction-sim

An aperture and the far-field diffraction pattern it produces, with aperture size, shape, and wavelength adjustable. Everything narrow in the aperture is wide in the pattern, and vice versa — the $\theta_1 \approx \lambda/a$ scaling of this section, seen whole rather than one angle at a time.
```

### Worked Example: Width of the Central Maximum

A slit of width $a = 0.0400\ \text{mm}$ is illuminated with $\lambda = 580\ \text{nm}$ light, and the pattern is observed on a screen $L = 2.00\ \text{m}$ away. Find the width of the central maximum.

The first minima are at

$$
\sin\theta_1 = \frac{\lambda}{a} = \frac{580\times10^{-9}\ \text{m}}{4.00\times10^{-5}\ \text{m}} = 0.0145,
$$

so $\theta_1 = 0.0145\ \text{rad} = 0.831°$ (the small-angle approximation is excellent here). On the screen,

$$
y_1 = L\tan\theta_1 \approx L\theta_1 = (2.00\ \text{m})(0.0145\ \text{rad}) = 0.0290\ \text{m},
$$

and the central maximum, running from $-y_1$ to $+y_1$, has full width

$$
w = 2y_1 = 5.80\ \text{cm}.
$$

Check the trend: halving the slit width to $0.0200\ \text{mm}$ would double this to $11.6\ \text{cm}$.

### Worked Example: A Slit Too Narrow to Have Minima

At what slit width does the first minimum disappear entirely, for $\lambda = 580\ \text{nm}$?

The first minimum requires $\sin\theta_1 = \lambda/a \le 1$, so it exists only if $a \ge \lambda = 580\ \text{nm}$. A slit narrower than one wavelength produces a smooth, minimum-free spread of light across the whole forward direction. Slits this narrow are difficult to make and transmit very little light, which is why the textbook idealization of a "point source slit" is easier to draw than to build — and why real double-slit experiments always show the envelope discussed below.

## Intensity in Single-Slit Diffraction

The pairing argument gives the zeros; getting the full curve requires actually doing the sum. The phasor picture of [Chapter 4](#ch-interference-of-light) makes this almost graphical.

:::{seealso}
The phasor construction used below is the continuous limit of the discrete $N$-slit phasor sum from [Chapter 4](#ch-interference-of-light): there, finitely many equal-length phasors are added tip-to-tail one at a time; here, infinitely many infinitesimal ones curl smoothly into an arc. Working through that chapter's phasor derivation first makes the "chord of a circular arc" argument below feel like the natural next step rather than a new trick.
:::

Divide the slit into $N$ narrow strips and let $N\to\infty$. Each strip contributes a tiny phasor of the same length, and each is rotated slightly relative to its neighbor, because it sits slightly farther along the slit and so contributes a slightly different path. Let $\beta$ be the *total* phase difference between the wavelet from one edge of the slit and the wavelet from the other:

$$
\beta \equiv \frac{2\pi}{\lambda}\,a\sin\theta .
$$

The chain of tiny phasors therefore turns through a total angle $\beta$ from beginning to end. A chain of equal segments turning at a uniform rate is an arc of a circle, and the resultant field is its **chord** ({numref}`Figure %s <fig:ch05-phasor-arc>`).

```{figure} ../images/ch05-phasor-arc.svg
:label: fig:ch05-phasor-arc
:alt: Three panels showing a chain of small phasors, straight for zero phase, curled into a semicircular arc, and closed into a full circle with zero resultant.

The single-slit phasor construction. The wavelets from across the slit form a chain of equal phasors turning through a total angle $\beta$. At $\theta = 0$ the chain is straight and the resultant equals the full arc length. As $\theta$ grows the chain curls and the chord falls behind the arc. At $\beta = 2\pi$ the chain closes into a circle and the resultant vanishes — the first minimum, $a\sin\theta = \lambda$. Original schematic generated with matplotlib; see `scripts/figures/`.
```

Everything follows from the geometry of a circular arc. Let the arc length be $E_0$ (this is the resultant at $\theta = 0$, when the chain is straight). An arc of length $E_0$ subtending angle $\beta$ has radius $R = E_0/\beta$, and the chord across it is $2R\sin(\beta/2)$. So

$$
E = 2\frac{E_0}{\beta}\sin\frac{\beta}{2} = E_0\,\frac{\sin(\beta/2)}{\beta/2},
$$

and squaring gives the **single-slit intensity pattern**

$$
I(\theta) = I_0\left[\frac{\sin(\beta/2)}{\beta/2}\right]^2, \qquad \beta = \frac{2\pi}{\lambda}a\sin\theta .
$$

The quantity in brackets is $\mathrm{sinc}(\beta/2)$, where $\mathrm{sinc}(x) \equiv \sin x / x$, so the pattern is often written $I = I_0\,\mathrm{sinc}^2(\beta/2)$.

:::{margin}
Two conventions for $\mathrm{sinc}$ circulate. The one used here, $\mathrm{sinc}(x) \equiv \sin x/x$, has its first zero at $x = \pi$. An engineering convention, common in signal-processing texts, instead defines $\mathrm{sinc}(x) \equiv \sin(\pi x)/(\pi x)$, with its first zero at $x = 1$. Check which one a source is using before comparing formulas across it.
:::

Three checks confirm this is the right answer:

- At $\theta = 0$, $\beta \to 0$ and $\sin(\beta/2)/(\beta/2)\to 1$, giving $I = I_0$: the central maximum.
- $I = 0$ whenever $\beta/2 = m\pi$ with $m$ a nonzero integer, i.e. $a\sin\theta = m\lambda$ — precisely the pairing-argument minima. The case $m = 0$ is excluded automatically, because $\sin x/x \to 1$ rather than $0$ there.
- The chord can never exceed the arc, so $I \le I_0$ everywhere.

```{figure} ../images/ch05-single-slit-intensity.svg
:label: fig:ch05-single-slit-intensity
:alt: The sinc-squared single-slit intensity curve with side lobes shown at twenty times magnification and labeled 4.7, 1.6 and 0.8 percent, with the corresponding fringe pattern strip above.

Single-slit diffraction intensity. The central maximum is twice as wide as the side lobes and vastly brighter — the first side lobe reaches only $4.7\%$ of the peak, so it is shown here magnified $20\times$. The strip above shows the pattern as it appears on a screen, with faint bands brightened so they reproduce. Generated with matplotlib; see `scripts/figures/`.
```

### The Secondary Maxima

Where are the maxima between the zeros? Setting $\mathrm{d}I/\mathrm{d}\beta = 0$ gives the transcendental condition $\tan(\beta/2) = \beta/2$, which has no closed-form solution. Solving numerically puts the secondary maxima at

$$
\frac{\beta}{2} = 1.4303\pi,\ 2.4590\pi,\ 3.4707\pi,\ \ldots
$$

slightly *inside* the naive halfway positions $1.5\pi$, $2.5\pi$, $3.5\pi$ — pulled toward the center because the envelope is falling. Relative to the central peak, the first three secondary maxima reach only

$$
4.7\%, \qquad 1.6\%, \qquad 0.83\%
$$

of $I_0$, falling off roughly as $1/m^2$. This is why a single-slit pattern does not look like a row of comparable fringes at all: it looks like one dominant bright band, flanked by faint ripples that most observers overlook entirely. It is also why {numref}`Figure %s <fig:ch05-single-slit-intensity>` has to magnify them $20\times$ before they are visible on the page.

## Double-Slit Diffraction: Both Effects Together

Now put the two chapters together. A *real* double slit consists of two openings, each of finite width $a$, whose centers are separated by $d > a$. Both effects operate at once, and — because the field from each slit is the single-slit field, and the two slits then interfere — the intensities simply multiply:

$$
I(\theta) = I_0\underbrace{\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right)}_{\text{interference, set by }d}\;\underbrace{\left[\frac{\sin(\beta/2)}{\beta/2}\right]^2}_{\text{diffraction envelope, set by }a}, \qquad \beta = \frac{2\pi}{\lambda}a\sin\theta .
$$

Since $d > a$, the $\cos^2$ factor oscillates rapidly and the $\mathrm{sinc}^2$ factor varies slowly: fine fringes under a broad envelope, as in {numref}`Figure %s <fig:ch05-double-slit>`.

```{figure} ../images/ch05-double-slit-envelope.svg
:label: fig:ch05-double-slit
:alt: Closely spaced interference fringes modulated by a broad single-slit envelope, with markers at the fifth and tenth orders showing the missing orders.

A real double slit with $d = 5a$. The rapid $\cos^2$ fringes are set by the slit separation $d$; the dashed envelope is the single-slit $\mathrm{sinc}^2$ pattern set by the slit width $a$. Orders $m = \pm5$ and $\pm10$ vanish because they coincide with zeros of the envelope. Generated with matplotlib; see `scripts/figures/`.
```

### Missing Orders

The striking feature of {numref}`Figure %s <fig:ch05-double-slit>` is that some interference maxima are simply absent. An interference maximum at $d\sin\theta = m\lambda$ is wiped out if a diffraction minimum, $a\sin\theta = m'\lambda$, falls at the same angle. Dividing one condition by the other, this happens when

$$
\frac{m}{m'} = \frac{d}{a},
$$

that is, whenever $m\,(a/d)$ is an integer. If $d/a$ is itself an integer, every $(d/a)$-th order is missing — for $d = 5a$ the missing orders are $m = \pm5, \pm10, \pm15,\ldots$, exactly as in the figure. If $d/a$ is a ratio of small integers, say $d/a = 5/2$, orders that are multiples of $5$ still vanish but nothing else does. If $d/a$ is irrational, no order is exactly missing, though those near an envelope zero are suppressed almost to nothing.

**Missing orders are a measurement, not a curiosity.** Counting how many interference fringes fit inside the central diffraction maximum tells you $d/a$ directly, without measuring either $d$ or $a$: the central envelope spans $|\sin\theta| < \lambda/a$ and fringes are spaced by $\lambda/d$ in $\sin\theta$, so the visible orders are those with $|m| \le d/a - 1$ — that is, $2(d/a) - 1$ bright fringes inside the central envelope, with the orders at $|m| = d/a$ missing at its edges. Looking at a laboratory double-slit pattern and counting bright fringes between the first envelope zeros is therefore a genuine measurement of a ratio of two dimensions far too small to measure with a ruler.

### Worked Example: Reading a Double-Slit Pattern

A double slit has slit width $a = 0.0200\ \text{mm}$ and separation $d = 0.100\ \text{mm}$, illuminated at $\lambda = 633\ \text{nm}$. (a) Which orders are missing? (b) How many bright fringes lie inside the central diffraction maximum? (c) Find the angular width of the central envelope.

**(a)** $d/a = (0.100\ \text{mm})/(0.0200\ \text{mm}) = 5$, an integer, so orders $m = \pm5, \pm10, \pm15,\ldots$ are missing.

**(b)** The central envelope runs from $\sin\theta = -\lambda/a$ to $+\lambda/a$; the fringes at its edges are the missing $m = \pm5$. The visible orders inside are $m = -4,\ldots,+4$: **nine bright fringes**, of which the central one is brightest.

**(c)** $\sin\theta_{\text{env}} = \lambda/a = (633\times10^{-9}\ \text{m})/(2.00\times10^{-5}\ \text{m}) = 0.0317$, so the envelope's first zeros are at $\theta = \pm1.81°$, giving a full angular width of $3.63°$. On a screen $2.00\ \text{m}$ away that is a central band $12.7\ \text{cm}$ wide, containing nine fringes spaced $\lambda L/d = 12.7\ \text{mm}$ apart — a comfortable laboratory pattern.

## Diffraction Gratings

A **diffraction grating** is the $N$-slit device of [Chapter 4](#ch-interference-of-light) built for real: thousands of parallel slits per millimeter, ruled onto glass (a transmission grating) or onto a reflective surface (a reflection grating, which is what most modern spectrometers use). A compact disc is an accidental reflection grating, its data tracks spaced $1.6\ \mu\text{m}$ apart; a DVD's tracks are $0.74\ \mu\text{m}$ apart, which is why it throws colors more widely.

Everything derived for $N$ ideal slits carries over. The principal maxima satisfy the **grating equation**

$$
d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2,\ldots
$$

with $d$ the spacing between adjacent rulings; their width scales as $1/N$ and their peak intensity as $N^2$. What is new is only that $N$ is now enormous — a $1\ \text{cm}$ beam on a grating with $600$ lines per millimeter illuminates $6000$ lines at once — so the maxima are not fringes but needle-sharp spectral lines. And of course the finite width of each ruling imposes a diffraction envelope, exactly as for the double slit, so some orders are weak or missing. (Precision gratings are *blazed*: each groove is cut at an angle chosen to steer the envelope's peak into a chosen order, so that most of the light ends up where it is wanted rather than in the useless $m = 0$ direction.)

### Dispersion

Because the diffraction angle depends on $\lambda$, a grating spreads white light into a spectrum — one spectrum per order, on each side of the center. Differentiating the grating equation gives the **angular dispersion**

$$
\frac{\mathrm{d}\theta}{\mathrm{d}\lambda} = \frac{m}{d\cos\theta},
$$

so the spectrum spreads out more in higher orders and with finer rulings. It also shows that the orders eventually overlap: the red end of order $m$ can fall on top of the blue end of order $m+1$, which is why spectrometers often place a coarse filter in front of the detector to isolate a single order.

Since $|\sin\theta| \le 1$, the highest order available is $m_{\max} = \lfloor d/\lambda\rfloor$ — a grating so fine that $d < \lambda$ produces no spectrum at all beyond $m = 0$.

:::{tip}
Before trusting any computed grating or Bragg angle, check that the sine you solved for is actually $\le 1$. Both $d\sin\theta = m\lambda$ and $n\lambda = 2d\sin\theta$ are linear in the order and carry no built-in ceiling, so plugging in one order too many silently returns a mathematically valid but physically nonexistent angle. Get in the habit of computing $m_{\max} = \lfloor d/\lambda\rfloor$ (or $n_{\max} = \lfloor 2d/\lambda\rfloor$ for Bragg reflection, later in this chapter) *before* solving for individual angles, so you already know which orders exist.
:::

### Resolving Power

The property that makes gratings scientific instruments rather than ornaments is their **resolving power**: the ability to display two nearly equal wavelengths as two separate lines rather than one blur.

Adopt the Rayleigh criterion — two lines are *just resolved* when the principal maximum of one falls on the first zero of the other. The principal maximum for wavelength $\lambda$ in order $m$ sits at $d\sin\theta = m\lambda$, and its first zero is $\lambda/(Nd\cos\theta)$ away in angle. The line at $\lambda + \Delta\lambda$ sits $m\,\Delta\lambda/(d\cos\theta)$ away. Setting these equal,

$$
\frac{m\,\Delta\lambda}{d\cos\theta} = \frac{\lambda}{Nd\cos\theta}
\qquad\Longrightarrow\qquad
\boxed{\;R \equiv \frac{\lambda}{\Delta\lambda} = mN\;}
$$

{numref}`Figure %s <fig:ch05-resolving-power>` shows the criterion in action. The resolving power depends only on the order and on the number of lines actually illuminated. Two consequences are worth noting. First, resolving power improves with the *illuminated* width of the grating, not with the total number of lines ruled on it; underfilling a grating with a narrow beam throws resolution away. Second, working in second or third order doubles or triples the resolution, at the cost of dimmer lines and increased risk of overlapping orders — a trade every spectroscopist makes.

```{figure} ../images/ch05-grating-resolving-power.svg
:label: fig:ch05-resolving-power
:alt: Three stacked panels showing the sodium doublet recorded with 300, 982 and 3000 illuminated grating lines, going from a single blur to two clearly separated peaks.

Resolving the sodium doublet ($589.0$ and $589.6$ nm) in first order. With too few illuminated lines the two principal maxima are broader than their separation and merge into one feature. At $N = 982$, $R = mN$ equals $\lambda/\Delta\lambda$ and the peak of one line falls on the first zero of the other — the Rayleigh criterion. With $N = 3000$ the lines are cleanly separated. Generated with matplotlib; see `scripts/figures/`.
```

### Worked Example: Resolving the Sodium Doublet

The **sodium doublet** — the pair of yellow lines responsible for the color of a sodium street lamp — consists of lines at $\lambda_1 = 589.0\ \text{nm}$ and $\lambda_2 = 589.6\ \text{nm}$. How many grating lines must be illuminated to resolve them in first order?

The required resolving power is

$$
R = \frac{\lambda}{\Delta\lambda} = \frac{589.0\ \text{nm}}{0.6\ \text{nm}} = 982 .
$$

From $R = mN$ with $m = 1$,

$$
N = \frac{R}{m} = 982\ \text{lines}.
$$

On a grating with $600$ lines per millimeter this needs a beam only $1.64\ \text{mm}$ wide — trivially met by any laboratory setup, which is why the sodium doublet is a standard first-week demonstration. In second order only $491$ lines would be needed. By contrast, resolving the hyperfine structure *within* one of those lines, where $\Delta\lambda \sim 2\times10^{-5}\ \text{nm}$, would demand $R \sim 3\times10^7$ — far beyond any ruled grating, and the reason such measurements use interferometric methods instead.

### Worked Example: A Grating Spectrum

A transmission grating has $5000$ lines per centimeter. (a) Find the line spacing. (b) Find the angle of the first-order maximum for $\lambda = 500\ \text{nm}$. (c) Find the highest observable order. (d) Find the angular separation between the $486\ \text{nm}$ and $656\ \text{nm}$ hydrogen lines in first order.

**(a)** $d = (1\ \text{cm})/5000 = 2.00\times10^{-6}\ \text{m} = 2.00\ \mu\text{m}$.

**(b)** $\sin\theta_1 = \lambda/d = (500\times10^{-9}\ \text{m})/(2.00\times10^{-6}\ \text{m}) = 0.250$, so $\theta_1 = 14.5°$.

**(c)** $m_{\max} = \lfloor d/\lambda\rfloor = \lfloor 4.00\rfloor = 4$, but $m = 4$ gives $\sin\theta = 1.00$ exactly — grazing emergence, unobservable in practice. The highest usable order is $m = 3$, at $\theta = 48.6°$.

**(d)** $\theta(486\ \text{nm}) = \arcsin(0.243) = 14.06°$ and $\theta(656\ \text{nm}) = \arcsin(0.328) = 19.14°$, a separation of $5.08°$. A grating spreads the visible spectrum over several degrees in first order — enough to project a spectrum across a wall.

## Circular Apertures and the Limits of Resolution

Every real optical instrument — a camera lens, a telescope mirror, a microscope objective, the pupil of the eye — collects light through a *circular* aperture of diameter $D$. Its diffraction pattern is the circular analog of the single-slit pattern: a bright central disk, the **Airy disk**, surrounded by faint concentric rings.

The mathematics is harder than the slit case, because the integral runs over a disk rather than a line, and the answer involves a Bessel function rather than a sine. The structure of the result, however, is identical, differing only by a numerical factor that comes from the circular geometry: the first dark ring lies at

$$
\sin\theta_{\min} = 1.22\,\frac{\lambda}{D} \approx \theta_{\min}.
$$

Compare this with $\lambda/a$ for a slit. Nothing has changed except the $1.22$ — which is, in fact, the first zero of the Bessel function $J_1$ divided by $\pi$.

:::{dropdown} Where the factor 1.22 comes from
For a circular aperture of diameter $D$, the far-field amplitude at angle $\theta$ is proportional to the two-dimensional analog of the single-slit integral, evaluated over a disk instead of a line:

$$
E(\theta) \propto \frac{2J_1(kR\sin\theta)}{kR\sin\theta}, \qquad k = \frac{2\pi}{\lambda},\quad R = \frac{D}{2},
$$

where $J_1$ is the Bessel function of the first kind, order one — the circular-geometry replacement for the $\sin x/x$ that came from integrating across a slit. This combination plays exactly the role $\mathrm{sinc}(\beta/2)$ played in the single-slit case: it equals $1$ at zero argument, giving the central Airy peak, and has its first zero at the first zero of $J_1$ itself,

$$
kR\sin\theta_{\min} = 3.8317\ldots
$$

Substituting $k = 2\pi/\lambda$ and $R = D/2$ and solving for $\sin\theta_{\min}$,

$$
\sin\theta_{\min} = \frac{3.8317}{\pi}\,\frac{\lambda}{D} = 1.2197\,\frac{\lambda}{D} \approx 1.22\,\frac{\lambda}{D}.
$$

The extra factor, compared with a slit's plain $\lambda/D$, is a purely geometric consequence of integrating over a disk rather than a line. No new physics enters — only a different shape of aperture.
:::

### The Rayleigh Criterion

Two distant point sources — two stars, or two features on a microscope slide — each produce their own Airy pattern in the image. If the sources are close together in angle, the two patterns overlap and merge into a single blob. Lord Rayleigh proposed a workable convention for where to draw the line: two sources are **just resolved** when the center of one Airy disk falls on the first dark ring of the other. That is, when their angular separation equals

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D} \qquad (\textbf{Rayleigh criterion}).
$$

{numref}`Figure %s <fig:ch05-rayleigh>` shows what this looks like. At the criterion there is a shallow dip between the two peaks — about $26\%$ down from the maxima — which is roughly the smallest contrast a human observer can pick out reliably. The criterion is a convention, not a law of nature: with a high signal-to-noise ratio and a known point-spread function, computational methods routinely do better, and modern super-resolution fluorescence microscopy beats it by orders of magnitude using tricks that exploit the *non*-simultaneity of individual emitters. But as an estimate of what an instrument can do, it is excellent.

```{figure} ../images/ch05-airy-rayleigh.svg
:label: fig:ch05-rayleigh
:alt: Three simulated images of two point sources separated by 0.5, 1.0 and 2.0 times the Rayleigh angle, with intensity cross-sections beneath each.

Two point sources imaged through a circular aperture, at separations of $0.5$, $1.0$, and $2.0$ times $\theta_{\min} = 1.22\lambda/D$, with intensity profiles beneath. At half the Rayleigh separation the pair is indistinguishable from a single elongated source; at the Rayleigh separation a shallow dip appears between the peaks; at twice it the two sources are unmistakable. Generated with matplotlib; see `scripts/figures/`.
```

The crucial thing about the Rayleigh criterion is its universality. It applies to every instrument with aperture $D$, however perfectly made. It is not an engineering shortcoming to be designed away; it is a consequence of light having a wavelength and the instrument having an edge. The only levers available are $\lambda$ and $D$: use a shorter wavelength, or build a bigger aperture.

Both levers are pulled hard in practice. Telescopes get larger, and radio astronomers link dishes thousands of kilometers apart to synthesize an aperture the size of the Earth. Photolithography, which prints circuit features by projecting a mask onto a silicon wafer, has driven its light source from visible wavelengths down through deep ultraviolet to today's extreme-ultraviolet at $13.5\ \text{nm}$ for exactly this reason. And electron microscopy takes the argument to its conclusion by abandoning light altogether in favor of electron matter waves whose wavelength ([Chapter 7](#ch-wave-properties-of-particles)) can be a hundred thousand times shorter than visible light.

### Worked Example: The Hubble Space Telescope

The Hubble Space Telescope has a primary mirror of diameter $D = 2.4\ \text{m}$. (a) Estimate its diffraction-limited resolution at $\lambda = 550\ \text{nm}$. (b) What is the smallest feature it could resolve on the Moon, $3.84\times10^8\ \text{m}$ away?

**(a)**

$$
\theta_{\min} = 1.22\,\frac{\lambda}{D} = 1.22\,\frac{550\times10^{-9}\ \text{m}}{2.4\ \text{m}} = 2.80\times10^{-7}\ \text{rad} = 0.058\ \text{arcsec}.
$$

**(b)**

$$
s = \theta_{\min}\,d = (2.80\times10^{-7}\ \text{rad})(3.84\times10^8\ \text{m}) = 107\ \text{m}.
$$

Hubble could not photograph the Apollo landing sites; the largest hardware left there is a few meters across. The limitation is not the telescope's quality but its aperture, and no amount of image processing changes the fact that the information never entered the instrument.

### Worked Example: The Eye, and Why Ground Telescopes Are Different

**(a)** The pupil of the eye is about $D = 4.0\ \text{mm}$ in ordinary lighting. Its diffraction limit at $\lambda = 550\ \text{nm}$ is

$$
\theta_{\min} = 1.22\,\frac{550\times10^{-9}\ \text{m}}{4.0\times10^{-3}\ \text{m}} = 1.68\times10^{-4}\ \text{rad} \approx 0.6\ \text{arcmin} .
$$

At a reading distance of $25\ \text{cm}$ this corresponds to $s = (1.68\times10^{-4}\ \text{rad})(0.25\ \text{m}) = 42\ \mu\text{m}$ — about half the width of a human hair, and in reasonable agreement with measured visual acuity of about $1$ arcmin. The eye is, remarkably, working close to its diffraction limit.

**(b)** Now apply the same formula to a $2.4\ \text{m}$ telescope on the ground: $\theta_{\min} = 0.058$ arcsec, the same as Hubble. Yet ground-based images at visible wavelengths are typically blurred to about $1$ arcsec, a factor of $17$ worse. The culprit is not diffraction but **atmospheric seeing**: turbulent cells of air, of order $10\ \text{cm}$ across, refract the incoming wavefront by slightly different amounts and scramble it. The effective aperture is set by the turbulence, not the mirror. Two responses are possible — put the telescope above the atmosphere, which is why Hubble exists, or measure the distortion hundreds of times a second and cancel it with a deformable mirror, which is *adaptive optics*, and which now lets large ground telescopes reach their diffraction limits in the infrared.

This example is worth keeping in mind whenever a diffraction limit is quoted: it is a ceiling on performance, not a promise of it.

## X-Ray Diffraction and Bragg's Law

Gratings work because their line spacing is comparable to the wavelength of the light. To probe the arrangement of atoms in a solid, spaced a few tenths of a nanometer apart, we would need a grating with that spacing — and nature supplies one, in the form of a crystal, provided we bring a wave with a matching wavelength. That means **X-rays**, with $\lambda \sim 0.1\ \text{nm}$.

:::{margin}
Crystallographers often quote spacings in **angstroms** ($1\ \text{Å} \equiv 10^{-10}\ \text{m} = 0.1\ \text{nm}$), a unit sized conveniently to typical interatomic distances. The copper $K_\alpha$ wavelength of $0.154\ \text{nm}$ used in the worked example below is equivalently $1.54\ \text{Å}$.
:::

Max von Laue proposed the experiment in 1912 and his collaborators Friedrich and Knipping performed it, obtaining a pattern of discrete spots from a copper sulfate crystal that established two things at once: that X-rays are waves, and that crystals are periodic arrays of atoms. Both had been conjectures until that afternoon.

W. H. Bragg and his son W. L. Bragg supplied the simple picture that made the technique usable, shown in {numref}`Figure %s <fig:ch05-bragg>`. Regard the crystal as a stack of parallel atomic planes separated by $d$, and consider X-rays reflecting specularly from successive planes. By long-standing crystallographic convention, the angle $\theta$ is measured *from the plane itself*, not from the normal — a trap for anyone importing habits from optics.

:::{warning}
The Bragg angle $\theta$ is measured from the reflecting *plane*, not from the normal to it — the opposite of the convention used for mirrors and lenses elsewhere in optics. A beam that grazes the planes at nearly $0°$ corresponds to *small* $\theta$ in Bragg's law, not large. Carrying over the normal-incidence habit from geometric optics is the single most common source of a sine-versus-cosine error in Bragg's law calculations.
:::

```{figure} ../images/ch05-bragg-law.svg
:label: fig:ch05-bragg
:alt: Two parallel X-rays reflecting from successive atomic planes in a crystal, with the extra path length of the lower ray marked as two segments each equal to d sine theta.

Bragg reflection. Two parallel X-rays strike successive atomic planes separated by $d$. Relative to the wavefronts through $A$, the ray reflecting from the lower plane travels two extra legs, each of length $d\sin\theta$. Constructive interference requires the total, $2d\sin\theta$, to be a whole number of wavelengths. Original schematic generated with matplotlib; see `scripts/figures/`.
```

Ray 2 penetrates one layer deeper. Measured between the wavefronts through the point $A$ where ray 1 reflects, it travels two extra legs — one on the way in, one on the way out — each of length $d\sin\theta$. Constructive interference between rays reflected from successive planes therefore requires

$$
n\lambda = 2d\sin\theta \qquad (\textbf{Bragg's law}), \qquad n = 1, 2, 3, \ldots
$$

The consequence is that a crystal reflects a given X-ray wavelength strongly *only* at particular angles. Rotate a crystal in a monochromatic X-ray beam and the detector sees nothing at all until an angle satisfying Bragg's law comes up, at which point a sharp peak appears. Measuring the set of such angles, for a set of crystal orientations, determines the spacings and symmetry of the atomic planes.

This is **X-ray crystallography**, and its record is hard to overstate: the structures of table salt and diamond (the Braggs, 1913), of penicillin and vitamin B$_{12}$ (Dorothy Hodgkin), of DNA — the double helix inferred by Watson and Crick from the diffraction photographs taken by Rosalind Franklin and Raymond Gosling — and of hundreds of thousands of proteins since. Nearly everything we know about where atoms sit in condensed matter came through Bragg's law.

The lattice on the other side of Bragg's law is the subject of
{numref}`Figure %s <fig:ch05-crystal-sim>`. Changing the unit cell changes the set of atomic planes,
their spacings $d$, and therefore the angles at which reflections appear —
including the aperiodic case, where the diffraction pattern is as sharp as a
crystal's but carries a symmetry no crystal can have.

```{openphysics} CrystalLattice
:label: fig:ch05-crystal-sim

Crystal structure in five screens: the two-dimensional Bravais lattices, cubic
unit cells, close packing, Miller indices, and aperiodic order. The Miller-index
screen is the direct companion to Bragg's law — it is where the planes of
spacing $d$ come from.
```

### Worked Example: An Interplanar Spacing

X-rays of wavelength $\lambda = 0.154\ \text{nm}$ (the copper $K_\alpha$ line, the workhorse of laboratory diffractometers) produce a first-order Bragg reflection at $\theta = 22.5°$. Find the spacing of the reflecting planes, and find where the second-order reflection appears.

First order, $n = 1$:

$$
d = \frac{n\lambda}{2\sin\theta} = \frac{0.154\ \text{nm}}{2\sin 22.5°} = \frac{0.154\ \text{nm}}{2(0.3827)} = 0.201\ \text{nm},
$$

a typical interatomic spacing. For $n = 2$,

$$
\sin\theta_2 = \frac{2\lambda}{2d} = \frac{0.154\ \text{nm}}{0.201\ \text{nm}} = 0.766 \quad\Longrightarrow\quad \theta_2 = 50.0°.
$$

Note that a third order would require $\sin\theta_3 = 1.149 > 1$: with this wavelength and this spacing, only two orders exist. Requiring $n\lambda \le 2d$ also shows why X-rays are essential — with visible light, $\lambda \gg 2d$ and *no* order exists at all, which is exactly why crystals look like ordinary transparent solids rather than gratings.

### Not Just X-Rays

Bragg's law contains no reference to what kind of wave is diffracting. Any wave whose wavelength is comparable to the interplanar spacing will do — and by the time you reach [Chapter 7](#ch-wave-properties-of-particles), you will know that electrons and neutrons are such waves.

That is not a rhetorical flourish; it is the historical route by which matter waves were confirmed. In 1927 Clinton Davisson and Lester Germer fired low-energy electrons at a nickel crystal and found the scattered intensity peaking at exactly the angles Bragg's law predicts, for a wavelength matching de Broglie's $\lambda = h/p$. Neutron diffraction, which is sensitive to light atoms in a way X-rays are not, is now the standard way to locate hydrogen in a crystal structure and to map magnetic ordering. The same equation, first written for X-rays, ended up as one of the sharpest pieces of evidence for the wave nature of matter.

## Holography

An ordinary photograph records intensity and throws away phase, which is why it is flat: all the information about the *shape* of the wavefront arriving from the scene is lost. A **hologram**, invented by Dennis Gabor in 1947, records the phase as well — by the only means available, namely by converting phase differences into intensity differences through interference.

The recording step splits a laser beam in two. One part, the *object beam*, illuminates the subject and scatters from it onto the film. The other, the *reference beam*, goes straight to the film. Where the two arrive in phase the film is exposed; where they arrive out of phase it is not. What the film records is therefore a dense, fine interference pattern — nothing resembling a picture, just an apparently random speckle of microscopic fringes — which encodes both the amplitude and the phase of the light arriving from every point of the object.

The reconstruction step is pure diffraction. Illuminate the developed film with the reference beam alone, and the recorded fringe pattern acts as a complicated diffraction grating, diffracting the reference beam into exactly the wavefront that the object originally sent out. An observer looking into the film sees that wavefront and cannot tell it from the object: it has full parallax, and looking around the edge of a foreground object reveals what is behind it.

Two properties follow directly from this account. First, holography demands a source with a coherence length longer than the depth of the scene, which is why it was impossible before the laser and why Gabor's original demonstrations were so limited. Second, every part of the hologram receives light from every part of the object, so a hologram cut in half still reconstructs the whole scene — from a smaller effective aperture, and therefore, by the Rayleigh criterion, with correspondingly poorer resolution.

## Looking Ahead: Diffraction and the Uncertainty Principle

There is one more thing to extract from single-slit diffraction, and it is the reason this chapter belongs in a book on modern physics.

Take the pattern seriously as a statement about photons. A photon that passes through a slit of width $a$ has, at that moment, a position along the slit known to within

$$
\Delta y \approx a .
$$

It arrives traveling straight ahead, with no transverse momentum. Yet it lands somewhere within the central diffraction maximum, which means that on emerging it has acquired a transverse momentum of order $p\sin\theta_1$, where $\theta_1$ is the angle to the first minimum. Using $\sin\theta_1 = \lambda/a$ and the photon momentum $p = h/\lambda$ (established in [Chapter 6](#ch-particle-properties-of-waves)),

$$
\Delta p_y \approx p\sin\theta_1 = \frac{h}{\lambda}\cdot\frac{\lambda}{a} = \frac{h}{a}.
$$

Multiply:

$$
\Delta y\,\Delta p_y \approx a \cdot \frac{h}{a} = h .
$$

The width of the slit has canceled out. Squeeze the slit to pin down the photon's position and the diffraction pattern widens by exactly enough to keep the product fixed; open it up and the reverse happens. There is no way to make both small at once — not because the measuring apparatus is clumsy, but because the light is a wave, and this relation is a property of waves.

This is the **Heisenberg uncertainty principle**, arrived at from nothing but classical wave optics and one quantum fact ($p = h/\lambda$). [Chapter 7](#ch-wave-properties-of-particles) derives it properly, shows that it applies to electrons and every other particle, and works out its consequences. But it is worth seeing now, in this chapter, that its origin lies in the ordinary mathematics of diffraction — that the strangest feature of quantum mechanics is, at bottom, the same phenomenon that spreads light behind a narrow slit.

## Summary

- Diffraction and interference are the same physics — coherent waves added as fields. The words distinguish a continuum of sources (an integral) from a discrete set (a sum), and nothing more.
- The **Huygens–Fresnel principle** treats each point of an aperture as a source of wavelets that are summed *with their phases*. **Fraunhofer** (far-field) diffraction applies when the Fresnel number $F = a^2/L\lambda \ll 1$, or whenever a lens is used to bring parallel bundles to a focus; **Fresnel** (near-field) diffraction applies otherwise, and produces effects such as the Poisson spot.
- **Single-slit minima** occur at $a\sin\theta = m\lambda$ for nonzero integer $m$, derived by pairing points $a/2m$ apart so that every pair cancels. $m = 0$ is excluded: the center is a broad maximum.
- The **single-slit intensity** is $I = I_0[\sin(\beta/2)/(\beta/2)]^2$ with $\beta = (2\pi/\lambda)a\sin\theta$, obtained from the chord of the circular phasor arc. The central maximum has half-width $\theta_1 \approx \lambda/a$, is twice as wide as the side lobes, and dominates: the first side lobe reaches only $4.7\%$ of the peak.
- **Narrower slits spread light more.** For $a \le \lambda$ no minimum exists and the slit radiates like a point source, justifying the idealization of [Chapter 4](#ch-interference-of-light).
- A **real double slit** gives the product $I = I_0\cos^2(\pi d\sin\theta/\lambda)[\sin(\beta/2)/(\beta/2)]^2$: fine interference fringes set by $d$, under a broad envelope set by $a$. Orders for which $m\,a/d$ is an integer are **missing**; counting the fringes inside the central envelope measures $d/a$.
- A **diffraction grating** obeys $d\sin\theta = m\lambda$ with angular dispersion $\mathrm{d}\theta/\mathrm{d}\lambda = m/(d\cos\theta)$ and resolving power $R = \lambda/\Delta\lambda = mN$, where $N$ is the number of *illuminated* lines. Only orders up to $m_{\max} = \lfloor d/\lambda\rfloor$ exist.
- A **circular aperture** of diameter $D$ produces an Airy pattern with first zero at $\theta_{\min} = 1.22\lambda/D$. The **Rayleigh criterion** adopts this as the resolution limit of any instrument with that aperture — a fundamental diffraction limit, though real performance may be worse (atmospheric seeing) or, with enough signal and cleverness, better.
- **Bragg's law**, $n\lambda = 2d\sin\theta$ with $\theta$ measured from the atomic planes, governs constructive reflection from a crystal lattice. It underlies X-ray crystallography, and applies equally to electron and neutron waves — as Davisson and Germer showed in 1927 ([Chapter 7](#ch-wave-properties-of-particles)).
- A **hologram** records the interference between an object beam and a reference beam, capturing phase as well as amplitude; illuminating it with the reference beam diffracts a reconstruction of the original wavefront.
- Applying $\Delta y \approx a$ and $\Delta p_y \approx h/a$ to a single slit gives $\Delta y\,\Delta p_y \approx h$: the **uncertainty principle**, already visible in classical diffraction.

## Conceptual Questions

1. State, in one sentence each, the physical difference between the conditions $d\sin\theta = m\lambda$ for a double slit and $a\sin\theta = m\lambda$ for a single slit. Why do two nearly identical formulas describe opposite things?

2. Explain, using the pairing argument, why $\theta = 0$ can never be a diffraction minimum, no matter how many strips the slit is divided into.

3. A single slit is illuminated with red light, then with blue light. Which pattern is wider, and why? Now the same slit is made narrower. Which way does the pattern change? Are the two answers consistent with a single rule?

4. Explain why a wider telescope aperture *improves* angular resolution, while a wider slit *narrows* the diffraction pattern. These sound like opposite statements about what a bigger aperture does. Show that they are the same statement.

5. In a real double-slit pattern, some interference maxima are missing entirely. Explain what has happened to the light that "should" have been there, and why energy is nonetheless conserved.

6. Why can visible light not be used to determine crystal structures by Bragg diffraction? Answer quantitatively, using the constraint $n\lambda \le 2d$.

7. A hologram is cut in half. Explain why each half still reconstructs the entire scene, and what is degraded.

8. A camera lens is stopped down from $f/2$ to $f/16$, reducing the aperture diameter by a factor of $8$. Aberrations improve when a lens is stopped down, but diffraction gets worse. Explain the trade-off, and state which effect dominates at very small apertures.

## Problems

:::{exercise}
:label: ex-diffraction-of-light-1

A single slit of width $a = 0.0250\ \text{mm}$ is illuminated at $\lambda = 633\ \text{nm}$. Find the angles to the first and second diffraction minima, and the width of the central maximum on a screen $1.80\ \text{m}$ away.
:::

:::{solution} ex-diffraction-of-light-1
:label: sol-diffraction-of-light-1
:class: dropdown

The minima obey $a\sin\theta_m=m\lambda$.  With $a=0.0250\ \text{mm}=2.50\times10^{-5}\ \text{m}$ and $\lambda=633\ \text{nm}$,

$$\sin\theta_1=0.02532,\quad\theta_1=1.45^\circ,\qquad \sin\theta_2=0.05064,\quad\theta_2=2.90^\circ.$$

The central maximum extends from the first minimum on one side to that on the other, so its small-angle width is

$$w=\frac{2L\lambda}{a}=\frac{2(1.80\ \text{m})(633\times10^{-9}\ \text{m})}{2.50\times10^{-5}\ \text{m}}=9.12\times10^{-2}\ \text{m}=9.12\ \text{cm}.$$

Therefore, the first and second minima are at $1.45^\circ$ and $2.90^\circ$, and the central maximum is $9.12\ \text{cm}$ wide.
:::

:::{exercise}
:label: ex-diffraction-of-light-2

A slit of unknown width produces a central diffraction maximum $4.00\ \text{cm}$ wide on a screen $1.50\ \text{m}$ away, using $\lambda = 520\ \text{nm}$ light. Find the slit width.
:::

:::{solution} ex-diffraction-of-light-2
:label: sol-diffraction-of-light-2
:class: dropdown

For a central-maximum width $w=2L\lambda/a$,

$$a=\frac{2L\lambda}{w}=\frac{2(1.50\ \text{m})(520\times10^{-9}\ \text{m})}{4.00\times10^{-2}\ \text{m}}=3.90\times10^{-5}\ \text{m}.$$

Therefore, the slit width is $3.90\times10^{-5}\ \text{m}$, or $0.0390\ \text{mm}$.
:::

:::{exercise}
:label: ex-diffraction-of-light-3

Using $I = I_0[\sin(\beta/2)/(\beta/2)]^2$, compute the intensity, as a fraction of $I_0$, at the angle exactly halfway between the first and second minima ($\beta/2 = 1.5\pi$). Compare your answer with the true first secondary maximum, $4.7\%$ at $\beta/2 = 1.4303\pi$, and comment on the size of the discrepancy.
:::

:::{solution} ex-diffraction-of-light-3
:label: sol-diffraction-of-light-3
:class: dropdown

At $\beta/2=1.5\pi$,

$$\frac{I}{I_0}=\left[\frac{\sin(1.5\pi)}{1.5\pi}\right]^2=\left(\frac{-1}{4.712}\right)^2=0.0450.$$

The true first secondary maximum is $0.0470I_0$, so the midpoint estimate is lower by $0.0020I_0$, or about $4\%$ of the secondary-maximum value.  Therefore, the halfway-point intensity is $4.50\%$ of the central maximum and is already a good approximation to the true $4.7\%$ secondary maximum.
:::

:::{exercise}
:label: ex-diffraction-of-light-4

Show that the Fresnel number for a $0.10\ \text{mm}$ slit at $\lambda = 550\ \text{nm}$ becomes of order unity at a screen distance of about $2\ \text{cm}$. What does this tell you about the observation distance needed for the far-field formulas of this chapter to apply?
:::

:::{solution} ex-diffraction-of-light-4
:label: sol-diffraction-of-light-4
:class: dropdown

The Fresnel number is $F=a^2/(\lambda L)$.  Setting $F\sim1$ gives

$$L\sim\frac{a^2}{\lambda}=\frac{(0.10\times10^{-3}\ \text{m})^2}{550\times10^{-9}\ \text{m}}=1.82\times10^{-2}\ \text{m}=1.8\ \text{cm}.$$

Therefore, distances only of order $2\ \text{cm}$ are still at the Fresnel--Fraunhofer boundary; the far-field formulas require a screen appreciably farther away than this scale.
:::

:::{exercise}
:label: ex-diffraction-of-light-5

A double slit has slit width $a = 0.020\ \text{mm}$ and separation $d = 0.100\ \text{mm}$, illuminated at $\lambda = 550\ \text{nm}$. (a) Find $d/a$. (b) List the missing orders up to $m = 12$. (c) Find the number of bright fringes visible within the central diffraction maximum.
:::

:::{solution} ex-diffraction-of-light-5
:label: sol-diffraction-of-light-5
:class: dropdown

The ratio is

$$\frac da=\frac{0.100\ \text{mm}}{0.020\ \text{mm}}=5.$$

An interference maximum is missing when $m\lambda/d=p\lambda/a$, or $m=p(d/a)=5p$.  Up to $m=12$, the missing orders are $m=5$ and $m=10$.  The central envelope contains $|m|<d/a=5$, namely $m=-4,\ldots,4$, for nine nonmissing bright fringes — exactly the pattern plotted in {numref}`Figure %s <fig:ch05-double-slit>`, whose missing orders $m=\pm5,\pm10$ are this problem's $d/a=5$.  Therefore, $d/a=5$, orders $5$ and $10$ are absent, and nine bright fringes lie inside the central diffraction maximum.
:::

:::{exercise}
:label: ex-diffraction-of-light-6

A double slit produces $7$ bright fringes inside its central diffraction maximum (counting the central fringe, and excluding the missing orders at the edges). Deduce the ratio $d/a$.
:::

:::{solution} ex-diffraction-of-light-6
:label: sol-diffraction-of-light-6
:class: dropdown

If $d/a$ is an integer $q$, the central maximum contains the orders $m=-(q-1),\ldots,0,\ldots,q-1$, a total of $2q-1$ bright fringes.  Hence

$$2q-1=7\quad\Rightarrow\quad q=4.$$

Therefore, the slit-separation-to-width ratio is $d/a=4$.
:::

:::{exercise}
:label: ex-diffraction-of-light-7

A diffraction grating has $5000$ lines per centimeter. (a) Find the line spacing $d$. (b) Find the angle of the first-order maximum for $\lambda = 500\ \text{nm}$. (c) Find the highest order observable for this wavelength. (d) Find the angular dispersion $\mathrm{d}\theta/\mathrm{d}\lambda$ in first order at this wavelength, in degrees per nanometer.
:::

:::{solution} ex-diffraction-of-light-7
:label: sol-diffraction-of-light-7
:class: dropdown

The line density is $5000\ \text{cm}^{-1}=5.00\times10^5\ \text{m}^{-1}$, so

$$d=\frac1{5.00\times10^5\ \text{m}^{-1}}=2.00\times10^{-6}\ \text{m}.$$

For first order, $\sin\theta=\lambda/d=(500\ \text{nm})/(2000\ \text{nm})=0.250$, so $\theta=14.5^\circ$.  The largest order is $m_{\max}=\lfloor d/\lambda\rfloor=4$.  Differentiating $d\sin\theta=m\lambda$ gives

$$\frac{d\theta}{d\lambda}=\frac{m}{d\cos\theta}=5.16\times10^5\ \text{rad/m}=0.0296^\circ/\text{nm}.$$

Therefore, the spacing is $2.00\ \mu\text{m}$, the first-order angle is $14.5^\circ$, the highest order is $4$, and the first-order dispersion is $0.0296^\circ/\text{nm}$.
:::

:::{exercise}
:label: ex-diffraction-of-light-8

A grating with $N = 4000$ illuminated lines is used in second order. (a) Find the smallest wavelength difference it can resolve near $\lambda = 600\ \text{nm}$. (b) Repeat for first order, and state the factor by which the resolution changes. (c) If the beam is narrowed so that only $1000$ lines are illuminated, what happens to the resolving power, and why does the total number of lines ruled on the grating not matter?
:::

:::{solution} ex-diffraction-of-light-8
:label: sol-diffraction-of-light-8
:class: dropdown

Resolving power is $R=mN=\lambda/\Delta\lambda$.  In second order,

$$\Delta\lambda=\frac{600\ \text{nm}}{(2)(4000)}=0.0750\ \text{nm}.$$

In first order it is $600/4000=0.150\ \text{nm}$, twice as large, so the resolution is two times poorer.  If only $1000$ lines are illuminated in second order, $R=2000$ and $\Delta\lambda=0.300\ \text{nm}$; only illuminated lines contribute coherently, exactly as {numref}`Figure %s <fig:ch05-resolving-power>` shows for the sodium doublet: raising $N$ narrows each order's peak until two close wavelengths separate.  Therefore, second order resolves $0.0750\ \text{nm}$ versus $0.150\ \text{nm}$ in first order, and narrowing the beam reduces the resolving power in direct proportion to the illuminated line count.
:::

:::{exercise}
:label: ex-diffraction-of-light-9

A grating with $600$ lines per millimeter is illuminated with white light ($400$–$700\ \text{nm}$). (a) Find the angular width of the first-order spectrum. (b) Find the angular width of the second-order spectrum. (c) Show that the second- and third-order spectra overlap, and find the wavelength at which the overlap begins.
:::

:::{solution} ex-diffraction-of-light-9
:label: sol-diffraction-of-light-9
:class: dropdown

The spacing is $d=(600\ \text{mm}^{-1})^{-1}=1.667\ \mu\text{m}$.  In first order the endpoint angles are $\sin^{-1}(400/1667)=13.9^\circ$ and $\sin^{-1}(700/1667)=24.8^\circ$, so the width is $10.9^\circ$.  In second order they are $\sin^{-1}(0.480)=28.7^\circ$ and $\sin^{-1}(0.840)=57.1^\circ$, so the width is $28.4^\circ$.

Overlap begins where $2\lambda_2=3\lambda_3$.  The first common direction occurs for $\lambda_2=600\ \text{nm}$ and $\lambda_3=400\ \text{nm}$, at $\sin\theta=0.720$ or $\theta=46.1^\circ$.

```{figure} ../images/ch05-sol-order-overlap.svg
:label: fig:ch05-sol-order-overlap
:alt: Diffraction angle versus wavelength for the first, second, and third grating orders, with the angular band where the second and third orders overlap shaded.

The three orders' angular ranges as $\lambda$ sweeps across the visible spectrum. The shaded band is where 2nd- and 3rd-order light arrive at the same angle; it begins where the 2nd order's $600\ \text{nm}$ meets the 3rd order's $400\ \text{nm}$, both at $46.1^\circ$.
```

Therefore, the first- and second-order widths are $10.9^\circ$ and $28.4^\circ$, and second and third orders overlap from $46.1^\circ$ onward.
:::

:::{exercise}
:label: ex-diffraction-of-light-10

The human eye has a pupil diameter of about $D = 4.0\ \text{mm}$ in typical lighting. Using the Rayleigh criterion at $\lambda = 550\ \text{nm}$, estimate (a) the smallest angular separation the eye can resolve and (b) the corresponding separation of two objects at a reading distance of $25\ \text{cm}$.
:::

:::{solution} ex-diffraction-of-light-10
:label: sol-diffraction-of-light-10
:class: dropdown

The Rayleigh limit is

$$\theta_{\min}=\frac{1.22\lambda}{D}=\frac{1.22(550\times10^{-9}\ \text{m})}{4.0\times10^{-3}\ \text{m}}=1.68\times10^{-4}\ \text{rad}=34.6\ \text{arcsec}.$$

At $L=0.250\ \text{m}$, $s\simeq L\theta=(0.250)(1.68\times10^{-4})=4.19\times10^{-5}\ \text{m}=42\ \mu\text{m}$.  This is the "just resolved" case of {numref}`Figure %s <fig:ch05-rayleigh>`, where the two Airy patterns are separated by exactly $\theta_{\min}$.  Therefore, the ideal eye resolves about $34.6\ \text{arcsec}$, corresponding to $42\ \mu\text{m}$ at reading distance.
:::

:::{exercise}
:label: ex-diffraction-of-light-11

A car's headlights are separated by $1.3\ \text{m}$. Using the eye's diffraction limit from [Problem 10](#ex-diffraction-of-light-10), estimate the greatest distance at which they could in principle be resolved as two separate lights. Then comment on whether atmospheric turbulence, the eye's own aberrations, or the finite spacing of retinal cells is likely to set a more restrictive limit in practice.
:::

:::{solution} ex-diffraction-of-light-11
:label: sol-diffraction-of-light-11
:class: dropdown

Using $s=L\theta_{\min}$,

$$L_{\max}=\frac{1.3\ \text{m}}{1.68\times10^{-4}\ \text{rad}}=7.75\times10^3\ \text{m}=7.8\ \text{km}.$$

Therefore, diffraction alone would permit resolution to roughly $7.8\ \text{km}$, but atmospheric turbulence, aberrations, contrast loss, and retinal sampling make the practical distance much shorter.
:::

:::{exercise}
:label: ex-diffraction-of-light-12

A telescope's objective diameter is doubled at fixed wavelength. By what factor does the smallest resolvable angle change? By what factor would it change instead if the diameter were held fixed but the observing wavelength were shifted from $\lambda = 550\ \text{nm}$ to $\lambda = 275\ \text{nm}$?
:::

:::{solution} ex-diffraction-of-light-12
:label: sol-diffraction-of-light-12
:class: dropdown

Since $\theta_{\min}=1.22\lambda/D$, doubling $D$ changes the limit to $\theta_{\min}/2$.  Halving $\lambda$ from $550\ \text{nm}$ to $275\ \text{nm}$ at fixed $D$ also changes it to $\theta_{\min}/2$.  Therefore, either modification improves the angular resolution by a factor of two.
:::

:::{exercise}
:label: ex-diffraction-of-light-13

A microscope objective of diameter $5.0\ \text{mm}$ has a working distance of $8.0\ \text{mm}$. (a) Estimate the smallest separation it can resolve at $\lambda = 550\ \text{nm}$, treating the objective as a circular aperture subtending the corresponding angle. (b) Estimate how much better an electron microscope would do if its electron waves have $\lambda = 4.0\ \text{pm}$ and the effective aperture angle is the same.
:::

:::{solution} ex-diffraction-of-light-13
:label: sol-diffraction-of-light-13
:class: dropdown

The aperture numerical angle is approximately $\mathrm{NA}=D/(2L)=5.0/(16.0)=0.313$.  Thus

$$d_{\min}\simeq\frac{0.61\lambda}{\mathrm{NA}}=\frac{0.61(550\ \text{nm})}{0.313}=1.07\ \mu\text{m}.$$

At the same aperture angle, replacing $550\ \text{nm}$ by $4.0\ \text{pm}$ gives $d_{\min}=7.8\ \text{pm}$, an improvement by $550\ \text{nm}/4.0\ \text{pm}=1.38\times10^5$.  Therefore, the light microscope resolves about $1.1\ \mu\text{m}$ and the electron microscope about $8\ \text{pm}$ under the stated idealized comparison.
:::

:::{exercise}
:label: ex-diffraction-of-light-14

X-rays of wavelength $\lambda = 0.0709\ \text{nm}$ (the molybdenum $K_\alpha$ line) produce a first-order Bragg reflection at $\theta = 15.0°$. (a) Find the interplanar spacing. (b) Find the angle of the second-order reflection. (c) Determine the highest order that exists for these planes.
:::

:::{solution} ex-diffraction-of-light-14
:label: sol-diffraction-of-light-14
:class: dropdown

Bragg's law is $2d\sin\theta=m\lambda$.  For first order,

$$d=\frac{0.0709\ \text{nm}}{2\sin15.0^\circ}=0.137\ \text{nm}.$$

For second order, $\sin\theta_2=2\lambda/(2d)=0.518$, so $\theta_2=31.2^\circ$.  Finally $m\le2d/\lambda=3.86$, so $m_{\max}=3$.

```{figure} ../images/ch05-sol-bragg-order-limit.svg
:label: fig:ch05-sol-bragg-order-limit
:alt: Bar chart of sin(theta_m) for orders m = 1 through 5, with m = 1, 2, 3 below the sin(theta) = 1 limit and m = 4, 5 shown as impossible above it.

$\sin\theta_m=m\lambda/2d$ grows in equal steps with $m$; it crosses the physical ceiling $\sin\theta=1$ between $m=3$ and $m=4$, so no reflection of any order beyond $m=3$ exists for these planes.
```

Therefore, the plane spacing is $0.137\ \text{nm}$, the second-order reflection is at $31.2^\circ$, and orders through $m=3$ exist.
:::

:::{exercise}
:label: ex-diffraction-of-light-15

A crystal has an interplanar spacing $d = 0.282\ \text{nm}$, close to the value for sodium chloride. (a) Find the X-ray wavelength that produces a first-order Bragg reflection at $\theta = 20.0°$. (b) Confirm that this wavelength lies in the X-ray region. (c) Find the longest wavelength that can produce any Bragg reflection at all from these planes.
:::

:::{solution} ex-diffraction-of-light-15
:label: sol-diffraction-of-light-15
:class: dropdown

For first order,

$$\lambda=2d\sin\theta=2(0.282\ \text{nm})\sin20.0^\circ=0.193\ \text{nm}.$$

This is $1.93\times10^{-10}\ \text{m}$, in the X-ray region.  Since $\sin\theta\le1$, the longest diffracting wavelength is $\lambda_{\max}=2d=0.564\ \text{nm}$.  Therefore, the required wavelength is $0.193\ \text{nm}$ and no wavelength longer than $0.564\ \text{nm}$ can produce a Bragg reflection from these planes.
:::

:::{exercise}
:label: ex-diffraction-of-light-16

Show that the general condition for a Bragg reflection to exist is $\lambda \le 2d$, and use it to explain why $\lambda = 550\ \text{nm}$ light produces no diffraction peaks from a crystal with $d = 0.3\ \text{nm}$.
:::

:::{solution} ex-diffraction-of-light-16
:label: sol-diffraction-of-light-16
:class: dropdown

Bragg's law requires $m\lambda=2d\sin\theta$.  Because $\sin\theta\le1$ and the smallest order is $m=1$, an order can exist only if $\lambda\le2d$.  For $d=0.3\ \text{nm}$, $2d=0.6\ \text{nm}$, whereas visible light has $\lambda=550\ \text{nm}$.  Therefore, visible light is about $900$ times too long in wavelength to diffract from atomic crystal planes.
:::

:::{exercise}
:label: ex-diffraction-of-light-17

Explain physically why a narrower slit produces a wider central maximum, using $\theta_1 \approx \lambda/a$, and reconcile this with the fact that a larger telescope aperture gives finer resolution. Are the two statements in tension? Explain carefully.
:::

:::{solution} ex-diffraction-of-light-17
:label: sol-diffraction-of-light-17
:class: dropdown

The first minimum of a narrow slit obeys $\theta_1\simeq\lambda/a$, so decreasing $a$ makes the diffracted beam wider: localization at a smaller opening creates a larger angular spread.  A telescope, however, uses a large aperture to make the diffraction pattern of each *point source* narrower, allowing two nearby patterns to be distinguished.  Therefore, the statements are complementary rather than contradictory: a narrow aperture spreads one beam widely, while a large collecting aperture reduces the diffraction blur of an image.
:::

:::{exercise}
:label: ex-diffraction-of-light-18

A single slit of width $a = 1.0\ \mu\text{m}$ is illuminated at $\lambda = 500\ \text{nm}$. (a) Find the angle to the first minimum. (b) Treating the transmitted light as photons of momentum $p = h/\lambda$, estimate $\Delta p_y$ from the angular spread and verify that $\Delta y\,\Delta p_y \approx h$. (c) Repeat for $a = 0.50\ \mu\text{m}$ and confirm that the product does not change.
:::

:::{solution} ex-diffraction-of-light-18
:label: sol-diffraction-of-light-18
:class: dropdown

For $a=1.0\ \mu\text{m}$, $\sin\theta_1=\lambda/a=0.500$, hence $\theta_1=30.0^\circ$.  Taking $\Delta p_y\sim p\sin\theta_1$ and $p=h/\lambda$,

$$\Delta p_y\sim\frac{h}{\lambda}\frac{\lambda}{a}=\frac{h}{a}=6.63\times10^{-28}\ \text{kg m/s},$$

so $\Delta y\Delta p_y\sim(1.0\times10^{-6}\ \text{m})(6.63\times10^{-28}\ \text{kg m/s})=6.63\times10^{-34}\ \text{J s}=h$.  For $a=0.50\ \mu\text{m}$, the first minimum is at $90^\circ$, $\Delta p_y\sim h/(0.50\ \mu\text{m})=1.33\times10^{-27}\ \text{kg m/s}$, and the product is again $h$.  Therefore, halving the slit doubles the momentum uncertainty while leaving $\Delta y\Delta p_y$ of order $h$.
:::

:::{exercise}
:label: ex-diffraction-of-light-19

The Event Horizon Telescope images the black hole at the center of the galaxy M87 at a wavelength of $1.3\ \text{mm}$, using an array of radio dishes spread across the Earth to synthesize an aperture $D \approx 1.0\times10^7\ \text{m}$. (a) Find its angular resolution. (b) The black hole's shadow subtends about $40$ microarcseconds. Show that the array can just resolve it. (c) Explain why the same resolution cannot be achieved with a single dish.
:::

:::{solution} ex-diffraction-of-light-19
:label: sol-diffraction-of-light-19
:class: dropdown

The synthesized aperture has

$$\theta_{\min}=\frac{1.22(1.3\times10^{-3}\ \text{m})}{1.0\times10^7\ \text{m}}=1.59\times10^{-10}\ \text{rad}=32.7\ \mu\text{arcsec}.$$

Since $32.7\ \mu\text{arcsec}<40\ \mu\text{arcsec}$, the shadow is just resolvable.

```{figure} ../images/ch05-sol-eht-resolution.svg
:label: fig:ch05-sol-eht-resolution
:alt: Log-log plot of angular resolution versus aperture diameter at 1.3 millimeter wavelength, marking a 100 meter single dish, the 40 microarcsecond M87 shadow, and the Earth-scale synthesized aperture that reaches it.

Angular resolution improves only as $1/D$, so reaching $40\ \mu\text{arcsec}$ at $\lambda=1.3\ \text{mm}$ requires an aperture the size of the Earth; even the largest single dish ($D\sim100\ \text{m}$) falls short by a factor of $10^5$.
```

Therefore, Earth-scale interferometry provides just enough resolution, whereas a single dish would need an impossible diameter comparable to Earth to supply the same aperture.
:::

:::{exercise}
:label: ex-diffraction-of-light-20

A compact disc has data tracks spaced $1.6\ \mu\text{m}$ apart and acts as a reflection grating. (a) Find the first-order diffraction angle for $\lambda = 650\ \text{nm}$ light at normal incidence. (b) Find the highest order that exists. (c) A DVD has tracks spaced $0.74\ \mu\text{m}$ apart; explain, using your results, why a DVD spreads colors more widely than a CD.
:::

:::{solution} ex-diffraction-of-light-20
:label: sol-diffraction-of-light-20
:class: dropdown

For a CD, $d=1.6\ \mu\text{m}$ and $\sin\theta_1=650/1600=0.406$, so $\theta_1=24.0^\circ$.  The maximum order is $\lfloor1600/650\rfloor=2$.  For a DVD, $d=0.74\ \mu\text{m}$, so $\sin\theta_1=650/740=0.878$ and $\theta_1=61.4^\circ$.

```{figure} ../images/ch05-sol-cd-dvd-orders.svg
:label: fig:ch05-sol-cd-dvd-orders
:alt: Bar chart comparing diffraction angles for orders 1 through 3 on a CD and a DVD, with the DVD's first order already larger than the CD's second order, and higher orders impossible for the DVD.

At the same wavelength, the DVD's smaller track spacing pushes every order to a larger angle; its first order alone exceeds the CD's, and no second order exists for the DVD at all, since $2\lambda/d>1$ there.
```

Therefore, a DVD sends the first order to a much larger angle than a CD, producing a wider color spread because its track spacing is smaller.
:::
