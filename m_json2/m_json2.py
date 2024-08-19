import json

path = "m_json1/m_json_student.json"
with open(path, "r") as file:
    data = json.load(file)


def hat_uni(json, studentname: str, wochentag: str) -> bool:
    for student_key, student_value in json.items():
        if student_value.get("Name") == studentname:
            vorlesungszeiten = student_value.get("Vorlesungszeiten", {})
            for modul, zeiten in vorlesungszeiten.items():
                if zeiten and wochentag in zeiten:
                    return True
    return False

print(hat_uni(data, "Max", "Donnerstag"))
print(hat_uni(data, "Max", "Freitag"))

def setze_wunschnote(json_data, studentname: str, fachname: str, wunschnote: float):
    for student_key, student_value in json_data.items():
        if student_value.get("Name") == studentname:
            wunschnoten = student_value.get("Wunschnoten", {})
            if fachname in wunschnoten:
                wunschnoten[fachname] = wunschnote
                print(f"Die Wunschnote für {fachname} wurde auf {wunschnote} geändert.")
                return
            else:
                print(f"Das Fach {fachname} existiert nicht in den Wunschnoten.")
                return
    print(f"Der Student {studentname} wurde nicht gefunden.")

setze_wunschnote(data, "Max", "Lineare Algebra", 2.3)

with open("m_json_student2.json", "w") as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

print("Die Änderungen wurden in 'm_json_student2.json' gespeichert.")
