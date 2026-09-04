"""Figures embedded in Chapter 6 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"
H = 6.626e-34
C = 2.998e8
KB = 1.381e-23


def planck(lam_m, T):
    x = H * C / (lam_m * KB * T)
    return (1.0 / lam_m ** 5) / (np.exp(x) - 1.0)


def tungsten_spectrum():
    """Tungsten-filament blackbody curve at T=2900K: peak in the infrared, little visible output (Problem 2)."""
    lam_nm = np.linspace(150, 4000, 3000)
    T = 2900.0
    B = planck(lam_nm * 1e-9, T)
    B /= B.max()

    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    ax.plot(lam_nm, B, color=RED, lw=1.8)
    ax.axvspan(380, 750, color=GREEN, alpha=0.18, lw=0)
    ax.text(565, 1.05, "visible", ha="center", color=GREEN, fontsize=10)

    lam_peak = 2.898e-3 / T * 1e9
    ax.axvline(lam_peak, color=GRAY, lw=1.0, ls="--")
    ax.annotate(rf"$\lambda_{{\max}}={lam_peak:.0f}\ \mathrm{{nm}}$ (Wien's law)",
                xy=(lam_peak, 1.0), xytext=(lam_peak + 250, 1.08),
                fontsize=9.5, color=DARK, arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.9))

    ax.set_xlim(150, 4000)
    ax.set_ylim(0, 1.18)
    ax.set_xlabel(r"wavelength (nm)")
    ax.set_ylabel(r"spectral radiance (normalized to peak)")
    ax.set_title(r"Tungsten filament at $T=2900\ \mathrm{K}$: most output is invisible infrared")
    save(fig, "ch06-sol-tungsten-spectrum")


def photoelectric_two_point():
    """Stopping potential vs. frequency: two data points fix both h/e (slope) and phi/e (intercept), Problem 5."""
    f1, V1 = 6.67e14, 0.65
    f2, V2 = 8.33e14, 1.28
    slope = (V2 - V1) / (f2 - f1)          # h/e
    intercept = V1 - slope * f1            # -phi/e
    f0 = -intercept / slope                # threshold frequency

    f = np.linspace(0.85 * f0, 1.05 * f2, 200)
    V = slope * f + intercept

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.plot(f / 1e14, V, color=BLUE, lw=1.8, zorder=3)
    ax.plot([f1 / 1e14, f2 / 1e14], [V1, V2], "o", ms=8, color=RED, zorder=5)
    ax.annotate(f"({f1/1e14:.2f}, {V1})", (f1 / 1e14, V1), textcoords="offset points",
                xytext=(8, -14), fontsize=9, color=RED)
    ax.annotate(f"({f2/1e14:.2f}, {V2})", (f2 / 1e14, V2), textcoords="offset points",
                xytext=(8, 6), fontsize=9, color=RED)
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.plot([f0 / 1e14], [0], marker="o", ms=6, color=DARK, zorder=5)
    ax.annotate(r"$f_0$ (threshold)" "\n" r"$eV_0=0,\ hf_0=\phi$", xy=(f0 / 1e14, 0),
                xytext=(f0 / 1e14 - 1.3, 0.35), fontsize=9, color=DARK,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.9))
    ax.text(0.97, 0.06, r"slope $=h/e$" "\n" r"$y$-intercept $=-\phi/e$",
            transform=ax.transAxes, ha="right", fontsize=9.5, color=DARK)

    ax.set_xlim(f0 / 1e14 - 1.5, f2 / 1e14 + 0.4)
    ax.set_ylim(-0.6, 1.5)
    ax.set_xlabel(r"frequency $f$  ($10^{14}$ Hz)")
    ax.set_ylabel(r"stopping potential $V_0$ (V)")
    ax.set_title(r"Two stopping-potential measurements fix both $h$ and $\phi$")
    save(fig, "ch06-sol-photoelectric-fit")


def compton_angle_and_regime():
    """Delta-lambda(theta) with the 90 deg and 180 deg cases, plus why visible light hides the effect (9, 10, 12)."""
    lam_C = 2.426  # pm

    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.0), gridspec_kw=dict(width_ratios=[3, 2]))

    theta = np.linspace(0, 180, 400)
    dlam = lam_C * (1 - np.cos(np.radians(theta)))
    axes[0].plot(theta, dlam, color=BLUE, lw=1.8)
    for th, label in [(90, "Problem 9"), (180, "Problem 10")]:
        d = lam_C * (1 - np.cos(np.radians(th)))
        axes[0].plot([th], [d], marker="o", ms=7, color=RED, zorder=5)
        axes[0].annotate(f"{th}$^\\circ$: {d:.3f} pm\n({label})", (th, d),
                          textcoords="offset points", xytext=(-10, 10 if th == 90 else -32),
                          fontsize=9, color=RED, ha="right" if th == 180 else "left")
    axes[0].set_xlim(0, 180)
    axes[0].set_ylim(0, 5.4)
    axes[0].set_xticks([0, 45, 90, 135, 180])
    axes[0].set_xlabel(r"scattering angle $\theta$ (deg)")
    axes[0].set_ylabel(r"$\Delta\lambda$ (pm)")
    axes[0].set_title(r"$\Delta\lambda=\dfrac{h}{m_ec}(1-\cos\theta)$", fontsize=11)

    cases = [("visible\n600 nm", 4.04e-6, GREEN), ("X-ray\n0.0711 nm", 2.426 / 71.1, ORANGE)]
    axes[1].bar([0, 1], [c[1] for c in cases], color=[c[2] for c in cases],
                edgecolor=DARK, width=0.55, zorder=3)
    axes[1].set_yscale("log")
    axes[1].set_xticks([0, 1])
    axes[1].set_xticklabels([c[0] for c in cases], fontsize=9)
    for i, c in enumerate(cases):
        axes[1].text(i, c[1] * 1.3, f"{c[1]:.1e}", ha="center", fontsize=9, color=DARK)
    axes[1].set_ylabel(r"$\Delta\lambda/\lambda$ at $90^\circ$")
    axes[1].set_title("same $\\Delta\\lambda$, very\ndifferent fraction", fontsize=10)

    fig.tight_layout()
    save(fig, "ch06-sol-compton-angle")


def pair_production_budget():
    """Energy budget of a 2.50 MeV photon converting to an e+e- pair with shared kinetic energy (Problem 14)."""
    segments = [("$e^-$ rest\n$0.511$", 0.511, BLUE),
                ("$e^+$ rest\n$0.511$", 0.511, PURPLE),
                ("$e^-$ KE\n$0.739$", 0.739, GREEN),
                ("$e^+$ KE\n$0.739$", 0.739, ORANGE)]
    fig, ax = plt.subplots(figsize=(7.6, 2.4))
    left = 0.0
    for label, width, color in segments:
        ax.barh(0, width, left=left, color=color, edgecolor=DARK, height=0.6, zorder=3)
        ax.text(left + width / 2, 0, label, ha="center", va="center", fontsize=9.5, color="white", fontweight="bold")
        left += width
    ax.axvline(0, color=DARK, lw=1.0)
    ax.axvline(2.50, color=DARK, lw=1.0)
    ax.annotate("", xy=(0, -0.55), xytext=(2.50, -0.55),
                arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    ax.text(1.25, -0.78, r"incident photon, $E_\gamma=2.50\ \mathrm{MeV}$", ha="center", fontsize=10, color=DARK)
    ax.set_xlim(-0.05, 2.55)
    ax.set_ylim(-1.0, 0.55)
    ax.axis("off")
    ax.set_title("Where the photon's energy goes: two rest masses, then shared kinetic energy")
    save(fig, "ch06-sol-pair-production-budget")


def compton_spectrum():
    """Idealized detector spectrum for 0.662 MeV gammas: Compton continuum up to its edge, plus the photopeak (Problem 17)."""
    E = np.linspace(0, 0.75, 2000)
    edge = 0.478
    photopeak = 0.662

    continuum = np.where(E < edge, 0.35 + 0.9 * (E / edge) ** 3, 0.0)
    continuum = np.where(E < edge, continuum, 0.0)
    # soften the edge slightly for visual clarity without implying a precise cross-section
    smoothing = 1 / (1 + np.exp((E - edge) / 0.004))
    continuum *= smoothing

    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ax.fill_between(E, continuum, color=BLUE, alpha=0.35, lw=0)
    ax.plot(E, continuum, color=BLUE, lw=1.6, label="Compton continuum (idealized shape)")
    ax.annotate("", xy=(edge, 0), xytext=(edge, 1.15),
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=1.0, ls="--"))
    ax.text(edge, 1.20, f"Compton edge\n{edge} MeV", ha="center", fontsize=9, color=GRAY)

    ax.annotate("", xy=(photopeak, 0), xytext=(photopeak, 1.6),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4))
    ax.text(photopeak, 1.68, f"photopeak\n{photopeak} MeV", ha="center", fontsize=9.5, color=RED)

    ax.set_xlim(0, 0.75)
    ax.set_ylim(0, 1.9)
    ax.set_yticks([])
    ax.set_xlabel("energy deposited in detector (MeV)")
    ax.set_ylabel("counts (schematic)")
    ax.set_title(r"$^{137}$Cs spectrum: partial (Compton) vs. complete (photoelectric) absorption")
    save(fig, "ch06-sol-compton-spectrum")


if __name__ == "__main__":
    use_style()
    print("Chapter 6 solution figures:")
    tungsten_spectrum()
    photoelectric_two_point()
    compton_angle_and_regime()
    pair_production_budget()
    compton_spectrum()
