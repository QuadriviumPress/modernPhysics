"""Static fallbacks for the locally hosted animation figures."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, PURPLE, ORANGE, GRAY, LIGHT, save, use_style


def path_to_phase():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.5))
    ax, graph = axes
    sources = np.array([[0.0, 0.7], [0.0, -0.7]])
    detector = np.array([3.5, 0.9])
    ax.scatter(sources[:, 0], sources[:, 1], s=80, color=[BLUE, RED], zorder=3)
    ax.scatter(*detector, s=60, color=GREEN, zorder=3)
    for index, source in enumerate(sources, 1):
        ax.plot([source[0], detector[0]], [source[1], detector[1]], color=GRAY)
        midpoint = (source + detector) / 2
        ax.text(*midpoint, rf"$r_{index}$", ha="center", va="bottom")
    ax.text(detector[0], detector[1] + 0.18, "detector", ha="center")
    ax.set_xlim(-0.4, 4.0)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(r"geometry gives $\Delta r=r_2-r_1$")

    delta = np.linspace(0, 3, 600)
    intensity = np.cos(np.pi * delta) ** 2
    graph.plot(delta, intensity, color=BLUE)
    graph.scatter(np.arange(4), np.ones(4), color=GREEN, zorder=3, label="constructive")
    graph.scatter(np.arange(0.5, 3, 1), np.zeros(3), color=RED, zorder=3, label="destructive")
    graph.set(xlabel=r"path difference $\Delta r/\lambda$", ylabel=r"$I/I_{\max}$", ylim=(-0.08, 1.15))
    graph.legend(loc="upper right")
    fig.tight_layout()
    save(fig, "ch04-path-to-phase")


def standing_wave_formation():
    x = np.linspace(0, 2, 600)
    fig, axes = plt.subplots(3, 1, figsize=(7.8, 5.2), sharex=True)
    for ax, phase in zip(axes, [0, np.pi / 4, np.pi / 2]):
        right = np.sin(2 * np.pi * x - phase)
        left = np.sin(2 * np.pi * x + phase)
        total = right + left
        ax.plot(x, right, color=BLUE, ls="--", alpha=0.65)
        ax.plot(x, left, color=RED, ls="--", alpha=0.65)
        ax.plot(x, total, color=GREEN, lw=2.2)
        ax.scatter(np.arange(0, 2.01, 0.5), np.zeros(5), color=RED, s=18, zorder=4)
        ax.axhline(0, color=LIGHT, lw=0.8)
        ax.set_ylim(-2.2, 2.2)
        ax.set_yticks([])
    axes[-1].set_xlabel("position")
    axes[0].set_title("opposite traveling waves form fixed nodes")
    fig.tight_layout()
    save(fig, "ch07-standing-wave-formation")


def fourier_synthesis():
    x = np.linspace(-np.pi, np.pi, 1000, endpoint=False)
    fig, axes = plt.subplots(2, 2, figsize=(8.0, 5.1), sharex=True, sharey=True)
    for ax, count in zip(axes.flat, [1, 3, 10, 40]):
        total = sum(((-1) ** (k + 1)) * np.sin(k * x) / k for k in range(1, count + 1)) * 2 / np.pi
        ax.plot(x, x / np.pi, color=LIGHT, ls="--")
        ax.plot(x, total, color=BLUE)
        ax.set_title(f"{count} component" + ("s" if count > 1 else ""))
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_ylim(-1.35, 1.35)
    fig.supxlabel("position")
    fig.supylabel("amplitude")
    fig.suptitle("a broader Fourier spectrum makes sharper structure")
    fig.tight_layout()
    save(fig, "ch07-fourier-synthesis")


def two_frequency_envelope():
    x = np.linspace(0, 5, 1200)
    y1 = np.sin(2 * np.pi * 4.0 * x)
    y2 = np.sin(2 * np.pi * 4.5 * x)
    total = y1 + y2
    envelope = 2 * np.abs(np.cos(np.pi * 0.5 * x))
    fig, axes = plt.subplots(3, 1, figsize=(8.0, 5.2), sharex=True)
    axes[0].plot(x, y1, color=BLUE)
    axes[0].set_title(r"component 1: $f_1$")
    axes[1].plot(x, y2, color=ORANGE)
    axes[1].set_title(r"component 2: nearby $f_2$")
    axes[2].plot(x, total, color=PURPLE)
    axes[2].plot(x, envelope, color=RED, ls="--")
    axes[2].plot(x, -envelope, color=RED, ls="--")
    axes[2].set_title("sum and beat envelope")
    for ax in axes:
        ax.axhline(0, color=LIGHT, lw=0.7)
        ax.set_yticks([])
    axes[-1].set_xlabel("time")
    fig.tight_layout()
    save(fig, "ch07-two-frequency-envelope")


def resonance_linewidth():
    ratio = np.linspace(0.05, 2.0, 1000)
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    for q, color in [(15, BLUE), (5, GREEN), (1.5, RED)]:
        response = 1 / np.sqrt((1 - ratio**2) ** 2 + (ratio / q) ** 2)
        ax.plot(ratio, response / response.max(), color=color, label=rf"$Q={q}$")
    ax.axvline(1, color=GRAY, lw=0.8, ls=":")
    ax.set(xlabel=r"driving frequency $f/f_0$", ylabel="normalized response", ylim=(0, 1.08))
    ax.legend()
    ax.set_title(r"short lifetime $\leftrightarrow$ broad linewidth")
    fig.tight_layout()
    save(fig, "ch07-resonance-linewidth")


def box_modes():
    x = np.linspace(0, 1, 700)
    fig, axes = plt.subplots(4, 1, figsize=(7.5, 5.6), sharex=True)
    for ax, n, color in zip(axes, range(1, 5), [BLUE, GREEN, PURPLE, ORANGE]):
        y = np.sin(n * np.pi * x)
        ax.plot(x, y, color=color, lw=2)
        ax.plot(x, -y, color=color, lw=1, alpha=0.3)
        nodes = np.arange(n + 1) / n
        ax.scatter(nodes, np.zeros_like(nodes), color=RED, s=16, zorder=4)
        ax.axhline(0, color=LIGHT, lw=0.7)
        ax.text(0.02, 0.78, rf"$n={n}$", transform=ax.transAxes)
        ax.set_ylim(-1.2, 1.2)
        ax.set_yticks([])
    axes[-1].set_xlabel(r"position $x/L$")
    axes[0].set_title("particle-in-a-box modes vanish at both walls")
    fig.tight_layout()
    save(fig, "ch08-box-modes")


if __name__ == "__main__":
    use_style()
    path_to_phase()
    standing_wave_formation()
    fourier_synthesis()
    two_frequency_envelope()
    resonance_linewidth()
    box_modes()
