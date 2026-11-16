"""Abb. 2.1 (winkel_einheitskreis.svg) und Abb. 2.2 (dreieck_ankathete_gegenkathete.svg).
Beide Bilder haben denselben Bildausschnitt und Maßstab, damit Koordinatensystem
und Einheitskreis in beiden Abbildungen genau gleich groß sind.
Stil: Achsen hellgrau, Kreis gestrichelt, Linien schwarz; Cosinus rot, Sinus blau.
Aufruf: python3 einheitskreis_abbildungen.py"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 15, "svg.fonttype": "path"})
HELL, GRAU, DGRAU = "#BFBFBF", "#808080", "#404040"
ROT, BLAU = "#C62828", "#1565C0"
PHI = np.radians(30)
C, S = np.cos(PHI), np.sin(PHI)
ORDNER = os.path.dirname(os.path.abspath(__file__))


def grundbild():
    """Gemeinsamer Rahmen: gleiche Bildgröße, gleicher Ausschnitt, Achsen, Kreis, Ursprung."""
    fig = plt.figure(figsize=(6.2, 5.2))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.3, 1.85); ax.set_ylim(-1.3, 1.35)
    ax.annotate("", xy=(1.3, 0), xytext=(-1.3, 0), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
    ax.annotate("", xy=(0, 1.3), xytext=(0, -1.3), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
    ax.text(1.3, -0.08, "1", color=HELL, ha="center", va="top")
    ax.text(-0.06, 1.3, "2", color=HELL, ha="right", va="top")
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), "k", lw=0.8, ls=(0, (4, 3)))
    ax.text(-0.04, -0.04, r"$\mathcal{O}$", color=DGRAU, ha="right", va="top")
    return fig, ax


def winkelbogen(ax, mit_pfeil):
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=np.degrees(PHI), color=GRAU, lw=0.8))
    if mit_pfeil:
        ende = np.array([0.25 * np.cos(PHI), 0.25 * np.sin(PHI)])
        ax.add_patch(FancyArrowPatch(ende + 0.03 * np.array([np.sin(PHI), -np.cos(PHI)]), ende,
                                     arrowstyle="->", mutation_scale=8, color=GRAU, lw=0.8))
    ax.text(0.36 * np.cos(PHI / 2), 0.36 * np.sin(PHI / 2), r"$\varphi$", color=GRAU, ha="center", va="center")


# Abb. 2.1: Der Winkel ist die Länge des Kreisbogens
fig, ax = grundbild()
ax.plot([0, C], [0, S], "k", lw=1.0)
ax.text(0.55 * C - 0.08 * S, 0.55 * S + 0.08 * C, "$r=1$", ha="center", va="center", rotation=np.degrees(PHI))
t = np.linspace(0, PHI, 60)
ax.plot(np.cos(t), np.sin(t), "k", lw=2.2)
ax.add_patch(FancyArrowPatch((np.cos(PHI - 0.05), np.sin(PHI - 0.05)), (C, S),
                             arrowstyle="->", mutation_scale=12, color="k", lw=2.2))
ax.text(1.1 * np.cos(PHI / 2), 1.1 * np.sin(PHI / 2), r"$\varphi$", ha="center", va="center")
winkelbogen(ax, mit_pfeil=True)
ax.plot(C, S, "o", ms=5, mfc="white", mec="k", zorder=5)
ax.plot(1, 0, "o", ms=5, mfc="k", mec="k", zorder=5)
fig.savefig(os.path.join(ORDNER, "winkel_einheitskreis.svg"), transparent=True)

# Abb. 2.2: Cosinus als Ankathete (rot), Sinus als Gegenkathete (blau)
fig, ax = grundbild()
ax.plot([0, C], [0, S], "k", lw=1.0)
ax.plot([0, C], [0, 0], color=ROT, lw=2.2)
ax.plot([C, C], [0, S], color=BLAU, lw=2.2)
q = 0.07
ax.plot([C - q, C - q, C], [0, q, q], "k", lw=0.6)
winkelbogen(ax, mit_pfeil=False)
ax.plot(C, S, "o", ms=5, mfc="white", mec="k", zorder=5)
ax.text(C + 0.05, S + 0.04, r"$P\,(\cos\varphi\,|\,\sin\varphi)$", ha="left", va="bottom", fontsize=13)
ax.text(0.5 * C - 0.08 * S, 0.5 * S + 0.08 * C, "$1$", ha="center", va="center")
ax.text(0.5 * C - 0.08 * S - 0.05, 0.5 * S + 0.08 * C + 0.13, "Hypotenuse", ha="center", va="center",
        fontsize=11, color=GRAU, rotation=np.degrees(PHI))
ax.text(C / 2, -0.06, r"$\cos\varphi$", ha="center", va="top", color=ROT)
ax.text(C / 2, -0.22, "Ankathete", ha="center", va="top", fontsize=11, color=ROT)
ax.text(C - 0.05, S / 2, r"$\sin\varphi$", ha="right", va="center", color=BLAU)
ax.plot([C + 0.03, 1.08], [S / 2, S / 2], color=BLAU, lw=0.5)
ax.text(1.11, S / 2, "Gegenkathete", ha="left", va="center", fontsize=11, color=BLAU)
fig.savefig(os.path.join(ORDNER, "dreieck_ankathete_gegenkathete.svg"), transparent=True)
