"""Generate the computed figures for Chapter 4, Interference of Light."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, fringe_strip, save, use_style


def two_slit_intensity():
    """I(theta) = I0 cos^2(pi d sin(theta)/lambda), with the fringe pattern above it."""
    x = np.linspace(-3.2, 3.2, 4000)          # x = d sin(theta) / lambda
    intensity = np.cos(np.pi * x) ** 2

    fig = plt.figure(figsize=(7.6, 4.2))
    gs = GridSpec(2, 1, height_ratios=[1, 4], hspace=0.10, figure=fig)

    fringe_strip(fig.add_subplot(gs[0]), x, intensity)

    ax = fig.add_subplot(gs[1])
    ax.plot(x, intensity, color=BLUE)
    ax.axhline(0.5, color=GRAY, lw=0.9, ls=":")
    ax.text(3.15, 0.53, r"average, $I_0/2$", color=GRAY, ha="right", fontsize=9)

    for m in range(-3, 4):
        ax.plot([m], [1.0], marker="o", ms=4.5, color=RED, zorder=5)
        ax.annotate(f"$m={m}$", (m, 1.0), textcoords="offset points", xytext=(0, 7),
                    ha="center", fontsize=9, color=RED)

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, 1.22)
    ax.set_xlabel(r"$d\sin\theta/\lambda$   (path difference, in wavelengths)")
    ax.set_ylabel(r"$I/I_0$")
    ax.set_xticks(np.arange(-3, 3.5, 0.5))
    ax.set_xticklabels(["-3", "", "-2", "", "-1", "", "0", "", "1", "", "2", "", "3"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    save(fig, "ch04-two-slit-intensity")


def n_slit_intensity():
    """Principal maxima sharpen as N^-1 and brighten as N^2 as slits are added."""
    x = np.linspace(-2.15, 2.15, 5000)       # x = d sin(theta) / lambda
    phi = 2 * np.pi * x

    fig, axes = plt.subplots(4, 1, figsize=(7.6, 7.2), sharex=True)
    for ax, (n, color) in zip(axes, [(2, BLUE), (3, GREEN), (5, PURPLE), (20, RED)]):
        num = np.sin(n * phi / 2) ** 2
        den = np.sin(phi / 2) ** 2
        intensity = np.where(den < 1e-12, n ** 2, num / np.maximum(den, 1e-12)) / n ** 2
        ax.plot(x, intensity, color=color, lw=1.4)
        ax.set_ylim(0, 1.42)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["0", r"$N^2 I_1$"])
        ax.text(0.012, 0.80, f"$N = {n}$", transform=ax.transAxes, ha="left",
                fontsize=11, fontweight="bold", color=color)
        if n > 2:
            half = 1.0 / n          # full width of a principal maximum is 2 lambda/(N d)
            ax.annotate("", xy=(half, 0.5), xytext=(-half, 0.5),
                        arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.9))
            if n < 10:
                ax.text(0.0, 0.58, r"width $\propto 1/N$", ha="center", fontsize=9, color=GRAY)
            else:
                ax.annotate(r"width $\propto 1/N$", xy=(half, 0.5), xytext=(0.22, 1.16),
                            fontsize=9, color=GRAY,
                            arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))

    axes[-1].set_xlim(x[0], x[-1])
    axes[-1].set_xticks([-2, -1, 0, 1, 2])
    axes[-1].set_xlabel(r"$d\sin\theta/\lambda$")
    axes[0].set_title("Principal maxima stay put; they sharpen and brighten as $N$ grows")
    fig.text(0.005, 0.5, "intensity (each panel scaled to its own peak)",
             rotation="vertical", va="center", fontsize=10)
    save(fig, "ch04-n-slit-intensity")


def coherence():
    """A coherent wave versus a chain of randomly phased wave trains."""
    rng = np.random.default_rng(4)
    t = np.linspace(0, 12, 6000)
    tau_c = 2.0

    fig, axes = plt.subplots(2, 1, figsize=(7.6, 4.0), sharex=True)

    axes[0].plot(t, np.sin(2 * np.pi * 2.2 * t), color=BLUE, lw=1.2)
    axes[0].set_title("Ideal coherent source: one unbroken wave train")

    phase = np.zeros_like(t)
    for k in range(1, int(t[-1] / tau_c) + 2):
        phase[t >= k * tau_c] = rng.uniform(0, 2 * np.pi)
    axes[1].plot(t, np.sin(2 * np.pi * 2.2 * t + phase), color=RED, lw=1.2)
    for k in range(1, int(t[-1] / tau_c) + 1):
        axes[1].axvline(k * tau_c, color=GRAY, lw=0.8, ls="--")
    axes[1].annotate("", xy=(2 * tau_c, -1.5), xytext=(tau_c, -1.5),
                     arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.9))
    axes[1].text(1.5 * tau_c, -2.15, r"coherence time $\tau_c$", ha="center",
                 fontsize=9, color=GRAY)
    axes[1].set_title("Real source: phase resets randomly every few nanoseconds")

    for ax in axes:
        ax.set_ylim(-2.45, 1.5)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
    axes[1].set_xlabel("time")
    axes[1].set_xticks([])
    fig.tight_layout()
    save(fig, "ch04-coherence")


def thin_film_color():
    """Reflected intensity versus soap-film thickness for red, green and blue light."""
    n = 1.33
    t_nm = np.linspace(0, 700, 3000)

    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for lam, color, label in [(650, "#c0392b", "red, 650 nm"),
                              (550, "#2e7d5b", "green, 550 nm"),
                              (450, "#1769aa", "blue, 450 nm")]:
        # Net pi shift between the two reflections => reflected I proportional to sin^2.
        ax.plot(t_nm, np.sin(2 * np.pi * n * t_nm / lam) ** 2,
                color=color, label=label, lw=1.6)

    ax.axvspan(0, 40, color=GRAY, alpha=0.15, lw=0)
    ax.text(20, 1.06, "black\nfilm", ha="center", fontsize=9, color=GRAY)
    ax.set_xlim(0, 700)
    ax.set_ylim(0, 1.2)
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_xlabel(r"film thickness $t$ (nm)")
    ax.set_ylabel("reflected intensity")
    ax.set_title(r"Soap film in air ($n = 1.33$): which color reflects depends on thickness")
    ax.legend(loc="upper right", ncol=3, fontsize=9)
    save(fig, "ch04-thin-film-color")


if __name__ == "__main__":
    use_style()
    print("Chapter 4 figures:")
    two_slit_intensity()
    n_slit_intensity()
    coherence()
    thin_film_color()
