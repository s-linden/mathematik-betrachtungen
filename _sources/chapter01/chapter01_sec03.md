# 1.3 Bestimmte Werte von Sinus und Cosinus

Für einige Winkel kann man die Werte von Sinus und Cosinus exakt angeben, ohne Taschenrechner. Es sind die Winkel $0$, $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$ und $\frac{\pi}{2}$, also $0°$, $30°$, $45°$, $60°$ und $90°$. In {numref}`Abb. %s <werte_sinus_cosinus>` sind die zugehörigen Werte auf den Graphen von Sinus und Cosinus markiert.

```{figure} pics/werte_sinus_cosinus.svg
---
width: 100%
name: werte_sinus_cosinus
---
Die Werte von Sinus (gestrichelt, gefüllte Punkte) und Cosinus (gepunktet, offene Punkte) bei $0$, $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$ und $\frac{\pi}{2}$
(Quelle: eigene Darstellung; Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

Für sich genommen sehen diese Werte wenig geordnet aus: $0$, $\frac{1}{2}$, $\frac{1}{2}\sqrt{2}$, $\frac{1}{2}\sqrt{3}$ und $1$. Schreiben wir sie aber alle in der Form $\frac{\sqrt{n}}{2}$, dann zeigt sich eine bemerkenswerte Symmetrie. Es ist nämlich $0=\frac{\sqrt{0}}{2}$, $\frac{1}{2}=\frac{\sqrt{1}}{2}$ und $1=\frac{\sqrt{4}}{2}$:

| Winkel in Grad | Winkel $\varphi$ | $\sin\varphi$ | $\cos\varphi$ |
|:-:|:-:|:-:|:-:|
| $0°$ | $0$ | $\frac{\sqrt{0}}{2}=0$ | $\frac{\sqrt{4}}{2}=1$ |
| $30°$ | $\frac{\pi}{6}$ | $\frac{\sqrt{1}}{2}=\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ |
| $45°$ | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| $60°$ | $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{1}}{2}=\frac{1}{2}$ |
| $90°$ | $\frac{\pi}{2}$ | $\frac{\sqrt{4}}{2}=1$ | $\frac{\sqrt{0}}{2}=0$ |

Die Werte des Sinus steigen von $\frac{\sqrt{0}}{2}$ bis $\frac{\sqrt{4}}{2}$, unter der Wurzel steht der Reihe nach $0$, $1$, $2$, $3$, $4$. Die Werte des Cosinus durchlaufen genau dieselben Zahlen, nur andersherum, von $\frac{\sqrt{4}}{2}$ bis $\frac{\sqrt{0}}{2}$. Wer sich diese Reihe merkt, hat alle zehn Werte im Kopf.

Dass die Cosinuswerte die Sinuswerte in umgekehrter Reihenfolge sind, ist kein Zufall. In {numref}`Abb. %s <werte_sinus_cosinus>` sieht man, dass der Graph des Cosinus der um $\frac{\pi}{2}$ nach links verschobene Graph des Sinus ist. Im ersten Viertel bedeutet das: Der Cosinus eines Winkels ist der Sinus des Winkels, der ihm zu $\frac{\pi}{2}$ fehlt,

$$\cos\varphi=\sin\left(\frac{\pi}{2}-\varphi\right).$$

Zum Beispiel ist $\cos\frac{\pi}{6}=\sin\left(\frac{\pi}{2}-\frac{\pi}{6}\right)=\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$. Bei $\frac{\pi}{4}$, genau in der Mitte, treffen sich die beiden Graphen, dort ist $\sin\frac{\pi}{4}=\cos\frac{\pi}{4}=\frac{\sqrt{2}}{2}$.

Mit denselben Werten kommt man auch in den anderen Vierteln des Einheitskreises aus. Am Graphen des Sinus sieht man zum Beispiel, dass er nach $\pi$ dieselben Werte mit umgekehrtem Vorzeichen annimmt:

$$\sin(\varphi+\pi)=-\sin\varphi.$$

So ist etwa

$$\sin\frac{7\pi}{6}=\sin\left(\pi+\frac{\pi}{6}\right)=-\sin\frac{\pi}{6}=-\frac{1}{2}.$$
