# einkaufsliste-defekt2.md

F1: Die Funktion print_grocery_items_by_location() regelt die Ausgabe

---

F2:

- Was wird in der Funktion definiert:
  - In der Funktion werden zwei Unterfunktionen definiert: where_key(x), where_then_name_key(x)
  - zwei Variablen grocery_items und groups
- Welche Variablen und Funktionen werden tatsächlich genutzt
  - Die Funktion where_then_name_key(x)
  - die beiden Variablen
- Welchen Inhalt haben die Variablen?
  - grocery_items wird an die Funktion übergeben und wird dann die nach whre_then_name_key sortierte Eingabe zugewiesen
  - groups enthält den Inhalt von grocery_items gruppiert nach where_then_name_key
- Wo genau findet die Ausgabe statt?
  - in der for Schleife findet die Ausgabe der Kategorien statt. Die innere For Schleife gibt die Itmes in der jeweiligen Kategorie aus

---

F3: grocery_items stimmt mit den Erwartungen überein, aber groups nicht, da auch nach namen gruppiert wird und nicht nur nach Kategorie

---

F4:

- groups stimmt nicht überein, da neben den Kategorien (where) auch noch nach name gruppiert wird
- Die Unterfunktion where_key() wurde in der Funktion zwar defineirt, aber nicht genutzt
  - Sie liefert nur where anstatt where und name
  - where ist Schlüssel, nach dem gruppiert werden soll, da sonst zu viele Gruppen entstehen
  - where_key muss somit in groups = itertools.groupby(groucery_items, key=where_then_name_key) als key eingesetzt werden
  - Durch eine Ersetztung kommen wir direkt auf das gewünschte Ergebnis mit der richtigen Gruppierung
