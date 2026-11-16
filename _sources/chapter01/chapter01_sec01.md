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

## Schlussrichtung, hinreichende und notwendige Bedingung

Eine Implikation hat eine Richtung. Der Pfeil in $p\Rightarrow q$ zeigt an, in welche Richtung wir schließen dürfen: von links nach rechts, von $p$ auf $q$. Nehmen wir als Beispiel die beiden Aussagen

* $p$: „Ich bin ein Mensch.“
* $q$: „Ich bin sterblich.“

Die Implikation $p\Rightarrow q$ ist wahr: Ich bin ein Mensch, also bin ich sterblich. Die umgekehrte Schlussrichtung, von rechts nach links, gilt aber nicht. Nur weil ich sterblich bin, bin ich noch lange kein Mensch, auch eine Katze oder ein Baum ist sterblich. Will man ausdrücklich von rechts nach links schließen, schreibt man den Pfeil andersherum, $q\Leftarrow p$ bedeutet dasselbe wie $p\Rightarrow q$.

Für die beiden Seiten einer wahren Implikation $p\Rightarrow q$ gibt es feste Namen:

* $p$ ist eine **hinreichende Bedingung** für $q$. Es reicht zu wissen, dass $p$ gilt, dann wissen wir auch, dass $q$ gilt. Mensch sein reicht aus, um sterblich zu sein.
* $q$ ist eine **notwendige Bedingung** für $p$. Ohne $q$ kein $p$: Wer nicht sterblich ist, kann kein Mensch sein. Sterblich sein ist notwendig, um ein Mensch zu sein, aber es reicht nicht aus.

Dass $q$ notwendig für $p$ ist, kann man also auch als $\neg q\Rightarrow\neg p$ schreiben. Diese Aussage ist logisch äquivalent zu $p\Rightarrow q$, das zeigen wir in Abschnitt 1.2.

Eine notwendige Bedingung ist so etwas wie ein **Verdachtsfall**. Ist sie erfüllt, dann *könnte* $p$ vorliegen, und es lohnt sich, genauer hinzusehen. Ob $p$ wirklich vorliegt, ist damit aber noch nicht entschieden. Ist die notwendige Bedingung dagegen nicht erfüllt, dann ist die Sache klar: $p$ liegt sicher nicht vor.

In der Mathematik begegnet uns das ständig. Hat eine differenzierbare Funktion $f$ an der Stelle $x_0$ ein Maximum oder Minimum, dann ist dort $f'(x_0)=0$:

$$x_0 \text{ ist Extremstelle von } f \quad\Rightarrow\quad f'(x_0)=0.$$

Die Bedingung $f'(x_0)=0$ ist notwendig, aber nicht hinreichend. Bei $f(x)=x^3$ ist $f'(0)=0$, trotzdem hat $f$ bei $0$ weder ein Maximum noch ein Minimum. Die Nullstellen von $f'$ sind also genau die Verdachtsfälle: Nur dort *kann* ein Extremum liegen, und jede dieser Stellen muss man anschließend einzeln prüfen.

Damit können wir die **Äquivalenz** als einen logischen Schluss verstehen, der in beide Richtungen richtig ist: von links nach rechts, $p\Rightarrow q$, und von rechts nach links, $p\Leftarrow q$. Dann ist $p$ zugleich hinreichend und notwendig für $q$:

$$p\Leftrightarrow q \quad\text{bedeutet}\quad p\Rightarrow q \ \text{ und } \ p\Leftarrow q.$$

Man sagt dann „$p$ genau dann, wenn $q$“. Ein Beispiel ist „Eine ganze Zahl ist gerade genau dann, wenn sie durch $2$ teilbar ist.“ Hier darf man in beide Richtungen schließen.

<br />

Dieser Abschnitt folgt in Inhalt und Aufbau M. Hasse: *Grundbegriffe der Mengenlehre und Logik*, Mathematische Schülerbücherei Nr. 2, B. G. Teubner, Leipzig 1966, Kapitel 1.
