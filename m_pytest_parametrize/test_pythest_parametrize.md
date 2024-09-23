# test_pytest_parametrize

F1: Mit pytest.mark.parametrize können übersichtlich verschiedene Testfälle dargestellt werden. Wenn man das mit einer Schleife machen würde, würde es zusätzliche Logik brauchen. Es liefert mehr Informationen über die einzelnen Testfälle, denn bei einer Schleife in der Testfunktion würden alle Testfälle als ein einziger betrachtet werden, sodass der gesamte Test fehlschlägt, sobald ein einzelner Testfall fehlschlägt.

---

F2: Man kann eine solche Tabelle auch aus eine Datei (z.B. csv oder json) einlesen, indem man eine Funktion zum öffnen der Datei schreibt und anstelle der Tabelle die Funktion aufruft.
