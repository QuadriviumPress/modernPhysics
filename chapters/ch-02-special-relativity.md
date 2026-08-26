---
title: Special Relativity
short_title: Chapter 2. Special Relativity
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Derive and apply the relativity of simultaneity from Einstein's postulates.
- Derive and apply time dilation, including the concept of proper time.
- Derive and apply length contraction, including the concept of proper length.
- Use the Lorentz transformation to relate the space and time coordinates of an event in two inertial frames.
- Apply the relativistic velocity-addition formula and show that it never yields a result exceeding $c$.
- Construct and interpret simple spacetime diagrams.

## Introduction

Chapter 1 established that Einstein's two postulates — the equivalence of all inertial frames, and the invariance of the speed of light — are incompatible with the Galilean transformation. This chapter works out what *does* follow from the postulates: a new set of rules relating space and time measurements between observers in relative motion, called the Lorentz transformation. Its consequences are strange by the standards of everyday experience — moving clocks run slow, moving objects are measured as shortened, and two events that are simultaneous for one observer need not be simultaneous for another — but they are not arbitrary. Each follows directly, and only, from insisting that every inertial observer measures the same speed $c$ for light.

Throughout, an **event** is something that happens at a definite place and a definite time — a flashbulb going off, a particle passing a marker — specified by four coordinates $(x, y, z, t)$ in a given reference frame. Two different inertial observers, in relative motion, will in general assign different coordinates to the same event; the question this chapter answers is exactly how those coordinate sets are related.

## The Relativity of Simultaneity

Consider a train car moving at constant velocity $v$ relative to the ground, with a light source at its exact center. When the source flashes, light travels outward in all directions at speed $c$ — in *every* inertial frame, by the second postulate.

To an observer sitting at the center of the car, the light reaches the front and back walls simultaneously, since both walls are equidistant from the source and light travels at the same speed $c$ in both directions in the car's own frame.

To an observer standing on the ground watching the car go by, the situation is different. In the ground frame, light still travels at speed $c$ in both directions — but the back wall of the car is moving *toward* the point where the backward-going light was emitted, while the front wall is moving *away* from the point where the forward-going light was emitted. So light reaches the back wall first. The two flashes, simultaneous in the car's frame, are **not** simultaneous in the ground frame.

This is not a measurement error or a signal-delay artifact to be corrected for — it is a genuine disagreement about which events are simultaneous, forced on us by the requirement that both observers measure the same speed $c$ for the same light pulses. **Simultaneity is relative to the observer's frame of motion**, not an absolute, frame-independent relation between events. This single fact is the seed from which time dilation and length contraction both grow.

## Time Dilation

Consider a **light clock**: two mirrors facing each other, separated by a distance $L$, with a single light pulse bouncing between them. In the frame where the clock is at rest, one "tick" — one round trip — takes

$$
\Delta t_0 = \frac{2L}{c}.
$$

This time, measured in the frame where the clock does not move, is called the **proper time** between the two events (pulse leaves the bottom mirror; pulse returns to the bottom mirror) — the time measured by a clock present at both events, at the same location.

Now view the same clock from a frame in which it moves at speed $v$ perpendicular to the line joining the mirrors. In this frame, between emission and return the light pulse must travel not just up and down but also sideways with the clock, tracing a diagonal path. Since light still travels at speed $c$ in this frame (postulate 2), and the diagonal path is longer than $2L$, the round trip must take *longer* as measured here. Writing $\Delta t$ for the round-trip time in this frame, the pulse travels a horizontal distance $v\Delta t$ while covering the diagonal distance $c\Delta t$, and by the Pythagorean theorem applied to each mirror-to-mirror leg,

$$
\left(\frac{c\Delta t}{2}\right)^2 = L^2 + \left(\frac{v\Delta t}{2}\right)^2.
$$

Substituting $L = c\Delta t_0/2$ and solving for $\Delta t$ gives

$$
\Delta t = \frac{\Delta t_0}{\sqrt{1 - v^2/c^2}} \equiv \gamma\, \Delta t_0,
$$

where the **Lorentz factor**

$$
\gamma \equiv \frac{1}{\sqrt{1 - v^2/c^2}}
$$

is greater than or equal to $1$ for any $v < c$, and grows without bound as $v \to c$. This is **time dilation**: a clock moving at speed $v$ relative to an observer is measured by that observer to run slow, ticking out $\Delta t = \gamma \Delta t_0$ of the observer's own time for every $\Delta t_0$ of proper time it displays. The effect is symmetric — each of two observers in relative motion sees the *other's* clock as running slow, since each is equally entitled to regard themselves as at rest. Although derived here for a light clock, time dilation applies to time itself, and hence to every physical process — mechanical clocks, radioactive decay rates, biological aging — since two different physical clocks, built differently, must stay in agreement in every frame or their disagreement could be used to detect absolute motion, contradicting postulate 1.

Time dilation is not a hypothesis awaiting confirmation; it is routinely observed. Muons created by cosmic rays in the upper atmosphere have a mean lifetime, at rest, of about $2.2\ \mu\text{s}$ — long enough, at nearly the speed of light, to travel only a few hundred meters before decaying, far short of the several kilometers to Earth's surface. Yet large numbers of these muons are detected at sea level. In Earth's frame, the muons' internal "clock" — the process governing decay — runs slow by the factor $\gamma$, extending their mean range by that same factor, which is exactly what is observed.

## Length Contraction

Time dilation has a companion effect for lengths. Consider a rod of length $L_0$ at rest along the $x$-axis of frame $S$; call $L_0$ the **proper length** — the length measured in the frame where the rod is at rest. How long is this rod as measured by an observer in frame $S'$, moving at speed $v$ relative to $S$ along the rod's length?

To measure a moving rod's length, an observer must record the positions of both ends *at the same instant* in their own frame. Consider the muon example again, now from the muon's own rest frame, in which it is Earth's atmosphere that rushes past at speed $v$. In the muon's frame, the muon does not live any longer than its proper lifetime $\Delta t_0$; instead, it is the *distance* to Earth's surface that must be short enough to be crossed in that proper time, i.e., $L = v\Delta t_0$. Combining this with the Earth-frame result $\Delta t = \gamma \Delta t_0$ and $L_0 = v\Delta t$ (the proper atmospheric depth, as measured in Earth's frame) gives

$$
L = v\Delta t_0 = \frac{v \Delta t}{\gamma} = \frac{L_0}{\gamma},
$$

or

$$
L = \frac{L_0}{\gamma} = L_0\sqrt{1 - v^2/c^2}.
$$

This is **length contraction**: an object of proper length $L_0$, measured by an observer relative to whom it moves at speed $v$ along its own length, is found to have length $L = L_0/\gamma \le L_0$. Only lengths *along* the direction of relative motion contract; lengths perpendicular to the motion are unaffected (a consequence one can show is required for consistency between the two observers' descriptions of, e.g., a rod passing through a ring). Note the resemblance to the Fitzgerald–Lorentz contraction of Chapter 1 — the same formula, but now derived as a necessary consequence of the postulates rather than invented to hide a null result.

## The Lorentz Transformation

Time dilation and length contraction are special cases of a general coordinate transformation between inertial frames, replacing the Galilean transformation of Chapter 1. For frame $S'$ moving at velocity $v$ along the common $x$-$x'$ axis relative to frame $S$, with origins coinciding at $t = t' = 0$, the **Lorentz transformation** is

$$
x' = \gamma(x - vt), \qquad y' = y, \qquad z' = z, \qquad t' = \gamma\left(t - \frac{vx}{c^2}\right).
$$

The inverse transformation (from $S'$ back to $S$) has the same form with $v \to -v$:

$$
x = \gamma(x' + vt'), \qquad t = \gamma\left(t' + \frac{vx'}{c^2}\right).
$$

Two features are worth noting. First, in the limit $v \ll c$, $\gamma \to 1$ and the $vx/c^2$ term becomes negligible, and the Lorentz transformation reduces to the Galilean transformation — special relativity does not discard Newtonian kinematics but contains it as the low-speed limit. Second, the time coordinate $t'$ depends on *both* $t$ and $x$: two events at different locations $x$ that are simultaneous ($t_1 = t_2$) in frame $S$ are, in general, *not* simultaneous in $S'$ unless they also share the same $x$ — a direct, quantitative statement of the relativity of simultaneity derived qualitatively above.

A quantity that has the same value in every inertial frame is called a **Lorentz invariant**. The most important one is the *spacetime interval* between two events,

$$
(\Delta s)^2 = c^2(\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2,
$$

which every inertial observer computes to be the same number, even though $\Delta t$ and $\Delta x$ individually differ between frames. This invariance can be verified directly by substituting the Lorentz transformation.

## Velocity Addition

If a particle moves with velocity $u_x'$ along the $x'$-axis of frame $S'$, and $S'$ moves at velocity $v$ relative to $S$, what velocity $u_x$ does the particle have in $S$? Differentiating the Lorentz transformation (or applying it to two nearby events along the particle's path) gives the **relativistic velocity-addition formula**:

$$
u_x = \frac{u_x' + v}{1 + \dfrac{u_x' v}{c^2}}.
$$

For $u_x', v \ll c$, the denominator is nearly $1$ and this reduces to the familiar Galilean rule $u_x \approx u_x' + v$. But for $u_x' = c$ (light, in the particle's own frame), the formula gives

$$
u_x = \frac{c + v}{1 + v/c} = c,
$$

for *any* $v < c$ — exactly consistent with the second postulate: adding any sub-light velocity to $c$ still gives $c$. More generally, one can show that if $u_x' < c$ and $v < c$, then $u_x < c$ always: no combination of sub-light velocities, added relativistically, ever reaches or exceeds $c$.

## Spacetime Diagrams

A useful way to visualize these effects is a **spacetime diagram**: a plot with $x$ on the horizontal axis and $ct$ (rather than $t$, so both axes share units of length) on the vertical axis, drawn in a chosen frame $S$. A particle at rest at some fixed $x$ traces a vertical line (its **worldline**); a light ray traces a line at $45°$, since $x = ct$. An observer moving at speed $v$ in frame $S$ has a worldline tilted from vertical by an angle $\theta$ with $\tan\theta = v/c$.

In frame $S'$, that same moving observer's own $x'$ and $ct'$ axes are *not* perpendicular in the diagram as drawn in $S$: the $ct'$ axis coincides with the observer's own worldline, while the $x'$ axis — the locus of events simultaneous with the origin in $S'$ — tilts up from the $x$-axis by the same angle $\theta$ that the $ct'$ axis tilts from the $ct$-axis. This tilted-axis picture is a direct graphical statement of the relativity of simultaneity: the set of events an $S'$-observer calls "now" is not the same as the set an $S$-observer calls "now." Reading distances off a spacetime diagram requires care (the Lorentz-transformed axes are not orthogonal in the Euclidean sense), but the picture makes clear that simultaneity, not merely elapsed time, is the coordinate that differs between frames.

## Summary

- Because both postulates must hold simultaneously, two events simultaneous in one inertial frame are, in general, not simultaneous in another: **simultaneity is relative**.
- A clock moving at speed $v$ relative to an observer runs slow by the Lorentz factor $\gamma = 1/\sqrt{1-v^2/c^2}$: $\Delta t = \gamma\, \Delta t_0$, where $\Delta t_0$ is the **proper time**, measured in the clock's own rest frame. This is **time dilation**, confirmed directly by observations such as cosmic-ray muon decay.
- An object of proper length $L_0$ (measured in its own rest frame) has length $L = L_0/\gamma$ as measured by an observer relative to whom it moves along its length. This is **length contraction**; only lengths along the direction of motion are affected.
- The **Lorentz transformation**, $x' = \gamma(x-vt)$, $t' = \gamma(t - vx/c^2)$, replaces the Galilean transformation and reduces to it for $v \ll c$. The spacetime interval $(\Delta s)^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is the same in every inertial frame.
- Velocities combine via $u_x = (u_x' + v)/(1 + u_x'v/c^2)$, which reduces to Galilean addition at low speed and never produces a result at or above $c$ when combining sub-light speeds.
- Spacetime diagrams represent these effects graphically: a moving observer's axes of space and time are both tilted, by an equal angle, relative to a "stationary" observer's axes.

## Problems

1. A spaceship passes Earth at $v = 0.80c$. A clock on the ship ticks off exactly $1.00\ \text{s}$ of proper time between two events at the same location on the ship. (a) What time interval between these two events is measured by an observer on Earth? (b) What is $\gamma$ for this speed?

2. A meter stick at rest in frame $S'$ makes an angle such that it lies entirely along the direction of relative motion. If $S'$ moves at $v = 0.60c$ relative to $S$, what length is the stick measured to have in $S$?

3. Two events occur at the same time $t=0$ in frame $S$, at positions $x_1 = 0$ and $x_2 = 300\ \text{m}$. Frame $S'$ moves at $v = 0.50c$ relative to $S$ along the $x$-axis, with origins coinciding at $t=t'=0$. Use the Lorentz transformation to find $t_1'$ and $t_2'$, and confirm that the two events are not simultaneous in $S'$.

4. A cosmic-ray muon is created at an altitude of $15\ \text{km}$, moving straight down at $v = 0.998c$. Its proper mean lifetime is $2.2\ \mu\text{s}$. (a) Using time dilation, find the mean lifetime as measured in Earth's frame, and the mean distance the muon travels before decaying in that frame. (b) Working instead in the muon's rest frame, use length contraction to find the depth of the $15\ \text{km}$ atmospheric layer as the muon measures it, and show your two calculations of whether the muon is likely to reach the ground agree.

5. Two spaceships approach each other, each moving at speed $0.75c$ relative to Earth, in opposite directions. (a) What speed does an observer on one ship measure for the other ship, using relativistic velocity addition? (b) Explain why simply adding $0.75c + 0.75c$ would give an unphysical answer, and identify which postulate this would violate.

6. Sketch a spacetime diagram (axes $x$ and $ct$) in the rest frame $S$ of a laboratory. Draw the worldline of a particle at rest at $x = 2\ \text{m}$, the worldline of a particle moving at $v = 0.5c$ starting from the origin, and the worldline of a light pulse emitted from the origin at $t=0$. Identify the angle each worldline makes with the vertical axis.
