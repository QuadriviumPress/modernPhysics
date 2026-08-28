---
title: Special Relativity
short_title: Chapter 2. Special Relativity
label: ch-special-relativity
numbering:
  enumerator: "2.%s"
---

## Learning Objectives

By the end of this chapter, you should be able to:

- Derive and apply the relativity of simultaneity from Einstein's postulates, and describe an operational procedure for synchronizing clocks within a single frame.
- Derive and apply time dilation, including the concept of proper time.
- Derive and apply length contraction, including the concept of proper length.
- Use the Lorentz transformation to relate the space and time coordinates of an event in two inertial frames.
- Apply the relativistic velocity-addition formula, show that it never yields a result exceeding $c$, and use it to explain the Fizeau drag coefficient of [Chapter 1](#ch-need-for-relativity).
- Construct and interpret simple spacetime diagrams, including the light cone and its role in cause and effect.
- Explain the resolution of the twin paradox in terms of the asymmetry between inertial and non-inertial motion.
- Derive and apply the relativistic Doppler effect.
- Explain why magnetism can be understood as a relativistic consequence of length contraction acting on electric fields.

## Introduction

[Chapter 1](#ch-need-for-relativity) established that Einstein's two postulates — the equivalence of all inertial frames, and the invariance of the speed of light — are incompatible with the Galilean transformation. This chapter works out what *does* follow from the postulates: a new set of rules relating space and time measurements between observers in relative motion, called the Lorentz transformation. Its consequences are strange by the standards of everyday experience — moving clocks run slow, moving objects are measured as shortened, and two events that are simultaneous for one observer need not be simultaneous for another — but they are not arbitrary. Each follows directly, and only, from insisting that every inertial observer measures the same speed $c$ for light.

Throughout, an **event** is something that happens at a definite place and a definite time — a flashbulb going off, a particle passing a marker — specified by four coordinates $(x, y, z, t)$ in a given reference frame. Two different inertial observers, in relative motion, will in general assign different coordinates to the same event; the question this chapter answers is exactly how those coordinate sets are related.

## The Relativity of Simultaneity

Consider a train car moving at constant velocity $v$ relative to the ground, with a light source at its exact center. When the source flashes, light travels outward in all directions at speed $c$ — in *every* inertial frame, by the second postulate.

To an observer sitting at the center of the car, the light reaches the front and back walls simultaneously, since both walls are equidistant from the source and light travels at the same speed $c$ in both directions in the car's own frame.

To an observer standing on the ground watching the car go by, the situation is different. In the ground frame, light still travels at speed $c$ in both directions — but the back wall of the car is moving *toward* the point where the backward-going light was emitted, while the front wall is moving *away* from the point where the forward-going light was emitted. So light reaches the back wall first. The two flashes, simultaneous in the car's frame, are **not** simultaneous in the ground frame.

This is not a measurement error or a signal-delay artifact to be corrected for — it is a genuine disagreement about which events are simultaneous, forced on us by the requirement that both observers measure the same speed $c$ for the same light pulses. **Simultaneity is relative to the observer's frame of motion**, not an absolute, frame-independent relation between events. This single fact is the seed from which time dilation and length contraction both grow.

The basic geometry is shown in {numref}`Figure %s <fig:ch02-simultaneity>`. The two flashes are simultaneous in the train frame, but the moving observer travels toward the front flash and away from the rear flash.

```{figure} ../images/ch02-relativity-of-simultaneity.svg
:label: fig:ch02-simultaneity
:alt: A moving train with flashes at its ends and a ground observer at the midpoint, illustrating different judgments of simultaneity.

Simultaneity depends on the observer's frame. The diagram is schematic: the ground observer is at the midpoint, while the train observer moves toward the front flash. Original schematic by the author.
```

### An Operational Procedure for Synchronizing Clocks

The train example shows *that* simultaneity depends on the observer's frame, but it is worth being explicit about *how* an observer within a single frame decides that two clocks, at different locations, are synchronized in the first place — otherwise "simultaneous in the car's frame" is just as vague a phrase as "simultaneous" was before Einstein.

Here is one way to do it, entirely within a single inertial frame $S$. An observer, Amy, sits at a fixed location with a clock. At some time $t_1$ (her own clock reading), she sends a light pulse toward a distant mirror a known distance away. The pulse reflects and returns to her at time $t_3$. Because light travels at the same speed $c$ in both directions (postulate 2), the pulse must have reached the mirror at the midpoint time,

$$
t_2 = \frac{t_1 + t_3}{2}.
$$

Amy can use this fact to synchronize a second clock, placed at the mirror's location: she instructs whoever is stationed there to set their clock to read $t_2$ at the moment the light pulse arrives. Any two clocks synchronized this way — by "radar," bouncing a light signal and splitting the round-trip time evenly — will agree with each other and with any other pair of clocks in the same frame synchronized by the same method. (An equivalent, more homely method: synchronize two clocks side by side, then separate them by moving them apart *very slowly*; since relativistic effects on a moving clock's rate are of order $v^2/c^2$, they can be made as small as desired by transporting the clocks slowly enough.)

This procedure defines, unambiguously, a notion of "simultaneous" *within* a single inertial frame — but it is frame-dependent by construction, because it relies on the frame in which the observer doing the synchronizing is at rest. An observer in a second frame $S'$, moving relative to $S$, will synchronize clocks by the identical procedure applied within $S'$, and — as the train example already showed — the two resulting sets of "simultaneous" clocks will not agree with each other. Both sets of clocks are perfectly well synchronized, each within its own frame; there is simply no frame-independent fact about which distant events are simultaneous with a given event here and now.

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

The two clocks of that argument run side by side in {numref}`Figure %s <fig:ch02-light-clock-sim>`: one at rest in the laboratory, one gliding past at a speed you set, with the moving pulse's zigzag path drawn in. Nothing in the simulation makes the moving clock tick slowly by fiat. Both pulses travel at $c$; the moving one simply has a longer path to cover between reflections, and the two tick counts drift apart by exactly the factor $\gamma$ computed above.

```{openphysics} SpecialRelativity
:screen: 1
:label: fig:ch02-light-clock-sim

A light clock at rest beside an identical one moving at $\beta = v/c$, with the diagonal light path and both tick counts displayed. The other screens of this simulation return in the sections that follow — length contraction, the twin paradox, and the relativistic Doppler effect are each one screen along.
```

Time dilation is not a hypothesis awaiting confirmation; it is routinely observed. Muons created by cosmic rays in the upper atmosphere have a mean lifetime, at rest, of about $2.2\ \mu\text{s}$ — long enough, at nearly the speed of light, to travel only a few hundred meters before decaying, far short of the several kilometers to Earth's surface. Yet large numbers of these muons are detected at sea level. In Earth's frame, the muons' internal "clock" — the process governing decay — runs slow by the factor $\gamma$, extending their mean range by that same factor, which is exactly what is observed. (This effect was confirmed with precision in a classic 1941 experiment by Bruno Rossi and David Hall, comparing muon flux measured at the top of Mount Washington in New Hampshire to the flux at a lower elevation.)

### The Twin Paradox

Time dilation invites an apparent paradox that is worth confronting directly. Suppose Alice stays on Earth while her twin Bob boards a spaceship, accelerates to a large fraction of $c$, travels to a distant star, turns around, and returns to Earth. From Alice's perspective, Bob's clock runs slow throughout the trip (by the factor $\gamma$), so Bob should be younger than Alice when he returns. But motion is relative — can't Bob equally well claim that *he* was at rest the whole time, and that it was Alice, receding and then approaching, whose clock ran slow? If so, each twin should conclude the other has aged less, which is a genuine contradiction: when they are reunited at the same place, they can directly compare clocks, and only one answer can be correct.

The resolution is that the situation is **not** symmetric between the twins, and the asymmetry is exactly the thing time dilation was derived for: proper time is measured by a clock that is present at both endpoint events, without changing inertial frames in between. Alice never leaves a single inertial frame. Bob does not: he must decelerate, reverse course, and re-accelerate at the turnaround point (and again to land back on Earth), and no inertial frame is present at all three key moments of his trip — departure, turnaround, and return — the way Alice's single frame is present at both departure and return. Time dilation, as derived above, compares proper time in one frame to elapsed time in *a single other* inertial frame; it does not directly apply to a clock that switches frames partway through. When the trip is analyzed correctly — by computing the proper time elapsed along each twin's actual worldline in a single, fixed inertial frame (say, Earth's) — Bob's path necessarily accumulates less proper time than Alice's straight, inertial path between the same two events, essentially because his path involves a nonzero, non-inertial detour that always makes his elapsed proper time work out to be shorter, not the same. Bob really is younger when he returns, and both twins, correctly accounting for Bob's acceleration, agree on this.

The physical content of the paradox's resolution is this: there is no contradiction, because *only Bob* can locally detect (with an accelerometer, for instance) that he underwent a change of inertial frame. That detectable asymmetry is exactly what breaks the naive symmetry argument and picks out which twin's elapsed time is shorter.

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

This is **length contraction**: an object of proper length $L_0$, measured by an observer relative to whom it moves at speed $v$ along its own length, is found to have length $L = L_0/\gamma \le L_0$. Only lengths *along* the direction of relative motion contract; lengths perpendicular to the motion are unaffected (a consequence one can show is required for consistency between the two observers' descriptions of, e.g., a rod passing through a ring). Note the resemblance to the Fitzgerald–Lorentz contraction of [Chapter 1](#ch-need-for-relativity) — the same formula, but now derived as a necessary consequence of the postulates rather than invented to hide a null result.

### Application: Bell's Spaceship Paradox

Length contraction raises a subtle question about rigid bodies that is worth working through carefully, since getting it wrong is a common source of confusion. Consider two identical spaceships, initially at rest a fixed distance $L_0$ apart in some frame $S$, connected by a taut string of exactly that length. At $t=0$ (in $S$), both ships fire identical engines, executing identical acceleration profiles, so that at every later instant in $S$ each ship has exactly the same velocity as the other. Does the string, stretched between them, break?

The naive answer is "no": since both ships always move identically, the distance between them, measured in $S$, never changes from $L_0$. But this overlooks what happens to the string. The string is a physical object with its own proper length, and *in the frame in which it is momentarily at rest*, that proper length must be shrinking, not staying fixed — because the string's own rest frame changes as it accelerates, and simultaneously requiring the ships to keep the *same* $S$-frame separation $L_0$ is a different condition from requiring their separation to stay constant *as measured by the string itself*. Since the ships' separation, measured in $S$, stays exactly $L_0$ while the ships (and any observer moving with them) are increasingly length-contracted relative to $S$, the string's own rest-frame length must actually *increase* to keep up — equivalently, the distance between the ships, measured in the ships' own instantaneous rest frame, grows beyond $L_0$ as their common speed increases. A string of fixed material length cannot stretch to match this demand, and it snaps.

The paradox dissolves once it is clear that "the two ships have identical velocity at every instant of $S$-time" is a statement *specific to frame $S$*; it does not mean the ships are relatively at rest, nor does it mean the string, whose integrity depends on physics internal to its own rest frame, experiences no strain. This scenario (due to John Bell, 1976, who reported that it caused genuine disagreement even among professional physicists at CERN) is a useful check on intuition: length contraction is a real, physical effect with real, physical (and sometimes destructive) consequences for extended objects undergoing acceleration, not merely a bookkeeping artifact of coordinate choices.

## The Lorentz Transformation

Time dilation and length contraction are special cases of a general coordinate transformation between inertial frames, replacing the Galilean transformation of [Chapter 1](#ch-need-for-relativity). For frame $S'$ moving at velocity $v$ along the common $x$-$x'$ axis relative to frame $S$, with origins coinciding at $t = t' = 0$, the **Lorentz transformation** is

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

which every inertial observer computes to be the same number, even though $\Delta t$ and $\Delta x$ individually differ between frames. This invariance can be verified directly by substituting the Lorentz transformation. The interval plays the same role for spacetime that ordinary Euclidean distance, $d^2 = \Delta x^2 + \Delta y^2$, plays for a plane: it is unchanged by a change of coordinates (there, a rotation of axes; here, a Lorentz "boost" to a new inertial frame), even though the individual coordinate differences are not.

### Worked Example: Applying the Lorentz Transformation

Two events occur in frame $S$: event 1 at $(x_1, t_1) = (0, 0)$, and event 2 at $(x_2, t_2) = (600\ \text{m}, 1.00\ \mu\text{s})$. Frame $S'$ moves at $v = 0.60c$ relative to $S$. Find the coordinates of both events in $S'$, and verify that the interval is the same in both frames.

First, $\gamma = 1/\sqrt{1-0.36} = 1/\sqrt{0.64} = 1.25$. Event 1 is at the shared origin, so $(x_1', t_1') = (0,0)$ trivially. For event 2,

$$
x_2' = \gamma(x_2 - vt_2) = 1.25\left[600\ \text{m} - (0.60)(3.00\times10^8\ \text{m/s})(1.00\times10^{-6}\ \text{s})\right] = 1.25(600\ \text{m} - 180\ \text{m}) = 525\ \text{m},
$$

$$
t_2' = \gamma\left(t_2 - \frac{vx_2}{c^2}\right) = 1.25\left[1.00\times10^{-6}\ \text{s} - \frac{(0.60)(600\ \text{m})}{3.00\times10^8\ \text{m/s}}\right] = 1.25(1.00\times10^{-6}\ \text{s} - 1.20\times10^{-6}\ \text{s}) = -0.25\ \mu\text{s}.
$$

In $S$, the interval is $(\Delta s)^2 = c^2(\Delta t)^2 - (\Delta x)^2 = (300\ \text{m})^2 - (600\ \text{m})^2 = -270{,}000\ \text{m}^2$ (using $c\,\Delta t = 300\ \text{m}$). In $S'$, $c\,\Delta t' = (3.00\times10^8\ \text{m/s})(-0.25\times10^{-6}\ \text{s}) = -75\ \text{m}$, so $(\Delta s')^2 = (-75\ \text{m})^2 - (525\ \text{m})^2 = 5625\ \text{m}^2 - 275{,}625\ \text{m}^2 = -270{,}000\ \text{m}^2$ — the same value, confirming invariance. Note also that $t_2' < 0$: event 2 occurs *before* event 1 in $S'$, even though event 2 occurs after event 1 in $S$. This is only possible because, as the next section shows, the interval between these two events is spacelike.

## Light Cones and Causality

Einstein's 1905 paper introduced the two postulates that resolved the experimental tension; a later portrait of Einstein is included in {numref}`Figure %s <fig:ch02-einstein-historical>`.

```{figure} ../images/historical-einstein-1921.jpg
:label: fig:ch02-einstein-historical
:alt: Historical portrait photograph of Albert Einstein in 1921.

Albert Einstein in 1921. Photograph by Underwood & Underwood; public domain via Wikimedia Commons.
```

The Lorentz transformation permits the *order* of two events to reverse between frames, as the worked example above just demonstrated — but only for certain pairs of events, and understanding which pairs is essential to understanding why relativity does not undermine cause and effect.

Classify any two events by the sign of the interval between them, $(\Delta s)^2 = c^2(\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2$:

- **Timelike** separation, $(\Delta s)^2 > 0$: more time separates the events than would be needed for a signal traveling at or below $c$ to get from one to the other. Equivalently, $|\Delta x|/|\Delta t| < c$. A material particle, which travels slower than $c$, can pass through both events, so one event can causally influence the other.
- **Spacelike** separation, $(\Delta s)^2 < 0$: the events are separated by more space than light could cross in the available time, $|\Delta x|/|\Delta t| > c$. No signal, of any kind consistent with the postulates, can connect them; neither event can be the cause of the other.
- **Lightlike** (or null) separation, $(\Delta s)^2 = 0$: the events lie exactly on each other's light cone, connectible only by a signal moving at precisely $c$.

Because $(\Delta s)^2$ is Lorentz-invariant, every inertial observer agrees on which of these three categories a given pair of events falls into, even though they may disagree on $\Delta t$ and $\Delta x$ individually. This is the resolution of the apparent puzzle in the worked example above: event 2 was found to occur *before* event 1 in $S'$ despite occurring after it in $S$, but a direct calculation shows the interval between them, $-270{,}000\ \text{m}^2$, is negative — the events are spacelike separated ($|\Delta x| = 600\ \text{m}$ is covered by light in only $2.0\times10^{-6}\ \text{s}$, less than the $\Delta t$ needed... actually here $\Delta x/c = 2.0\ \mu\text{s} > \Delta t = 1.0\ \mu\text{s}$, confirming spacelike separation). Because no signal could have traveled from event 1 to event 2 in the first place, no observer's disagreement about their time-ordering creates any physical contradiction: neither event could possibly have caused the other, in any frame.

The full set of events timelike-separated from a given event $x$ and in its future is called $x$'s **future light cone**; the analogous set in the past is its **past light cone**. Events in $x$'s future light cone are exactly the events $x$ could causally influence; events in its past light cone are exactly the events that could have influenced $x$. All observers agree on the light cone structure of any event, because it is built entirely from the invariant interval.

This structure is what protects causality in relativity. **If two events are timelike separated, every inertial observer agrees on their order** (the earlier one always is measured to occur first, in every frame) — only the *time interval* between them, not their order, is frame-dependent. Order can only reverse between frames, as in the worked example, for spacelike-separated events — and by construction, no causal signal can link spacelike-separated events anyway, since that would require traveling faster than $c$. If it were somehow possible to send a signal faster than $c$ — a hypothetical "subspace radio" — that signal would connect two spacelike-separated events, and by the argument above there would exist a frame in which the signal is received *before* it is sent, an unambiguous violation of cause and effect. This is the deep reason the speed limit $c$ is not merely an engineering inconvenience but is woven into the logical structure of the theory: **no particle, signal, or influence of any kind can propagate faster than $c$ without permitting effects to precede their causes** in some valid inertial frame.

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

### Worked Example: Explaining the Fizeau Coefficient

[Chapter 1](#ch-need-for-relativity) described Fizeau's 1851 measurement of light's speed in flowing water, which showed a puzzling *partial* drag coefficient $f = 1-1/n^2$ rather than full or zero entrainment. This is now straightforward to explain, with no separate assumption about the ether at all. Let $S$ be the lab frame and $S'$ the frame of the flowing water, moving at speed $v \ll c$ relative to the lab. In the water's own rest frame, light travels at the ordinary speed for that medium, $u_x' = c/n$. By the velocity-addition formula, the speed measured in the lab is

$$
u_x = \frac{c/n + v}{1 + \dfrac{(c/n)v}{c^2}} = \frac{c/n + v}{1 + v/(nc)}.
$$

Since $v \ll c$, expand the denominator using $(1+x)^{-1} \approx 1 - x$ for small $x = v/(nc)$:

$$
u_x \approx \left(\frac{c}{n} + v\right)\left(1 - \frac{v}{nc}\right) \approx \frac{c}{n} + v - \frac{v}{n^2} + O(v^2/c) = \frac{c}{n} + v\left(1 - \frac{1}{n^2}\right),
$$

dropping the term of order $v^2/c$, which is negligible for the modest flow speeds ($\sim$few m/s) used in the experiment. This is exactly Fizeau's measured result, with the drag coefficient $f = 1-1/n^2$ emerging directly from relativistic velocity addition applied to ordinary light propagation in a moving medium — no partial ether entrainment need be assumed at all.

## The Relativistic Doppler Effect

The classical Doppler effect — the pitch of an ambulance siren rising as it approaches and falling as it recedes — arises from the finite travel time of successive wave crests to a stationary observer. Light shows an analogous effect, but with a relativistic correction on top of it, because the *source's clock itself* runs slow according to the observer, an effect with no classical counterpart at all.

It is worth being precise about what the classical effect does and does not depend on, because the difference is the whole point. {numref}`Figure %s <fig:ch02-classical-doppler-sim>` is the acoustic case, with the source and the observer independently movable. Move the source toward a stationary listener at speed $u$ and the received frequency is $f_0/(1 - u/v_s)$; leave the source alone and move the *listener* toward it at the same $u$ and the answer is $f_0(1 + u/v_s)$ instead. The two disagree at second order in $u/v_s$, and they must: the air is a medium, the medium picks out a frame, and "which one is really moving" is a question sound can answer. Light has no such medium, so the formula derived below can depend on the relative velocity and on nothing else — and that constraint alone is nearly enough to fix it.

```{openphysics} DopplerEffect
:label: fig:ch02-classical-doppler-sim

The *classical* Doppler effect, for sound in air. Drag the source and the observer independently and compare the shift produced by moving one against the shift produced by moving the other; the asymmetry between the two cases is the signature of a medium, and it is what disappears in the relativistic formula.
```

Consider a source emitting light of proper frequency $f_0$ (the frequency measured by an observer at rest relative to the source), receding directly away from an observer at speed $v$. Two effects combine:

1. **Time dilation** of the source's own clock, as measured by the observer: successive wave crests are emitted at intervals of $\gamma \Delta t_0$ in the observer's frame, rather than $\Delta t_0 = 1/f_0$, purely because the moving source's clock runs slow.
2. **Light travel time**, which increases from one crest to the next because the source is receding, stretching the effective interval further by an additional factor.

Carrying out this calculation ([Problem 14](#ex-special-relativity-14) outlines the steps) gives the **relativistic Doppler formula** for a source receding directly away from the observer:

$$
f_{\text{obs}} = f_0\sqrt{\frac{1 - v/c}{1 + v/c}}, \qquad \text{(receding)}
$$

with the source's speed $v$ measured relative to the observer; a source approaching directly gives the same formula with $v \to -v$, i.e.,

$$
f_{\text{obs}} = f_0\sqrt{\frac{1 + v/c}{1 - v/c}}, \qquad \text{(approaching)}.
$$

For $v \ll c$, expanding to first order in $v/c$ recovers $f_{\text{obs}} \approx f_0(1 \mp v/c)$, the same leading-order shift familiar from the classical (sound) Doppler effect. The distinctively relativistic feature appears at *second* order and in a special geometric case: even a source moving **perpendicular** to the line of sight at the instant of emission — for which there is no classical Doppler shift at all, since the source is neither approaching nor receding — shows a purely relativistic **transverse Doppler shift**,

$$
f_{\text{obs}} = \frac{f_0}{\gamma},
$$

a direct consequence of time dilation alone, with no light-travel-time contribution. This effect was confirmed with high precision by Ives and Stilwell (1938), who measured the frequency of light emitted by fast-moving hydrogen atoms viewed from the side, finding exactly the $1/\gamma$ shift predicted by time dilation and none of the shift a purely classical (source-frame) Doppler picture would have predicted.

The relativistic Doppler effect is not a laboratory curiosity: the cosmological redshift of light from distant galaxies, $1+z \equiv f_0/f_{\text{obs}}$, is precisely this formula (generalized to an expanding spacetime), and the same physics, applied to radio signals rather than light, is a correction that must be built into GPS satellite transmissions alongside the time-dilation correction already discussed.

### Worked Example: Redshift from a Receding Galaxy

A distant galaxy's hydrogen emission line, with rest-frame (proper) wavelength $\lambda_0 = 656.3\ \text{nm}$, is observed at $\lambda_{\text{obs}} = 682.0\ \text{nm}$. Find the galaxy's recession speed.

Since $f = c/\lambda$, the frequency ratio is $f_{\text{obs}}/f_0 = \lambda_0/\lambda_{\text{obs}} = (656.3\ \text{nm})/(682.0\ \text{nm}) = 0.9623$. Setting this equal to $\sqrt{(1-v/c)/(1+v/c)}$ and squaring gives $0.9260 = (1-v/c)/(1+v/c)$. Solving for $v/c$:

$$
0.9260(1+v/c) = 1 - v/c \implies v/c(1 + 0.9260) = 1 - 0.9260 \implies v/c = \frac{0.0740}{1.9260} = 0.0384,
$$

so $v \approx 0.038c \approx 1.15\times 10^7\ \text{m/s}$, receding.

## Spacetime Diagrams

A useful way to visualize these effects is a **spacetime diagram**: a plot with $x$ on the horizontal axis and $ct$ (rather than $t$, so both axes share units of length) on the vertical axis, drawn in a chosen frame $S$. A particle at rest at some fixed $x$ traces a vertical line (its **worldline**); a light ray traces a line at $45°$, since $x = ct$. An observer moving at speed $v$ in frame $S$ has a worldline tilted from vertical by an angle $\theta$ with $\tan\theta = v/c$.

In frame $S'$, that same moving observer's own $x'$ and $ct'$ axes are *not* perpendicular in the diagram as drawn in $S$: the $ct'$ axis coincides with the observer's own worldline, while the $x'$ axis — the locus of events simultaneous with the origin in $S'$ — tilts up from the $x$-axis by the same angle $\theta$ that the $ct'$ axis tilts from the $ct$-axis. This tilted-axis picture is a direct graphical statement of the relativity of simultaneity: the set of events an $S'$-observer calls "now" is not the same as the set an $S$-observer calls "now." Reading distances off a spacetime diagram requires care (the Lorentz-transformed axes are not orthogonal in the Euclidean sense), but the picture makes clear that simultaneity, not merely elapsed time, is the coordinate that differs between frames.

The light cone of the previous section appears naturally on such a diagram: the two $45°$ lines through any event $x$ divide the diagram into the future (above both lines), the past (below both lines), and two "elsewhere" regions (spacelike-separated from $x$), to either side. As a frame's axes tilt with increasing relative speed $v$, they close in like a pair of scissors toward — but, for any $v<c$, never quite reaching — the $45°$ light-cone lines themselves. This is the geometrical statement that no continuous process of acceleration can bring a massive object's worldline from a slope less steep than $45°$ to one that equals or exceeds it: velocities do not simply add in relativity, and the speed $c$ is a genuine asymptote, never attained.

The causal regions and their light-speed boundaries are shown in {numref}`Figure %s <fig:ch02-light-cone>`.

```{figure} ../images/ch02-light-cone.svg
:label: fig:ch02-light-cone
:alt: Spacetime diagram with ct vertical, x horizontal, and light rays forming a cone that separates future, past, and elsewhere regions.

The light cone divides events into the causal future, causal past, and spacelike-separated “elsewhere.” Its $45°$ boundaries are the worldlines of light in units where the horizontal coordinate is $x$ and the vertical coordinate is $ct$. Original schematic by the author.
```

The simulation in {numref}`Figure %s <fig:ch02-sr-sim>` draws these diagrams live. Sliding the
relative speed tilts the $x'$ and $ct'$ axes toward the light cone exactly as
described above, and dragging an event shows how its coordinates — and, on the
other screens, the reading of a moving light clock and the ageing of the
travelling twin — change between frames.

```{openphysics} SpecialRelativity
:label: fig:ch02-sr-sim

Special relativity in five screens: a moving light clock, an interactive
Minkowski diagram, the ladder-and-barn paradox, the twin paradox, and the
relativistic Doppler effect. Set the relative speed and watch the tilted axes
close on the $45°$ light-cone lines without ever reaching them.
```

## Application: Magnetism as a Relativistic Effect

It may seem that special relativity, having explained a handful of subtle high-precision optical experiments, is otherwise disconnected from everyday electromagnetism. In fact one of the most familiar phenomena in electromagnetism — magnetism itself — can be understood as a direct consequence of length contraction applied to electric charge.

Consider a lone charged particle sitting next to a long, electrically neutral wire that carries a current: equal densities of positive and negative charge, moving in opposite directions along the wire, so that the wire's *net* charge density is zero. In the frame in which the wire's charges (of both signs) move at equal and opposite speeds, the two charge densities are, by symmetry, equally length-contracted, so the linear charge density of positive charge exactly cancels that of negative charge at every point — the wire really does look uncharged, and the lone external particle feels no *electric* force from it. Textbook electromagnetism instead attributes any force on the lone particle (if it happens to be moving parallel to the current) to the *magnetic* field generated by the current.

Now view the same situation from a frame in which the lone particle is at rest (equivalently, an observer moving alongside it). In this frame, by relativistic velocity addition, the two species of charge carriers in the wire no longer move at equal speeds relative to the observer — one is sped up and the other slowed down, since velocities do not add in relativity the way lengths and velocities might naively suggest. Because length contraction depends on speed, the two charge densities, both boosted by different amounts, are no longer equal: the wire acquires a small net linear charge density in this frame, of just the right sign and magnitude to produce, via an ordinary electric field, exactly the same force on the (now stationary) lone particle that the magnetic field produced in the original frame.

Both descriptions — "magnetic force in the wire's rest frame" and "electric force from a net charge density in the particle's rest frame" — refer to the same underlying physical event (the particle accelerating, or not, toward the wire), and both observers must agree on that concrete outcome. Requiring this agreement is what forces the electric and magnetic fields to mix into one another under a change of frame, in a way that is fully consistent with, and in fact required by, the Lorentz transformation. Magnetism is not a separate, additional force bolted onto electricity; it is what electric forces look like when viewed from a frame in which the source charges are in motion. This unification is one of the clearest illustrations that relativity is not a remote, exotic correction confined to particle accelerators and GPS satellites, but a structural feature of the electromagnetic force that operates, imperceptibly, in every electric motor and every compass needle.

## Summary

- Because both postulates must hold simultaneously, two events simultaneous in one inertial frame are, in general, not simultaneous in another: **simultaneity is relative**. Simultaneity within a single frame can be defined operationally by radar synchronization: bounce a light signal off a distant clock and assign it the round-trip midpoint time.
- A clock moving at speed $v$ relative to an observer runs slow by the Lorentz factor $\gamma = 1/\sqrt{1-v^2/c^2}$: $\Delta t = \gamma\, \Delta t_0$, where $\Delta t_0$ is the **proper time**, measured in the clock's own rest frame. This is **time dilation**, confirmed directly by observations such as cosmic-ray muon decay (Rossi–Hall, 1941).
- The **twin paradox** is resolved by recognizing that the traveling twin's worldline is not inertial throughout the trip (it includes acceleration at turnaround), breaking the naive symmetry between the twins; the twin who departs from and returns to a single inertial frame ages more.
- An object of proper length $L_0$ (measured in its own rest frame) has length $L = L_0/\gamma$ as measured by an observer relative to whom it moves along its length. This is **length contraction**; only lengths along the direction of motion are affected.
- **Bell's spaceship paradox** shows that length contraction has real physical consequences: two spaceships accelerating identically, as measured in a common frame $S$, maintain constant separation in $S$, but a string connecting them experiences increasing strain and eventually breaks, because the string's own proper length would have to grow to keep pace with the ships' increasing length-contraction relative to $S$.
- The **Lorentz transformation**, $x' = \gamma(x-vt)$, $t' = \gamma(t - vx/c^2)$, replaces the Galilean transformation and reduces to it for $v \ll c$. The spacetime interval $(\Delta s)^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is the same in every inertial frame.
- Pairs of events are classified as **timelike** ($(\Delta s)^2>0$), **spacelike** ($(\Delta s)^2<0$), or **lightlike** ($(\Delta s)^2=0$) separated; all observers agree on this classification and on the time-order of timelike-separated events, which is what prevents faster-than-light signaling from creating causal paradoxes.
- Velocities combine via $u_x = (u_x' + v)/(1 + u_x'v/c^2)$, which reduces to Galilean addition at low speed, never produces a result at or above $c$ when combining sub-light speeds, and reproduces the Fizeau drag coefficient $f = 1-1/n^2$ as its low-speed limit for light in a moving medium.
- The **relativistic Doppler effect**, $f_{\text{obs}} = f_0\sqrt{(1\mp v/c)/(1\pm v/c)}$ for direct recession/approach, combines the classical light-travel-time shift with time dilation of the source's clock; even purely transverse motion produces a shift, $f_{\text{obs}} = f_0/\gamma$, confirmed by the Ives–Stilwell experiment.
- Spacetime diagrams represent these effects graphically: a moving observer's axes of space and time are both tilted, by an equal angle, relative to a "stationary" observer's axes, and the light cone through any event marks the boundary of what that event can causally affect or be affected by.
- **Magnetism can be understood as a relativistic effect**: length contraction, applied unequally to the two oppositely-moving charge species in a current-carrying wire as seen from different frames, converts what looks like a purely magnetic force in one frame into a purely electric force (from a net charge density) in another.

## Problems

:::{exercise}
:label: ex-special-relativity-1

A spaceship passes Earth at $v = 0.80c$. A clock on the ship ticks off exactly $1.00\ \text{s}$ of proper time between two events at the same location on the ship. (a) What time interval between these two events is measured by an observer on Earth? (b) What is $\gamma$ for this speed?
:::

:::{solution} ex-special-relativity-1
:label: sol-special-relativity-1
:class: dropdown

The Lorentz factor is

$$
\gamma=\frac{1}{\sqrt{1-v^2/c^2}}
=\frac{1}{\sqrt{1-(0.80)^2}}
=\frac{1}{\sqrt{0.36}}
=1.67.
$$

Because the $1.00\ \text{s}$ interval is proper time, Earth measures

$$
\Delta t=\gamma\Delta t_0=(1.67)(1.00\ \text{s})=1.67\ \text{s}.
$$

Therefore, $\gamma=1.67$, and the Earth observer measures a time interval of $1.67\ \text{s}$.
:::

:::{exercise}
:label: ex-special-relativity-2

A meter stick at rest in frame $S'$ makes an angle such that it lies entirely along the direction of relative motion. If $S'$ moves at $v = 0.60c$ relative to $S$, what length is the stick measured to have in $S$?
:::

:::{solution} ex-special-relativity-2
:label: sol-special-relativity-2
:class: dropdown

The meter stick's proper length is $L_0=1.00\ \text{m}$.  Its Lorentz factor is

$$
\gamma=\frac{1}{\sqrt{1-(0.60)^2}}
=\frac{1}{0.800}=1.25.
$$

Since it is parallel to the motion,

$$
L=\frac{L_0}{\gamma}
=\frac{1.00\ \text{m}}{1.25}
=0.800\ \text{m}.
$$

Therefore, frame $S$ measures the moving meter stick to be $0.800\ \text{m}$ long.
:::

:::{exercise}
:label: ex-special-relativity-3

Two events occur at the same time $t=0$ in frame $S$, at positions $x_1 = 0$ and $x_2 = 300\ \text{m}$. Frame $S'$ moves at $v = 0.50c$ relative to $S$ along the $x$-axis, with origins coinciding at $t=t'=0$. Use the Lorentz transformation to find $t_1'$ and $t_2'$, and confirm that the two events are not simultaneous in $S'$.
:::

:::{solution} ex-special-relativity-3
:label: sol-special-relativity-3
:class: dropdown

For $v=0.50c$,

$$
\gamma=\frac{1}{\sqrt{1-(0.50)^2}}=1.1547.
$$

The time transformation is $t'=\gamma(t-vx/c^2)$.  For event 1,

$$
t_1'=1.1547\left[0-\frac{(0.50c)(0\ \text{m})}{c^2}\right]=0\ \text{s}.
$$

For event 2,

$$
\begin{aligned}
t_2'&=1.1547\left[0-\frac{(0.50)(3.00\times10^8\ \text{m/s})(300\ \text{m})}
 {(3.00\times10^8\ \text{m/s})^2}\right]\\
&=-5.77\times10^{-7}\ \text{s}.
\end{aligned}
$$

Therefore, $t_1'=0\ \text{s}$ and $t_2'=-5.77\times10^{-7}\ \text{s}$, so the event at $x=300\ \text{m}$ occurs earlier in $S'$ and the events are not simultaneous there.
:::

:::{exercise}
:label: ex-special-relativity-4

A cosmic-ray muon is created at an altitude of $15\ \text{km}$, moving straight down at $v = 0.998c$. Its proper mean lifetime is $2.2\ \mu\text{s}$. (a) Using time dilation, find the mean lifetime as measured in Earth's frame, and the mean distance the muon travels before decaying in that frame. (b) Working instead in the muon's rest frame, use length contraction to find the depth of the $15\ \text{km}$ atmospheric layer as the muon measures it, and show your two calculations of whether the muon is likely to reach the ground agree.
:::

:::{solution} ex-special-relativity-4
:label: sol-special-relativity-4
:class: dropdown

First calculate the Lorentz factor:

$$
\gamma=\frac{1}{\sqrt{1-(0.998)^2}}=15.8.
$$

In Earth's frame, the mean lifetime is

$$
\tau=\gamma\tau_0=(15.8)(2.2\ \mu\text{s})=34.8\ \mu\text{s}.
$$

The corresponding mean travel distance is

$$
\begin{aligned}
d&=v\tau=(0.998)(3.00\times10^8\ \text{m/s})(34.8\times10^{-6}\ \text{s})\\
&=1.04\times10^4\ \text{m}=10.4\ \text{km}.
\end{aligned}
$$

In the muon's rest frame, the atmosphere is length-contracted:

$$
L'=\frac{L_0}{\gamma}=\frac{15.0\ \text{km}}{15.8}=0.948\ \text{km}.
$$

The ground approaches at $0.998c$, so the muon-frame time to the ground is

$$
t'=\frac{0.948\times10^3\ \text{m}}{(0.998)(3.00\times10^8\ \text{m/s})}
=3.17\ \mu\text{s}.
$$

Therefore, the Earth-frame mean range is $10.4\ \text{km}$, less than $15\ \text{km}$, and equivalently the ground takes $3.17\ \mu\text{s}$ to arrive in the muon frame, longer than the $2.2\ \mu\text{s}$ mean proper lifetime; reaching the ground is not typical but is quite possible for a surviving fraction of muons.

```{figure} ../images/ch02-sol-muon-frames.svg
:label: fig:ch02-sol-muon-frames
:alt: Side-by-side diagrams of a muon crossing the atmosphere in the Earth frame and the muon frame.

Time dilation in the Earth frame and length contraction in the muon frame describe the same physical crossing, with matching survival conclusion.
```
:::

:::{exercise}
:label: ex-special-relativity-5

Two spaceships approach each other, each moving at speed $0.75c$ relative to Earth, in opposite directions. (a) What speed does an observer on one ship measure for the other ship, using relativistic velocity addition? (b) Explain why simply adding $0.75c + 0.75c$ would give an unphysical answer, and identify which postulate this would violate.
:::

:::{solution} ex-special-relativity-5
:label: sol-special-relativity-5
:class: dropdown

Take one ship to have $v=+0.75c$ and the other $u=-0.75c$ in the Earth frame.  The speed magnitude measured from the first ship is

$$
|u'|=\left|\frac{u-v}{1-uv/c^2}\right|
=\left|\frac{-0.75c-0.75c}{1-(-0.75)(0.75)}\right|
=\frac{1.50c}{1.5625}
=0.960c.
$$

Therefore, either ship measures the other to approach at $0.960c$; ordinary addition would give $1.50c$, an unphysical speed that would violate Einstein's second postulate that every inertial observer measures light at $c$ and no sublight velocity combination exceeds it.
:::

:::{exercise}
:label: ex-special-relativity-6

Sketch a spacetime diagram (axes $x$ and $ct$) in the rest frame $S$ of a laboratory. Draw the worldline of a particle at rest at $x = 2\ \text{m}$, the worldline of a particle moving at $v = 0.5c$ starting from the origin, and the worldline of a light pulse emitted from the origin at $t=0$. Identify the angle each worldline makes with the vertical axis.
:::

:::{solution} ex-special-relativity-6
:label: sol-special-relativity-6
:class: dropdown

On axes with $ct$ vertical and $x$ horizontal, the object at rest has $x=2\ \text{m}$ for every $t$, so its worldline is vertical and makes an angle $0^\circ$ with the vertical axis.  The moving particle obeys

$$
x=vt=(0.5c)t=0.5(ct),
$$

so its angle $\theta$ from vertical obeys $\tan\theta=\Delta x/\Delta(ct)=0.5$, giving $\theta=26.6^\circ$.  The light pulse obeys $x=ct$, so $\tan\theta=1$ and $\theta=45.0^\circ$.  Therefore, the requested sketch contains a vertical line at $x=2\ \text{m}$, a $26.6^\circ$-from-vertical line from the origin for the massive particle, and a $45.0^\circ$-from-vertical light ray from the origin.

```{figure} ../images/ch02-sol-worldline-angles.svg
:label: fig:ch02-sol-worldline-angles
:alt: Spacetime diagram with a stationary worldline, a particle moving at half the speed of light, and a light ray.

On equal $x$ and $ct$ scales, a worldline's angle from the vertical directly encodes $v/c$.
```
:::

:::{exercise}
:label: ex-special-relativity-7

Twin Bob leaves Earth at $v = 0.80c$, travels to a star $8.0$ light-years away (in Earth's frame), immediately turns around, and returns at the same speed. (a) How much time elapses on Earth, according to Alice? (b) How much proper time elapses for Bob over the whole round trip? (c) Explain, referring specifically to Bob's turnaround, why it is Bob and not Alice who ages less, even though each twin sees the other's clock running slow during the constant-velocity legs of the trip.
:::

:::{solution} ex-special-relativity-7
:label: sol-special-relativity-7
:class: dropdown

In Alice's frame, each leg lasts

$$
t_{\rm leg}=\frac{8.0\ \text{light-years}}{0.80c}=10.0\ \text{years},
$$

so Alice's elapsed time is $20.0\ \text{years}$.  At $0.80c$, $\gamma=1.67$, and Bob's proper time is

$$
\tau_B=\frac{20.0\ \text{years}}{1.67}=12.0\ \text{years}.
$$

Therefore, Alice ages $20.0\ \text{years}$ while Bob ages $12.0\ \text{years}; Bob, unlike Alice, changes inertial frames at turnaround, so the apparent symmetry between their constant-velocity observations does not apply to the full trip.

```{figure} ../images/ch02-sol-twin-worldlines.svg
:label: fig:ch02-sol-twin-worldlines
:alt: Earth-frame spacetime diagram of Alice remaining on Earth and Bob travelling to a star and returning.

Bob's kinked worldline identifies the turnaround—the event that makes the two twins' complete histories physically different.
```
:::

:::{exercise}
:label: ex-special-relativity-8

Two events are separated by $\Delta x = 5.0\times10^{8}\ \text{m}$ and $\Delta t = 1.0\ \text{s}$ in frame $S$. (a) Determine whether the interval between them is timelike, spacelike, or lightlike. (b) If it is spacelike, explain why no observer's disagreement about which event happened first can create a causality paradox. (c) Find the speed $v$ (as a fraction of $c$) of a frame $S'$ in which the two events are simultaneous, if such a frame exists.
:::

:::{solution} ex-special-relativity-8
:label: sol-special-relativity-8
:class: dropdown

The interval is

$$
\begin{aligned}
(\Delta s)^2&=c^2\Delta t^2-\Delta x^2\\
&=(3.00\times10^8\ \text{m/s})^2(1.0\ \text{s})^2-(5.0\times10^8\ \text{m})^2\\
&=-1.6\times10^{17}\ \text{m}^2.
\end{aligned}
$$

It is negative, so the separation is spacelike.  Simultaneity in $S'$ requires

$$
0=\Delta t'=\gamma\left(\Delta t-\frac{v\Delta x}{c^2}\right),
\qquad
v=\frac{c^2\Delta t}{\Delta x}
=\frac{(3.00\times10^8\ \text{m/s})^2(1.0\ \text{s})}{5.0\times10^8\ \text{m}}
=0.600c.
$$

Therefore, the events are spacelike separated and a frame moving at $0.600c$ makes them simultaneous; their order can reverse without a causality paradox because no light-speed-or-slower signal can connect them.
:::

:::{exercise}
:label: ex-special-relativity-9

Light travels through a block of glass with refractive index $n = 1.50$ moving at $v = 20\ \text{m/s}$ relative to the lab, in the same direction as the light. Using the relativistic velocity-addition formula (not the approximation), find the light's speed in the lab frame, and compare the result to the Fizeau-formula approximation $c/n + v(1-1/n^2)$.
:::

:::{solution} ex-special-relativity-9
:label: sol-special-relativity-9
:class: dropdown

In the glass rest frame the light speed is $u'=c/n=2.00\times10^8\ \text{m/s}$.  Exact velocity addition gives

$$
u=\frac{u'+v}{1+u'v/c^2}
=\frac{2.00\times10^8\ \text{m/s}+20\ \text{m/s}}
 {1+(2.00\times10^8\ \text{m/s})(20\ \text{m/s})/(3.00\times10^8\ \text{m/s})^2}
=2.00000011111\times10^8\ \text{m/s}.
$$

The Fizeau approximation gives

$$
\frac{c}{n}+v\left(1-\frac{1}{n^2}\right)
=2.00\times10^8\ \text{m/s}+(20\ \text{m/s})\left(1-\frac{1}{2.25}\right)
=2.00000011111\times10^8\ \text{m/s}.
$$

Therefore, both methods give $u\approx2.00000011111\times10^8\ \text{m/s}$ (an increase of $11.1\ \text{m/s}$); their difference is below $10^{-6}\ \text{m/s}$ at this speed because the omitted terms are of order $(v/c)^2$.
:::

:::{exercise}
:label: ex-special-relativity-10

A wire carries equal and opposite densities of positive and negative charge moving at $\pm 0.90c$ relative to the lab frame (an exaggerated, but illustrative, speed), with the wire electrically neutral in the lab frame. (a) Qualitatively explain, using length contraction, why an observer moving alongside one species of charge carrier would measure a net charge density on the wire. (b) Explain why this observer must nonetheless agree with the lab-frame observer about whether a nearby test charge, initially at rest in the observer's frame, accelerates toward or away from the wire.
:::

:::{solution} ex-special-relativity-10
:label: sol-special-relativity-10
:class: dropdown

In the lab the positive and negative linear charge densities cancel, so the wire is neutral.  An observer moving alongside one species sees that species at rest but sees the other species moving at a different relativistic relative speed.  Because moving charge separations along the wire are length-contracted by different factors, the two charge densities no longer have equal magnitudes in that frame, and the observer therefore measures a net charge density and an electric field.  Therefore, the test charge has an electric force in that observer's frame, while the lab observer describes the same physical acceleration using the transformed electric and magnetic fields; the two descriptions must agree because they are related by the Lorentz transformation.
:::

:::{exercise}
:label: ex-special-relativity-11

A spacecraft recedes directly from Earth at $v = 0.60c$, transmitting a radio signal at proper frequency $f_0 = 100.0\ \text{MHz}$. (a) What frequency does a receiver on Earth measure? (b) If the same spacecraft instead approached Earth at the same speed, what frequency would be measured? (c) Explain why the approaching and receding frequencies are not simply related by $f_0(1\pm v/c)$, i.e., why they are not symmetric about $f_0$ the way the low-speed (classical) approximation would suggest.
:::

:::{solution} ex-special-relativity-11
:label: sol-special-relativity-11
:class: dropdown

For recession,

$$
f_{\rm rec}=f_0\sqrt{\frac{1-v/c}{1+v/c}}
=(100.0\ \text{MHz})\sqrt{\frac{1-0.60}{1+0.60}}
=50.0\ \text{MHz}.
$$

For approach, the signs interchange:

$$
f_{\rm app}=(100.0\ \text{MHz})\sqrt{\frac{1+0.60}{1-0.60}}
=200.0\ \text{MHz}.
$$

Therefore, Earth receives $50.0\ \text{MHz}$ from the receding spacecraft and $200.0\ \text{MHz}$ from the approaching one; the shifts are not the classical $f_0(1\pm v/c)$ because time dilation changes the emitted crest spacing in addition to the changing light-travel distance.
:::

:::{exercise}
:label: ex-special-relativity-12

A star's light source moves in a circular orbit, at speed $v = 0.30c$, around a companion too dim to see, so that at one point in the orbit its velocity is purely transverse to the line of sight to Earth. (a) Find the fractional frequency shift, $(f_0 - f_{\text{obs}})/f_0$, expected at that instant from the transverse Doppler effect alone. (b) Explain why this shift is always a redshift (lower observed frequency), regardless of the direction of the transverse motion, unlike the ordinary (longitudinal) Doppler shift, which can be a redshift or blueshift depending on direction.
:::

:::{solution} ex-special-relativity-12
:label: sol-special-relativity-12
:class: dropdown

For transverse motion, $f_{\rm obs}=f_0/\gamma$.  Here

$$
\gamma=\frac{1}{\sqrt{1-(0.30)^2}}=1.0483,
\qquad
\frac{f_{\rm obs}}{f_0}=\frac{1}{1.0483}=0.9539.
$$

Thus

$$
\frac{f_0-f_{\rm obs}}{f_0}=1-0.9539=0.0461=4.61\%.
$$

Therefore, the transverse Doppler shift is a $4.61\%$ redshift, because time dilation always makes the moving source's clock run slow; reversing a purely transverse velocity does not change $v^2$ or $\gamma$, whereas reversing longitudinal motion changes whether successive crests are emitted closer to or farther from the observer.
:::

:::{exercise}
:label: ex-special-relativity-13

In Bell's spaceship paradox, both ships execute identical acceleration profiles as measured in frame $S$, so that their $S$-frame separation stays fixed at $L_0$. Explain why an observer riding along with either ship would nonetheless measure the *other* ship to be receding, at least for part of the trip, and connect this to the reason the connecting string comes under increasing tension. (You do not need to compute the tension quantitatively — a clear qualitative argument, referencing length contraction of the string versus the fixed $S$-frame separation of the ships, is sufficient.)
:::

:::{solution} ex-special-relativity-13
:label: sol-special-relativity-13
:class: dropdown

Although the ships keep the same separation $L_0$ in frame $S$, the instantaneous rest frame of either accelerating ship changes continuously.  In each such momentary rest frame, the other ship is not generally at rest at the same separation: relativity of simultaneity assigns the two ships' simultaneous positions differently, and the other ship is seen to recede during part of the acceleration.  A string that would be unstressed in a common instantaneous rest frame requires a larger proper length as the ships gain speed, while its endpoints are constrained to remain only $L_0$ apart in $S$.  Therefore, the string is stretched beyond its natural proper length and develops increasing tension, eventually breaking if it is not strong enough.
:::

:::{exercise}
:label: ex-special-relativity-14

Outline the derivation of the relativistic Doppler formula for direct recession, by combining (a) the time-dilation factor $\gamma$ for the interval between successive wave crests as emitted, and (b) the classical light-travel-time stretching factor $(1+v/c)$ that arises because the source recedes an additional distance $v\Delta t$ between emitting successive crests. Show that multiplying these two factors and using $\Delta t_{\text{obs}} = \gamma(1+v/c)\Delta t_0$ reproduces $f_{\text{obs}} = f_0\sqrt{(1-v/c)/(1+v/c)}$.
:::

:::{solution} ex-special-relativity-14
:label: sol-special-relativity-14
:class: dropdown

Let $\Delta t_0=1/f_0$ be the proper interval between emitted crests.  Time dilation makes the Earth-frame emission interval $\Delta t=\gamma\Delta t_0$.  During that interval a receding source moves an additional distance $v\Delta t$, adding a propagation delay $v\Delta t/c$, so

$$
\Delta t_{\rm obs}=\Delta t+\frac{v\Delta t}{c}
=\gamma\Delta t_0\left(1+\frac{v}{c}\right).
$$

Using $\gamma=1/\sqrt{(1-v/c)(1+v/c)}$ gives

$$
\frac{\Delta t_{\rm obs}}{\Delta t_0}
=\frac{1+v/c}{\sqrt{(1-v/c)(1+v/c)}}
=\sqrt{\frac{1+v/c}{1-v/c}}.
$$

Since frequency is the reciprocal of period,

$$
f_{\rm obs}=\frac{1}{\Delta t_{\rm obs}}
=f_0\sqrt{\frac{1-v/c}{1+v/c}}.
$$

Therefore, combining time dilation with the extra light-travel time produces the relativistic Doppler formula for direct recession.
:::
