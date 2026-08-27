"""Figures embedded in Chapter 10 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def selection_rule_transitions():
    """Which of four proposed transitions satisfy Delta ell = +/-1 (Problem 3)."""
    levels = {"1s": (1, 0), "2s": (2, 0), "2p": (2, 1), "3s": (3, 0), "3p": (3, 1), "3d": (3, 2)}
    x_by_l = {0: 0.0, 1: 1.0, 2: 2.0}
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    for label, (n, l) in levels.items():
        x = x_by_l[l]
        ax.hlines(n, x - 0.3, x + 0.3, color=BLUE, lw=2.4)
        ax.text(x, n + 0.12, label, ha="center", fontsize=10, color=DARK)

    transitions = [
        ("3d", "2p", GREEN, "allowed", -0.05),
        ("3s", "2s", RED, "forbidden", 0.0),
        ("3p", "1s", GREEN, "allowed", 0.05),
        ("2p", "1s", GREEN, "allowed", 0.10),
    ]
    for start, end, color, verdict, offset in transitions:
        n1, l1 = levels[start]
        n2, l2 = levels[end]
        x1, x2 = x_by_l[l1] + offset, x_by_l[l2] + offset
        style = "-|>" if verdict == "allowed" else "-|>"
        ls = "-" if verdict == "allowed" else "--"
        ax.annotate("", xy=(x2, n2), xytext=(x1, n1),
                    arrowprops=dict(arrowstyle=style, color=color, lw=1.8, ls=ls,
                                     shrinkA=8, shrinkB=8))

    ax.plot([], [], color=GREEN, lw=1.8, label="allowed ($\\Delta\\ell=\\pm1$)")
    ax.plot([], [], color=RED, lw=1.8, ls="--", label="forbidden")
    ax.legend(loc="upper left", fontsize=9.5)

    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["$s$ ($\\ell=0$)", "$p$ ($\\ell=1$)", "$d$ ($\\ell=2$)"])
    ax.set_yticks([1, 2, 3])
    ax.set_ylabel("$n$")
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0.5, 3.6)
    ax.set_title(r"Only $3s\to2s$ violates $\Delta\ell=\pm1$")
    save(fig, "ch10-sol-selection-rule-transitions")


def hydrogenic_z_scaling():
    """Ground-state radial probability for H (Z=1) vs. Li2+ (Z=3): peak moves in, energy scales as Z^2 (Problem 7)."""
    rho = np.linspace(0, 3, 1000)
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for Z, color, label, EI in [(1, BLUE, "H ($Z=1$)", 13.6), (3, RED, "Li$^{2+}$ ($Z=3$)", 122.4)]:
        R = 2 * Z ** 1.5 * np.exp(-Z * rho)
        P = rho ** 2 * R ** 2
        P /= P.max()
        ax.plot(rho, P, color=color, lw=2.0,
                label=f"{label}: $E_I={EI}$ eV, peak at $r={1/Z:.3f}\\,a_0$")
    for Z, color in [(1, BLUE), (3, RED)]:
        ax.axvline(1 / Z, color=color, lw=0.8, ls=":")
    ax.set_xlim(0, 3)
    ax.set_xlabel(r"$r/a_0$")
    ax.set_ylabel(r"$P(r)$ (each curve normalized to its own peak)")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title(r"Higher $Z$ pulls the electron in by $1/Z$ and binds it $Z^2$ times harder")
    save(fig, "ch10-sol-hydrogenic-z-scaling")


def stern_gerlach_schematic():
    """Beam of silver atoms splitting into two spots in an inhomogeneous field (Problem 8)."""
    L, D = 0.20, 0.40
    z1 = 2.16e-4
    fig, ax = plt.subplots(figsize=(7.6, 3.4))
    ax.add_patch(plt.Rectangle((0, -0.35), L, 0.7, facecolor="#eee0c9", edgecolor=DARK, lw=1.0))
    ax.text(L / 2, 0.55, r"magnet, $\partial B_z/\partial z=15\ \text{T/m}$", ha="center", fontsize=9.5, color=DARK)

    x_screen = L + D
    ax.axvline(x_screen, color=DARK, lw=2.0)
    ax.text(x_screen + 0.01, 0, "screen", rotation=90, va="center", fontsize=9.5, color=DARK)

    x0 = np.array([0])
    x_mid = L
    x_end = x_screen
    scale = 400  # exaggerate the (tiny) real deflection so the geometry is visible
    for sign, color, label in [(+1, BLUE, "$m_s=+1/2$"), (-1, RED, "$m_s=-1/2$")]:
        xs = [0, x_mid, x_end]
        zs = [0, sign * z1 * scale * 0.35, sign * z1 * scale]
        ax.plot(xs, zs, color=color, lw=1.8)
        ax.plot([x_end], [zs[-1]], marker="o", ms=8, color=color, zorder=5)
        ax.text(x_end + 0.015, zs[-1], label, va="center", fontsize=9.5, color=color)

    ax.annotate("", xy=(x_end + 0.09, z1 * scale), xytext=(x_end + 0.09, -z1 * scale),
                arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    ax.text(x_end + 0.10, 0, f"$2z={2*z1*1e3:.3f}$ mm", va="center", fontsize=9.5, color=DARK)

    ax.set_xlim(-0.05, x_end + 0.32)
    ax.set_ylim(-0.11, 0.65)
    ax.axis("off")
    ax.set_title("Stern–Gerlach: the field gradient splits the beam into two spots")
    save(fig, "ch10-sol-stern-gerlach")


def zeeman_line_splitting():
    """A single spectral line splits into a Zeeman triplet under an external field (Problem 9)."""
    lam0 = 486.1
    dlam = 0.00551
    fig, axes = plt.subplots(2, 1, figsize=(7.0, 3.6), sharex=True, gridspec_kw=dict(height_ratios=[1, 1]))

    axes[0].axvline(lam0, color=BLUE, lw=2.4)
    axes[0].text(lam0, 1.1, r"$B=0$: one line", ha="center", fontsize=10, color=BLUE)
    axes[0].set_ylim(0, 1.4)
    axes[0].set_yticks([])

    for lam, color in [(lam0 - dlam, RED), (lam0, GREEN), (lam0 + dlam, RED)]:
        axes[1].axvline(lam, color=color, lw=2.4)
    axes[1].annotate("", xy=(lam0 - dlam, 0.7), xytext=(lam0, 0.7),
                      arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    axes[1].text(lam0 - dlam / 2, 0.85, f"$\\Delta\\lambda={dlam}$ nm", ha="center", fontsize=9, color=DARK)
    axes[1].text(lam0, 1.1, r"$B=0.50$ T: Zeeman triplet", ha="center", fontsize=10, color=DARK)
    axes[1].set_ylim(0, 1.4)
    axes[1].set_yticks([])
    axes[1].set_xlim(lam0 - 4 * dlam, lam0 + 4 * dlam)
    axes[1].set_xlabel(r"wavelength near H$_\beta$, $486.1$ nm")

    fig.suptitle("A magnetic field splits one spectral line into three, spaced by $\\Delta\\lambda$", fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch10-sol-zeeman-line-splitting")


if __name__ == "__main__":
    use_style()
    print("Chapter 10 solution figures:")
    selection_rule_transitions()
    hydrogenic_z_scaling()
    stern_gerlach_schematic()
    zeeman_line_splitting()
