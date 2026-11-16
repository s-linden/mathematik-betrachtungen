"""Abb. 2.2: Sinus und Cosinus als Gegen- und Ankathete im Einheitskreis.
Stil wie Abb. 2.1: Achsen hellgrau, Kreis gestrichelt, Linien schwarz.
Aufruf: python3 dreieck_ankathete_gegenkathete.py  ->  dreieck_ankathete_gegenkathete.svg"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 15, "svg.fonttype": "path"})
HELL, GRAU, DGRAU = "#BFBFBF", "#808080", "#404040"
phi = np.radians(35)
c, s = np.cos(phi), np.sin(phi)

fig, ax = plt.subplots(figsize=(6.2, 5.2))
ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-1.3, 1.85); ax.set_ylim(-1.3, 1.35)
ax.annotate("", xy=(1.3, 0), xytext=(-1.3, 0), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
ax.annotate("", xy=(0, 1.3), xytext=(0, -1.3), arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
ax.text(1.3, -0.08, "1", color=HELL, ha="center", va="top")
ax.text(-0.06, 1.3, "2", color=HELL, ha="right", va="top")
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), "k", lw=0.8, ls=(0, (4, 3)))
ax.text(-0.04, -0.04, r"$\mathcal{O}$", color=DGRAU, ha="right", va="top")

ax.plot([0, c], [0, s], "k", lw=1.0)            # Hypotenuse (Radius)
ax.plot([0, c], [0, 0], "k", lw=1.8)            # Ankathete
ax.plot([c, c], [0, s], "k", lw=1.8)            # Gegenkathete
q = 0.07
ax.plot([c - q, c - q, c], [0, q, q], "k", lw=0.6)
ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=np.degrees(phi), color=GRAU, lw=0.8))
ax.text(0.33 * np.cos(phi / 2), 0.33 * np.sin(phi / 2), r"$\varphi$", color=GRAU, ha="center", va="center")
ax.plot(c, s, "o", ms=5, mfc="white", mec="k")
ax.text(c + 0.05, s + 0.04, r"$P\,(\cos\varphi\,|\,\sin\varphi)$", ha="left", va="bottom", fontsize=13)
ax.text(0.5 * c - 0.08 * s, 0.5 * s + 0.08 * c, "$1$", ha="center", va="center")
ax.text(c / 2, -0.06, r"$\cos\varphi$", ha="center", va="top")
ax.text(c / 2, -0.22, "Ankathete", ha="center", va="top", fontsize=11, color=GRAU)
ax.text(c - 0.05, s / 2, r"$\sin\varphi$", ha="right", va="center")
ax.plot([c + 0.03, 1.08], [s / 2, s / 2], color=GRAU, lw=0.5)
ax.text(1.11, s / 2, "Gegenkathete", ha="left", va="center", fontsize=11, color=GRAU)
ax.text(0.5 * c - 0.08 * s - 0.05, 0.5 * s + 0.08 * c + 0.13, "Hypotenuse", ha="center", va="center",
        fontsize=11, color=GRAU, rotation=np.degrees(phi))
fig.tight_layout()
fig.savefig(__file__.replace(".py", ".svg"), transparent=True)
