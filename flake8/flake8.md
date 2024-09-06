# flake8

F1: Die Homepage gibt Informationen zur Installation aber nicht zum Zweck des Werkzeuges

---

F2: Das FAQ beantwortet vor allem Fragen in Bezug auf die Veröffentlichung neuer Versionen gibt aber nicht wirklich Informationen über den Zweck.

---

F3: mccabe, pycodestyle, Pyflakes

---

F4: mccabe: Ermittelt die McCabe-Komplexität und findet zu komplexen Code mit einem Wert über 10, da dieser für Menschen nicht mehr nachvollziehbar ist. [Dokumentation:](https://github.com/PyCQA/mccabe)

---

F5: Auf der Hompage von flake8 steht nichts von mccabe und im Vergleich zum Glossar wird die Installation und Anwendung in der Dokumentation beschrieben.

---

F6: pycodestyle: Fügt checks für PEP8 ein. [Dokumentation](https://pycodestyle.pycqa.org/en/latest/)

---

F7: pylflakes: Überprüft auf ungenutze variablen und importierte Module. [Dokumentaion](https://pypi.org/project/pyflakes/)

---

F8: In der Dokumentetaion steht, dass pyflakes den Code auf verschiedene Fehler überprüft. Es werden aber keine konkreten genannt, wie im flake8-Glossar (ungenutzte Variablen/Modeule).

---

F9: Es macht mir mehr freude als erwartet, da der Code somit einheitlicher aussieht. Außerdem verbessert man dadurch die Gewohnheiten

---

F10: Durch: E211 whitespace before '(' und E265 block comment should start with '# ' sieht der Code einheitlicher aus. Als lästig empfand ich E501 line too long (99 > 79 characters) und E701 multiple statements on one line (colon), da ersterer sich nicht unbedingt leicht fixen lässt und zweiterer platzaufwändiger ist.

---

F11: Ich kann mir vorstellen den Code vor allem bei größeren Projekten damit zu bereinigen, damit er besser lesbar ist.
