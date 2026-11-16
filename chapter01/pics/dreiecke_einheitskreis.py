"""Abb. 1.4: Dreiecke im Einheitskreis für 45°, 30° (mit Spiegelung) und 60°.
Stil wie Abb. 1.1: Achsen hellgrau, Kreis gestrichelt, Linien schwarz.
Aufruf: python3 dreiecke_einheitskreis.py  ->  dreiecke_einheitskreis.svg"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 14, "svg.fonttype": "path"})
HELL, GRAU, DGRAU = "#BFBFBF", "#808080", "#404040"
LW = 1.0


def grundbild(ax, titel):
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-0.35, 1.3); ax.set_ylim(-1.05, 1.15)
    ax.annotate("", xy=(1.25, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
    ax.annotate("", xy=(0, 1.12), xytext=(0, -1.0), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
    ax.text(1.25, -0.1, "1", color=HELL, ha="center", va="top")
    ax.text(-0.06, 1.12, "2", color=HELL, ha="right", va="top")
    t = np.linspace(-np.pi / 2 - 0.15, np.pi / 2 + 0.15, 300)
    ax.plot(np.cos(t), np.sin(t), "k", lw=LW * 0.8, ls=(0, (4, 3)))
    ax.text(-0.04, -0.04, r"$\mathcal{O}$", color=DGRAU, ha="right", va="top")
    ax.set_title(titel, fontsize=15)


def dreieck(ax, phi, sin_lab, cos_lab, r_lab=True):
    c, s = np.cos(phi), np.sin(phi)
    ax.plot([0, c], [0, s], "k", lw=LW)            # Radius
    ax.plot([0, c], [0, 0], "k", lw=LW * 1.8)      # cos
    ax.plot([c, c], [0, s], "k", lw=LW * 1.8)      # sin
    q = 0.07                                        # rechter Winkel
    ax.plot([c - q, c - q, c], [0, q, q], "k", lw=0.6)
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=np.degrees(phi), color=GRAU, lw=0.8))
    ax.text(0.33 * np.cos(phi / 2), 0.33 * np.sin(phi / 2), f"${np.degrees(phi):.0f}°$",
            color=GRAU, ha="center", va="center", fontsize=11)
    ax.plot(c, s, "o", ms=5, mfc="white", mec="k")
    if r_lab:
        ax.text(0.5 * c - 0.09 * s, 0.5 * s + 0.09 * c, "$1$", ha="center", va="center",
                rotation=np.degrees(phi))
    ax.text(c / 2, -0.06, cos_lab, ha="center", va="top")
    ax.text(c + 0.04, s / 2, sin_lab, ha="left", va="center")


fig, axs = plt.subplots(1, 3, figsize=(10.5, 4.2))

# 45°: gleichschenklig
grundbild(axs[0], r"$45°$")
dreieck(axs[0], np.pi / 4, r"$a$", r"$a$")
axs[0].text(0.35, -0.55, r"$a^2+a^2=1$", ha="center")

# 30°: an der 1-Achse gespiegelt -> gleichseitiges Dreieck
grundbild(axs[1], r"$30°$")
c, s = np.cos(np.pi / 6), np.sin(np.pi / 6)
axs[1].plot([0, c], [0, -s], color=GRAU, lw=LW)
axs[1].plot([c, c], [0, -s], color=GRAU, lw=LW * 1.8)
axs[1].plot(c, -s, "o", ms=5, mfc="white", mec=GRAU)
axs[1].text(c - 0.04, -s / 2, r"$\frac{1}{2}$", ha="right", va="center", color=GRAU)
axs[1].text(0.5 * c - 0.09 * s, -0.5 * s - 0.09 * c, "$1$", ha="center", va="center",
            rotation=-30, color=GRAU)
axs[1].text(c + 0.06, s + 0.02, r"$P$", ha="left", va="bottom")
axs[1].text(c + 0.06, -s - 0.02, r"$P^{\prime}$", ha="left", va="top", color=GRAU)
dreieck(axs[1], np.pi / 6, "", "")
axs[1].text(c - 0.04, s / 2, r"$\frac{1}{2}$", ha="right", va="center")
axs[1].text(c / 2 + 0.05, -0.04, r"$\cos 30°$", ha="center", va="top", fontsize=12)

# 60°: dasselbe Dreieck, gekippt
grundbild(axs[2], r"$60°$")
dreieck(axs[2], np.pi / 3, r"$\sin 60°$", r"$\frac{1}{2}$")

fig.tight_layout()
fig.savefig(__file__.replace(".py", ".svg"), transparent=True)
