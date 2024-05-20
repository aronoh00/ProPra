# Shell-Grundlagen2

F1: Weil der error stream unabhängig vom output stream ist und standardmäßig zum Terminal führt. (man stdin)
F2: grep partner_ student.yaml diesedatiegibtesnicht > /tmp/out 2> /tmp/err
F3: Es stehen immernoch zwei Zeilen im Output, aber es sind neue Zeilen, da die alten Überschrieben werden. Den gesamten Output kann man bekommen wenn noch ein weiteres > hinzugefügt wird
F4: && wird verwendet um zwei Befehle nacheinander auszuführen
F5: bei && muss der erste Befehl erfolgreich abgeschlossen sein, damit der zweite ausgeführt wird. Bei ; nicht
F6: Die Klammern bedueten, dass der Befehl in einer Untershell ausgeführt wird
F7: Sie befinden sich noch im ursprünglichen Verzeichnis, da der Befehl in einer Subshell ausgeführt wurde. Wenn die Klammern nicht gesetzt werden müsste man im anschluss wieder in das ursprüngliche Verzeichnis wechseln
F8: mit jobs -r können Hintergrundprozesse angezeigt werden
F9: mit kill -s STOP pid können Prozesse gestoppt werden