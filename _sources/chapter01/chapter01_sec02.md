# 1.2 Schlussrichtung, hinreichende und notwendige Bedingung

Eine Implikation hat eine Richtung. Der Pfeil in $p\Rightarrow q$ zeigt an, in welche Richtung wir schließen dürfen: von links nach rechts, von $p$ auf $q$. Nehmen wir als Beispiel die beiden Aussagen

* $p$: „Ich bin ein Mensch.“
* $q$: „Ich bin sterblich.“

Die Implikation $p\Rightarrow q$ ist wahr: Ich bin ein Mensch, also bin ich sterblich. Die umgekehrte Schlussrichtung, von rechts nach links, gilt aber nicht. Nur weil ich sterblich bin, bin ich noch lange kein Mensch, auch eine Katze oder ein Baum ist sterblich. Will man ausdrücklich von rechts nach links schließen, schreibt man den Pfeil andersherum, $q\Leftarrow p$ bedeutet dasselbe wie $p\Rightarrow q$.

Für die beiden Seiten einer wahren Implikation $p\Rightarrow q$ gibt es feste Namen:

* $p$ ist eine **hinreichende Bedingung** für $q$. Es reicht zu wissen, dass $p$ gilt, dann wissen wir auch, dass $q$ gilt. Mensch sein reicht aus, um sterblich zu sein.
* $q$ ist eine **notwendige Bedingung** für $p$. Ohne $q$ kein $p$: Wer nicht sterblich ist, kann kein Mensch sein. Sterblich sein ist notwendig, um ein Mensch zu sein, aber es reicht nicht aus.

Dass $q$ notwendig für $p$ ist, kann man also auch als $\neg q\Rightarrow\neg p$ schreiben. Sie sagt dasselbe wie $p\Rightarrow q$, nur von der anderen Seite her. Darauf beruht der *Beweis durch Kontraposition*: Statt „aus $p$ folgt $q$“ zeigt man „aus nicht $q$ folgt nicht $p$“.

Eine notwendige Bedingung ist so etwas wie ein **Verdachtsfall**. Ist sie erfüllt, dann *könnte* $p$ vorliegen, und es lohnt sich, genauer hinzusehen. Ob $p$ wirklich vorliegt, ist damit aber noch nicht entschieden. Ist die notwendige Bedingung dagegen nicht erfüllt, dann ist die Sache klar: $p$ liegt sicher nicht vor.

In der Mathematik begegnet uns das ständig. Hat eine differenzierbare Funktion $f$ an der Stelle $x_0$ ein Maximum oder Minimum, dann ist dort $f'(x_0)=0$:

$$x_0 \text{ ist Extremstelle von } f \quad\Rightarrow\quad f'(x_0)=0.$$

Die Bedingung $f'(x_0)=0$ ist notwendig, aber nicht hinreichend. Bei $f(x)=x^3$ ist $f'(0)=0$, trotzdem hat $f$ bei $0$ weder ein Maximum noch ein Minimum. Die Nullstellen von $f'$ sind also genau die Verdachtsfälle: Nur dort *kann* ein Extremum liegen, und jede dieser Stellen muss man anschließend einzeln prüfen.

Damit können wir die **Äquivalenz** als einen logischen Schluss verstehen, der in beide Richtungen richtig ist: von links nach rechts, $p\Rightarrow q$, und von rechts nach links, $p\Leftarrow q$. Dann ist $p$ zugleich hinreichend und notwendig für $q$:

$$p\Leftrightarrow q \quad\text{bedeutet}\quad p\Rightarrow q \ \text{ und } \ p\Leftarrow q.$$

Man sagt dann „$p$ genau dann, wenn $q$“. Ein Beispiel ist „Eine ganze Zahl ist gerade genau dann, wenn sie durch $2$ teilbar ist.“ Hier darf man in beide Richtungen schließen.
