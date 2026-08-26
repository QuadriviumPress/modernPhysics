---
title: The Need for Relativity
short_title: Chapter 1. The Need for Relativity
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain why late-nineteenth-century physics appeared essentially complete, and identify the handful of unresolved puzzles that undid that picture.
- State the Galilean transformation and Galilean velocity-addition rule, and explain what they predict for the speed of light.
- Describe the luminiferous-ether hypothesis and the reasoning behind the Michelson–Morley experiment.
- Explain why the null result of the Michelson–Morley experiment could not be explained away within Newtonian mechanics and a stationary ether.
- State Einstein's two postulates of special relativity and explain why they are jointly incompatible with Galilean relativity.

## Introduction

By the 1890s, many physicists believed their subject was nearly finished. Newtonian mechanics predicted the motion of planets, projectiles, and machinery with extraordinary precision; Maxwell's equations had unified electricity, magnetism, and optics into a single theory of the electromagnetic field and correctly predicted that light is an electromagnetic wave. A famous (if perhaps apocryphal) remark attributed to physicists of the era held that all that remained was to measure constants to more decimal places.

That confidence concealed a handful of loose threads. This chapter follows one of them: Maxwell's equations predict a definite speed for light, $c \approx 3.00\times10^{8}\ \text{m/s}$, but they do not say *relative to what* that speed is measured. Every other wave known to nineteenth-century physics — sound, water waves, waves on a string — is a disturbance in a material medium, and its speed is fixed relative to that medium, not relative to an observer. It was natural to assume light must be the same: a wave in some all-pervading substance, the *luminiferous ether*, with $c$ being its speed relative to the ether alone. Observers moving through the ether should then measure a different speed for light, just as a swimmer's speed relative to the shore depends on whether they swim with or against a current. The experiment designed to detect this effect — and its stubborn refusal to find one — is where this chapter begins.

## Galilean Relativity and the Speed of Light

Newtonian mechanics is built on a specific rule for relating measurements made by observers moving relative to one another. Consider two reference frames, $S$ and $S'$, with $S'$ moving at constant velocity $v$ along the $x$-axis of $S$, and with their origins coinciding at $t = 0$. The *Galilean transformation* relates the coordinates of an event as measured in each frame:

$$
x' = x - vt, \qquad y' = y, \qquad z' = z, \qquad t' = t.
$$

The last equation encodes an assumption so natural to everyday experience that it usually goes unstated: time flows identically for every observer, regardless of how they are moving. Differentiating the transformation for $x$ gives the familiar classical velocity-addition rule. If an object moves with velocity $u_x$ in frame $S$, its velocity in $S'$ is

$$
u_x' = u_x - v.
$$

This is the rule that lets you add your walking speed to a moving walkway, or a thrown ball's speed to the speed of the train from which it is thrown. Applied to light, it makes a sharp prediction: if light travels at speed $c$ relative to the ether, and Earth moves through the ether at orbital speed $v \approx 3\times 10^4\ \text{m/s}$, then an observer on Earth measuring light traveling in the same direction as Earth's motion should get $c - v$, and light traveling in the opposite direction should give $c + v$. The effect is small — about one part in $10^4$ — but with an interferometer sensitive enough to detect a shift in the interference pattern of order that size, it should be measurable.

## The Michelson–Morley Experiment

Albert Michelson (and later Michelson working with Edward Morley) built exactly such an interferometer. Its principle is to split a beam of light into two perpendicular paths, reflect each off a mirror, recombine the beams, and observe the resulting interference pattern. If Earth moves through the ether, the round-trip travel time along the path parallel to that motion should differ slightly from the round-trip time along the perpendicular path, because a "cross-stream" trip and an "upstream–downstream" trip through a moving medium take different times even when the two paths have equal length — the same effect that makes a boat crossing a river directly and returning take less time than travelling the same distance upstream and back. The predicted difference is small, but the interferometer was sensitive enough to detect a shift of a small fraction of a fringe, and the apparatus was mounted on a stone slab floating on mercury so that it could be rotated smoothly to swap the roles of the two arms.

The prediction was unambiguous: rotating the apparatus should shift the fringe pattern by an amount corresponding to Earth's motion through the ether, roughly $0.4$ fringe in the original 1887 apparatus — well above its sensitivity of about $0.01$ fringe. The experiment was repeated at different times of day and different seasons, in case Earth happened to be momentarily at rest relative to the ether when first tested. **No shift of the predicted size was ever observed, in any orientation, at any time of year.** The measured shift was consistent with zero, roughly twenty times smaller than the effect Galilean relativity plus a stationary ether required.

## Attempts to Save the Ether

The null result did not immediately convince anyone to abandon the ether; instead, it triggered a series of increasingly strained patches:

- **Ether drag.** Perhaps Earth drags the nearby ether along with it, so light near Earth's surface shows no relative motion. This was ruled out by *stellar aberration* — the small annual shift in the apparent position of stars, which is correctly predicted only if the ether near Earth is *not* dragged along with it.
- **The Fitzgerald–Lorentz contraction.** George FitzGerald and, independently, Hendrik Lorentz proposed that objects moving through the ether physically contract along their direction of motion by just the factor needed to make the two arms of the interferometer take equal time, hiding the effect. Taken on its own this is an *ad hoc* fix — a contraction invented for the sole purpose of explaining away one null result. It turns out to contain a genuine piece of the truth, but only once it is derived from a deeper principle rather than posited to save a failing hypothesis, which is what Einstein did in 1905 (Chapter 2).
- **Emission theories.** Perhaps light simply travels at speed $c$ relative to its *source*, with no ether needed at all — a proposal in the spirit of a bullet's speed depending on the gun that fired it. This was ruled out by observations of binary star systems (de Sitter, 1913): if the light emitted from each star carried the star's velocity, light from the approaching star would arrive systematically earlier than light from the receding star, garbling the observed orbital motion. No such garbling is seen.

Each patch could account for the existing data but only by adding a new, unmotivated assumption. What was needed was not another patch but a new starting point.

## Einstein's Postulates

In 1905, Einstein proposed to stop patching Galilean relativity and instead take the null result at face value, elevating it (together with a principle already implicit in mechanics) to a postulate. Special relativity rests on two statements:

1. **The principle of relativity.** The laws of physics take the same form in all inertial reference frames. No experiment performed entirely within a closed laboratory can distinguish one inertial frame from another.
2. **The constancy of the speed of light.** The speed of light in vacuum has the same value $c$ in every inertial reference frame, independent of the motion of the source or the observer.

The first postulate was not new — it already held for Newtonian mechanics, where no mechanical experiment can detect uniform motion (this is why you cannot feel the constant-velocity phase of a smooth flight). Einstein's step was to insist that this postulate apply to *all* of physics, electromagnetism included, so that no experiment of any kind — mechanical or optical — can distinguish inertial frames. The second postulate is the one that clashes head-on with Galilean relativity: if $u_x' = u_x - v$ held for light as it does for baseballs, two observers in relative motion could not both measure the same speed $c$ for the same light beam. Taken together, the postulates require that time and space themselves — not just the "aether wind" — behave differently than Galilean relativity assumes.

This is a genuinely radical move. Rather than asking "what medium is light waving in?", Einstein asked what kinematics — what set of rules for relating space and time coordinates between observers — is consistent with light having the same speed for everyone. The answer is not the Galilean transformation but the *Lorentz transformation*, and working out its consequences — the relativity of simultaneity, time dilation, length contraction — is the subject of Chapter 2.

## Summary

- By the late nineteenth century, Maxwell's equations predicted a definite speed of light $c$, and it was assumed this speed was defined relative to a hypothetical medium, the luminiferous ether.
- The Galilean transformation and its associated velocity-addition rule, $u_x' = u_x - v$, predict that an observer moving through the ether should measure a speed of light different from $c$, by an amount of order Earth's orbital speed.
- The Michelson–Morley interferometer was sensitive enough to detect this predicted shift but found none, at any time of year or orientation: the speed of light showed no dependence on the observer's motion through the presumed ether.
- Proposed rescues of the ether hypothesis — ether drag, length contraction posited purely to hide the effect, and emission theories — each failed to survive further tests (stellar aberration, binary star observations) or amounted to an unmotivated patch rather than a principle.
- Einstein's 1905 postulates take the null result at face value: the laws of physics (postulate 1) and the speed of light in particular (postulate 2) are the same in every inertial frame. Together these are incompatible with the Galilean transformation and require a new kinematics, developed in Chapter 2.

## Problems

1. Earth orbits the Sun at approximately $v = 3.0\times10^4\ \text{m/s}$. Using the (incorrect) Galilean velocity-addition rule, estimate the fractional difference $(c+v)/(c-v) - 1$ between the speed of light measured "downstream" and "upstream" of Earth's motion through a stationary ether. Compare your estimate to the sensitivity you would need in an experiment to detect it.

2. A swimmer who swims at speed $u$ in still water crosses a river of width $L$ flowing at speed $v < u$. (a) Find the time to swim straight across and back if the swimmer aims to always move perpendicular to the bank as seen from the shore. (b) Find the time to swim a distance $L$ directly upstream and then back downstream. (c) Show the two times are unequal, and explain the analogy to the two arms of the Michelson–Morley interferometer.

3. Explain, in your own words, why a null result from a single run of the Michelson-Morley experiment would not have been convincing on its own, and why repeating it at different times of year strengthened the conclusion.

4. Suppose light, rather than obeying Einstein's second postulate, were emitted at speed $c$ relative to its source (an "emission theory" of light), like a bullet fired from a moving gun. Explain qualitatively why light from the two stars of a binary system, observed from Earth over one orbital period, would arrive with systematically distorted timing under this theory, and why this distortion is not observed.

5. Explain why the principle of relativity (postulate 1) already applied to Newtonian mechanics before 1905, and identify precisely what Einstein's second postulate adds that Newtonian mechanics did not have.
