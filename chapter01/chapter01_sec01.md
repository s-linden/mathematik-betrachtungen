# 1.1 Grundbegriffe der Aussagenlogik

## Aussagen

Unter einer **Aussage** verstehen wir einen Satz, der entweder wahr oder falsch ist. Eine Aussage hat also genau einen der beiden **Wahrheitswerte** „wahr“ (W) oder „falsch“ (F). Beispiele für Aussagen sind:

1. $13$ ist eine Primzahl.
2. $\sqrt{2}$ ist eine transzendente Zahl.
3. Für keine natürliche Zahl $n>2$ gibt es natürliche Zahlen $x$, $y$, $z$ mit $x^n+y^n=z^n$.

Die erste Aussage ist wahr, die zweite falsch. Auch die dritte Aussage, die Fermatsche Vermutung, hat einen Wahrheitswert. Über 350 Jahre lang kannte ihn niemand, erst 1995 hat Andrew Wiles bewiesen, dass sie wahr ist.

## Aussageformen und Quantoren

Eng verwandt mit der Aussage ist die **Aussageform**. Sie hat die Form eines Satzes, in dem eine oder mehrere Variablen vorkommen. Setzt man für die Variablen Objekte aus einer festgelegten Grundmenge $X$ ein, dann wird aus der Aussageform eine Aussage. Man spricht von einer Aussageform über $X$.

So ist zum Beispiel „$x$ ist durch $3$ teilbar“ eine Aussageform über den ganzen Zahlen. Für $x=26$ wird daraus eine falsche Aussage, für $x=27$ eine wahre. Aussageformen über den reellen Zahlen sind etwa „$y=3x+5$“ oder „$(x+y)^2=x^2+2xy+y^2$“. Die erste liefert für $x=1$, $y=8$ eine wahre Aussage und für $x=1$, $y=9$ eine falsche. Die zweite liefert für jede Wahl von $x$ und $y$ eine wahre Aussage.

Man kann aus einer Aussageform auch dadurch eine Aussage machen, dass man ihre Variablen **quantifiziert**. Dazu stellt man eine der folgenden Wendungen voran:

* „Für alle $x$ gilt …“, in Zeichen $\forall x$ (**Allquantor**),
* „Es gibt ein $x$, für das gilt …“, in Zeichen $\exists x$ (**Existenzquantor**).

Die so entstehenden Aussagen heißen **Allaussagen** bzw. **Existenzaussagen**. Zum Beispiel ist „$\forall x\in\mathbb{R}:\ (x+1)^2=x^2+2x+1$“ eine wahre Allaussage und „$\exists x\in\mathbb{Z}:\ x$ ist durch $3$ teilbar“ eine wahre Existenzaussage.

## Aussagenverbindungen

Aus gegebenen Aussagen kann man neue Aussagen bilden. Dazu setzt man vor eine Aussage das Wort „nicht“ oder verknüpft zwei Aussagen mit „und“, „oder“, „wenn …, dann …“ oder „genau dann, wenn“. Das Ergebnis heißt **Aussagenverbindung**. Wir bezeichnen Aussagen mit den Buchstaben $p$, $q$, $r$, … und legen fest:

* Die **Negation** „nicht $p$“, in Zeichen $\neg p$, ist genau dann wahr, wenn $p$ falsch ist.

  Beispiel: Die Aussage „$2+2=4$“ ist wahr. Ihre Negation „$2+2\neq 4$“ ist falsch.

* Die **Konjunktion** „$p$ und $q$“, in Zeichen $p\wedge q$, ist genau dann wahr, wenn sowohl $p$ als auch $q$ wahr ist.

  Beispiel: „$2+2=4$ und $3$ ist eine gerade Zahl“ ist falsch, denn die zweite Aussage ist falsch.

* Die **Disjunktion** „$p$ oder $q$“, in Zeichen $p\vee q$, ist genau dann falsch, wenn sowohl $p$ als auch $q$ falsch ist. Das „oder“ ist also nicht ausschließend gemeint, $p\vee q$ ist auch wahr, wenn beide Aussagen wahr sind.

  Beispiel: „$2+2=4$ oder $3$ ist eine gerade Zahl“ ist wahr, denn die erste Aussage ist wahr.

* Die **Implikation** „wenn $p$, dann $q$“, in Zeichen $p\Rightarrow q$, ist genau dann falsch, wenn $p$ wahr und $q$ falsch ist.

  Beispiel: „Für alle ganzen Zahlen $x$ gilt: Wenn $x$ durch $4$ teilbar ist, dann ist $x$ gerade.“ Diese Aussage ist wahr.

* Die **Äquivalenz** „$p$ genau dann, wenn $q$“, in Zeichen $p\Leftrightarrow q$, ist genau dann wahr, wenn $p$ und $q$ denselben Wahrheitswert haben.

  Beispiel: „Für alle ganzen Zahlen $x$ gilt: $x$ ist gerade genau dann, wenn $x^2$ gerade ist.“ Diese Aussage ist wahr, man darf hier in beide Richtungen schließen.


Wesentlich ist dabei: Der Wahrheitswert einer Aussagenverbindung hängt nur von den Wahrheitswerten der einzelnen Aussagen ab. Man kann die Festlegungen deshalb vollständig in einer **Wahrheitstafel** zusammenfassen:

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p\wedge q$ | $p\vee q$ | $p\Rightarrow q$ | $p\Leftrightarrow q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| W | W | F | F | W | W | W | W |
| W | F | F | W | F | W | F | F |
| F | W | W | F | F | W | W | F |
| F | F | W | W | F | F | W | W |

So liest man eine Wahrheitstafel: Die ersten beiden Spalten legen fest, welche Wahrheitswerte $p$ und $q$ haben. Jede Zeile ist ein möglicher Fall, und weil jede der beiden Aussagen wahr oder falsch sein kann, gibt es genau vier Fälle. In den übrigen Spalten steht, welchen Wahrheitswert die jeweilige Aussagenverbindung in diesem Fall hat.

In der dritten Zeile wird zum Beispiel angenommen, dass $p$ falsch ist (F) und $q$ wahr (W). Wenn $p$ falsch ist, dann ist $\neg p$ wahr (W). Weil $q$ wahr ist, ist $\neg q$ aber falsch (F). $p\wedge q$ kann nicht wahr sein, da ja $p$ falsch ist. $p\vee q$ wiederum ist wahr, denn eine der beiden Aussagen ist ja wahr, nämlich $q$.

Bemerkenswert ist die Implikation: Ist $p$ falsch, dann ist $p\Rightarrow q$ immer wahr, egal ob $q$ wahr oder falsch ist. Aus einer falschen Annahme kann man also alles folgern. Das ist ein weiterer Grund, warum man die Annahmen einer Schlusskette immer prüfen muss.

## Implikation und Folgerung

Die Wahrheitstafel prüft nur Wahrheitswerte, nicht den Inhalt. Nach der Tafel ist zum Beispiel „Wenn $2+2=4$, dann ist $3$ eine ungerade Zahl“ eine wahre Aussage, denn beide Teilaussagen sind wahr. Trotzdem kann man aus $2+2=4$ nicht folgern, dass $3$ ungerade ist. Die beiden Aussagen haben nichts miteinander zu tun. Wenn wir in der Mathematik sagen „aus $p$ folgt $q$“, dann meinen wir mehr: Wir meinen eine Implikation zwischen Aussageformen, die für *alle* Werte der Variablen wahr ist, wie im Beispiel oben: „Für alle ganzen Zahlen $x$ gilt: Wenn $x$ durch $4$ teilbar ist, dann ist $x$ gerade.“ Weil die Implikation für jedes $x$ gelten muss, braucht es einen echten Zusammenhang zwischen den beiden Teilen. Ersetzt man „gerade“ durch „ungerade“, findet man sofort ein Gegenbeispiel, etwa $x=8$.

```{admonition} Merke: Eine Implikation ist noch keine Folgerung
:class: note
Die **Implikation** $p\Rightarrow q$ ist eine Aussagenverbindung. Ihr Wahrheitswert ergibt sich allein aus den Wahrheitswerten von $p$ und $q$, ein inhaltlicher Zusammenhang wird nicht verlangt.

Eine **Folgerung** „aus $p$ folgt $q$“ ist mehr: Die Implikation muss für alle Werte der Variablen gelten, ohne ein einziges Gegenbeispiel. Erst dann darf man von $p$ auf $q$ schließen.

In der Mathematik schreibt man für beides denselben Pfeil $\Rightarrow$.

**Wenn wir im Folgenden von Schlüssen sprechen, meinen wir immer Folgerungen.**
```

<br />

Dieser Abschnitt folgt in Inhalt und Aufbau M. Hasse: *Grundbegriffe der Mengenlehre und Logik*, Mathematische Schülerbücherei Nr. 2, B. G. Teubner, Leipzig 1966, Kapitel 1.
