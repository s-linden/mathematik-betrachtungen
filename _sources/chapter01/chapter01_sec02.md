# 1.2 Tautologien und logische Äquivalenz

Manche Aussagenverbindungen haben immer den Wahrheitswert W, ganz gleich, welche Aussagen man für $p$, $q$, $r$, … einsetzt. Sie heißen **Tautologien**. Aussagenverbindungen, die immer den Wahrheitswert F haben, heißen **Kontradiktionen**. So ist $p\vee\neg p$ eine Tautologie, der *Satz vom ausgeschlossenen Dritten*. Die Verbindung $p\wedge\neg p$ ist eine Kontradiktion, der *Satz vom ausgeschlossenen Widerspruch*.

Zwei Aussagenverbindungen $a_1$ und $a_2$ heißen **logisch äquivalent**, wenn sie immer denselben Wahrheitswert haben, ganz gleich, welche Aussagen man einsetzt. Das ist genau dann der Fall, wenn die Äquivalenz $a_1\Leftrightarrow a_2$ eine Tautologie ist. Wenn wir im Folgenden $a_1\Leftrightarrow a_2$ schreiben, meinen wir damit, dass diese Äquivalenz immer gilt.

Die logische Äquivalenz hat folgende Eigenschaften:

1. $a\Leftrightarrow a$ (Reflexivität),
2. aus $a_1\Leftrightarrow a_2$ folgt $a_2\Leftrightarrow a_1$ (Symmetrie),
3. aus $a_1\Leftrightarrow a_2$ und $a_2\Leftrightarrow a_3$ folgt $a_1\Leftrightarrow a_3$ (Transitivität),
4. aus $a_1\Leftrightarrow a_2$ folgt $\neg a_1\Leftrightarrow\neg a_2$,
5. aus $a_1\Leftrightarrow a_2$ und $a_3\Leftrightarrow a_4$ folgt $(a_1\wedge a_3)\Leftrightarrow(a_2\wedge a_4)$, und genauso für $\vee$, $\Rightarrow$ und $\Leftrightarrow$.

Man darf also in einer Aussagenverbindung jeden Teil durch einen logisch äquivalenten Teil ersetzen, ohne dass sich der Wahrheitswert ändert. Genau so rechnet man auch mit Termen: Man ersetzt einen Term durch einen gleichwertigen.

Treten mehrere Verknüpfungszeichen auf, dann bindet $\neg$ am stärksten, danach $\wedge$ und $\vee$, und am schwächsten $\Rightarrow$ und $\Leftrightarrow$. Im Zweifel setzt man Klammern.

**Beispiele für Tautologien:**

$$(p\Rightarrow\neg p)\Rightarrow\neg p$$

$$\bigl(p\wedge(p\Rightarrow q)\bigr)\Rightarrow q$$ (modus-ponens)

$$(p\wedge q)\Rightarrow p,\qquad (p\wedge q)\Rightarrow q$$

$$p\Rightarrow(p\vee q),\qquad q\Rightarrow(p\vee q)$$

$$(p\Rightarrow q)\Rightarrow\bigl((q\Rightarrow r)\Rightarrow(p\Rightarrow r)\bigr)$$

$$\bigl((p\Rightarrow q)\wedge(q\Rightarrow r)\wedge p\bigr)\Rightarrow r$$

**Beispiele für logische Äquivalenzen:**

$$(p\wedge q)\Leftrightarrow(q\wedge p),\qquad (p\vee q)\Leftrightarrow(q\vee p)$$

$$\bigl(p\wedge(q\wedge r)\bigr)\Leftrightarrow\bigl((p\wedge q)\wedge r\bigr),\qquad \bigl(p\vee(q\vee r)\bigr)\Leftrightarrow\bigl((p\vee q)\vee r\bigr)$$

$$\bigl(p\wedge(q\vee r)\bigr)\Leftrightarrow\bigl((p\wedge q)\vee(p\wedge r)\bigr),\qquad \bigl(p\vee(q\wedge r)\bigr)\Leftrightarrow\bigl((p\vee q)\wedge(p\vee r)\bigr)$$

$$(p\Rightarrow q)\Leftrightarrow(\neg p\vee q)$$

$$(p\Rightarrow q)\Leftrightarrow(\neg q\Rightarrow\neg p)$$ (kontraposition)

$$\bigl((p\wedge\neg q)\Rightarrow(r\wedge\neg r)\bigr)\Leftrightarrow(p\Rightarrow q)$$ (widerspruchsbeweis)

$$(p\Leftrightarrow q)\Leftrightarrow\bigl((p\Rightarrow q)\wedge(q\Rightarrow p)\bigr)$$

$$(p\Leftrightarrow q)\Leftrightarrow\bigl((p\wedge q)\vee(\neg p\wedge\neg q)\bigr)$$

$$\neg(p\wedge q)\Leftrightarrow(\neg p\vee\neg q),\qquad \neg(p\vee q)\Leftrightarrow(\neg p\wedge\neg q)$$ (de-morgan)

$$\bigl((p\Rightarrow q)\wedge(r\Rightarrow q)\bigr)\Leftrightarrow\bigl((p\vee r)\Rightarrow q\bigr)$$

$$\bigl(p\vee(q\wedge\neg q)\bigr)\Leftrightarrow p$$

$$\bigl(p\wedge(q\vee\neg q)\bigr)\Leftrightarrow p$$

Einige dieser Formeln beschreiben Schlussweisen, die wir beim Beweisen ständig benutzen. Formel {eq}`modus-ponens` ist der *Modus ponens*: Ist $p$ wahr und folgt aus $p$ die Aussage $q$, dann ist auch $q$ wahr. Formel {eq}`kontraposition` ist der *Beweis durch Kontraposition*: Statt „aus $p$ folgt $q$“ zeigt man „aus nicht $q$ folgt nicht $p$“. Formel {eq}`widerspruchsbeweis` ist der *Widerspruchsbeweis*: Man nimmt $p$ und das Gegenteil von $q$ an und leitet daraus einen Widerspruch her. Die beiden Formeln {eq}`de-morgan` heißen die *Regeln von De Morgan*.

<br />

Dieser Abschnitt folgt in Inhalt und Aufbau M. Hasse: *Grundbegriffe der Mengenlehre und Logik*, Mathematische Schülerbücherei Nr. 2, B. G. Teubner, Leipzig 1966, Kapitel 1.
