"""Generate the computed figures for Chapter 5, Diffraction of Light."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.special import j1

from figstyle import (BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, LIGHT,
                      fringe_strip, mono_cmap, save, use_style)


def sinc2(u):
    """[sin(u)/u]^2, with the removable singularity at u = 0 filled in."""
    return np.where(np.abs(u) < 1e-12, 1.0, (np.sin(u) / np.where(u == 0, 1, u)) ** 2)


def single_slit_intensity():
    """The sinc^2 pattern, with the side lobes shown at 20x magnification."""
    x = np.linspace(-3.6, 3.6, 5000)          # x = a sin(theta) / lambda
    intensity = sinc2(np.pi * x)

    fig = plt.figure(figsize=(7.6, 4.8))
    gs = GridSpec(2, 1, height_ratios=[1, 4], hspace=0.12, figure=fig)

    fringe_strip(fig.add_subplot(gs[0]), x, intensity, gamma=0.55)

    ax = fig.add_subplot(gs[1])
    ax.plot(x, intensity, color=BLUE)

    # Show the side lobes magnified, but only outside the central maximum, so the
    # magnified curve never runs off the top of the frame.
    side = np.abs(x) >= 1.0
    mag = np.where(side, 20 * intensity, np.nan)
    ax.plot(x, mag, color=ORANGE, lw=1.2, ls="--")
    ax.text(-2.46, 0.72, r"side lobes, $\times 20$", color=ORANGE, fontsize=9.5, ha="center")

    for m in [-3, -2, -1, 1, 2, 3]:
        ax.axvline(m, color=GRAY, lw=0.7, ls=":")
    ax.annotate("", xy=(1, 1.13), xytext=(-1, 1.13),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.1))
    ax.text(0, 1.18, r"central maximum: full width $2\lambda/a$",
            ha="center", fontsize=9.5, color=RED)
    ax.annotate("", xy=(2, 0.16), xytext=(1, 0.16),
                arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.9))
    ax.text(1.5, 0.20, r"$\lambda/a$", ha="center", fontsize=9, color=GRAY)

    for pk, lbl in [(1.4303, "4.7%"), (2.4590, "1.6%"), (3.4707, "0.8%")]:
        ax.plot([pk], [20 * sinc2(np.pi * pk)], marker="o", ms=3.5, color=ORANGE)
        ax.annotate(lbl, (pk, 20 * sinc2(np.pi * pk)), textcoords="offset points",
                    xytext=(4, 4), fontsize=8.5, color=ORANGE)

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, 1.34)
    ax.set_xlabel(r"$a\sin\theta/\lambda$   (minima at $a\sin\theta = m\lambda$, $m \neq 0$)")
    ax.set_ylabel(r"$I/I_0$")
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    save(fig, "ch05-single-slit-intensity")


def slit_width_scaling():
    """Narrowing the slit widens the pattern: the only thing that matters is lambda/a."""
    theta = np.linspace(-np.pi / 2, np.pi / 2, 3000)
    s = np.sin(theta)

    fig, axes = plt.subplots(4, 1, figsize=(7.6, 6.6), sharex=True)
    for ax, (ratio, color) in zip(axes, [(1, RED), (2, PURPLE), (5, GREEN), (20, BLUE)]):
        intensity = sinc2(np.pi * ratio * s)
        ax.plot(s, intensity, color=color, lw=1.6)
        if ratio > 1:
            w = 1.0 / ratio     # central maximum spans sin(theta) = +/- lambda/a
            ax.annotate("", xy=(w, 0.5), xytext=(-w, 0.5),
                        arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.0))
            ax.plot([-w, -w], [0, 0.5], color=GRAY, lw=0.7, ls=":")
            ax.plot([w, w], [0, 0.5], color=GRAY, lw=0.7, ls=":")
        ax.set_ylim(0, 1.62)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["0", "$I_0$"])
        ax.text(0.012, 0.62, rf"$a = {ratio}\lambda$", transform=ax.transAxes,
                ha="left", fontsize=11, fontweight="bold", color=color)
        if ratio == 1:
            ax.text(0.5, 0.80, "no minimum anywhere: the slit radiates\nalmost like a single point source",
                    transform=ax.transAxes, ha="center", fontsize=9, color=GRAY)
        else:
            ax.text(0.5, 0.84, rf"first minimum at $\sin\theta = 1/{ratio}$",
                    transform=ax.transAxes, ha="center", fontsize=9, color=GRAY)

    axes[-1].set_xlim(-1, 1)
    axes[-1].set_xticks([-1, -0.5, 0, 0.5, 1])
    axes[-1].set_xlabel(r"$\sin\theta$")
    axes[0].set_title(r"Diffraction depends only on the ratio $\lambda/a$")
    fig.tight_layout()
    save(fig, "ch05-slit-width-scaling")


def double_slit_envelope():
    """Real double slit: interference fringes under a single-slit envelope."""
    d_over_a = 5.0
    x = np.linspace(-12.4, 12.4, 8000)        # x = d sin(theta) / lambda
    envelope = sinc2(np.pi * x / d_over_a)
    fringes = np.cos(np.pi * x) ** 2
    intensity = envelope * fringes

    fig = plt.figure(figsize=(7.8, 4.6))
    gs = GridSpec(2, 1, height_ratios=[1, 4], hspace=0.12, figure=fig)

    fringe_strip(fig.add_subplot(gs[0]), x, intensity, gamma=0.55)

    ax = fig.add_subplot(gs[1])
    ax.plot(x, intensity, color=BLUE, lw=1.3, label="real double slit")
    ax.plot(x, envelope, color=RED, lw=1.4, ls="--",
            label=r"single-slit envelope ($a = d/5$)")
    ax.set_ylim(0, 1.30)

    for m in (-10, -5, 5, 10):
        ax.plot([m], [0], marker="v", ms=7, color=ORANGE, clip_on=False, zorder=6)
    ax.annotate("missing orders  $m = \\pm 5,\\ \\pm 10$", xy=(5, 0.0),
                xytext=(6.2, 0.42), fontsize=9.5, color=ORANGE,
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9))

    ax.set_xlim(x[0], x[-1])
    ax.set_xticks(np.arange(-12, 13, 2))
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_xlabel(r"$d\sin\theta/\lambda$   (interference order $m$)")
    ax.set_ylabel(r"$I/I_0$")
    ax.legend(loc="upper right", fontsize=9)
    save(fig, "ch05-double-slit-envelope")


def grating_resolving_power():
    """Resolving the sodium doublet: R = mN decides whether two lines separate."""
    lam1, lam2 = 589.0, 589.6                  # nm
    d = 1e6 / 600.0                            # 600 lines/mm, spacing in nm
    theta1 = np.arcsin(lam1 / d)
    theta2 = np.arcsin(lam2 / d)
    sep = theta2 - theta1                      # angular separation of the doublet

    theta = theta1 + sep * np.linspace(-1.6, 2.6, 6000)
    u = (theta - theta1) / sep                 # angle in units of the doublet separation

    def grating(n, lam):
        phi = 2 * np.pi * d * np.sin(theta) / lam
        num = np.sin(n * phi / 2) ** 2
        den = np.sin(phi / 2) ** 2
        return np.where(den < 1e-12, n ** 2, num / np.maximum(den, 1e-12)) / n ** 2

    fig, axes = plt.subplots(3, 1, figsize=(7.6, 6.4), sharex=True)
    verdicts = {300: "not resolved: one broad blur",
                982: "just resolved: the Rayleigh criterion, $R = 982$",
                3000: "comfortably resolved"}
    for ax, n in zip(axes, [300, 982, 3000]):
        i1, i2 = grating(n, lam1), grating(n, lam2)
        ax.plot(u, i1 + i2, color=GRAY, lw=2.4, alpha=0.35, label="what the detector records")
        ax.plot(u, i1, color=ORANGE, lw=1.3, label=r"$589.0$ nm")
        ax.plot(u, i2, color=BLUE, lw=1.3, label=r"$589.6$ nm")
        ax.set_ylim(0, 2.9)
        ax.set_yticks([])
        ax.set_xlim(u[0], u[-1])
        ax.text(0.012, 0.80, rf"$N = {n}$   ($R = mN = {n}$)" "\n" f"{verdicts[n]}",
                transform=ax.transAxes, fontsize=10, color="#333333")

    axes[0].legend(loc="upper right", fontsize=9)
    axes[0].set_title(r"Sodium doublet in first order: $\lambda/\Delta\lambda = 982$ is needed")
    axes[-1].set_xlabel("diffraction angle, in units of the doublet's angular separation")
    axes[-1].set_xticks([-1, 0, 1, 2])
    fig.tight_layout()
    save(fig, "ch05-grating-resolving-power")


def airy_and_rayleigh():
    """The Airy pattern, and two point sources at three angular separations."""
    def airy(r):
        r = np.where(r == 0, 1e-9, r)
        return (2 * j1(np.pi * 1.21967 * r) / (np.pi * 1.21967 * r)) ** 2

    fig = plt.figure(figsize=(7.8, 5.6))
    gs = GridSpec(2, 3, height_ratios=[3, 2], hspace=0.20, wspace=0.20, figure=fig)

    grid = np.linspace(-3.2, 3.2, 420)
    xx, yy = np.meshgrid(grid, grid)
    cmap = mono_cmap("#e8e2d0")

    seps = [(0.5, "0.5 " + r"$\theta_{\min}$" + "\nnot resolved"),
            (1.0, "1.0 " + r"$\theta_{\min}$" + "\njust resolved"),
            (2.0, "2.0 " + r"$\theta_{\min}$" + "\nwell resolved")]

    for col, (sep, label) in enumerate(seps):
        img = airy(np.hypot(xx - sep / 2, yy)) + airy(np.hypot(xx + sep / 2, yy))
        ax = fig.add_subplot(gs[0, col])
        ax.imshow(img ** 0.45, cmap=cmap, origin="lower",
                  extent=(grid[0], grid[-1], grid[0], grid[-1]))
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(label, fontsize=10)

        axp = fig.add_subplot(gs[1, col])
        line = airy(np.abs(grid - sep / 2)) + airy(np.abs(grid + sep / 2))
        axp.plot(grid, line, color=BLUE, lw=1.4)
        axp.plot(grid, airy(np.abs(grid - sep / 2)), color=GRAY, lw=0.8, ls=":")
        axp.plot(grid, airy(np.abs(grid + sep / 2)), color=GRAY, lw=0.8, ls=":")
        axp.set_ylim(0, 2.15)
        axp.set_xlim(-3.2, 3.2)
        axp.set_yticks([])
        axp.set_xlabel(r"angle / $\theta_{\min}$", fontsize=9)
        if col == 0:
            axp.set_ylabel("intensity", fontsize=9)

    fig.suptitle(r"Rayleigh criterion: $\theta_{\min} = 1.22\,\lambda/D$ for a circular aperture",
                 fontsize=12, fontweight="bold", y=0.98)
    save(fig, "ch05-airy-rayleigh")


if __name__ == "__main__":
    use_style()
    print("Chapter 5 figures:")
    single_slit_intensity()
    slit_width_scaling()
    double_slit_envelope()
    grating_resolving_power()
    airy_and_rayleigh()
