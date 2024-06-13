# Shell-Grundlagen

#### F1: Sie führt Kommandos aus einer Datei aus
---
#### F2: Das bedeutet, dass neue Kommandos schon ausgeführt werden können, während die Shell noch das erste ausführt Tokens besitzen viele interessante Eigenschaften, da sie vielseitig eingesetzt werden können
---
#### F3: Das Argument erfasst alle Python- und Textdatein, die ein Verzeichnis unter dem Home Verzeichnis sich befinden und mit process_ beginnen.
---
#### F4: Die beiden Pfade kann man sich mit Pfad1="..." und Pfad2="..." in Variablen Speichern. Dann kann man mit cpp1p2='cp "$Pfad1" "$Pfad2" ' das Verkürzen
---
#### F5: Mit CDPATH="..." wird das Verzeichnis der Liste hinzugefügt. Mit cd subdir kann nun darauf zugegriffen werden
---
#### F6: pyimports() { grep -r -P --include '*py' "^import $1" . | wc -l; }
---
#### F7: Ich habe die pyimports Funktion hinzugefügt und die Variablen CDPATH und PATH1.
---
#### F8: echo $PATH1 hat folgende Ausgabe:/home/aron/ws/propra
---
#### F9: der erste Teil /home/aron/ ist verzichtbar, da ich mich immer in diesem Verzeichnis aufhalte
---
#### F10: Ich werde mich an which gewöhnen, da es schneller ist, aber je nach Anwendungsfall werde ich auch auf command -v zurückgreifen