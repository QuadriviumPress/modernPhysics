"""Figures embedded in Chapter 8 worked solutions (not the main chapter body)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite, factorial

from figstyle import BLUE, RED, GREEN, GRAY, ORANGE, PURPLE, save, use_style

DARK = "#333333"


def infinite_well_levels():
    """Energy ladder E_n = n^2 E_1 for the infinite square well, with the n=2->1 photon (Problem 1)."""
    E1 = 9.40
    ns = [1, 2, 3, 4]
    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    for n in ns:
        E = n ** 2 * E1
        ax.hlines(E, 0, 1, color=BLUE, lw=2.2)
        ax.text(1.05, E, f"$n={n}$:  ${E:.1f}$ eV", va="center", fontsize=10, color=DARK)

    ax.annotate("", xy=(0.5, E1), xytext=(0.5, 4 * E1),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.2))
    ax.text(0.35, 2.5 * E1, r"$28.2\ \mathrm{eV}$" "\nphoton", color=RED, ha="right", fontsize=10)

    ax.set_xlim(-0.1, 2.6)
    ax.set_ylim(0, 17 * E1)
    ax.set_xticks([])
    ax.set_ylabel("energy (eV)")
    ax.set_title(r"Infinite well, $L=0.20\ \mathrm{nm}$: $E_n=n^2E_1$")
    save(fig, "ch08-sol-infinite-well-levels")


def step_reflection():
    """Reflection coefficient vs. step height, marking the two computed cases (Problem 4)."""
    E = 3.00
    V0 = np.linspace(0.001, 2.999, 500)
    k_ratio = np.sqrt((E - V0) / E)
    R = ((1 - k_ratio) / (1 + k_ratio)) ** 2

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.plot(V0 / E, R, color=BLUE, lw=1.8)
    for v0, label in [(2.00, "(a)"), (0.500, "(c)")]:
        r = ((1 - np.sqrt((E - v0) / E)) / (1 + np.sqrt((E - v0) / E))) ** 2
        ax.plot([v0 / E], [r], marker="o", ms=7, color=RED, zorder=5)
        ax.annotate(f"{label} $V_0={v0:.2f}$ eV\n$R={r*100:.2f}\\%$", (v0 / E, r),
                     textcoords="offset points", xytext=(10, 12), fontsize=9, color=RED)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel(r"$V_0/E$")
    ax.set_ylabel(r"reflection coefficient $R$")
    ax.set_title(r"$E=3.00\ \mathrm{eV}$: $R\to0$ smoothly as the step height $V_0\to0$")
    save(fig, "ch08-sol-step-reflection")


def tunneling_barrier():
    """Wavefunction envelope through a barrier: the heavier alpha particle decays faster inside (Problem 6)."""
    L = 2.0  # fm
    kappa_p = 0.491
    kappa_a = 0.982
    x = np.linspace(-1.5, L + 1.5, 800)

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    ax.axvspan(0, L, color="#eee0c9", alpha=0.7, lw=0)
    ax.text(L / 2, 1.18, r"barrier, $V_0=10.0\ \mathrm{MeV}$", ha="center", fontsize=10, color=DARK)

    for kappa, color, label in [(kappa_p, BLUE, "proton"), (kappa_a, RED, "alpha")]:
        env = np.ones_like(x)
        inside = (x >= 0) & (x <= L)
        beyond = x > L
        env = np.where(inside, np.exp(-kappa * x), env)
        amp_at_L = np.exp(-kappa * L)
        env = np.where(beyond, amp_at_L, env)
        ax.plot(x, env, color=color, lw=1.8, label=rf"{label}: $\kappa={kappa}\ \mathrm{{fm}}^{{-1}}$")

    ax.set_xlim(-1.5, L + 1.5)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel("position (fm)")
    ax.set_ylabel("wavefunction amplitude envelope (relative)")
    ax.legend(loc="upper right", fontsize=9.5)
    ax.set_title("Heavier particles decay faster inside the barrier, so they tunnel less")
    save(fig, "ch08-sol-tunneling-barrier")


def oscillator_ladder_and_spread():
    """Harmonic-oscillator level spacing hf and the H2 zero-point spread vs. bond length (Problems 9, 10)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2), gridspec_kw=dict(width_ratios=[1, 1.3]))

    hf = 0.360
    ax0 = axes[0]
    for n in range(4):
        E = (n + 0.5) * hf
        ax0.hlines(E, 0, 1, color=BLUE, lw=2.0)
        ax0.text(1.05, E, f"$n={n}$", va="center", fontsize=9.5, color=DARK)
    ax0.annotate("", xy=(0.5, 0.5 * hf), xytext=(0.5, 1.5 * hf),
                 arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    ax0.text(0.5, 1.9 * hf, r"$hf=0.360$ eV", color=RED, ha="center", fontsize=9.5)
    ax0.text(0.5, -0.6 * hf, r"$E_0=\frac{1}{2}hf=0.180$ eV", color=DARK, ha="center", fontsize=9)
    ax0.set_xlim(-0.1, 2.2)
    ax0.set_ylim(-1.0 * hf, 4 * hf)
    ax0.set_xticks([])
    ax0.set_ylabel("energy (eV)")
    ax0.set_title("Level ladder", fontsize=11)

    ax1 = axes[1]
    x = np.linspace(-40, 90, 600)
    sigma_macro_scaled = 3  # illustrative width only; true 1 kg value is unplottable at this scale
    ax1.axvspan(0, 74, color=GREEN, alpha=0.15, lw=0)
    ax1.annotate("", xy=(0, 0.55), xytext=(74, 0.55),
                 arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.2))
    ax1.text(37, 0.62, r"H$_2$ bond length, $74\ \mathrm{pm}$", ha="center", fontsize=9.5, color=GREEN)
    gauss = 0.62 * np.exp(-x ** 2 / (2 * 8.7 ** 2))
    ax1.plot(x, gauss, color=BLUE, lw=1.8)
    ax1.annotate("", xy=(-8.7, 0.30), xytext=(8.7, 0.30),
                 arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.2))
    ax1.text(0, 0.36, r"$\Delta x_{\rm H_2}=8.7$ pm", ha="center", fontsize=9.5, color=BLUE)
    ax1.set_xlim(-40, 90)
    ax1.set_ylim(0, 0.75)
    ax1.set_yticks([])
    ax1.set_xlabel("position (pm)")
    ax1.set_title(r"$\mathrm{H}_2$ zero-point spread is $\sim$12% of the bond length", fontsize=11)

    fig.tight_layout()
    save(fig, "ch08-sol-oscillator-ladder-spread")


def selection_rule_ladder():
    """Delta n = +/-1 makes 2->1 allowed and 2->0 forbidden for single-photon emission (Problem 12)."""
    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    for n in range(3):
        ax.hlines(n, 0, 1.3, color=BLUE, lw=2.2)
        ax.text(1.38, n, f"$n={n}$", va="center", fontsize=10, color=DARK)
    ax.annotate("", xy=(0.4, 1), xytext=(0.4, 2),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.2))
    ax.text(0.25, 1.5, r"allowed" "\n" r"$\Delta n=-1$", color=GREEN, ha="right", fontsize=9.5)
    ax.annotate("", xy=(0.9, 0), xytext=(0.9, 2),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6, ls="--"))
    ax.text(1.05, 1.0, r"forbidden" "\n" r"$\Delta n=-2$", color=RED, ha="left", fontsize=9.5)
    ax.set_xlim(-0.1, 2.3)
    ax.set_ylim(-0.4, 2.5)
    ax.set_xticks([])
    ax.set_ylabel(r"energy ($\hbar\omega$ units)")
    ax.set_title(r"$\Delta n=\pm1$: only $2\to1$ is a single-photon transition")
    save(fig, "ch08-sol-selection-rule")


def correspondence_principle():
    """|psi_n|^2 for n=0 vs. a highly excited state, compared with the classical probability density (Problem 13)."""
    def psi2(n, x):
        Hn = eval_hermite(n, x)
        norm = 1.0 / np.sqrt(2 ** n * factorial(n) * np.sqrt(np.pi))
        return (norm * Hn * np.exp(-x ** 2 / 2)) ** 2

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0), sharey=False)

    x0 = np.linspace(-4, 4, 1000)
    axes[0].plot(x0, psi2(0, x0), color=BLUE, lw=1.8)
    axes[0].set_title(r"$n=0$: peaked at $x=0$", fontsize=11)
    axes[0].set_xlim(-4, 4)
    axes[0].set_xlabel(r"$x$ (osc. units)")
    axes[0].set_yticks([])

    n = 20
    xmax = np.sqrt(2 * n + 1)
    x1 = np.linspace(-xmax * 1.05, xmax * 1.05, 4000)
    p_quantum = psi2(n, x1)
    classical = np.where(np.abs(x1) < xmax * 0.999, 1.0 / (np.pi * np.sqrt(np.maximum(xmax ** 2 - x1 ** 2, 1e-6))), np.nan)
    classical *= np.nanmax(p_quantum) / np.nanmax(classical[np.abs(x1) < xmax * 0.9])
    axes[1].plot(x1, p_quantum, color=BLUE, lw=1.0, label=f"quantum $n={n}$")
    axes[1].plot(x1, classical, color=RED, lw=1.8, ls="--", label="classical (time-averaged)")
    axes[1].axvline(-xmax, color=GRAY, lw=0.8, ls=":")
    axes[1].axvline(xmax, color=GRAY, lw=0.8, ls=":")
    axes[1].set_title(rf"$n={n}$: peaked at the classical turning points", fontsize=11)
    axes[1].set_xlim(-xmax * 1.05, xmax * 1.05)
    axes[1].set_xlabel(r"$x$ (osc. units)")
    axes[1].set_yticks([])
    axes[1].legend(loc="upper center", fontsize=9)

    fig.suptitle("Correspondence principle: probability density approaches the classical time-average as $n$ grows",
                 fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch08-sol-correspondence-principle")


def finite_well_bound_states():
    """Graphical solution k tan(kL/2) = kappa: a deeper well intersects more branches (Problem 17)."""
    z = np.linspace(0.001, 9.5, 4000)
    y = z * np.tan(z)
    y_masked = np.where((y > 0) & (y < 12), y, np.nan)
    # break the curve at each asymptote so matplotlib doesn't draw vertical connector lines
    branch_edges = [np.pi / 2, 3 * np.pi / 2, 5 * np.pi / 2, 7 * np.pi / 2]
    for edge in branch_edges:
        y_masked[np.abs(z - edge) < 0.02] = np.nan

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(z, y_masked, color=BLUE, lw=1.6, label=r"$z\tan z$  (even solutions)")

    for z0, color, label in [(2.2, GREEN, "shallow well"), (6.0, RED, "deep well")]:
        circle = np.sqrt(np.maximum(z0 ** 2 - z ** 2, 0))
        circle = np.where(z <= z0, circle, np.nan)
        ax.plot(z, circle, color=color, lw=1.8, label=f"{label}, $z_0={z0}$")
        # find intersections numerically
        diff = y_masked - circle
        sign = np.sign(diff)
        crossings = np.where(np.diff(sign) != 0)[0]
        count = 0
        for c in crossings:
            if np.isfinite(diff[c]) and np.isfinite(diff[c + 1]):
                count += 1
                ax.plot([z[c]], [circle[c]], marker="o", ms=6, color=color, zorder=5)
        ax.text(z0 * 0.35, np.sqrt(z0 ** 2) * 0.55, f"{count} bound\nstate(s)", color=color,
                fontsize=9, ha="center")

    ax.set_xlim(0, 9.5)
    ax.set_ylim(0, 8)
    ax.set_xlabel(r"$z = kL/2$")
    ax.set_ylabel(r"$z\tan z$  or  $\sqrt{z_0^2-z^2}$")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title(r"Larger $V_0$ (larger $z_0=\sqrt{2mV_0}\,L/2\hbar$) crosses more branches")
    save(fig, "ch08-sol-finite-well-bound-states")


if __name__ == "__main__":
    use_style()
    print("Chapter 8 solution figures:")
    infinite_well_levels()
    step_reflection()
    tunneling_barrier()
    oscillator_ladder_and_spread()
    selection_rule_ladder()
    correspondence_principle()
    finite_well_bound_states()
