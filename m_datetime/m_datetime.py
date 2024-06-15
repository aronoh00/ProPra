import datetime as dt
import zoneinfo

aktuelle_zeit = dt.datetime.now()
print ("aktuelle Zeit:" , aktuelle_zeit)

zeitpunkt = dt.datetime(2024, 12, 1, 13, 9)
formatierter_zeitpunkt = zeitpunkt.strftime("%A, %d. %B %Y %H:%M Uhr")

print ("Zeitpunkt: ", formatierter_zeitpunkt)

datum_einlesen = "2024-12-15##13:09:44"

datum_objekt = dt.datetime.strptime(datum_einlesen, "%Y-%m-%d##%H:%M:%S")

print ("geparste Zeit: ", datum_objekt)

b_Zeit = dt.datetime.now(zoneinfo.ZoneInfo("Europe/Berlin"))
c_Zeit = dt.datetime.now(zoneinfo.ZoneInfo("America/Caracas"))

print ("Berliner Zeit: ", b_Zeit)
print ("Caracas Zeit: ", c_Zeit)

zeitdifferenz_berlin = b_Zeit.utcoffset()
zeitdifferenz_caracas = c_Zeit.utcoffset()

print ("Zeitdifferenz zur UTC Berlin: ", zeitdifferenz_berlin)
print ("Zeitdifferenz zur UTC Caracas: ", zeitdifferenz_caracas)

diff = dt.timedelta(days = 1024, minutes = 512)
caracas_neu = c_Zeit + diff

print ("Caracas Zeit in 1024 Tagen und 512 Minuten: ", caracas_neu)


def time_average(logs: list[tuple[str, int, str]]) -> dt.timedelta:
    start = {}
    diffs = []

    # convert strings and calculate difference
    for timestamp, eventnumber, flag in logs:
        timestamp_dt = dt.datetime.strptime(timestamp, "%Y-%m-%d##%H:%M:%S")
        if flag == 'start':
            start[eventnumber] = timestamp_dt
        elif flag == 'end':
            if eventnumber in start:
                diffs.append(timestamp_dt - start[eventnumber])

    # calculate average
    if diffs:
        average_diff = sum(diffs, dt.timedelta()) / len(diffs)
    else:
        average_diff = dt.timedelta()

    return average_diff

# Beispiel Log-Daten
logs = [
  ('2024-01-01##10:11:14', 1, 'start'),
  ('2024-01-02##03:01:01', 2, 'start'),
  ('2024-01-03##00:11:15', 1, 'end'),
  ('2024-01-03##03:02:02', 2, 'end')
]

# Berechnung der durchschnittlichen Bearbeitungszeit
durchschnittliche_bearbeitungszeit = time_average(logs)
print("Durchschnittliche Bearbeitungszeit:", durchschnittliche_bearbeitungszeit)
