# Fehler-Defekt-Versagen

F1: Nicht jeder Defekt ist auf eine falsche Programmierung zurückzuführen. Ein Defekt kann auch durch Umgebung auftreten in der das Programm ausgeführt wird. Zum Beispiel durch Hardware, Nertzwerkfehler oder Benutzerfehler. Man kann allerdings dann auch argumentieren, dass das beim erstellen des Programmes mit berücksichtigt werden muss, aber man kann auch nicht jedes Deteil als Anforderung formulieren.

---

F2: Unrealistisch, denn mit steigender Komplexität erhöht sich die Wahrscheinlichkeit, dass der Programmierer einen Fehler begeht, der zu einem Defekt führt.

---

F3: Bei einem komplexen Programm kann ein Fehler sich in einem Programmabschnitt verbergen, der weitgehend ungenutzt ist und daher in den meisten Fällen der Programmausführung unbemerkt bleibt. Somit kann das Programm in den meisten Fällen korrekte Ausgaben liefern, obwohl es einen Defekt gibt.

---

F4: Es könnte sein, dass die Anwendung nicht optimiert ist und sehr viel Arbeitsspeicher benötigt. Wenn dem einen System mehr zur Verfügung steht, kann es sein, dass die Anwendung auf dem funktioniert, aber auf dem anderen nicht. Außerdem gibt es zwischen Windows und Linux Unterschiede im Dateisystem und Unterschiede im Threading. [Quelle](https://www.ostc.de/windows.html)

---

F5: Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen für 24 Stunden

- möglich zu überprüfen, aber dauert zu lange
- Änderung: Das System sperrt das Konto nach drei aufeinanderfolgenden fehlgeschlagenen Anmeldeversuchen für eine bestimmte Zeit
- für Testzwecke eine kurze Zeitspanne festlegen

---

F6:

1. Versagen: Ein Nutzer soll sich nur mit einer gültigen E-Mail-Adresse anmelden können und nicht mit seinem Benutzernamen.

2. Versagen: Anmeldung erfolgt mit E-Mail-Adresse und nicht mit Benutzername, ungültiges Passwort ist hier zweitrangig, da hier bereits ein Versagen vorliegt.

3. Kein Versagen.

4. Versagen, wenn es sich bei dem Nutzer nicht um den Portal-Administrator handelt

5. Wahrscheinlich ein Versagen: lange Wartezeit ist zwar theoretisch akzeptiertes Verhalten, da sie nicht in den Kriterien spezifiziert wurde,  ist aber eigentlich inakzeptabel.

---

F7: Das System zeigt eine Fehlermeldung, wenn der Anmeldeprozess 30 Sekunden überschreitet.

---

F8: Zu Punkt 4.

Guter Bericht:

- Beschreibung: Ein Benutzer mit gültigen Anmeldedaten wird bei der Anmeldung fälschlicherweise auf Portal des Administrators geleitet, obwohl dieser kein Administrator ist.
- Betriebssystem: Windwos 11 Pro Version 23H2
- Schritte zum Reproduzieren
  - Gehe zu Loginseite
  - Gebe eine gültige E-Mail-Adresse mit einem gültigen Passwort ein
  - Klicke auf Anmelden
- Tatsächliches Ergebnis: Der Nutzer wird auf das Portal des Administrators geleitet
- Erwartets Ergebnis: Der Nutzer wird sein Nutzer-Profiel geleitet

---

F9: Ich würde mir beide Berichte durchlesen um sicherzustellen, dass sie vom selben Defekt handeln und anhand des besseren den Defekt versuchen zu lösen. Möglicherweise kann der weniger deteilierte Berichte trotzdem nützlich sein, wenn er noch Zusatzinformationen beinhalten.
