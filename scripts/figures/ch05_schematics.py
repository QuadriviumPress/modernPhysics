"""Schematic diagrams for Chapter 5, Diffraction of Light."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def single_slit_pairing():
    """Cancel the slit against itself: halves for m = 1, quarters for m = 2."""
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.6))

    a = 3.0
    theta = np.radians(24)
    u = np.array([np.cos(theta), np.sin(theta)])

    for ax, (nstrip, order) in zip(axes, [(2, 1), (4, 2)]):
        ax.add_patch(Rectangle((-0.16, a / 2), 0.32, 1.4, color="#5a5a5a", zorder=3))
        ax.add_patch(Rectangle((-0.16, -a / 2 - 1.4), 0.32, 1.4, color="#5a5a5a", zorder=3))

        for e in np.linspace(a / 2, -a / 2, nstrip + 1)[1:-1]:
            ax.plot([-0.42, 0.42], [e, e], color=GRAY, lw=1.0, ls="--", zorder=4)

        for y in np.linspace(a / 2 - 0.15, -a / 2 + 0.15, 9):
            ax.annotate("", xy=np.array([0, y]) + 2.3 * u, xytext=(0, y),
                        arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=0.8, alpha=0.45))

        gap = a / nstrip
        A = np.array([0.0, a / 2 - 0.10])          # a point in the top strip
        B = np.array([0.0, A[1] - gap])            # its partner, a/nstrip below
        for P, c in [(A, RED), (B, GREEN)]:
            ax.plot(*P, marker="o", ms=8, color=c, zorder=6)
            ax.annotate("", xy=tuple(P + 3.4 * u), xytext=tuple(P),
                        arrowprops=dict(arrowstyle="-|>", color=c, lw=2.1))

        # The lower ray must travel an extra (a/nstrip) sin(theta) to reach the
        # wavefront through A, drawn here as the thin perpendicular.
        foot = B + np.dot(A - B, u) * u
        ax.plot([A[0], foot[0]], [A[1], foot[1]], color=DARK, lw=1.1, zorder=5)
        ax.plot([B[0], foot[0]], [B[1], foot[1]], color=ORANGE, lw=4.2,
                solid_capstyle="butt", zorder=5)
        ax.annotate(rf"extra path $\dfrac{{a}}{{{nstrip}}}\sin\theta$",
                    xy=tuple((B + foot) / 2), xytext=(2.5, B[1] - 1.15),
                    fontsize=10.5, color=ORANGE, ha="center",
                    arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.9))

        ax.annotate("", xy=(-0.62, A[1]), xytext=(-0.62, B[1]),
                    arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.3))
        ax.text(-0.75, (A[1] + B[1]) / 2, rf"$a/{nstrip}$",
                ha="right", va="center", fontsize=11.5, color=PURPLE)

        ax.annotate("", xy=(-1.85, a / 2), xytext=(-1.85, -a / 2),
                    arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
        ax.text(-1.98, 0, "$a$", ha="right", va="center", fontsize=13, color=RED)

        ax.plot([B[0], B[0] + 2.6], [B[1], B[1]], color=GRAY, lw=0.9, ls="--")
        ax.add_patch(Arc(B, 2.6, 2.6, theta1=0, theta2=np.degrees(theta),
                         edgecolor=DARK, lw=1.1))
        ax.text(B[0] + 1.45, B[1] + 0.16, r"$\theta$", fontsize=13, color=DARK)

        ax.set_title(
            rf"split into {nstrip}:  $\dfrac{{a}}{{{nstrip}}}\sin\theta = \dfrac{{\lambda}}{{2}}$"
            rf"   $\Longrightarrow$   $a\sin\theta = {order}\lambda$", fontsize=11)
        ax.set_xlim(-2.8, 4.6)
        ax.set_ylim(-3.6, 3.1)
        ax.set_aspect("equal")
        ax.set_anchor("N")
        ax.axis("off")

    fig.tight_layout()
    save(fig, "ch05-single-slit-pairing")


def phasor_arc():
    """The slit's phasors curl up: straight, then an arc, then a closed circle."""
    fig, axes = plt.subplots(1, 3, figsize=(8.8, 3.4))
    n = 30

    cases = [(0.0, r"$\beta = 0$  ($\theta = 0$)",
              "every wavelet in step;\nresultant = full arc length"),
             (np.pi, r"$\beta = \pi$  ($a\sin\theta = \lambda/2$)",
              "the chain curls;\nchord is shorter than the arc"),
             (2 * np.pi, r"$\beta = 2\pi$  ($a\sin\theta = \lambda$)",
              "the chain closes;\nchord $= 0$: the first minimum")]

    for ax, (total, title, note) in zip(axes, cases):
        step = total / n
        off = np.array([0.0, 0.10]) if total == 0 else np.zeros(2)
        pts = [off.copy()]
        for k in range(n):
            ang = (k + 0.5) * step
            pts.append(pts[-1] + np.array([np.cos(ang), np.sin(ang)]) / n)
        pts = np.array(pts)
        ax.plot(pts[:, 0], pts[:, 1], color=BLUE, lw=2.4, solid_capstyle="round")
        for k in range(0, n, 3):
            ax.annotate("", xy=pts[k + 1], xytext=pts[k],
                        arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.1))
        tail, head = pts[0], pts[-1]
        if total == 0:
            tail, head = tail - 2 * off, head - 2 * off
        ax.annotate("", xy=tuple(head), xytext=tuple(tail),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4))
        ax.plot(*pts[0], marker="o", ms=5, color=DARK, zorder=5)
        ax.set_title(title, fontsize=10.5)

        cx, cy = pts[:, 0].mean(), pts[:, 1].mean()
        ax.set_xlim(cx - 0.80, cx + 0.80)
        ax.set_ylim(cy - 0.86, cy + 0.52)
        ax.text(cx, cy - 0.52, note, ha="center", va="top", fontsize=9, color=GRAY)
        ax.set_aspect("equal")
        ax.set_anchor("N")
        ax.axis("off")

    axes[0].text(0.5, -0.24, "resultant", color=RED, fontsize=9.5, ha="center", va="top")
    axes[1].text(-0.05, 0.30, "chord", color=RED, fontsize=9.5, ha="right", va="center")
    axes[1].text(0.38, 0.30, "arc", color=BLUE, fontsize=9.5, ha="left", va="center")
    fig.suptitle("Adding the wavelets from every point across the slit",
                 fontsize=11.5, fontweight="bold", y=1.04)
    fig.tight_layout()
    save(fig, "ch05-phasor-arc")


def bragg():
    """X-rays reflecting from successive atomic planes pick up 2 d sin(theta)."""
    fig, ax = plt.subplots(figsize=(7.8, 4.8))

    d = 1.5
    theta = np.radians(30)
    u_in = np.array([np.cos(theta), -np.sin(theta)])
    u_out = np.array([np.cos(theta), np.sin(theta)])

    for k, y in enumerate([0.0, -d, -2 * d]):
        ax.plot([-4.4, 4.4], [y, y], color=GRAY, lw=0.8, ls="--", zorder=1)
        for x in np.arange(-4.2, 4.3, 0.75):
            ax.add_patch(Circle((x, y), 0.16, facecolor="#b9cedb",
                                edgecolor="#6f93a8", lw=0.7, zorder=2))
        ax.text(4.6, y, f"plane {k + 1}", fontsize=9.5, color=DARK, va="center")

    A = np.array([0.0, 0.0])
    B = np.array([0.0, -d])
    L = 3.4
    for P, color, tag in [(A, BLUE, "ray 1"), (B, RED, "ray 2")]:
        ax.annotate("", xy=tuple(P), xytext=tuple(P - L * u_in),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2))
        ax.annotate("", xy=tuple(P + L * u_out), xytext=tuple(P),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2))
        ax.plot(*P, marker="o", ms=7, color=color, zorder=6)
        ax.text(*(P + (L + 0.15) * u_out), tag, color=color, fontsize=10,
                va="center", ha="left")

    # The wavefronts through A, and the two extra legs of ray 2, each d sin(theta).
    C = B - d * np.sin(theta) * u_in
    D = B + d * np.sin(theta) * u_out
    for P0, P1 in [(C, B), (B, D)]:
        ax.plot([P0[0], P1[0]], [P0[1], P1[1]], color=ORANGE, lw=4.5,
                solid_capstyle="butt", zorder=5)
    for Q in (C, D):
        ax.plot([A[0], Q[0]], [A[1], Q[1]], color=GREEN, lw=1.2, zorder=4)
    ax.text(1.18, -0.42, "wavefronts\nthrough $A$", color=GREEN,
            fontsize=9, ha="left", va="center")
    ax.text(-0.16, 0.26, "$A$", color=BLUE, fontsize=12, ha="right")
    ax.text(-0.16, -d - 0.12, "$B$", color=RED, fontsize=12, ha="right", va="top")

    ax.annotate("", xy=(-3.6, 0), xytext=(-3.6, -d),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.3))
    ax.text(-3.75, -d / 2, "$d$", ha="right", va="center", fontsize=13, color=PURPLE)

    ax.add_patch(Arc(A, 3.0, 3.0, theta1=180, theta2=180 + np.degrees(theta),
                     edgecolor=DARK, lw=1.1))
    ax.text(-1.72, -0.44, r"$\theta$", fontsize=13, color=DARK)
    ax.text(-3.5, 2.05, r"incoming X-rays, wavelength $\lambda$",
            fontsize=10, color=DARK)

    ax.annotate(r"each leg is $d\sin\theta$", xy=tuple((B + D) / 2),
                xytext=(2.4, -2.05), fontsize=10.5, color=ORANGE, ha="center",
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.9))

    ax.text(0.0, -3.85,
            r"extra path traveled by ray 2:  $2d\sin\theta$"
            "\n"
            r"constructive interference:  $n\lambda = 2d\sin\theta$",
            ha="center", va="top", fontsize=11.5, color=DARK)

    ax.set_xlim(-5.4, 6.2)
    ax.set_ylim(-4.9, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    save(fig, "ch05-bragg-law")


if __name__ == "__main__":
    use_style()
    print("Chapter 5 schematics:")
    single_slit_pairing()
    phasor_arc()
    bragg()
