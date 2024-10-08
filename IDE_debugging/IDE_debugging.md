# IDE_debugging

F1: Zuerst müssen wir in die Debuggingansicht, indem wir in der Spalte auf der linken Seite auf das Symbol mit dem Käfer klicken (oder str + Umschlat + d). Anschließend müssen wir eine Konfigurationsdatei erstellen

---

F2: Ein Breakpoint signalisiert dem Debugger, dass der Code bis zu diesem Punkt ausgeführt wird. In VS Code kann man einen Brackpoint setzten, indem man die Zeile links neben der Zeilennummer anklickt. Wir können ein Log Message ausgeben lassen, wenn wir ihn erreichen oder einen Hit Count einfügen.

---

F3: Wir können mit der rechten Maustaste den Breakpoint editieren und eine Bedingung festlegen, sodass er nur unter dieser Bedingung aktiviert wrid.

---

F4: Im Grunde sind es ähnliche Funktionen wie in pdb (continue, step over, step into, step out und breakpoints)

1. step into (F11) bewirkt, dass wir in eine Funktion oder Methode hinein gehen und sie uns genauer anschauen können
2. step out (Umschlt + F11) bewirkt, dass wir aus der Funktion oder Methode hinaus gehen
3. step over (F10) bewirkt, dass wir zur nächsten Codezeile springen
4. Breakpoints können wir auch während des debuggens so setzen wie oben beschrieben
5. continue (F5) bewirkt das wir das Programm solange ausführen, bis wir zu einem Breakpoint kommen

---

F5: Ich finde es im Vergleich zu pdb gut, dass man einen besseren Überblick (list wie in pbd ist nicht notwendig, da wir im Code direkt sehen, wo wir uns befinden) hat. Außerdem ist es leichter Breakpoints zu setzen und man kann während des Debuggens den Code verändern.
