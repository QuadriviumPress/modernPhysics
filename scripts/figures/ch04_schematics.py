"""Schematic diagrams for Chapter 4, Interference of Light."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrow, Polygon, Rectangle, Wedge

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def _barrier(ax, x, y0, y1, width=0.09, color="#5a5a5a"):
    ax.add_patch(Rectangle((x - width / 2, y0), width, y1 - y0, color=color, zorder=3))


def huygens():
    """Wavelets rebuild a plane wavefront, and bend when the aperture narrows."""
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 3.2))

    # (a) plane wave rebuilding itself
    ax = axes[0]
    r = 0.9
    for y in np.linspace(-1.5, 1.5, 9):
        ax.add_patch(Arc((0, y), 2 * r, 2 * r, theta1=-88, theta2=88,
                         edgecolor=BLUE, lw=0.9, alpha=0.75))
        ax.plot([0], [y], marker="o", ms=2.6, color=RED, zorder=4)
    ax.plot([0, 0], [-1.75, 1.75], color=DARK, lw=2.0)
    ax.plot([r, r], [-1.75, 1.75], color=DARK, lw=2.0, ls=(0, (5, 3)))
    ax.annotate("", xy=(r + 0.55, 0), xytext=(r + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.4))
    ax.text(-0.12, 1.9, "wavefront\nnow", ha="right", fontsize=8.5, color=DARK)
    ax.text(r + 0.12, 1.9, "envelope\nlater", ha="left", fontsize=8.5, color=DARK)
    ax.text(0.45, -2.45, "each point is a\nsource of wavelets", ha="center",
            va="top", fontsize=8.5, color=RED)
    ax.set_title("(a)  free propagation", fontsize=10)
    ax.set_xlim(-0.5, 2.1)

    # (b) wide aperture: only the edges bend
    ax = axes[1]
    gap = 1.3
    _barrier(ax, 0, gap / 2, 2.4)
    _barrier(ax, 0, -2.4, -gap / 2)
    for x in (-0.75, -0.45, -0.15):
        ax.plot([x, x], [-2.2, 2.2], color=BLUE, lw=1.1, alpha=0.6)
    for y in np.linspace(-gap / 2 + 0.08, gap / 2 - 0.08, 6):
        ax.add_patch(Arc((0, y), 1.6, 1.6, theta1=-85, theta2=85,
                         edgecolor=BLUE, lw=0.8, alpha=0.6))
    ax.plot([0.8, 0.8], [-gap / 2 + 0.1, gap / 2 - 0.1], color=DARK, lw=2.0)
    ax.add_patch(Arc((0, gap / 2), 1.6, 1.6, theta1=0, theta2=80, edgecolor=DARK, lw=2.0))
    ax.add_patch(Arc((0, -gap / 2), 1.6, 1.6, theta1=-80, theta2=0, edgecolor=DARK, lw=2.0))
    ax.annotate("", xy=(0, gap / 2), xytext=(0, -gap / 2),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2))
    ax.text(-0.14, 0, r"$a \gg \lambda$", ha="right", va="center", fontsize=9.5, color=RED)
    ax.text(0.6, -2.45, "beam stays sharp;\nonly the edges bend", ha="center",
            va="top", fontsize=8.5, color=DARK)
    ax.set_title("(b)  wide aperture", fontsize=10)
    ax.set_xlim(-1.0, 2.1)

    # (c) narrow aperture: one wavelet, spreading everywhere
    ax = axes[2]
    gap = 0.22
    _barrier(ax, 0, gap / 2, 2.4)
    _barrier(ax, 0, -2.4, -gap / 2)
    for x in (-0.75, -0.45, -0.15):
        ax.plot([x, x], [-2.2, 2.2], color=BLUE, lw=1.1, alpha=0.6)
    for rad in (0.5, 0.9, 1.3, 1.7):
        ax.add_patch(Arc((0, 0), 2 * rad, 2 * rad, theta1=-88, theta2=88,
                         edgecolor=BLUE, lw=1.3))
    ax.plot([0], [0], marker="o", ms=4, color=RED, zorder=4)
    ax.text(0.14, 0.22, r"$a \lesssim \lambda$", fontsize=9.5, color=RED)
    ax.text(0.6, -2.45, "light floods the whole\nregion beyond the slit",
            ha="center", va="top", fontsize=8.5, color=DARK)
    ax.set_title("(c)  narrow aperture", fontsize=10)
    ax.set_xlim(-1.0, 2.1)

    for ax in axes:
        ax.set_ylim(-3.25, 2.45)
        ax.set_aspect("equal")
        ax.set_anchor("N")
        ax.axis("off")
    fig.tight_layout()
    save(fig, "ch04-huygens-principle")


def double_slit_geometry():
    """The setup, and the blow-up that produces the path difference d sin(theta)."""
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.9),
                             gridspec_kw={"width_ratios": [1.35, 1]})

    # --- (a) whole apparatus -------------------------------------------------
    ax = axes[0]
    d = 1.2
    ax.plot([-2.6, -1.5], [0, 0], color=BLUE, lw=1.4)
    ax.plot([-2.6], [0], marker="*", ms=13, color=ORANGE, zorder=5)
    ax.text(-2.6, -0.45, "source", ha="center", fontsize=9, color=DARK)
    _barrier(ax, -1.5, -0.09, 0.09, width=0.10)
    ax.text(-1.5, 1.15, "single slit\n(makes one\ncoherent wavefront)",
            ha="center", fontsize=8, color=GRAY)
    for rad in (0.35, 0.65, 0.95, 1.25):
        ax.add_patch(Arc((-1.5, 0), 2 * rad, 2 * rad, theta1=-70, theta2=70,
                         edgecolor=BLUE, lw=0.8, alpha=0.5))

    _barrier(ax, 0, -1.75, -d / 2 - 0.17)
    _barrier(ax, 0, -d / 2 + 0.17, d / 2 - 0.17)
    _barrier(ax, 0, d / 2 + 0.17, 1.75)
    for sgn in (1, -1):
        ax.plot([0], [sgn * d / 2], marker="o", ms=5, color=RED, zorder=5)
    ax.annotate("", xy=(0, d / 2), xytext=(0, -d / 2),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2))
    ax.text(-0.20, 0, "$d$", ha="right", va="center", fontsize=11, color=RED)
    ax.text(0.16, d / 2 + 0.06, "$S_1$", fontsize=10, color=RED)
    ax.text(0.16, -d / 2 - 0.3, "$S_2$", fontsize=10, color=RED)

    yP = 1.05
    L = 3.0
    for sgn in (1, -1):
        ax.plot([0, L], [sgn * d / 2, yP], color=BLUE, lw=1.2)
    ax.plot([0, L], [0, 0], color=GRAY, lw=0.9, ls="--")
    ax.add_patch(Arc((0, 0), 1.9, 1.9, theta1=0,
                     theta2=np.degrees(np.arctan2(yP, L)), edgecolor=DARK, lw=1.0))
    ax.text(1.05, 0.13, r"$\theta$", fontsize=11, color=DARK)

    # screen with fringes
    yy = np.linspace(-1.75, 1.75, 500)
    strip = np.cos(np.pi * 2.6 * yy) ** 2
    ax.imshow(strip[::-1, None], extent=(L, L + 0.30, -1.75, 1.75),
              aspect="auto", cmap="gray", vmin=0, vmax=1, zorder=4)
    ax.plot([L, L], [-1.75, 1.75], color=DARK, lw=1.0)
    ax.plot([L], [yP], marker="o", ms=5, color=DARK, zorder=6)
    ax.text(L + 0.42, yP, "$P$", fontsize=11, color=DARK, va="center")
    ax.text(L + 0.42, -1.5, "screen", fontsize=9, color=DARK, va="center")
    ax.annotate("", xy=(L, -2.05), xytext=(0, -2.05),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(L / 2, -2.35, r"$L \gg d$", ha="center", fontsize=10, color=GRAY)
    ax.annotate("", xy=(L, 0), xytext=(L, yP),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.0))
    ax.text(L - 0.12, yP / 2, "$y$", ha="right", va="center", fontsize=11, color=GREEN)
    ax.set_xlim(-3.1, 4.3)
    ax.set_ylim(-2.65, 1.95)
    ax.set_title("(a)  Young's arrangement", fontsize=10)

    # --- (b) blow-up of the path difference ---------------------------------
    ax = axes[1]
    theta = np.radians(28)
    d = 2.0
    S1 = np.array([0.0, d / 2])
    S2 = np.array([0.0, -d / 2])
    u = np.array([np.cos(theta), np.sin(theta)])       # direction towards distant P
    for S in (S1, S2):
        ax.annotate("", xy=S + 3.2 * u, xytext=S,
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.5))
        ax.plot(*S, marker="o", ms=6, color=RED, zorder=5)
    ax.annotate("", xy=S1, xytext=S2, arrowprops=dict(arrowstyle="<->", color=RED, lw=1.3))
    ax.text(-0.14, 0, "$d$", ha="right", va="center", fontsize=12, color=RED)

    foot = S2 + np.dot(S1 - S2, u) * u                 # perpendicular foot from S1
    ax.plot([S1[0], foot[0]], [S1[1], foot[1]], color=GREEN, lw=1.4)
    ax.plot([S2[0], foot[0]], [S2[1], foot[1]], color=ORANGE, lw=3.2, solid_capstyle="butt")
    mid = (S2 + foot) / 2
    ax.annotate(r"$\Delta r = d\sin\theta$", xy=tuple(mid), xytext=(1.45, -1.75),
                fontsize=11.5, color=ORANGE, ha="center",
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.9))
    # right-angle tick at the foot
    n = np.array([-u[1], u[0]])
    p = foot
    ax.plot(*np.array([p - 0.16 * u, p - 0.16 * u + 0.16 * n, p + 0.16 * n]).T,
            color=GREEN, lw=0.9)

    ax.plot([0, 2.6], [S2[1], S2[1]], color=GRAY, lw=0.9, ls="--")
    ax.add_patch(Arc(S2, 1.5, 1.5, theta1=0, theta2=np.degrees(theta),
                     edgecolor=DARK, lw=1.0))
    ax.text(S2[0] + 0.85, S2[1] + 0.14, r"$\theta$", fontsize=12, color=DARK)
    ax.text(-0.7, 2.45, "for $L \\gg d$ the two rays\nare effectively parallel",
            ha="left", fontsize=9, color=GRAY)
    ax.set_xlim(-1.3, 4.3)
    ax.set_ylim(-2.3, 3.1)
    ax.set_title("(b)  where the path difference comes from", fontsize=10)

    for ax in axes:
        ax.set_aspect("equal")
        ax.set_anchor("N")
        ax.axis("off")
    fig.tight_layout()
    save(fig, "ch04-double-slit-geometry")


def phasors():
    """Two-phasor addition, and what N phasors do at a maximum and at a zero."""
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.3))

    # (a) two equal phasors
    ax = axes[0]
    phi = np.radians(70)
    a = np.array([1.0, 0.0])
    b = np.array([np.cos(phi), np.sin(phi)])
    res = a + b
    ax.annotate("", xy=a, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2))
    ax.annotate("", xy=a + b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2))
    ax.annotate("", xy=res, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4))
    ax.plot([0, b[0]], [0, b[1]], color=BLUE, lw=1.0, ls=":")
    ax.add_patch(Arc(a, 0.8, 0.8, theta1=0, theta2=np.degrees(phi), edgecolor=GRAY, lw=1.0))
    ax.text(a[0] + 0.45, a[1] + 0.16, r"$\phi$", fontsize=12, color=GRAY)
    ax.add_patch(Arc((0, 0), 1.1, 1.1, theta1=0, theta2=np.degrees(phi) / 2,
                     edgecolor=GRAY, lw=1.0))
    ax.text(0.62, 0.14, r"$\phi/2$", fontsize=10, color=GRAY)
    ax.text(0.5, -0.22, r"$E_0$", fontsize=11.5, color=BLUE, ha="center")
    ax.text(a[0] + 0.42, a[1] + 0.42, r"$E_0$", fontsize=11.5, color=BLUE)
    ax.text(res[0] * 0.5 - 0.15, res[1] * 0.5 + 0.55,
            r"$E = 2E_0\cos(\phi/2)$", fontsize=11, color=RED, ha="center")
    ax.set_xlim(-0.7, 2.5)
    ax.set_ylim(-1.4, 2.2)
    ax.set_title("(a)  two slits", fontsize=10)

    # (b), (c) N phasors
    for ax, (n, step, label, note) in zip(
            axes[1:],
            [(6, 0.0, r"$\phi = 0$", "all in step:\n$E = NE_0$, so $I = N^2 I_1$"),
             (6, 2 * np.pi / 6, r"$\phi = 2\pi/N$",
              "the chain closes:\n$E = 0$, the first zero")]):
        pts = [np.array([0.0, 0.0])]
        for k in range(n):
            ang = k * step
            pts.append(pts[-1] + np.array([np.cos(ang), np.sin(ang)]))
        pts = np.array(pts)
        for k in range(n):
            ax.annotate("", xy=pts[k + 1], xytext=pts[k],
                        arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.6))
        if step == 0:
            ax.annotate("", xy=pts[-1] + np.array([0, -0.55]),
                        xytext=pts[0] + np.array([0, -0.55]),
                        arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4))
            ax.text(n / 2, -1.05, note, ha="center", va="top", fontsize=9, color=RED)
            ax.set_xlim(-1.2, n + 1.2)
            ax.set_ylim(-3.0, 1.6)
        else:
            ax.plot(*pts[0], marker="o", ms=7, color=RED, zorder=5)
            ax.text(0.5, -1.05, note, fontsize=9, color=RED, ha="center", va="top")
            ax.set_xlim(-1.6, 2.6)
            ax.set_ylim(-2.2, 2.6)
        ax.set_title(f"(b)  $N = {n}$ slits, {label}" if step == 0
                     else f"(c)  $N = {n}$ slits, {label}", fontsize=10)

    for ax in axes:
        ax.set_aspect("equal")
        ax.set_anchor("N")
        ax.axis("off")
    fig.tight_layout()
    save(fig, "ch04-phasors")


def thin_film():
    """Two reflections, one extra round trip inside the film, one pi phase flip."""
    fig, ax = plt.subplots(figsize=(7.6, 4.2))

    t = 1.0
    ax.add_patch(Rectangle((-3.6, 0), 8.0, t, facecolor="#cfe3f2", edgecolor=BLUE, lw=1.2))
    ax.text(4.3, t / 2, r"film, $n_{\rm film}$", fontsize=11, color=BLUE,
            ha="right", va="center")
    ax.text(-3.5, t + 0.62, r"air, $n_{\rm air} < n_{\rm film}$", fontsize=10, color=GRAY)
    ax.text(-3.5, -0.42, r"air (or glass) below", fontsize=10, color=GRAY)

    hit = np.array([-1.2, t])
    inner_b = np.array([0.0, 0.0])
    exit_p = np.array([1.2, t])

    ax.annotate("", xy=tuple(hit), xytext=(-2.6, t + 1.4),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2))
    ax.text(-2.72, t + 1.5, "incident", fontsize=10, color=ORANGE, ha="center")

    # ray 1: straight back off the front surface
    ax.annotate("", xy=(0.2, t + 1.4), xytext=tuple(hit),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.text(0.30, t + 1.45, "ray 1\n(front surface)", fontsize=9.5, color=RED, ha="left")
    ax.plot(*hit, marker="o", ms=7, color=RED, zorder=5)
    ax.text(-1.42, t + 0.30, r"$\pi$ shift" "\n" r"(air $\to$ denser)",
            fontsize=9, color=RED, ha="right", va="center")

    # ray 2: down through the film, off the back, out again
    for p0, p1 in [(hit, inner_b), (inner_b, exit_p), (exit_p, np.array([2.6, t + 1.4]))]:
        ax.annotate("", xy=tuple(p1), xytext=tuple(p0),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2))
    ax.text(2.72, t + 1.45, "ray 2\n(back surface)", fontsize=9.5, color=GREEN, ha="left")
    ax.plot(*inner_b, marker="o", ms=7, color=GREEN, zorder=5)
    ax.text(0.24, -0.42, "no shift" "\n" r"(film $\to$ rarer)",
            fontsize=9, color=GREEN, ha="left", va="center")

    ax.annotate("", xy=(-3.15, t), xytext=(-3.15, 0),
                arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.2))
    ax.text(-3.25, t / 2, "$t$", fontsize=12, color=DARK, ha="right", va="center")

    ax.text(-1.3, -1.75,
            r"extra optical path of ray 2:  $2 n_{\rm film} t$"
            "\n"
            r"net phase difference:  $\dfrac{2\pi}{\lambda}\,2n_{\rm film}t \; + \; \pi$",
            ha="center", fontsize=11, color=DARK)

    ax.set_xlim(-4.2, 4.6)
    ax.set_ylim(-2.5, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    save(fig, "ch04-thin-film-rays")


def michelson():
    """Beam splitter, two arms, one of them movable; fringes at the detector."""
    fig, ax = plt.subplots(figsize=(7.0, 4.6))

    bs = np.array([0.0, 0.0])
    ax.plot([-0.42, 0.42], [-0.42, 0.42], color=ORANGE, lw=5, solid_capstyle="round", zorder=4)
    ax.text(0.05, -0.62, "beam splitter", fontsize=9.5, color="#8a5a00", ha="left")

    ax.plot([-0.34, 0.34], [0.86, 1.54], color="#9ab", lw=4.0,
            solid_capstyle="round", zorder=1)
    ax.text(0.48, 1.25, "compensator\nplate", fontsize=8.5, color=GRAY, va="center")

    ax.add_patch(Rectangle((-0.12, 2.2), 0.24, 0.5, color="#4a4a4a", zorder=4))
    ax.text(0.0, 2.9, "mirror $M_1$ (movable)", fontsize=10, color=DARK, ha="center")
    ax.annotate("", xy=(0.72, 2.82), xytext=(0.72, 2.10),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
    ax.text(0.95, 2.45, r"move by $\delta$" "\n" r"$\Rightarrow 2\delta/\lambda$ fringes",
            fontsize=9.5, color=RED, va="center")

    ax.add_patch(Rectangle((2.2, -0.25), 0.5, 0.5, color="#4a4a4a", zorder=4))
    ax.text(2.45, -0.85, "mirror $M_2$\n(fixed)", fontsize=10, color=DARK, ha="center")

    ax.plot([-2.6], [0], marker="*", ms=15, color=ORANGE, zorder=5)
    ax.text(-2.6, -0.45, "source", fontsize=10, color=DARK, ha="center")

    for (x0, y0, x1, y1) in [(-2.35, 0, -0.15, 0), (0.15, 0, 2.1, 0), (0, 0.15, 0, 2.1)]:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2))
    for (x0, y0, x1, y1) in [(2.1, -0.16, 0.16, -0.16), (-0.16, 2.1, -0.16, 0.16)]:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4, linestyle="dashed"))
    ax.annotate("", xy=(0, -1.85), xytext=(0, -0.2),
                arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.2))

    # circular fringes at the detector
    for rad, shade in [(0.62, "#f2f2f2"), (0.48, "#5a5a5a"), (0.34, "#f2f2f2"),
                       (0.20, "#5a5a5a"), (0.08, "#f2f2f2")]:
        ax.add_patch(Circle((0, -2.5), rad, facecolor=shade, edgecolor="none", zorder=4))
    ax.add_patch(Circle((0, -2.5), 0.62, facecolor="none", edgecolor=DARK, lw=1.0, zorder=5))
    ax.text(0.85, -2.5, "detector:\nfringes shift as $M_1$ moves",
            fontsize=9.5, color=PURPLE, va="center")

    ax.annotate("", xy=(-0.62, 1.9), xytext=(-0.62, 0.15),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.1))
    ax.text(-0.75, 1.0, "$L_1$", fontsize=11, color=GREEN, ha="right", va="center")
    ax.annotate("", xy=(2.05, 0.52), xytext=(0.18, 0.52),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.1))
    ax.text(1.1, 0.64, "$L_2$", fontsize=11, color=GREEN, ha="center")

    ax.set_xlim(-3.3, 3.5)
    ax.set_ylim(-3.4, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    save(fig, "ch04-michelson")


if __name__ == "__main__":
    use_style()
    print("Chapter 4 schematics:")
    huygens()
    double_slit_geometry()
    phasors()
    thin_film()
    michelson()
