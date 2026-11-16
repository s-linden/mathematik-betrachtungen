# 2.4 Bestimmte Werte von Sinus und Cosinus

Für einige Winkel kann man die Werte von Sinus und Cosinus exakt angeben, ohne Taschenrechner. Es sind die Winkel $0$, $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$ und $\frac{\pi}{2}$, also $0°$, $30°$, $45°$, $60°$ und $90°$. In {numref}`Abb. %s <werte_sinus_cosinus>` sind die zugehörigen Werte auf den Graphen von Sinus und Cosinus markiert.

```{figure} pics/werte_sinus_cosinus.svg
---
width: 100%
name: werte_sinus_cosinus
---
Die Werte von Sinus (blau) und Cosinus (rot) bei $0$, $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$ und $\frac{\pi}{2}$
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

## Die Werte am Dreieck im Einheitskreis

Alle diese Werte lassen sich elementar am Einheitskreis herleiten. Wir benutzen dazu das Dreieck aus {numref}`Abb. %s <dreieck_ankathete_gegenkathete>`. Seine Hypotenuse ist die Radiuslinie mit der Länge $1$, die Ankathete hat die Länge $\cos\varphi$, die Gegenkathete die Länge $\sin\varphi$. Nach dem Satz des Pythagoras gilt deshalb für jeden Winkel

$$\sin^2\varphi+\cos^2\varphi=1.$$

```{figure} pics/dreiecke_einheitskreis.svg
---
width: 100%
name: dreiecke_einheitskreis
---
Die Dreiecke im Einheitskreis für $45°$, $30°$ (mit dem an der $1$-Achse gespiegelten Dreieck) und $60°$
(Quelle: eigene Darstellung; Lizenz: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0))
```

**$0°$ und $90°$.** Hier entsteht kein Dreieck. Bei $\varphi=0$ liegt der Punkt bei $(1|0)$, also ist $\cos 0°=1$ und $\sin 0°=0$. Bei $\varphi=\frac{\pi}{2}$ liegt er bei $(0|1)$, also ist $\cos 90°=0$ und $\sin 90°=1$.

**$45°$.** Die Winkelsumme im Dreieck ist $180°$. Neben dem rechten Winkel und dem Winkel $45°$ am Ursprung hat das Dreieck also noch einen Winkel von $45°$. Es ist gleichschenklig, die beiden Katheten sind gleich lang. Nennen wir ihre Länge $a$, dann gilt nach Pythagoras

$$a^2+a^2=1\quad\Leftrightarrow\quad a^2=\frac{1}{2}\quad\Leftrightarrow\quad a=\frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}.$$

Also ist $\sin 45°=\cos 45°=\frac{\sqrt{2}}{2}$.

**$30°$.** Wir spiegeln das Dreieck an der $1$-Achse. Zusammen bilden das Dreieck und sein Spiegelbild ein großes Dreieck mit den Ecken $\mathcal{O}$, $P$ und $P'$. Seine Seiten $\mathcal{O}P$ und $\mathcal{O}P'$ sind Radiuslinien und haben die Länge $1$. Der Winkel bei $\mathcal{O}$ ist $30°+30°=60°$, und weil das Dreieck gleichschenklig ist, sind auch die beiden anderen Winkel je $60°$ groß. Das große Dreieck ist also gleichseitig, auch die Seite $PP'$ hat die Länge $1$. Der Sinus ist genau die Hälfte davon:

$$\sin 30°=\frac{1}{2}.$$

Den Cosinus erhalten wir mit Pythagoras:

$$\cos 30°=\sqrt{1-\sin^2 30°}=\sqrt{1-\frac{1}{4}}=\sqrt{\frac{3}{4}}=\frac{\sqrt{3}}{2}.$$

**$60°$.** Im Dreieck für $30°$ ist der Winkel an der Ecke $P$ gleich $180°-90°-30°=60°$. Das Dreieck für $60°$ ist also dasselbe Dreieck, nur gekippt, sodass der $60°$-Winkel am Ursprung liegt. Dabei tauschen die beiden Katheten ihre Rollen:

$$\sin 60°=\cos 30°=\frac{\sqrt{3}}{2},\qquad \cos 60°=\sin 30°=\frac{1}{2}.$$

## Die Symmetrie der Werte

Dass die Cosinuswerte die Sinuswerte in umgekehrter Reihenfolge sind, ist kein Zufall. In {numref}`Abb. %s <werte_sinus_cosinus>` sieht man, dass der Graph des Cosinus der um $\frac{\pi}{2}$ nach links verschobene Graph des Sinus ist. Im ersten Viertel bedeutet das: Der Cosinus eines Winkels ist der Sinus des Winkels, der ihm zu $\frac{\pi}{2}$ fehlt,

$$\cos\varphi=\sin\left(\frac{\pi}{2}-\varphi\right).$$

Zum Beispiel ist $\cos\frac{\pi}{6}=\sin\left(\frac{\pi}{2}-\frac{\pi}{6}\right)=\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$. Bei $\frac{\pi}{4}$, genau in der Mitte, treffen sich die beiden Graphen, dort ist $\sin\frac{\pi}{4}=\cos\frac{\pi}{4}=\frac{\sqrt{2}}{2}$.

Mit denselben Werten kommt man auch in den anderen Vierteln des Einheitskreises aus. Am Graphen des Sinus sieht man zum Beispiel, dass er nach $\pi$ dieselben Werte mit umgekehrtem Vorzeichen annimmt:

$$\sin(\varphi+\pi)=-\sin\varphi.$$

So ist etwa

$$\sin\frac{7\pi}{6}=\sin\left(\pi+\frac{\pi}{6}\right)=-\sin\frac{\pi}{6}=-\frac{1}{2}.$$
