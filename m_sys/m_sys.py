import sys

if not sys.flags.quiet:
    
    print("sys.argv:", sys.argv)

    if len(sys.argv) > 2:
        print("sys.argv[2]", sys.argv[2])
    else:
        print("Fehler: Es wurden weniger als 2 Argumente übergeben")

else:
    print("Quiet-Modus aktiviert: Keine Ausgabe von sys.argv")

print("Meldung nach stderr:", file=sys.stderr)

print("Python-Version:", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

print("Pyhton-Module", list(sys.modules.keys()))

print("Pfad zu den Modulen:", sys.path)
