# 1.1 Grundbegriffe der Aussagenlogik

## Aussagen

Unter einer **Aussage** verstehen wir einen Satz, der entweder wahr oder falsch ist. Eine Aussage hat also genau einen der beiden **Wahrheitswerte** „wahr“ (W) oder „falsch“ (F). Beispiele für Aussagen sind:

1. $13$ ist eine Primzahl.
2. $\sqrt{2}$ ist eine transzendente Zahl.
3. Für keine natürliche Zahl $n>2$ gibt es natürliche Zahlen $x$, $y$, $z$ mit $x^n+y^n=z^n$.

Die erste Aussage ist wahr, die zweite falsch. Auch die dritte Aussage, die Fermatsche Vermutung, hat einen Wahrheitswert. Über 350 Jahre lang kannte ihn niemand, erst 1995 hat Andrew Wiles bewiesen, dass sie wahr ist.

## Aussageformen und Quantoren

Eng verwandt mit der Aussage ist die **Aussageform**. Sie hat die Form eines Satzes, in dem eine oder mehrere Variablen vorkommen. Setzt man für die Variablen Objekte aus einer festgelegten Grundmenge $X$ ein, dann wird aus der Aussageform eine Aussage. Man schreibt dafür $a(x)$ und spricht von einer Aussageform über $X$.

So ist zum Beispiel „$x$ ist durch $3$ teilbar“ eine Aussageform über den ganzen Zahlen. Für $x=26$ wird daraus eine falsche Aussage, für $x=27$ eine wahre. Aussageformen über den reellen Zahlen sind etwa „$y=3x+5$“ oder „$(x+y)^2=x^2+2xy+y^2$“. Die erste liefert für $x=1$, $y=8$ eine wahre Aussage und für $x=1$, $y=9$ eine falsche. Die zweite liefert für jede Wahl von $x$ und $y$ eine wahre Aussage.

Man kann aus einer Aussageform auch dadurch eine Aussage machen, dass man ihre Variablen **quantifiziert**. Dazu stellt man eine der folgenden Wendungen voran:

* „Für alle $x$ gilt …“, in Zeichen $\forall x$ (**Allquantor**),
* „Es gibt ein $x$, für das gilt …“, in Zeichen $\exists x$ (**Existenzquantor**).

Die so entstehenden Aussagen heißen **Allaussagen** bzw. **Existenzaussagen**. Zum Beispiel ist „$\forall x\in\mathbb{R}:\ (x+1)^2=x^2+2x+1$“ eine wahre Allaussage und „$\exists x\in\mathbb{Z}:\ x$ ist durch $3$ teilbar“ eine wahre Existenzaussage.

## Aussagenverbindungen

Aus gegebenen Aussagen kann man neue Aussagen bilden. Dazu setzt man vor eine Aussage das Wort „nicht“ oder verknüpft zwei Aussagen mit „und“, „oder“, „wenn …, dann …“ oder „genau dann, wenn“. Das Ergebnis heißt **Aussagenverbindung**. Wir bezeichnen Aussagen mit den Buchstaben $p$, $q$, $r$, … und legen fest:

* Die **Negation** „nicht $p$“, in Zeichen $\neg p$, ist genau dann wahr, wenn $p$ falsch ist.
* Die **Konjunktion** „$p$ und $q$“, in Zeichen $p\wedge q$, ist genau dann wahr, wenn sowohl $p$ als auch $q$ wahr ist.
* Die **Disjunktion** „$p$ oder $q$“, in Zeichen $p\vee q$, ist genau dann falsch, wenn sowohl $p$ als auch $q$ falsch ist. Das „oder“ ist also nicht ausschließend gemeint, $p\vee q$ ist auch wahr, wenn beide Aussagen wahr sind.
* Die **Implikation** „wenn $p$, dann $q$“, in Zeichen $p\Rightarrow q$, ist genau dann falsch, wenn $p$ wahr und $q$ falsch ist.
* Die **Äquivalenz** „$p$ genau dann, wenn $q$“, in Zeichen $p\Leftrightarrow q$, ist genau dann wahr, wenn $p$ und $q$ denselben Wahrheitswert haben.

Wesentlich ist dabei: Der Wahrheitswert einer Aussagenverbindung hängt nur von den Wahrheitswerten der einzelnen Aussagen ab. Man kann die Festlegungen deshalb vollständig in einer **Wahrheitstafel** zusammenfassen:

| $p$ | $q$ | $\neg p$ | $p\wedge q$ | $p\vee q$ | $p\Rightarrow q$ | $p\Leftrightarrow q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| W | W | F | W | W | W | W |
| W | F | F | F | W | F | F |
| F | W | W | F | W | W | F |
| F | F | W | F | F | W | W |

Bemerkenswert ist die Implikation: Ist $p$ falsch, dann ist $p\Rightarrow q$ immer wahr, egal ob $q$ wahr oder falsch ist. Aus einer falschen Annahme kann man also alles folgern. Das ist ein weiterer Grund, warum man die Annahmen einer Schlusskette immer prüfen muss.

Genauso kann man Aussageformen verneinen und miteinander verknüpfen, wenn ihre Variablen aus derselben Grundmenge stammen.

<br />

Dieser Abschnitt folgt in Inhalt und Aufbau M. Hasse: *Grundbegriffe der Mengenlehre und Logik*, Mathematische Schülerbücherei Nr. 2, B. G. Teubner, Leipzig 1966, Kapitel 1.
