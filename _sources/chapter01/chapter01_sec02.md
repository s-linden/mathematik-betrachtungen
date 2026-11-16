# 1.2 Schlussrichtung, hinreichende und notwendige Bedingung

Eine Folgerung hat eine Richtung. Der Pfeil in $p\Rightarrow q$ zeigt an, in welche Richtung wir schließen (folgern) dürfen: von links nach rechts, von $p$ auf $q$. Nehmen wir als Beispiel die Folgerung „Wer ein Mensch ist, ist sterblich“. Sie gilt für jedes Lebewesen, also auch für mich, mit den beiden Aussagen

* $p$: „Ich bin ein Mensch.“
* $q$: „Ich bin sterblich.“

Die Folgerung $p\Rightarrow q$ ist richtig: Ich bin ein Mensch, also bin ich sterblich. Die umgekehrte Schlussrichtung, von rechts nach links, gilt aber nicht. Nur weil ich sterblich bin, bin ich noch lange kein Mensch, auch eine Katze oder ein Baum ist sterblich. Will man ausdrücklich von rechts nach links schließen, schreibt man den Pfeil andersherum, $q\Leftarrow p$ bedeutet dasselbe wie $p\Rightarrow q$.

Für die beiden Seiten einer Folgerung $p\Rightarrow q$ gibt es feste Namen:

* $p$ ist eine **hinreichende Bedingung** für $q$. Es reicht zu wissen, dass $p$ gilt, dann wissen wir auch, dass $q$ gilt. Mensch sein reicht aus, um sterblich zu sein.
* $q$ ist eine **notwendige Bedingung** für $p$. Ohne $q$ kein $p$: Wer nicht sterblich ist, kann kein Mensch sein. Sterblich sein ist notwendig, um ein Mensch zu sein, aber es reicht nicht aus.

Dass $q$ notwendig für $p$ ist, kann man also auch als $\neg q\Rightarrow\neg p$ schreiben. Sie sagt dasselbe wie $p\Rightarrow q$, nur von der anderen Seite her. Darauf beruht der *Beweis durch Kontraposition*: Statt „aus $p$ folgt $q$“ zeigt man „aus nicht $q$ folgt nicht $p$“.

Eine notwendige Bedingung ist so etwas wie ein **Verdachtsfall**. Ist sie erfüllt, dann *könnte* $p$ vorliegen, und es lohnt sich, genauer hinzusehen. Ob $p$ wirklich vorliegt, ist damit aber noch nicht entschieden. Ist die notwendige Bedingung dagegen nicht erfüllt, dann ist die Sache klar: $p$ liegt sicher nicht vor.

In der Mathematik begegnet uns das ständig. Hat eine differenzierbare Funktion $f$ an der Stelle $x_0$ ein Maximum oder Minimum, dann ist dort $f'(x_0)=0$:

$$x_0 \text{ ist Extremstelle von } f \quad\Rightarrow\quad f'(x_0)=0.$$

Die Bedingung $f'(x_0)=0$ ist notwendig, aber nicht hinreichend. Bei $f(x)=x^3$ ist $f'(0)=0$, trotzdem hat $f$ bei $0$ weder ein Maximum noch ein Minimum. Die Nullstellen von $f'$ sind also genau die Verdachtsfälle: Nur dort *kann* ein Extremum liegen, und jede dieser Stellen muss man anschließend einzeln prüfen.

## Äquivalenz

Manchmal gilt eine Folgerung in beide Richtungen, von links nach rechts und von rechts nach links. Dann ist $p$ zugleich hinreichend und notwendig für $q$. Eine solche Folgerung in beide Richtungen heißt **Äquivalenz**. Man schreibt dafür $p\Leftrightarrow q$ und sagt „$p$ genau dann, wenn $q$“:

$$p\Leftrightarrow q \quad\text{bedeutet}\quad p\Rightarrow q \ \text{ und } \ p\Leftarrow q.$$

Beispiel: „Für alle ganzen Zahlen $x$ gilt: $x$ ist gerade genau dann, wenn $x^2$ gerade ist.“ Ist $x$ gerade, dann ist auch $x^2$ gerade. Und umgekehrt: Ist $x^2$ gerade, dann muss auch $x$ gerade sein, denn das Quadrat einer ungeraden Zahl ist ungerade. Man darf also in beide Richtungen schließen.

Dagegen ist „Für alle ganzen Zahlen $x$ gilt: $x$ ist durch $4$ teilbar genau dann, wenn $x$ gerade ist“ falsch. Die Folgerung von links nach rechts gilt, die von rechts nach links nicht: $6$ ist gerade, aber nicht durch $4$ teilbar.
