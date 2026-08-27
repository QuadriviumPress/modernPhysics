"""Figures embedded in Chapter 4 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, mono_cmap, save, use_style

DARK = "#333333"


def six_slit_pattern():
    """N = 6 principal maxima, with the zeros and secondary maxima between m=0 and m=1 (Problem 9)."""
    N = 6
    x = np.linspace(-1.05, 1.05, 6000)          # x = sin(theta)
    # d sin(theta)/lambda = 5 * sin(theta)  (since d/lambda = 3.00/0.600 = 5)
    u = 5 * x
    psi = np.pi * u
    intensity = np.where(np.abs(np.sin(psi)) < 1e-9, N ** 2,
                          (np.sin(N * psi) / np.sin(np.where(np.abs(np.sin(psi)) < 1e-9, 1, psi))) ** 2) / N ** 2

    fig = plt.figure(figsize=(7.6, 5.4))
    gs = GridSpec(2, 1, height_ratios=[1, 1], hspace=0.32, figure=fig)

    ax0 = fig.add_subplot(gs[0])
    ax0.plot(x, intensity, color=BLUE, lw=1.3)
    for m in range(-5, 6):
        s = m / 5
        ax0.plot([s], [1.0], marker="o", ms=4, color=RED, zorder=5)
    ax0.set_xlim(-1.05, 1.05)
    ax0.set_ylim(0, 1.15)
    ax0.set_xlabel(r"$\sin\theta$")
    ax0.set_ylabel(r"$I/I_{\max}$")
    ax0.set_title(r"Six slits, $d=3.00\ \mu\text{m}$, $\lambda=600\ \text{nm}$: principal maxima at $\sin\theta=0.200\,m$")

    ax1 = fig.add_subplot(gs[1])
    mask = (x >= -0.02) & (x <= 0.22)
    ax1.plot(x[mask], intensity[mask], color=BLUE, lw=1.6)
    for q in range(1, 6):
        s0 = q * (0.200 / 6)
        ax1.axvline(s0, color=GRAY, lw=0.8, ls=":")
    ax1.plot([0.0], [1.0], marker="o", ms=6, color=RED, zorder=5)
    ax1.text(0.0, 1.06, "$m=0$\nmax", ha="center", fontsize=9, color=RED)
    ax1.plot([0.200], [1.0], marker="o", ms=6, color=RED, zorder=5)
    ax1.text(0.200, 1.06, "$m=1$\nmax", ha="center", fontsize=9, color=RED)
    ax1.text(0.100, 0.30, "4 secondary maxima\nbetween 5 zeros", ha="center", fontsize=9.5, color=GRAY)
    ax1.set_xlim(-0.02, 0.22)
    ax1.set_ylim(0, 1.15)
    ax1.set_xlabel(r"$\sin\theta$  (zoomed between $m=0$ and $m=1$)")
    ax1.set_ylabel(r"$I/I_{\max}$")

    save(fig, "ch04-sol-six-slit")


def newton_rings():
    """Reflected Newton's-rings pattern for R = 2.00 m, lambda = 589 nm; dark center, 10th dark ring marked."""
    lam = 589e-9
    R = 2.00
    r10 = np.sqrt(10 * lam * R)          # 3.43 mm

    span = 1.25 * r10
    n_px = 700
    xs = np.linspace(-span, span, n_px)
    X, Y = np.meshgrid(xs, xs)
    Rr = np.sqrt(X ** 2 + Y ** 2)
    intensity = np.sin(np.pi * Rr ** 2 / (lam * R)) ** 2   # dark (I=0) at r=0: one phase reversal

    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    ax.imshow(intensity, cmap=mono_cmap(RED), origin="lower",
              extent=(-span * 1e3, span * 1e3, -span * 1e3, span * 1e3), vmin=0, vmax=1)
    circle_theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r10 * 1e3 * np.cos(circle_theta), r10 * 1e3 * np.sin(circle_theta),
            color="white", lw=1.2, ls="--")
    ax.annotate(r"$r_{10}=3.43\ \text{mm}$", xy=(r10 * 1e3 * np.cos(0.9), r10 * 1e3 * np.sin(0.9)),
                xytext=(span * 1e3 * 0.55, span * 1e3 * 0.85), color="white", fontsize=10,
                arrowprops=dict(arrowstyle="-", color="white", lw=0.9))
    ax.set_xlabel("mm")
    ax.set_ylabel("mm")
    ax.set_title("Newton's rings in reflection: dark center, $r_m=\\sqrt{m\\lambda R}$")
    fig.tight_layout()
    save(fig, "ch04-sol-newton-rings")


def wavelength_coincidence():
    """Two-wavelength fringe patterns overlaid, showing the first noncentral coincidence (Problem 20)."""
    d = 0.150e-3
    L = 2.00
    lam1, lam2 = 480e-9, 600e-9
    y = np.linspace(0, 0.045, 6000)

    I1 = np.cos(np.pi * d * y / (L * lam1)) ** 2
    I2 = np.cos(np.pi * d * y / (L * lam2)) ** 2
    y_coincide = L * 5 * lam1 / d   # = L*4*lam2/d, 3.20 cm

    fig, axes = plt.subplots(2, 1, figsize=(7.6, 4.2), sharex=True,
                              gridspec_kw=dict(height_ratios=[1, 1], hspace=0.12))
    axes[0].plot(y * 100, I1, color=BLUE, lw=1.3, label=r"$\lambda_1=480\ \text{nm}$")
    axes[0].plot(y * 100, I2, color=RED, lw=1.3, label=r"$\lambda_2=600\ \text{nm}$")
    axes[0].legend(loc="upper right", fontsize=9, ncol=2)
    axes[0].set_ylabel(r"$I/I_0$")
    axes[0].set_yticks([0, 1])

    axes[1].plot(y * 100, I1 * I2, color=PURPLE, lw=1.4)
    axes[1].axvline(y_coincide * 100, color=GRAY, lw=1.0, ls="--")
    axes[1].annotate(f"coincidence\n$y=3.20$ cm\n($m_1=5,\\,m_2=4$)",
                      xy=(y_coincide * 100, 1.0), xytext=(y_coincide * 100 + 0.4, 1.15),
                      fontsize=9, color=DARK, arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    axes[1].set_ylabel("product\n(both bright)")
    axes[1].set_yticks([0, 1])
    axes[1].set_ylim(0, 1.4)
    axes[1].set_xlim(0, 4.5)
    axes[1].set_xlabel(r"$y$ (cm)")
    axes[0].set_title(r"Bright fringes of two wavelengths coincide where $m_1\lambda_1=m_2\lambda_2$")
    save(fig, "ch04-sol-coincidence")


def thin_film_cases():
    """Case A (one phase reversal) vs. Case B (two reversals): oil on water vs. oil on n=1.60 (Problem 11)."""
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))

    layers = [
        (axes[0], "Case A: oil on water", 1.00, 1.45, 1.33, r"$\pi$ shift", "no shift",
         r"$t_{\min}=\dfrac{\lambda}{4n}=103\ \text{nm}$"),
        (axes[1], "Case B: oil on $n=1.60$", 1.00, 1.45, 1.60, r"$\pi$ shift", r"$\pi$ shift",
         r"$t_{\min}=\dfrac{\lambda}{2n}=207\ \text{nm}$"),
    ]
    for ax, title, n0, n1, n2, shift_top, shift_bot, formula in layers:
        ax.add_patch(Rectangle((-1.5, 0), 3.0, 1.0, facecolor="#cfe3f2", edgecolor=BLUE, lw=1.2))
        ax.text(1.65, 1.35, f"$n_0={n0:.2f}$ (air)", fontsize=9.5, color=GRAY, ha="right")
        ax.text(1.65, 0.5, f"$n_1={n1:.2f}$ (oil)", fontsize=9.5, color=BLUE, ha="right", va="center")
        ax.text(1.65, -0.35, f"$n_2={n2:.2f}$", fontsize=9.5, color=GRAY, ha="right")

        ax.annotate("", xy=(-0.5, 1.0), xytext=(-1.1, 1.9),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8))
        ax.annotate("", xy=(0.1, 1.9), xytext=(-0.5, 1.0),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8))
        ax.text(-0.05, 1.55, shift_top, fontsize=9.5, color=RED, ha="left")

        ax.annotate("", xy=(0.3, 0.0), xytext=(-0.5, 1.0),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4, ls="--"))
        ax.annotate("", xy=(0.9, 1.9), xytext=(0.3, 0.0),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8))
        ax.text(0.55, -0.55, shift_bot, fontsize=9.5, color=GREEN, ha="center")

        ax.text(0.0, -1.15, formula, fontsize=11, color=DARK, ha="center")
        ax.set_title(title, fontsize=11)
        ax.set_xlim(-1.8, 2.0)
        ax.set_ylim(-1.6, 2.1)
        ax.set_aspect("equal")
        ax.axis("off")

    fig.tight_layout()
    save(fig, "ch04-sol-thin-film-cases")


if __name__ == "__main__":
    use_style()
    print("Chapter 4 solution figures:")
    six_slit_pattern()
    newton_rings()
    wavelength_coincidence()
    thin_film_cases()
