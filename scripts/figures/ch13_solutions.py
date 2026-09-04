"""Figures embedded in Chapter 13 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def decay_curves():
    """Exponential decay: I-131 activity assay (Problem 3) and C-14 dating (Problem 9)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.2))

    t1 = np.linspace(0, 40, 400)
    T_half_I = 8.02
    N_I = 2.0 ** (-t1 / T_half_I)
    axes[0].plot(t1, N_I, color=BLUE, lw=1.8)
    t_mark = 24.0
    n_mark = 2.0 ** (-t_mark / T_half_I)
    axes[0].plot([t_mark], [n_mark], marker="o", ms=7, color=RED, zorder=5)
    axes[0].plot([t_mark, t_mark], [0, n_mark], color=GRAY, lw=0.8, ls="--")
    axes[0].plot([0, t_mark], [n_mark, n_mark], color=GRAY, lw=0.8, ls="--")
    axes[0].text(t_mark + 1, n_mark + 0.04, f"$t=24$ d\n$N/N_0={n_mark:.3f}$", fontsize=9, color=RED)
    axes[0].set_xlabel("time (days)")
    axes[0].set_ylabel(r"$N/N_0$")
    axes[0].set_xlim(0, 40)
    axes[0].set_ylim(0, 1.05)
    axes[0].set_title(r"$^{131}$I ($T_{1/2}=8.02$ d)", fontsize=11)

    t2 = np.linspace(0, 15000, 400)
    T_half_C = 5730
    N_C = 2.0 ** (-t2 / T_half_C)
    axes[1].plot(t2 / 1000, N_C, color=GREEN, lw=1.8)
    age = 7170
    axes[1].plot([age / 1000], [0.420], marker="o", ms=7, color=RED, zorder=5)
    axes[1].plot([age / 1000, age / 1000], [0, 0.420], color=GRAY, lw=0.8, ls="--")
    axes[1].plot([0, age / 1000], [0.420, 0.420], color=GRAY, lw=0.8, ls="--")
    axes[1].text(age / 1000 + 0.4, 0.44, f"$t=7.17$ kyr\n$A/A_0=0.420$", fontsize=9, color=RED)
    axes[1].set_xlabel("time (kyr)")
    axes[1].set_ylabel(r"$A/A_0$")
    axes[1].set_xlim(0, 15)
    axes[1].set_ylim(0, 1.05)
    axes[1].set_title(r"$^{14}$C ($T_{1/2}=5730$ yr)", fontsize=11)

    fig.suptitle("Reading a decay curve backward: measured fraction remaining fixes the elapsed time", fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch13-sol-decay-curves")


def secular_equilibrium():
    """Ra-226's long half-life keeps its activity flat while Rn-222 builds up to match it (Problem 8)."""
    t = np.linspace(0, 30, 500)  # days
    T_half_Rn = 3.8
    lam_Rn = np.log(2) / T_half_Rn
    A_Ra = 1.0
    A_Rn = A_Ra * (1 - np.exp(-lam_Rn * t))

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.axhline(A_Ra, color=BLUE, lw=1.8, label=r"$^{226}$Ra activity (essentially constant, $T_{1/2}=1600$ yr)")
    ax.plot(t, A_Rn, color=RED, lw=1.8, label=r"$^{222}$Rn activity ($T_{1/2}=3.8$ d), building up")
    ax.axhline(1.0, color=GRAY, lw=0.6, ls=":")
    ax.annotate("secular equilibrium:\n$A_{\\rm Rn}\\to A_{\\rm Ra}$", xy=(24, 0.97), xytext=(14, 0.55),
                fontsize=10, color=DARK, arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.9))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 1.15)
    ax.set_xlabel("time since sample sealed (days)")
    ax.set_ylabel(r"activity (relative to $^{226}$Ra)")
    ax.legend(loc="lower right", fontsize=9)
    ax.set_title("A short-lived daughter grows in until its activity matches its long-lived parent's")
    save(fig, "ch13-sol-secular-equilibrium")


def fusion_energy_sharing():
    """D-T fusion: equal and opposite momenta split the 17.6 MeV Q-value unevenly by mass (Problem 10)."""
    Q = 17.6
    K_alpha, K_n = 3.5, 14.1
    fig, ax = plt.subplots(figsize=(7.2, 2.2))
    ax.barh(0, K_alpha, color=BLUE, edgecolor=DARK, height=0.6, zorder=3)
    ax.barh(0, K_n, left=K_alpha, color=RED, edgecolor=DARK, height=0.6, zorder=3)
    ax.text(K_alpha / 2, 0, r"$\alpha$: $3.5$ MeV" "\n" r"$m_\alpha\approx4.00$ u", ha="center", va="center",
            fontsize=9.5, color="white", fontweight="bold")
    ax.text(K_alpha + K_n / 2, 0, r"$n$: $14.1$ MeV" "\n" r"$m_n\approx1.01$ u", ha="center", va="center",
            fontsize=9.5, color="white", fontweight="bold")
    ax.annotate("", xy=(0, -0.55), xytext=(Q, -0.55), arrowprops=dict(arrowstyle="<->", color=DARK, lw=1.0))
    ax.text(Q / 2, -0.78, r"$Q=17.6\ \mathrm{MeV}$ total", ha="center", fontsize=10, color=DARK)
    ax.set_xlim(-0.3, Q + 0.3)
    ax.set_ylim(-1.0, 0.55)
    ax.axis("off")
    ax.set_title("Equal and opposite momenta give the lighter neutron most of the energy")
    save(fig, "ch13-sol-fusion-energy-sharing")


if __name__ == "__main__":
    use_style()
    print("Chapter 13 solution figures:")
    decay_curves()
    secular_equilibrium()
    fusion_energy_sharing()
