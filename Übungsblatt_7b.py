# Aufgabe 1

def datum_einlesen():
    Datum = input("Bitte Datum in Form tt.mm.jjjj eingeben: ")
    try:
        Datum = Datum.split(".")
        tag = int(Datum[0])
        monat = int(Datum[1])
        jahr = int(Datum[2])
        return [tag, monat, jahr]
    except:
        print("Datum falsch formattiert.")
        return [0,0,0]

"""
datum = datum_einlesen()
tag, monat, jahr = datum

print(tag,monat,jahr,sep=".")
"""    

# Aufgabe 2

def datum_formatieren(tag, monat, jahr, ausgabe=False):
    ausgabe_string = f"{tag:02d}.{monat:02d}.{jahr:04d}"
    if ausgabe:
        print(ausgabe_string)
    return ausgabe_string

# datum_formatieren (15,10,1582,True)


# Aufgabe 3

daten = (19,12,2014), (28,2,2014), (29,2,2014), (29,2,2000), (29,2,1900), (31,4,2014), (15,13,2015)

def ist_schaltjahr(jahr):
    return jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0)

def anzahl_tage(monat, jahr):
    if monat in [1,3,5,7,8,10,12]:
        return 31
    if monat in [4,6,9,11]:
        return 30
    if monat == 2:
        return 29 if ist_schaltjahr(jahr) else 28
    return 0

def gueltiges_datum(tag, monat, jahr, untergrenze_jahr=1950, obergrenze_jahr = 2050, msg=False):
    ist_gueltiger_tag = 1 <= tag <= anzahl_tage(monat, jahr)
    ist_gueltiger_monat = 1 <= monat <= 12
    ist_gueltiges_jahr = untergrenze_jahr <= jahr <= obergrenze_jahr
    if msg:
        if not ist_gueltiger_tag:
            print(f"Datum {datum_formatieren(tag,monat,jahr)} besitzt eine ungültige Tageszahl.")
        if not ist_gueltiger_monat:
            print(f"Datum {datum_formatieren(tag,monat,jahr)} besitzt eine ungültige Monatszahl.")
        if not ist_gueltiges_jahr:
            print(f"Datum {datum_formatieren(tag,monat,jahr)} besitzt eine ungültige Jahreszahl.")
    return ist_gueltiger_tag, ist_gueltiger_monat, ist_gueltiges_jahr

for tag,monat,jahr in daten:
    gueltiges_datum(tag,monat,jahr, msg=True)

# Aufgabe 4

daten_im_februar = list(filter(lambda datum: datum[1] == 2,daten))
print(daten_im_februar)

# Aufgabe 5

# Statt all(gueltiges_datum(*datum)) hätte man auch
# gueltiges_datum(*datum) = (True, True, True) hardcodieren können.
gueltige_daten_im_februar = list(filter(lambda datum: all(gueltiges_datum(*datum)), daten_im_februar))
print(gueltige_daten_im_februar)

# Aufgabe 6

formatierte_daten = [datum_formatieren(*datum) for datum in daten]
# Statt des Sortierens der formattierten Daten wäre es sinnvoller,
# die Rohdaten aus Zahlentupeln zu sortieren
formatierte_daten.sort(key=lambda datum: (datum[6:10],datum[3:5],datum[:2]))
print(formatierte_daten)

# Aufgabe 7

umformatierte_daten = list(map(lambda datum: datum.replace(".","-"), formatierte_daten))
print(umformatierte_daten)

def datum_iso(datum):
    tag, monat, jahr = datum.split(".")
    return "-".join((jahr,monat,tag))

for iso_datum in map(datum_iso, formatierte_daten):
    print(iso_datum)