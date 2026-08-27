"""Figures embedded in Chapter 5 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def grating_order_overlap():
    """First-, second-, and third-order spectra of a 600 lines/mm grating in white light (Problem 9)."""
    d = 1e6 / 600.0                     # nm
    lam = np.linspace(400, 700, 600)

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    colors = {1: BLUE, 2: GREEN, 3: RED}
    for m, color in colors.items():
        arg = m * lam / d
        valid = arg <= 1.0
        theta = np.degrees(np.arcsin(np.where(valid, arg, np.nan)))
        ax.plot(lam[valid], theta[valid], color=color, lw=2.2, label=f"order $m={m}$")

    ax.axhspan(46.1, 57.1, color=GRAY, alpha=0.15, lw=0)
    ax.annotate("overlap: 2nd order at 600 nm\ncoincides with 3rd order at 400 nm",
                xy=(600, 46.1), xytext=(430, 66),
                fontsize=9.5, color=DARK,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
    ax.plot([600], [46.1], marker="o", ms=6, color=GREEN, zorder=5)
    ax.plot([400], [46.1], marker="o", ms=6, color=RED, zorder=5)

    ax.set_xlim(400, 700)
    ax.set_ylim(0, 90)
    ax.set_xlabel(r"wavelength $\lambda$ (nm)")
    ax.set_ylabel(r"diffraction angle $\theta$ (deg)")
    ax.set_title("600 lines/mm grating: the 2nd- and 3rd-order spectra overlap")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "ch05-sol-order-overlap")


def bragg_order_limit():
    """sin(theta_m) for a d = 0.137 nm crystal at lambda = 0.0709 nm: only m = 1, 2, 3 exist (Problem 14)."""
    d = 0.137     # nm
    lam = 0.0709  # nm
    m = np.arange(1, 6)
    s = m * lam / (2 * d)

    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    colors = [BLUE if si <= 1.0 else "#c9c9c9" for si in s]
    ax.bar(m, np.minimum(s, 1.15), color=colors, edgecolor=DARK, width=0.55, zorder=3)
    for mi, si in zip(m, s):
        label = f"{si:.3f}" if si <= 1.0 else "impossible\n(> 1)"
        ax.text(mi, min(si, 1.15) + 0.04, label, ha="center", fontsize=9,
                color=BLUE if si <= 1.0 else GRAY)
    ax.axhline(1.0, color=RED, lw=1.2, ls="--")
    ax.text(0.55, 1.03, r"$\sin\theta=1$ limit", color=RED, fontsize=9, ha="left")
    ax.set_xticks(m)
    ax.set_xlabel("order $m$")
    ax.set_ylabel(r"$\sin\theta_m=m\lambda/2d$")
    ax.set_ylim(0, 1.35)
    ax.set_title(r"$d=0.137\ \text{nm}$, $\lambda=0.0709\ \text{nm}$: orders $m=1,2,3$ exist, $m\geq4$ do not")
    save(fig, "ch05-sol-bragg-order-limit")


def eht_resolution():
    """Angular resolution vs. aperture diameter: a single large dish cannot match Earth-scale VLBI (Problem 19)."""
    lam = 1.3e-3   # m
    D = np.logspace(0, 7.3, 400)
    theta_arcsec = np.degrees(1.22 * lam / D) * 3600

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.loglog(D, theta_arcsec, color=BLUE, lw=1.8)

    ax.axhline(40e-6, color=RED, lw=1.2, ls="--")
    ax.text(1.3, 40e-6 * 1.6, r"M87 shadow, $40\ \mu\text{arcsec}$", color=RED, fontsize=9)

    for Dval, label, color in [(100, "large single dish\n($D\\sim100\\ \\text{m}$)", ORANGE),
                                (1.0e7, "Earth-scale array\n($D\\sim10^7\\ \\text{m}$)", GREEN)]:
        th = np.degrees(1.22 * lam / Dval) * 3600
        ax.plot([Dval], [th], marker="o", ms=7, color=color, zorder=5)
        ax.annotate(label, xy=(Dval, th), xytext=(Dval * 0.12, th * 6),
                    fontsize=9, color=color, ha="left",
                    arrowprops=dict(arrowstyle="->", color=color, lw=0.9))

    ax.set_xlabel("aperture diameter $D$ (m)")
    ax.set_ylabel(r"$\theta_{\min}=1.22\lambda/D$ (arcsec)")
    ax.set_title(r"At $\lambda=1.3\ \text{mm}$, only an Earth-sized aperture resolves the shadow")
    save(fig, "ch05-sol-eht-resolution")


def cd_dvd_orders():
    """First few diffraction orders for CD vs. DVD track spacing at 650 nm (Problem 20)."""
    lam = 650.0  # nm
    m = np.arange(1, 4)
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    width = 0.35
    for offset, (d, label, color) in zip([-1, 1], [(1600.0, "CD, $d=1.6\\ \\mu\\text{m}$", BLUE),
                                                     (740.0, "DVD, $d=0.74\\ \\mu\\text{m}$", RED)]):
        arg = m * lam / d
        valid = arg <= 1.0
        theta = np.degrees(np.arcsin(np.clip(arg, None, 1.0)))
        colors = [color if v else "#d9d9d9" for v in valid]
        ax.bar(m + offset * width / 2, theta, width=width, color=colors,
               edgecolor=DARK, label=label, zorder=3)

    ax.set_xticks(m)
    ax.set_xlabel("order $m$")
    ax.set_ylabel(r"diffraction angle $\theta$ (deg)")
    ax.set_ylim(0, 100)
    ax.axhline(90, color=GRAY, lw=0.8, ls=":")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("Smaller track spacing sends every order to a larger angle")
    save(fig, "ch05-sol-cd-dvd-orders")


if __name__ == "__main__":
    use_style()
    print("Chapter 5 solution figures:")
    grating_order_overlap()
    bragg_order_limit()
    eht_resolution()
    cd_dvd_orders()
