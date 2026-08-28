"""Figures embedded in Chapter 1 worked solutions (not the main chapter body)."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from figstyle import BLUE, GREEN, GRAY, ORANGE, PURPLE, RED, save, use_style

DARK = "#333333"


def river_arm_analogy():
    """River paths that make the two classical Michelson--Morley arm times unequal (Problem 2)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))

    # Perpendicular arm: swimmer must aim upstream to keep a shore-fixed vertical path.
    ax = axes[0]
    ax.add_patch(Rectangle((-1.7, -0.15), 3.4, 2.3, facecolor="#dcecf5", edgecolor=BLUE, lw=1.0))
    for y in [0.25, 0.8, 1.35, 1.9]:
        ax.annotate("", xy=(1.45, y), xytext=(-1.45, y),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1, alpha=0.65))
    ax.plot([-1.7, 1.7], [0, 0], color=DARK, lw=2.2)
    ax.plot([-1.7, 1.7], [2, 2], color=DARK, lw=2.2)
    ax.text(-1.65, 2.12, "far bank", fontsize=9, color=GRAY)
    ax.text(-1.65, -0.34, "near bank", fontsize=9, color=GRAY)
    ax.plot([0, 0], [0, 2], color=GREEN, lw=2.2, ls="--")
    ax.annotate("", xy=(-0.55, 1.12), xytext=(0, 0.15),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
    ax.text(-0.95, 0.52, r"swimming velocity $u$", fontsize=9, color=ORANGE, rotation=58)
    ax.annotate("", xy=(0.72, 1.12), xytext=(0, 1.12),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.0))
    ax.text(0.35, 1.26, r"current $v$", fontsize=9, color=BLUE)
    ax.annotate("", xy=(0, 1.82), xytext=(0, 0.20),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.0))
    ax.text(0.08, 1.55, r"shore-frame $u_y$", fontsize=9, color=GREEN)
    ax.annotate("", xy=(1.45, 0.08), xytext=(1.45, 1.92),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(1.52, 1.0, r"$L$", va="center", color=GRAY)
    ax.text(0, -0.72, r"$u_y=\sqrt{u^2-v^2}$" "\n" r"$t_\perp=2L/\sqrt{u^2-v^2}$",
            ha="center", fontsize=10, color=DARK)
    ax.set_title("Cross-river arm", fontsize=11)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-0.9, 2.35)
    ax.set_aspect("equal")
    ax.axis("off")

    # Parallel arm: the same swimmer is slower upstream and faster downstream.
    ax = axes[1]
    ax.add_patch(Rectangle((-1.7, -0.15), 3.4, 2.3, facecolor="#dcecf5", edgecolor=BLUE, lw=1.0))
    for y in [0.25, 0.8, 1.35, 1.9]:
        ax.annotate("", xy=(1.45, y), xytext=(-1.45, y),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1, alpha=0.65))
    ax.plot([-1.35, 1.35], [1.0, 1.0], color=GRAY, lw=1.1, ls=":")
    ax.plot([-1.25, 1.25], [1.0, 1.0], "o", ms=5.5, color=DARK)
    ax.annotate("", xy=(-1.08, 1.15), xytext=(1.05, 1.15),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.annotate("", xy=(1.08, 0.85), xytext=(-1.05, 0.85),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2))
    ax.text(0, 1.29, r"upstream: $u-v$", ha="center", fontsize=10, color=RED)
    ax.text(0, 0.56, r"downstream: $u+v$", ha="center", fontsize=10, color=GREEN)
    ax.text(0, 1.82, r"water current $v$ $\rightarrow$", ha="center", fontsize=10, color=BLUE)
    ax.annotate("", xy=(-1.25, 1.72), xytext=(1.25, 1.72),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
    ax.text(0, 1.87, r"$L$", ha="center", color=GRAY)
    ax.text(0, -0.72, r"$t_\parallel=L/(u-v)+L/(u+v)$" "\n" r"$t_\parallel>t_\perp$ for $v>0$",
            ha="center", fontsize=10, color=DARK)
    ax.set_title("Upstream--downstream arm", fontsize=11)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-0.9, 2.35)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.suptitle("The river analogy: the classical ether wind changes the two round-trip times differently", y=1.01,
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch01-sol-river-arms")


def ether_shift_scale():
    """Scale comparison for the predicted and bounded Michelson--Morley shifts (Problems 6--7)."""
    labels = ["1887 apparatus\n(predicted)", "4 km apparatus\n(stationary ether)", "modern upper bound"]
    shifts = [0.37, 75.0, 4.0e-6]
    colors = [ORANGE, RED, PURPLE]

    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ys = [2, 1, 0]
    ax.barh(ys, shifts, color=colors, edgecolor=DARK, height=0.53, zorder=3)
    for y, shift, label in zip(ys, shifts, ["0.37 fringe", "75 fringes", r"$4\times10^{-6}$ fringe"]):
        ax.text(shift * 1.45, y, label, va="center", fontsize=10, color=DARK)
    ax.set_xscale("log")
    ax.set_xlim(1e-7, 1e3)
    ax.set_yticks(ys)
    ax.set_yticklabels(labels)
    ax.set_xlabel("fringe shift (logarithmic scale)")
    ax.set_title("Ether-wind signal: a large classical prediction versus a stringent null bound")
    ax.grid(axis="x", color="#d7dfe5", lw=0.8, zorder=0)
    ax.text(0.02, -0.28, r"At fixed apparatus settings, $\Delta N\propto v^2$; the bound corresponds to $v<95\ \mathrm{m/s}$.",
            transform=ax.transAxes, fontsize=9.5, color=GRAY)
    save(fig, "ch01-sol-ether-shift-scale")


if __name__ == "__main__":
    use_style()
    print("Chapter 1 solution figures:")
    river_arm_analogy()
    ether_shift_scale()
