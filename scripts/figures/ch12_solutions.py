"""Figures embedded in Chapter 12 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def _wedge(ax, x0, y0, x1, y1, color=DARK, width0=0.03, width1=0.14):
    """A solid wedge bond, narrow at the central atom, wide at the substituent (coming toward viewer)."""
    dx, dy = x1 - x0, y1 - y0
    length = np.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    pts = [(x0 + nx * width0, y0 + ny * width0), (x0 - nx * width0, y0 - ny * width0),
           (x1 - nx * width1, y1 - ny * width1), (x1 + nx * width1, y1 + ny * width1)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor="none"))


def vsepr_shapes():
    """NH3 (trigonal pyramidal), CO2 (linear), SF6 (octahedral) (Problem 1)."""
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.8))

    ax = axes[0]
    ax.add_patch(Circle((0, 0), 0.12, color=BLUE, zorder=5))
    for ang in [200, 340]:
        x, y = 0.6 * np.cos(np.radians(ang)), 0.6 * np.sin(np.radians(ang))
        ax.plot([0, x], [0, y], color=DARK, lw=2.0)
        ax.add_patch(Circle((x, y), 0.09, color=GRAY, zorder=5))
    _wedge(ax, 0, 0, 0.0, 0.62, color=DARK)
    ax.add_patch(Circle((0.0, 0.62), 0.09, color=GRAY, zorder=5))
    ax.add_patch(Ellipse((0, -0.55), 0.5, 0.28, angle=0, facecolor=ORANGE, alpha=0.35, edgecolor=ORANGE))
    ax.text(0, -0.55, "lone pair", ha="center", va="center", fontsize=8, color="#8a5a00")
    ax.set_title(r"NH$_3$: $sp^3$" "\ntrigonal pyramidal", fontsize=10.5)

    ax = axes[1]
    ax.add_patch(Circle((0, 0), 0.12, color=BLUE, zorder=5))
    for x in [-0.7, 0.7]:
        ax.plot([0, x], [0, 0], color=DARK, lw=2.4)
        ax.add_patch(Circle((x, 0), 0.11, color=RED, zorder=5))
    ax.set_title(r"CO$_2$: $sp$" "\nlinear", fontsize=10.5)

    ax = axes[2]
    ax.add_patch(Circle((0, 0), 0.12, color=BLUE, zorder=5))
    for x, y in [(0.6, 0), (-0.6, 0), (0, 0.6), (0, -0.6)]:
        ax.plot([0, x], [0, y], color=DARK, lw=2.0)
        ax.add_patch(Circle((x, y), 0.09, color=GREEN, zorder=5))
    _wedge(ax, 0, 0, 0.42, 0.42, color=DARK)
    ax.add_patch(Circle((0.42, 0.42), 0.09, color=GREEN, zorder=5))
    ax.plot([0, -0.42], [0, -0.42], color=DARK, lw=1.2, ls=(0, (1, 1)))
    ax.add_patch(Circle((-0.42, -0.42), 0.09, color=GREEN, zorder=5))
    ax.set_title(r"SF$_6$: $sp^3d^2$" "\noctahedral", fontsize=10.5)

    for ax in axes:
        ax.set_xlim(-1.0, 1.0)
        ax.set_ylim(-1.0, 1.0)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("VSEPR geometry follows directly from the number of electron domains", fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch12-sol-vsepr-shapes")


def _mo_level_diagram(ax, levels, title):
    """levels: list of (label, y, n_electrons, is_antibonding)."""
    for label, y, n, anti in levels:
        color = RED if anti else BLUE
        ax.hlines(y, -0.35, 0.35, color=color, lw=2.2)
        ax.text(0.45, y, label, va="center", fontsize=9.5, color=DARK)
        if n >= 1:
            ax.annotate("", xy=(-0.15, y + 0.28), xytext=(-0.15, y + 0.02),
                        arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.3))
        if n >= 2:
            ax.annotate("", xy=(0.15, y + 0.02), xytext=(0.15, y + 0.28),
                        arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.3))
    ax.set_title(title, fontsize=10.5)
    ax.axis("off")


def he2_plus_mo():
    """He2+ molecular orbital diagram: bond order 1/2 (Problem 3)."""
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    _mo_level_diagram(ax, [
        (r"$\sigma_{1s}^{*}$", 1.0, 1, True),
        (r"$\sigma_{1s}$", 0.0, 2, False),
    ], r"He$_2^+$: bond order $\frac{2-1}{2}=\frac{1}{2}$")
    ax.set_xlim(-0.9, 1.6)
    ax.set_ylim(-0.4, 1.5)
    save(fig, "ch12-sol-he2-plus-mo")


def f2_mo_diagram():
    """F2 vs. F2+ molecular orbital filling: bond order 1 vs. 1.5, and the ion's paramagnetism (Problem 8)."""
    base_levels = [
        (r"$\sigma_{2p}^{*}$", 5.0, True),
        (r"$\pi_{2p}^{*}$", 4.0, True),
        (r"$\pi_{2p}$", 2.4, False),
        (r"$\sigma_{2p}$", 1.2, False),
        (r"$\sigma_{2s}^{*}$", 0.4, True),
        (r"$\sigma_{2s}$", -0.4, False),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 6.0))

    fills_f2 = {r"$\sigma_{2s}$": 2, r"$\sigma_{2s}^{*}$": 2, r"$\sigma_{2p}$": 2, r"$\pi_{2p}$": 4, r"$\pi_{2p}^{*}$": 4, r"$\sigma_{2p}^{*}$": 0}
    fills_f2p = dict(fills_f2)
    fills_f2p[r"$\pi_{2p}^{*}$"] = 3

    for ax, fills, title in [(axes[0], fills_f2, r"F$_2$: bond order $1$"),
                              (axes[1], fills_f2p, r"F$_2^+$: bond order $1.5$" "\n(paramagnetic)")]:
        for label, y, anti in base_levels:
            n = fills[label]
            color = RED if anti else BLUE
            width = 0.9 if label.startswith(r"$\pi") else 0.35
            if width == 0.9:
                for cx in (-0.5, 0.5):
                    ax.hlines(y, cx - 0.3, cx + 0.3, color=color, lw=2.0)
                slots = [min(2, n), max(0, n - 2)]
                for cx, ne in zip((-0.5, 0.5), slots):
                    if ne >= 1:
                        ax.annotate("", xy=(cx - 0.08, y + 0.26), xytext=(cx - 0.08, y + 0.02),
                                    arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.1))
                    if ne >= 2:
                        ax.annotate("", xy=(cx + 0.08, y + 0.02), xytext=(cx + 0.08, y + 0.26),
                                    arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.1))
            else:
                ax.hlines(y, -width, width, color=color, lw=2.2)
                if n >= 1:
                    ax.annotate("", xy=(-0.1, y + 0.26), xytext=(-0.1, y + 0.02),
                                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.1))
                if n >= 2:
                    ax.annotate("", xy=(0.1, y + 0.02), xytext=(0.1, y + 0.26),
                                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.1))
            ax.text(1.05, y, label, va="center", fontsize=9, color=DARK)
        ax.set_xlim(-1.1, 1.9)
        ax.set_ylim(-0.9, 5.7)
        ax.axis("off")
        ax.set_title(title, fontsize=10.5)

    fig.suptitle("Removing one antibonding electron strengthens the bond and leaves it paramagnetic", fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch12-sol-f2-mo-diagram")


def sf4_xef4_comparison():
    """One equatorial lone pair (SF4, seesaw) vs. two axial-equatorial lone pairs (XeF4, square planar) (Problem 7)."""
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.2))

    ax = axes[0]
    ax.add_patch(Circle((0, 0), 0.12, color=BLUE, zorder=5))
    for x, y in [(0.7, 0), (-0.35, 0.6), (-0.35, -0.6)]:
        ax.plot([0, x], [0, y], color=DARK, lw=2.0)
        ax.add_patch(Circle((x, y), 0.09, color=GREEN, zorder=5))
    _wedge(ax, 0, 0, -0.55, 0.35, color=DARK, width1=0.10)
    ax.add_patch(Circle((-0.55, 0.35), 0.09, color=GREEN, zorder=5))
    ax.add_patch(Ellipse((0.35, -0.55), 0.5, 0.28, angle=-25, facecolor=ORANGE, alpha=0.4, edgecolor=ORANGE))
    ax.text(0.35, -0.68, "equatorial\nlone pair", ha="center", fontsize=8, color="#8a5a00")
    ax.set_title(r"SF$_4$: one lone pair" "\n$\\to$ seesaw", fontsize=10.5)

    ax = axes[1]
    for x, y in [(0.6, 0.6), (-0.6, 0.6), (0.6, -0.6), (-0.6, -0.6)]:
        ax.plot([0, x], [0, y], color=DARK, lw=2.0, zorder=2)
        ax.add_patch(Circle((x, y), 0.09, color=GREEN, zorder=5))
    ax.add_patch(Ellipse((0, 0), 0.22, 0.62, angle=0, facecolor=ORANGE, alpha=0.45, edgecolor=ORANGE, zorder=3))
    ax.add_patch(Circle((0, 0), 0.12, color=BLUE, zorder=6))
    ax.annotate("front lone pair", xy=(0, 0.30), xytext=(0.85, 0.35), fontsize=8, color="#8a5a00",
                ha="left", arrowprops=dict(arrowstyle="-", color="#8a5a00", lw=0.7))
    ax.annotate("back lone pair", xy=(0, -0.30), xytext=(0.85, -0.35), fontsize=8, color="#8a5a00",
                ha="left", arrowprops=dict(arrowstyle="-", color="#8a5a00", lw=0.7))
    ax.set_title(r"XeF$_4$: two lone pairs" "\n$\\to$ square planar", fontsize=10.5)

    axes[0].set_xlim(-1.1, 1.1)
    axes[1].set_xlim(-1.1, 1.9)
    for ax in axes:
        ax.set_ylim(-1.1, 1.1)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.suptitle("Where the lone pairs go determines whether four bonds look bent or flat", fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch12-sol-sf4-xef4")


if __name__ == "__main__":
    use_style()
    print("Chapter 12 solution figures:")
    vsepr_shapes()
    he2_plus_mo()
    f2_mo_diagram()
    sf4_xef4_comparison()
