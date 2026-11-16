"""Abb. 1.3: Bestimmte Werte von Sinus und Cosinus (Stil wie Abb. 1.1/2.1:
schwarz, Sinus gestrichelt, Cosinus gepunktet, Achsen hellgrau).
Aufruf: python3 werte_sinus_cosinus.py  ->  werte_sinus_cosinus.svg"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "STIXGeneral", "mathtext.fontset": "stix",
                     "font.size": 13, "svg.fonttype": "path"})
HELL, GRAU = "#BFBFBF", "#808080"

fig, ax = plt.subplots(figsize=(9, 3.6))
x = np.linspace(0, 2 * np.pi + 0.3, 600)
ax.plot(x, np.sin(x), "k--", lw=1.1)
ax.plot(x, np.cos(x), "k:", lw=1.4)

# Achsen hellgrau mit Pfeil, ohne Rahmen
for s in ax.spines.values():
    s.set_visible(False)
ax.annotate("", xy=(2 * np.pi + 0.55, 0), xytext=(-0.4, 0),
            arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
ax.annotate("", xy=(0, 1.35), xytext=(0, -1.3),
            arrowprops=dict(arrowstyle="->", color=HELL, lw=1))
ax.text(2 * np.pi + 0.6, -0.12, r"$\varphi$", color=GRAU)
ax.text(0.08, 1.3, r"$f(\varphi)$", color=GRAU)
ax.set_xticks([]); ax.set_yticks([])

# Werte im ersten Viertel markieren
werte = [(np.pi / 6, r"$\frac{\pi}{6}$"), (np.pi / 4, r"$\frac{\pi}{4}$"),
         (np.pi / 3, r"$\frac{\pi}{3}$"), (np.pi / 2, r"$\frac{\pi}{2}$")]
for w, lab in werte:
    ax.plot([w, w], [0, max(np.sin(w), np.cos(w))], color=GRAU, lw=0.6, ls=(0, (1, 2)))
    ax.plot(w, np.sin(w), "o", ms=5, mfc="k", mec="k")
    ax.plot(w, np.cos(w), "o", ms=5, mfc="white", mec="k")
ax.plot(0, 0, "o", ms=5, mfc="k", mec="k")
ax.plot(0, 1, "o", ms=5, mfc="white", mec="k")
# Beschriftung der Winkel unter der Achse (leicht versetzt, damit nichts überlappt)
for w, lab in werte:
    ax.text(w, -0.15, lab, ha="center", va="top", fontsize=19)
for w, lab in [(np.pi, r"$\pi$"), (3 * np.pi / 2, r"$\frac{3\pi}{2}$"), (2 * np.pi, r"$2\pi$")]:
    ax.plot([w, w], [-0.04, 0.04], color=GRAU, lw=1)
    ax.text(w, -0.2 if w != 3 * np.pi / 2 else 0.12, lab, ha="center",
            va="top" if w != 3 * np.pi / 2 else "bottom", fontsize=17)
# Hochachse: 1 und -1
for y, lab in [(1, "$1$"), (-1, "$-1$")]:
    ax.plot([-0.04, 0.04], [y, y], color=GRAU, lw=1)
    ax.text(-0.15, y, lab, ha="right", va="center")
# Legende direkt an den Kurven
ax.annotate(r"$\sin\varphi$", xy=(2.3, np.sin(2.3)), xytext=(2.55, 1.12),
            arrowprops=dict(arrowstyle="-", lw=0.7))
ax.annotate(r"$\cos\varphi$", xy=(5.5, np.cos(5.5)), xytext=(5.0, 1.12),
            arrowprops=dict(arrowstyle="-", lw=0.7))

ax.set_xlim(-0.6, 2 * np.pi + 0.9); ax.set_ylim(-1.35, 1.45)
fig.tight_layout()
fig.savefig(__file__.replace(".py", ".svg"), transparent=True)
