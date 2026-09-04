---
title: The Need for Relativity
short_title: Chapter 1. The Need for Relativity
label: ch-need-for-relativity
numbering:
  enumerator: "1.%s"
  heading_2: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 1.1, 1.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-01-the-need-for-relativity.pdf
    chapter: 1
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Explain why late-nineteenth-century physics appeared essentially complete, and identify the handful of unresolved puzzles that undid that picture.
- State the principle of relativity as it already existed in Newtonian mechanics, and explain why it does not, by itself, forbid a preferred frame for light.
- State the Galilean transformation and Galilean velocity-addition rule, and explain what they predict for the speed of light.
- Describe the luminiferous-ether hypothesis and the reasoning behind the Michelson–Morley experiment, and compute the fringe shift it predicted.
- Explain why the null result of the Michelson–Morley experiment could not be explained away within Newtonian mechanics and a stationary ether.
- Explain why the Kennedy–Thorndike experiment shows that length contraction alone cannot account for the null results, and that an accompanying time-dilation effect is also required.
- Describe the Fizeau experiment and explain why its result was equally difficult to accommodate within a simple ether picture.
- State Einstein's two postulates of special relativity and explain why they are jointly incompatible with Galilean relativity.

### Introduction

By the 1890s, many physicists believed their subject was nearly finished. Newtonian mechanics predicted the motion of planets, projectiles, and machinery with extraordinary precision; Maxwell's equations had unified electricity, magnetism, and optics into a single theory of the electromagnetic field and correctly predicted that light is an electromagnetic wave. A famous (if perhaps apocryphal) remark attributed to physicists of the era held that all that remained was to measure constants to more decimal places.

That confidence concealed a handful of loose threads. This chapter follows one of them: Maxwell's equations predict a definite speed for light, $c \approx 3.00\times10^{8}\ \text{m/s}$, but they do not say *relative to what* that speed is measured. Every other wave known to nineteenth-century physics — sound, water waves, waves on a string — is a disturbance in a material medium, and its speed is fixed relative to that medium, not relative to an observer. It was natural to assume light must be the same: a wave in some all-pervading substance, the *luminiferous ether*, with $c$ being its speed relative to the ether alone. Observers moving through the ether should then measure a different speed for light, just as a swimmer's speed relative to the shore depends on whether they swim with or against a current. Two experiments designed to detect this effect — one that stubbornly refused to find it, and one that found something stranger still — are where this chapter begins, before turning to the radical reinterpretation Einstein proposed for both results at once.

:::{margin}
Today $c$ is *defined* to be exactly $299{,}792{,}458\ \text{m/s}$; the meter itself is defined in terms of it. In 1890 it was instead a measured quantity, and Maxwell's equations gave no reason to expect it to be measured the same by every observer.
:::

## The Ether Hypothesis and Michelson–Morley

### The Principle of Relativity, Before Einstein

It is worth being precise about what was, and was not, already understood before 1905. Galileo had already argued, nearly three centuries earlier, that uniform motion is undetectable from the inside. In his *Dialogue Concerning the Two Chief World Systems* (1632), he imagined an observer sealed below the deck of a smoothly sailing ship, with no portholes: butterflies fly about the cabin, fish swim in a bowl, drops fall from a bottle into a jar beneath it. Galileo's point was that no mechanical experiment performed in that sealed cabin can tell you whether the ship is at rest in harbor or cruising at constant velocity across a calm sea. The butterflies do not pile up against the stern wall; the drops fall straight down into the jar exactly as they would in harbor. Only *changes* in the ship's velocity — a lurch, a turn — are detectable from inside, because those involve acceleration, and acceleration is not relative in the same way.

This is the **principle of relativity** applied to mechanics alone: the laws of mechanics take the same form in every inertial (non-accelerating) reference frame, so no mechanical experiment, performed entirely inside a closed laboratory, can determine that laboratory's velocity — only changes in velocity are detectable. Formally, this is exactly the content of the Galilean transformation worked out below: Newton's second law, $F = ma$, keeps the same form under $x' = x - vt$ for any constant $v$, because acceleration is unchanged by the transformation ($a' = a$, since $v$ is constant). Nothing about this principle was controversial in 1890; it was already a working assumption of every mechanic and astronomer.

What was *not* yet settled was whether this principle extended beyond mechanics — in particular, to light and electromagnetism. Maxwell's equations, unlike Newton's laws, single out a specific speed $c$ for electromagnetic waves, and by the reasoning of the Introduction above, a wave's speed is normally measured relative to its medium, not relative to an arbitrary observer. If light truly is a disturbance in a material ether, then Maxwell's equations should hold their simplest form only in the ether's own rest frame, and an observer moving relative to the ether — such as anyone standing on the surface of a planet orbiting the Sun — should be able to detect that motion optically, even though no *mechanical* experiment inside a closed lab could reveal it. The question the rest of this chapter pursues is empirical: can such motion actually be detected?

### Galilean Relativity and the Speed of Light

Newtonian mechanics is built on a specific rule for relating measurements made by observers moving relative to one another. Consider two reference frames, $S$ and $S'$, with $S'$ moving at constant velocity $v$ along the $x$-axis of $S$, and with their origins coinciding at $t = 0$. The *Galilean transformation* relates the coordinates of an event as measured in each frame:

$$
x' = x - vt, \qquad y' = y, \qquad z' = z, \qquad t' = t.
$$

The last equation encodes an assumption so natural to everyday experience that it usually goes unstated: time flows identically for every observer, regardless of how they are moving. Differentiating the transformation for $x$ gives the familiar classical velocity-addition rule. If an object moves with velocity $u_x$ in frame $S$, its velocity in $S'$ is

$$
u_x' = u_x - v.
$$

This is the rule that lets you add your walking speed to a moving walkway, or a thrown ball's speed to the speed of the train from which it is thrown. Applied to light, it makes a sharp prediction: if light travels at speed $c$ relative to the ether, and Earth moves through the ether at orbital speed $v \approx 3\times 10^4\ \text{m/s}$, then an observer on Earth measuring light traveling in the same direction as Earth's motion should get $c - v$, and light traveling in the opposite direction should give $c + v$. The effect is small — about one part in $10^4$ — but with an interferometer sensitive enough to detect a shift in the interference pattern of order that size, it should be measurable.

:::{warning}
It is easy to mix up the sign in $u_x' = u_x - v$: the rule subtracts the *frame's* velocity from the object's velocity, not the other way around. A quick check that costs nothing: if $S'$ moves in the $+x$ direction relative to $S$ ($v>0$) and the object is at rest in $S$ ($u_x = 0$), it must appear to drift in the $-x$ direction in $S'$ ($u_x' = -v$), exactly as the ground appears to slide backward beneath a forward-moving train.
:::

The assumption hiding inside that argument is worth making explicit, because every wave known to nineteenth-century physics encouraged it. A wave is a disturbance of *something*, and that something fixes the frame in which the wave has its textbook speed: {numref}`Figure %s <fig:ch01-waves-sim>` runs one oscillating source as a ripple on water, as a sound wave in air, and as light. On the first two screens the medium can be put on display directly — the water surface, and the individual air molecules being pushed back and forth — and it is relative to that medium that the disturbance travels at its stated speed. The ether hypothesis is the assumption that the third screen works like the first two, and that the medium there is merely one nobody had yet managed to detect.

```{phet} waves-intro
:label: fig:ch01-waves-sim

A single oscillating source seen as a water wave, a sound wave, and a light wave. For water and sound the medium can be drawn on the screen, and it sets the frame in which the wave travels at its stated speed; light was expected to be no different, and the medium it was supposed to disturb was the ether.
```

### The Michelson–Morley Experiment

:::{note}
Albert Michelson, a graduate of the U.S. Naval Academy, built his first interferometer in 1881 (in Berlin, with support from Alexander Graham Bell) and refined it with Edward Morley at what is now Case Western Reserve University in 1887. Michelson went on to win the 1907 Nobel Prize in Physics — the first American laureate in the sciences — awarded for the precision of his optical instruments, notably this one, even though the experiment's headline result was a *null* one.
:::

Albert Michelson (and later Michelson working with Edward Morley) built exactly such an interferometer. Its principle is to split a beam of light into two perpendicular paths, reflect each off a mirror, recombine the beams, and observe the resulting interference pattern. If Earth moves through the ether, the round-trip travel time along the path parallel to that motion should differ slightly from the round-trip time along the perpendicular path, because a "cross-stream" trip and an "upstream–downstream" trip through a moving medium take different times even when the two paths have equal length — the same effect that makes a boat crossing a river directly and returning take less time than travelling the same distance upstream and back. The predicted difference is small, but the interferometer was sensitive enough to detect a shift of a small fraction of a fringe, and the apparatus was mounted on a stone slab floating on mercury so that it could be rotated smoothly to swap the roles of the two arms.

#### Computing the Predicted Fringe Shift

The prediction can be made quantitative. Let both interferometer arms have length $L$, with the apparatus moving at speed $v$ through the ether, and suppose (for the moment) that one arm lies along the direction of motion and the other perpendicular to it. Light traveling down the parallel arm and back takes

$$
t_\parallel = \frac{L}{c-v} + \frac{L}{c+v} = \frac{2Lc}{c^2 - v^2} = \frac{2L}{c}\left(1 - \frac{v^2}{c^2}\right)^{-1},
$$

since it travels at $c-v$ relative to the apparatus going one way (against the ether wind) and $c+v$ coming back. Light traveling down the perpendicular arm and back must be aimed slightly upstream (in the ether frame) to compensate for the sideways drift of the apparatus, so that its actual path through the ether is the hypotenuse of a right triangle with leg $L$; a short calculation (directly analogous to the light-clock argument of [Chapter 2](#ch-special-relativity)) gives

$$
t_\perp = \frac{2L}{c}\left(1 - \frac{v^2}{c^2}\right)^{-1/2}.
$$

:::{tip}
When a small parameter like $v/c$ appears, expand *before* subtracting, not after. Here $t_\parallel$ and $t_\perp$ individually differ from $2L/c$ only at order $(v/c)^2$; keeping just one or two terms of the binomial series for each is exactly precise enough to see that they don't cancel completely, while still being simple enough to work with by hand. Trying to compute $t_\parallel - t_\perp$ exactly first, then approximating, obscures the very cancellation that makes the leading term of order $(v/c)^2$ rather than $(v/c)$.
:::

For $v \ll c$, both expressions can be expanded with the binomial approximation, $(1-x)^{-1} \approx 1+x$ and $(1-x)^{-1/2} \approx 1 + x/2$:

$$
t_\parallel - t_\perp \approx \frac{2L}{c}\left[\left(1+\frac{v^2}{c^2}\right) - \left(1+\frac{v^2}{2c^2}\right)\right] = \frac{Lv^2}{c^3}.
$$

Rotating the apparatus by $90°$ swaps the roles of the two arms, doubling the effect, so the predicted shift in the interference pattern, measured in units of fringes (one fringe corresponding to one extra wavelength $\lambda$ of path-length difference), is

$$
\Delta N = \frac{2(t_\parallel - t_\perp)c}{\lambda} = \frac{2Lv^2}{\lambda c^2}.
$$

Plugging in the actual 1887 apparatus — effective arm length $L \approx 11\ \text{m}$ (achieved by multiple reflections), sodium light $\lambda \approx 590\ \text{nm}$, and Earth's orbital speed $v \approx 3.0\times10^4\ \text{m/s}$ — gives

$$
\Delta N = \frac{2(11\ \text{m})(3.0\times10^4\ \text{m/s})^2}{(590\times10^{-9}\ \text{m})(3.0\times10^8\ \text{m/s})^2} \approx 0.37\ \text{fringe},
$$

comfortably above the apparatus's sensitivity of about $0.01$ fringe — roughly a factor of $40$ in signal-to-noise. This is the calculation, worked in reverse from the design specifications, that told Michelson and Morley their apparatus was more than sensitive enough for the job.

#### The Null Result

The prediction was unambiguous: rotating the apparatus should shift the fringe pattern by an amount corresponding to Earth's motion through the ether, roughly $0.4$ fringe in the original 1887 apparatus — well above its sensitivity of about $0.01$ fringe. The experiment was repeated at different times of day and different seasons, in case Earth happened to be momentarily at rest relative to the ether when first tested — a concern that matters because Earth's *velocity* relative to any hypothetical ether should trace out an ellipse over the year as Earth orbits the Sun, vanishing at no more than isolated instants. **No shift of the predicted size was ever observed, in any orientation, at any time of year.** The measured shift was consistent with zero, roughly twenty times smaller than the effect Galilean relativity plus a stationary ether required. Later, more sensitive repetitions of the experiment (through the twentieth century, using lasers and eventually rotating optical cavities) have pushed the upper bound on any such effect down by many more orders of magnitude, with the same result: none.

The beam-splitting layout that makes this comparison possible is shown in {numref}`Figure %s <fig:ch01-interferometer>`.

```{figure} ../images/ch01-michelson-morley.svg
:label: fig:ch01-interferometer
:alt: Schematic of a Michelson–Morley interferometer with perpendicular arms, mirrors, a beam splitter, and a hypothetical ether wind.

The Michelson–Morley arrangement. A beam is split into perpendicular paths and recombined; rotating the apparatus exchanges the arms that are parallel and perpendicular to the hypothesized ether wind. Original schematic by the author.
```

What a fraction of a fringe looks like, and how little it takes to produce one, can be checked directly in {numref}`Figure %s <fig:ch01-interferometry-sim>`. Translating one mirror by half a wavelength moves the pattern by one full fringe, so the $0.37$ fringe that Michelson and Morley were hunting corresponds to an optical path difference of $0.37\lambda \approx 0.22\ \mu\text{m}$, and to a mirror motion of half that — small, but on this display an unmistakable movement of the whole pattern rather than a subtle change of shape. That is why the null result was so hard to argue with.

```{openphysics} InterferometryLab
:label: fig:ch01-interferometry-sim

The Michelson geometry that Michelson and Morley used, with the arms under direct control. The ether wind is not modeled — no experiment has ever needed it to be — but the instrument's response to a path-length difference between the arms is, and it is that response the 1887 apparatus was calibrated against.
```

## Further Null Results: Kennedy–Thorndike and Fizeau

### A Second Null Result: The Kennedy–Thorndike Experiment

The surviving photograph in {numref}`Figure %s <fig:ch01-historical-apparatus>` shows the scale and mechanical character of the original apparatus described above.

```{figure} ../images/historical-michelson-morley-1887.jpg
:label: fig:ch01-historical-apparatus
:alt: Historical photograph of the 1887 Michelson–Morley interferometer setup.

The Michelson–Morley apparatus at Case Western Reserve University, circa 1887. Photograph attributed to Case Western Reserve University; public domain via Wikimedia Commons.
```

One gap in the Michelson–Morley result deserves attention before moving on, because the way it was closed illustrates how tightly interlocking the eventual relativistic explanation would have to be. The Michelson–Morley experiment used two arms of *equal* length, and looked only for a fringe shift as the whole apparatus was *rotated*. This design has a subtle limitation: a length contraction ([Chapter 1](#ch-need-for-relativity), "Attempts to Save the Ether") of exactly the right amount would make $t_\parallel = t_\perp$ for *any* direction of the apparatus relative to the ether, since equal arm lengths contract to remain equal in the direction of motion — so rotating the equal-armed apparatus can never distinguish "no ether effects at all" from "an ether effect perfectly cancelled by length contraction alone." It says nothing about whether the *round-trip time itself* depends on velocity through the ether, only about whether the two perpendicular round-trip times remain equal to each other.

Roy Kennedy and Edward Thorndike closed this gap in 1932 with a modified apparatus using two arms of substantially *unequal* length, $L_1 \ne L_2$. With unequal arms, length contraction alone can no longer guarantee $t_1 = t_2$ at all times of year: even if each arm individually contracts as $L\sqrt{1-v^2/c^2}$, the resulting *difference* $t_1 - t_2$ still depends on the apparatus's instantaneous speed $v$ through the hypothetical ether — a speed that changes over the course of a year as Earth's orbital velocity vector changes direction (and, if the solar system itself moves through the ether, also has a component that does not average to zero). A length-contraction-only patch, with no accompanying change in the rate at which clocks run, predicts a fringe shift that slowly drifts as the year progresses. None was observed, to a precision even finer than Michelson and Morley's original bound.

The Kennedy–Thorndike null result rules out length contraction as a stand-alone patch: any viable account of these experiments must *also* include time dilation, changing the rate at which the light source's frequency (used as a built-in "clock" via the interference condition) ticks, in exactly the combination that the full Lorentz transformation provides. Michelson–Morley alone is consistent with "length contracts, nothing else needs to change"; Kennedy–Thorndike alone is consistent with several different combinations of length and time effects; only together, and only when combined with independent tests of time dilation itself ([Chapter 2](#ch-special-relativity)), do they pin down the Lorentz transformation uniquely, with no remaining free parameters. This is a useful methodological lesson that recurs throughout physics: a single null result can usually be explained away by more than one patch, and it typically takes a *family* of independent experiments, each closing off a different escape route, to force a genuinely new theory into place.

### A Complication: The Fizeau Experiment

The ether's troubles did not begin with Michelson and Morley. Decades earlier, in 1851, Hippolyte Fizeau performed a related but distinct experiment: rather than looking for an effect of Earth's motion through vacuum, he measured the speed of light *inside a moving medium* — water flowing rapidly through a pipe. Splitting a light beam so that one part traveled with the flow and the other against it, then recombining them interferometrically, Fizeau could measure how much the water's motion changed the light's speed compared to light in stationary water, $c/n$ (where $n\approx1.33$ is water's refractive index).

:::{margin}
The refractive index $n$ is defined so that light travels at speed $c/n$ in a stationary medium; $n>1$ for every ordinary transparent material, so $c/n<c$.
:::

The naive, purely mechanical expectation — light as a stream of particles, or the water fully "dragging" the ether along with it, either of which would give ordinary Galilean addition — predicts a shift of exactly $v$, the full speed of the flowing water:

$$
u_{\text{naive}} = \frac{c}{n} + v.
$$

Fizeau measured something different, and reproducibly so:

$$
u_{\text{measured}} = \frac{c}{n} + v\left(1 - \frac{1}{n^2}\right).
$$

The water drags the light along, but only *partially* — by a fraction $f = 1 - 1/n^2$ of its own speed, not the full speed $v$ predicted by simple addition, and not zero either (which is what a completely undragged, stationary ether unaffected by the moving medium would predict). This peculiar fractional drag coefficient had in fact been *predicted* in advance, in 1818, by Augustin-Jean Fresnel, on the strength of an equally peculiar ether model in which the ether inside a transparent medium is partially entrained in proportion to how much denser the medium's ether content is compared to vacuum's. The prediction matched Fizeau's measurement (and later, far more precise repetitions) to within experimental error — but it required inventing a specific, otherwise unmotivated rule for how much of the ether a given material drags along, a rule with no independent justification beyond fitting this one experiment.

Fizeau's result sat alongside the Michelson–Morley null result as a second, independent puzzle: whatever the ether was doing, it was not doing anything as simple as being either fully dragged along by matter or entirely undisturbed by it. As will become clear in [Chapter 2](#ch-special-relativity), once relativistic velocity addition replaces the Galilean rule, Fresnel's fractional drag coefficient emerges automatically — with no separate assumption about entrainment at all — as the leading term of $u_x = (u_x' + v)/(1 + u_x'v/c^2)$ evaluated at $u_x' = c/n$. What looked like an ad hoc patch to the ether model turns out to be an exact, parameter-free consequence of the correct kinematics.

:::{dropdown} Extracting the Fresnel coefficient from relativistic velocity addition
This chapter has not yet derived the relativistic velocity-addition formula — that is the work of [Chapter 2](#ch-special-relativity) — but it is worth seeing, in advance, exactly how the "unmotivated" Fresnel coefficient falls out of it, since the calculation is short. Substitute $u_x' = c/n$ (light's speed in water at rest) into $u_x = (u_x' + v)/(1 + u_x'v/c^2)$:

$$
u_x = \frac{\dfrac{c}{n} + v}{1 + \dfrac{v}{nc}}.
$$

For $v \ll c$, expand the denominator with $(1+x)^{-1} \approx 1 - x$:

$$
u_x \approx \left(\frac{c}{n} + v\right)\left(1 - \frac{v}{nc}\right)
\approx \frac{c}{n} + v - \frac{v}{n^2} + O(v^2)
= \frac{c}{n} + v\left(1 - \frac{1}{n^2}\right),
$$

where the cross term $v^2/(nc)$ from the first factor's $v$ times the second factor's $-v/(nc)$ has been dropped as second order in $v/c$. This reproduces Fizeau's measured formula exactly, with the fractional drag coefficient $f = 1 - 1/n^2$ appearing automatically — not as a separate hypothesis about how much ether a medium entrains, but as the leading correction to ordinary velocity addition once the correct (relativistic) addition rule is used in place of the Galilean one.
:::

Fizeau is shown in a late-nineteenth-century portrait in {numref}`Figure %s <fig:ch01-fizeau-historical>`.

```{figure} ../images/historical-fizeau.jpg
:label: fig:ch01-fizeau-historical
:alt: Historical portrait of physicist Hippolyte Fizeau.

Hippolyte Fizeau (1819–1896). Photograph by Charles Reutlinger; Académie des Sciences / Smithsonian Institution Libraries; public domain via Wikimedia Commons.
```

The three possibilities are summarized visually in {numref}`Figure %s <fig:ch01-fizeau>`: no drag, full Galilean drag, and the intermediate result actually observed.

```{figure} ../images/ch01-fizeau-velocity-addition.svg
:label: fig:ch01-fizeau
:alt: Moving water carries light by an amount between no drag and full Galilean drag, as described by the Fresnel coefficient.

Fizeau's moving-water result. The measured velocity is shifted by the Fresnel factor $1-1/n^2$, lying between the predictions of no drag and full Galilean addition. Original schematic by the author.
```

## Toward Einstein's Postulates

### Attempts to Save the Ether

The null result did not immediately convince anyone to abandon the ether; instead, it triggered a series of increasingly strained patches:

- **Ether drag.** Perhaps Earth drags the nearby ether along with it, so light near Earth's surface shows no relative motion. This was ruled out by *stellar aberration* — the small annual shift in the apparent position of stars (about $20.5$ arcseconds, first measured by James Bradley in 1727, well over a century before Michelson–Morley), caused by the combination of the finite speed of light and Earth's orbital velocity, in exact analogy to how vertically falling rain appears to come in at a slant to someone running through it. Aberration is correctly predicted only if the ether *at Earth's location* is not dragged along with Earth's motion — otherwise light arriving from a star would already share Earth's velocity by the time it reached a telescope, and no aberration would appear at all. This directly contradicts the ether-drag hypothesis needed to explain away Michelson–Morley.
- **The Fitzgerald–Lorentz contraction.** George FitzGerald and, independently, Hendrik Lorentz proposed that objects moving through the ether physically contract along their direction of motion by just the factor needed to make the two arms of the interferometer take equal time, hiding the effect. Concretely, if a rod of ether-frame length $L_0$ oriented along the direction of motion instead has length $L_0\sqrt{1-v^2/c^2}$, then $t_\parallel$ recomputed with this shortened arm length equals $t_\perp$ exactly, and no fringe shift results, for any $v$. Lorentz went further, introducing a fictitious "local time" that varied with position in exactly the combination $t - vx/c^2$ that would, decades later, turn out to be the correct relativistic time coordinate. Taken on its own, however, this is an *ad hoc* fix — a contraction (and a local time) invented for the sole purpose of explaining away one null result, with the ether itself still doing the conceptual work of defining a single true rest frame. It turns out to contain a genuine piece of the truth, but only once it is derived from a deeper principle rather than posited to save a failing hypothesis, which is what Einstein did in 1905 ([Chapter 2](#ch-special-relativity)).
- **Emission theories.** Perhaps light simply travels at speed $c$ relative to its *source*, with no ether needed at all — a proposal in the spirit of a bullet's speed depending on the gun that fired it. This was ruled out by observations of binary star systems (de Sitter, 1913): if the light emitted from each star carried the star's velocity, light from the approaching star would arrive systematically earlier than light from the receding star, garbling the observed orbital motion — in extreme cases, an observer might even see the same star appear to occupy several positions in its orbit at once, as light emitted at different orbital phases with different speeds arrived simultaneously. No such garbling is seen; binary star light curves and radial velocities are exactly periodic, matching Kepler's laws with the light's speed treated as constant, independent of the source's motion.

#### Worked Example: Estimating the Aberration Angle

The stellar-aberration bullet above asserts a value of about $20.5$ arcseconds; it is worth seeing where a number of that size comes from, since the same reasoning about combining velocities recurs throughout this chapter. Consider a star directly "overhead," so that in the Sun's rest frame its light arrives travelling straight down (speed $c$, along $-y$) at a telescope. In the frame of Earth, which moves at orbital speed $v \approx 3.0\times10^4\ \text{m/s}$ in some direction in the $x$-$y$ plane perpendicular to the line of sight, ordinary (Galilean) velocity subtraction gives the light's velocity components as measured on Earth: still $-c$ along $y$, but now also $-v$ along $x$, exactly as raindrops falling straight down acquire an apparent forward velocity component for a runner moving beneath them. The apparent direction of arrival is tilted from vertical by an angle $\theta$ with

$$
\tan\theta = \frac{v}{c} = \frac{3.0\times10^4\ \text{m/s}}{3.0\times10^8\ \text{m/s}} = 1.0\times10^{-4}.
$$

:::{margin}
The ratio $v/c \sim 10^{-4}$ for Earth's orbital motion is the recurring small number of this chapter: it sets the size of the Michelson–Morley fringe shift, the aberration angle, and the fractional Galilean speed shift in Exercise 1 alike.
:::

Since this is a very small angle, $\theta \approx 1.0\times10^{-4}\ \text{rad}$. Converting to arcseconds (using $1\ \text{rad} = 206{,}265''$),

$$
\theta \approx (1.0\times10^{-4}\ \text{rad})\left(\frac{206{,}265''}{1\ \text{rad}}\right) \approx 20.6'',
$$

in close agreement with the historically measured value of $20.5''$. Because Earth's velocity vector sweeps around in a full circle over the course of a year (always perpendicular to the instantaneous direction to a star near the pole of the ecliptic), each such star traces out a small circle of this same angular radius on the sky annually — exactly the periodic wobble Bradley detected in 1727, long before anyone suspected the ether was in trouble.

Each patch could account for the existing data but only by adding a new, unmotivated assumption, and no single patch accounted for *both* puzzles — the Michelson–Morley null result and the Fizeau partial-drag coefficient — without contradicting itself. What was needed was not another patch but a new starting point.

### Einstein's Postulates

In 1905, Einstein proposed to stop patching Galilean relativity and instead take the null result at face value, elevating it (together with the principle of relativity already implicit in mechanics, discussed above) to a postulate. Special relativity rests on two statements:

1. **The principle of relativity.** The laws of physics take the same form in all inertial reference frames. No experiment performed entirely within a closed laboratory can distinguish one inertial frame from another.
2. **The constancy of the speed of light.** The speed of light in vacuum has the same value $c$ in every inertial reference frame, independent of the motion of the source or the observer.

The first postulate was not new — as Galileo's ship illustrates, it already held for Newtonian mechanics, where no mechanical experiment can detect uniform motion (this is why you cannot feel the constant-velocity phase of a smooth flight, and why the butterflies in Galileo's cabin fly about undisturbed). Einstein's step was to insist that this postulate apply to *all* of physics, electromagnetism included, so that no experiment of any kind — mechanical or optical — can distinguish inertial frames; there is no preferred, ether-defined rest frame for anything, including light. The second postulate is the one that clashes head-on with Galilean relativity: if $u_x' = u_x - v$ held for light as it does for baseballs, two observers in relative motion could not both measure the same speed $c$ for the same light beam. Taken together, the postulates require that time and space themselves — not just the "aether wind" — behave differently than Galilean relativity assumes.

This is a genuinely radical move. Rather than asking "what medium is light waving in?", Einstein asked what kinematics — what set of rules for relating space and time coordinates between observers — is consistent with light having the same speed for everyone. The answer is not the Galilean transformation but the *Lorentz transformation*, and working out its consequences — the relativity of simultaneity, time dilation, length contraction, and (as noted above) the Fizeau drag coefficient as a special case of velocity addition — is the subject of [Chapter 2](#ch-special-relativity).

:::{seealso}
[](#ch-special-relativity) derives the Lorentz transformation from these two postulates and works out its consequences in detail — time dilation and length contraction (the effects this chapter's ether patches had to invent piecemeal), the relativity of simultaneity, and the relativistic velocity-addition formula used above to recover the Fizeau coefficient.
:::

Einstein was not working in a vacuum: Lorentz had already written down transformation equations of essentially the same mathematical form (motivated, as noted above, by fitting the Michelson–Morley and Fizeau data rather than by a physical principle), and Henri Poincaré, in the same year, independently emphasized that the principle of relativity should be regarded as an exact law of nature rather than an approximate consequence of ether dynamics, and showed that the Lorentz transformations form a mathematical group — a property essential for consistency, since applying two velocity boosts in succession must itself be equivalent to some single valid transformation. What distinguished Einstein's paper was not the equations themselves but their derivation: rather than reverse-engineering a transformation to fit the data, he started from the two postulates and showed that the Lorentz transformation is the *unique* kinematic consequence of taking them seriously, with time dilation, length contraction, and the relativity of simultaneity following as necessary theorems rather than independently adjustable assumptions.

It is worth appreciating just how much this single change in starting point accomplishes. The Michelson–Morley null result, the stellar-aberration data that rules out ether drag, the binary-star data that rules out emission theories, and the Fizeau drag coefficient were, before 1905, four separate empirical facts, each requiring its own explanation (or its own ad hoc patch) within the ether framework. Einstein's two postulates explain all four simultaneously, as different facets of a single underlying kinematic structure, with no adjustable parameters and no reference to a medium at all.

## Summary

- The principle of relativity — that no mechanical experiment inside a closed laboratory can detect uniform motion — already applied to Newtonian mechanics before 1905 (Galileo's ship). What was not settled was whether it extended to optics and electromagnetism, where Maxwell's equations single out a specific speed $c$ naturally interpreted as a speed relative to a medium, the luminiferous ether.
- The Galilean transformation and its associated velocity-addition rule, $u_x' = u_x - v$, predict that an observer moving through the ether should measure a speed of light different from $c$, by an amount of order Earth's orbital speed; the predicted Michelson–Morley fringe shift is $\Delta N = 2Lv^2/(\lambda c^2) \approx 0.4$ fringe for the 1887 apparatus.
- The Michelson–Morley interferometer was sensitive enough to detect this predicted shift but found none, at any time of year or orientation: the speed of light showed no dependence on the observer's motion through the presumed ether.
- The Kennedy–Thorndike experiment, using unequal interferometer arms, showed that length contraction alone (with no accompanying change in clock rates) cannot explain the null results: a genuine time-dilation effect must also be present, foreshadowing the two-part structure (length *and* time) of the Lorentz transformation derived in [Chapter 2](#ch-special-relativity).
- The Fizeau experiment, measuring the speed of light in flowing water, found a *partial* drag coefficient, $f = 1-1/n^2$ — neither the full entrainment nor the zero entrainment that simple ether pictures would predict — matching a formula (Fresnel's) that had no independent justification beyond fitting this one experiment.
- Proposed rescues of the ether hypothesis — ether drag, length contraction posited purely to hide the Michelson–Morley effect, and emission theories — each failed to survive further tests (stellar aberration, binary star observations) or amounted to an unmotivated patch rather than a principle, and none of them simultaneously accounted for the Fizeau coefficient.
- Einstein's 1905 postulates take the null result at face value: the laws of physics (postulate 1) and the speed of light in particular (postulate 2) are the same in every inertial frame. Together these are incompatible with the Galilean transformation and require a new kinematics, developed in [Chapter 2](#ch-special-relativity), which reproduces all of the results above — Michelson–Morley, aberration, binary-star timing, and the Fizeau coefficient — without any adjustable ether parameters.

## Problems

:::{exercise}
:label: ex-need-for-relativity-1

Earth orbits the Sun at approximately $v = 3.0\times10^4\ \text{m/s}$. Using the (incorrect) Galilean velocity-addition rule, estimate the fractional difference $(c+v)/(c-v) - 1$ between the speed of light measured "downstream" and "upstream" of Earth's motion through a stationary ether. Compare your estimate to the sensitivity you would need in an experiment to detect it.
:::

:::{solution} ex-need-for-relativity-1
:label: sol-need-for-relativity-1
:class: dropdown

Let $\beta=v/c$.  The requested fractional difference is

$$
\frac{c+v}{c-v}-1
=\frac{1+\beta}{1-\beta}-1
=\frac{(1+\beta)-(1-\beta)}{1-\beta}
=\frac{2\beta}{1-\beta}.
$$

With $c=3.00\times10^8\ \text{m/s}$,

$$
\beta=\frac{3.0\times10^4\ \text{m/s}}{3.00\times10^8\ \text{m/s}}
=1.0\times10^{-4},
$$

so

$$
\frac{2\beta}{1-\beta}
=\frac{2.0\times10^{-4}}{0.9999}
=2.000\times10^{-4}.
$$

Therefore, Galilean addition predicts a fractional directional difference of about $2.0\times10^{-4}$, or $200\ \text{parts per million}$, so an experiment would need sensitivity appreciably better than $2\times10^{-4}$ in speed or travel time to detect it.
:::

:::{exercise}
:label: ex-need-for-relativity-2

A swimmer who swims at speed $u$ in still water crosses a river of width $L$ flowing at speed $v < u$. (a) Find the time to swim straight across and back if the swimmer aims to always move perpendicular to the bank as seen from the shore. (b) Find the time to swim a distance $L$ directly upstream and then back downstream. (c) Show the two times are unequal, and explain the analogy to the two arms of the Michelson–Morley interferometer.
:::

:::{solution} ex-need-for-relativity-2
:label: sol-need-for-relativity-2
:class: dropdown

For the cross-river trip, the swimmer must devote a velocity component $v$ upstream to cancel the current.  If $u_y$ is the shore-frame component across the river, then

$$
u^2=v^2+u_y^2,
\qquad
u_y=\sqrt{u^2-v^2}.
$$

Each crossing takes $L/u_y$, so

$$
t_\perp=2\frac{L}{\sqrt{u^2-v^2}}.
$$

For the upstream--downstream trip, the two shore-frame speeds are $u-v$ and $u+v$.  Thus

$$
t_\parallel=\frac{L}{u-v}+\frac{L}{u+v}
=\frac{L[(u+v)+(u-v)]}{(u-v)(u+v)}
=\frac{2Lu}{u^2-v^2}.
$$

Their ratio is

$$
\frac{t_\parallel}{t_\perp}
=\frac{2Lu/(u^2-v^2)}{2L/\sqrt{u^2-v^2}}
=\frac{u}{\sqrt{u^2-v^2}}>1
\quad (v>0).
$$

Therefore, the upstream--downstream trip takes longer than the cross-river trip; this is precisely the classical ether prediction that the interferometer arm parallel to an ether wind has a longer round-trip light time than the perpendicular arm.

```{figure} ../images/ch01-sol-river-arms.svg
:label: fig:ch01-sol-river-arms
:alt: Side-by-side river diagrams showing a swimmer's cross-river and upstream-downstream round trips.

The river-current construction makes the key geometric difference explicit: holding a shore-fixed transverse path leaves a reduced crossing speed, while the parallel path has unequal upstream and downstream speeds.
```
:::

:::{exercise}
:label: ex-need-for-relativity-3

Explain, in your own words, why a null result from a single run of the Michelson-Morley experiment would not have been convincing on its own, and why repeating it at different times of year strengthened the conclusion.
:::

:::{solution} ex-need-for-relativity-3
:label: sol-need-for-relativity-3
:class: dropdown

One null result could have occurred at an unlucky orientation, at a time when Earth's velocity happened to have a small component relative to a hypothetical ether, or because of a temporary instrumental error.  A stationary-ether model predicts that Earth's velocity relative to the ether changes in direction and magnitude over a day and, especially, over a year as Earth orbits the Sun.  Therefore, obtaining null results after rotating the apparatus and repeating the measurement at many times of year rules out those accidental explanations: the predicted signal should have changed, but it did not.
:::

:::{exercise}
:label: ex-need-for-relativity-4

Suppose light, rather than obeying Einstein's second postulate, were emitted at speed $c$ relative to its source (an "emission theory" of light), like a bullet fired from a moving gun. Explain qualitatively why light from the two stars of a binary system, observed from Earth over one orbital period, would arrive with systematically distorted timing under this theory, and why this distortion is not observed.
:::

:::{solution} ex-need-for-relativity-4
:label: sol-need-for-relativity-4
:class: dropdown

In an emission theory, light emitted while a star moves toward Earth would initially have a larger Earth-frame speed than light emitted while it moves away.  During a binary orbit, successive pulses emitted at different orbital phases would therefore have different travel times across the same enormous star--Earth distance.  The apparent orbital timing would be systematically advanced for some phases and delayed for others, producing a distorted or scrambled light curve.  Since observed binary-star timing does not show that distance-amplified distortion, light cannot in general travel at $c$ relative to its moving source.
:::

:::{exercise}
:label: ex-need-for-relativity-5

Explain why the principle of relativity (postulate 1) already applied to Newtonian mechanics before 1905, and identify precisely what Einstein's second postulate adds that Newtonian mechanics did not have.
:::

:::{solution} ex-need-for-relativity-5
:label: sol-need-for-relativity-5
:class: dropdown

Newtonian mechanics already obeyed the first postulate because experiments involving forces, masses, and accelerations have the same form in every frame moving at constant velocity: $\vec F=m\vec a$ is unchanged by a Galilean transformation.  Einstein's second postulate adds the new empirical statement that every inertial observer also measures light in vacuum to have the same speed, $c=3.00\times10^8\ \text{m/s}$, independent of the source's or observer's motion.  This addition is absent from Newtonian mechanics and is incompatible with its velocity-addition rule.
:::

:::{exercise}
:label: ex-need-for-relativity-6

Derive the fringe-shift formula $\Delta N = 2Lv^2/(\lambda c^2)$ by working through the steps in the text, and use it to estimate the fringe shift a modern Michelson–Morley-style apparatus with arm length $L = 4\ \text{km}$ (comparable to a gravitational-wave observatory) and $\lambda = 1064\ \text{nm}$ would predict for Earth's orbital speed, if a stationary ether existed. Comment on how much more sensitive such an apparatus is, in principle, than Michelson and Morley's original tabletop instrument.
:::

:::{solution} ex-need-for-relativity-6
:label: sol-need-for-relativity-6
:class: dropdown

For the parallel arm, classical velocity addition gives

$$
t_\parallel=\frac{L}{c-v}+\frac{L}{c+v}
=\frac{2Lc}{c^2-v^2}
=\frac{2L}{c}\left(1-\frac{v^2}{c^2}\right)^{-1}.
$$

For the perpendicular arm, the light's transverse speed is $\sqrt{c^2-v^2}$, so

$$
t_\perp=\frac{2L}{\sqrt{c^2-v^2}}
=\frac{2L}{c}\left(1-\frac{v^2}{c^2}\right)^{-1/2}.
$$

For $v\ll c$, use $(1-x)^{-1}\simeq1+x$ and $(1-x)^{-1/2}\simeq1+x/2$:

$$
t_\parallel-t_\perp
\simeq\frac{2L}{c}\left(\frac{v^2}{c^2}-\frac{v^2}{2c^2}\right)
=\frac{Lv^2}{c^3}.
$$

Rotation reverses the sign of this difference, so it doubles the change in optical path:

$$
\Delta N=\frac{2c(t_\parallel-t_\perp)}{\lambda}
=\frac{2Lv^2}{\lambda c^2}.
$$

For $L=4.00\times10^3\ \text{m}$, $\lambda=1064\times10^{-9}\ \text{m}$, $v=3.0\times10^4\ \text{m/s}$, and $c=3.00\times10^8\ \text{m/s}$,

$$
\Delta N=\frac{2(4.00\times10^3\ \text{m})(3.0\times10^4\ \text{m/s})^2}
 {(1064\times10^{-9}\ \text{m})(3.00\times10^8\ \text{m/s})^2}
=7.5\times10^1\ \text{fringes}.
$$

Therefore, a stationary ether would predict about $75$ fringes for this apparatus, about $75/0.37\simeq2.0\times10^2$ times the original 1887 predicted shift, before considering the much better readout precision of modern instruments.
:::

:::{exercise}
:label: ex-need-for-relativity-7

A modern, high-precision version of the Michelson–Morley experiment finds an upper bound on any fringe shift roughly $10^{-5}$ times smaller than the shift $0.4$ fringe originally predicted by Galilean relativity plus a stationary ether. If this bound were instead interpreted (incorrectly, but for the sake of the exercise) as an upper limit on Earth's residual speed through a stationary ether, using the same fringe-shift formula, what upper limit on that speed would it imply? Compare this to Earth's orbital speed.
:::

:::{solution} ex-need-for-relativity-7
:label: sol-need-for-relativity-7
:class: dropdown

The stated upper bound is

$$
\Delta N_{\max}=(0.4\ \text{fringe})(10^{-5})=4.0\times10^{-6}\ \text{fringe}.
$$

For a fixed apparatus, $\Delta N\propto v^2$.  Thus, comparing this bound with the original prediction at $v_\oplus=3.0\times10^4\ \text{m/s}$ gives

$$
\frac{\Delta N_{\max}}{0.4\ \text{fringe}}
=\left(\frac{v_{\max}}{v_\oplus}\right)^2
=10^{-5},
$$

and hence

$$
v_{\max}=(3.0\times10^4\ \text{m/s})\sqrt{10^{-5}}
=9.5\times10^1\ \text{m/s}.
$$

Therefore, under the deliberately incorrect ether interpretation, the residual ether speed would be below about $95\ \text{m/s}$, which is about $3.2\times10^2$ times smaller than Earth's orbital speed.

```{figure} ../images/ch01-sol-ether-shift-scale.svg
:label: fig:ch01-sol-ether-shift-scale
:alt: Logarithmic comparison of the 1887 predicted fringe shift, the predicted shift for a four kilometre apparatus, and a modern null upper bound.

The logarithmic scale separates the large stationary-ether prediction from the tiny experimental bound; for a fixed apparatus, the signal varies as $v^2$.
```
:::

:::{exercise}
:label: ex-need-for-relativity-8

Using the Fizeau formula $u_{\text{measured}} = c/n + v(1-1/n^2)$, compute the predicted speed (in the lab frame) of light traveling through water ($n = 1.33$) flowing at $v = 7.0\ \text{m/s}$, both with and against the light's direction of travel. Find the difference between these two speeds, and compare it to the difference $2v$ that simple Galilean addition (full dragging) would predict.
:::

:::{solution} ex-need-for-relativity-8
:label: sol-need-for-relativity-8
:class: dropdown

The Fresnel coefficient for water is

$$
1-\frac{1}{n^2}=1-\frac{1}{(1.33)^2}=0.435.
$$

The speed of light in stationary water is

$$
\frac{c}{n}=\frac{3.00\times10^8\ \text{m/s}}{1.33}
=2.256\times10^8\ \text{m/s}.
$$

For water flowing with the light,

$$
u_+=\frac{c}{n}+v\left(1-\frac{1}{n^2}\right)
=2.256\times10^8\ \text{m/s}+(7.0\ \text{m/s})(0.435)
=225\,563\,912.8\ \text{m/s}.
$$

For water flowing against the light, the sign of $v$ reverses:

$$
u_-=225\,563\,906.7\ \text{m/s}.
$$

Thus $u_+-u_-=2(3.04\ \text{m/s})=6.09\ \text{m/s}$; this is smaller than the $2v=14.0\ \text{m/s}$ difference predicted by full Galilean dragging.
:::

:::{exercise}
:label: ex-need-for-relativity-9

Jupiter orbits the Sun at an orbital speed of about $v = 1.3\times10^4\ \text{m/s}$. If an astronomer stationed on Jupiter observed the same "overhead" star discussed in the worked example on aberration, using the same reasoning, what angular radius (in arcseconds) would that astronomer measure for the star's annual aberration ellipse? Explain why the ratio of your answer to Earth's $20.5''$ depends only on the ratio of the two planets' orbital speeds.
:::

:::{solution} ex-need-for-relativity-9
:label: sol-need-for-relativity-9
:class: dropdown

For a small aberration angle, $\tan\theta\simeq\theta=v/c$, so the aberration angle is proportional to orbital speed.  Therefore

$$
\theta_J=\theta_\oplus\frac{v_J}{v_\oplus}
=(20.5\ \text{arcsec})\frac{1.3\times10^4\ \text{m/s}}{3.0\times10^4\ \text{m/s}}
=8.9\ \text{arcsec}.
$$

Therefore, the astronomer on Jupiter would measure an annual aberration ellipse with angular radius about $8.9\ \text{arcsec}$, and the ratio to Earth's angle depends only on $v_J/v_\oplus$ because the common factor $1/c$ cancels.
:::

:::{exercise}
:label: ex-need-for-relativity-10

Explain why an ether model in which Earth *fully* drags the surrounding ether along with it (proposed to explain the Michelson–Morley null result) is inconsistent with the existence of stellar aberration, using the falling-rain analogy described in the text: a person standing still under vertically falling rain gets wet only from directly above, while a person running through the rain must tilt an umbrella forward to stay dry. What would "full ether drag" have to imply about the umbrella, if starlight is the falling rain and Earth's atmosphere is analogous to the region being dragged?
:::

:::{solution} ex-need-for-relativity-10
:label: sol-need-for-relativity-10
:class: dropdown

Starlight behaves like the falling rain: because Earth moves sideways while the light enters the telescope, the telescope must be tilted slightly into the apparent direction from which the light arrives.  Full ether drag near Earth would make the local ether, and hence the starlight's propagation direction relative to Earth, move along with Earth.  In the rain analogy, it would make the rain in the dragged region fall exactly vertically for the runner, so the umbrella would never need a forward tilt.  Therefore, full ether drag predicts zero stellar aberration, whereas the observed nonzero annual aberration rules it out.
:::

:::{exercise}
:label: ex-need-for-relativity-11

Explain, in your own words, why the original Michelson–Morley design (equal-length arms, apparatus rotated) cannot by itself distinguish "no ether effects" from "an ether effect exactly cancelled by a velocity-dependent length contraction." Then explain why making the two arms unequal in length (Kennedy–Thorndike) closes this loophole.
:::

:::{solution} ex-need-for-relativity-11
:label: sol-need-for-relativity-11
:class: dropdown

With equal arms, a hypothesized length contraction can shorten whichever arm is instantaneously parallel to the ether wind by exactly the amount needed to make its longer classical light time equal to the perpendicular-arm time.  After a $90^\circ$ rotation the other equal arm contracts by the same rule, so the experiment still gives no difference; an equal-arm null result therefore cannot distinguish this cancellation from no ether effect at all.  With unequal arms, $L_1\ne L_2$, the two light times retain a difference whose size depends on Earth's speed through the ether, even if each parallel length contracts.  Therefore, an annual change in the hypothetical ether speed would produce a Kennedy--Thorndike fringe drift unless time-rate changes accompany the length contraction, and the observed absence of that drift closes the loophole.
:::

:::{exercise}
:label: ex-need-for-relativity-12

Suppose (contrary to fact) that the Kennedy–Thorndike experiment *had* detected a fringe drift over the course of a year, of a size consistent with length contraction being the *only* relativistic effect (i.e., with clocks ticking at the same rate in every frame). Explain qualitatively why this outcome would have been logically consistent with the original Michelson–Morley null result, even though it would have been inconsistent with the time dilation and Lorentz transformation developed in [Chapter 2](#ch-special-relativity).
:::

:::{solution} ex-need-for-relativity-12
:label: sol-need-for-relativity-12
:class: dropdown

A length-contraction-only theory could make the two equal Michelson--Morley arms have equal round-trip times at every orientation, so the original rotation experiment could still have produced its observed null result.  However, for unequal Kennedy--Thorndike arms, that same theory leaves a velocity-dependent difference in travel time because the arms have different lengths; Earth's changing speed relative to the ether would then create a yearly fringe drift.  Therefore, the hypothetical drift would be consistent with the original equal-arm null result but would show that clock rates do not transform with the compensating time-dilation factor required by the Lorentz transformation, contradicting special relativity.
:::
