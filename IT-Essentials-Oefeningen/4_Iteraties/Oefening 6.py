artikelnr = int(input("Geef het artikelnr:\n"))

while artikelnr!=999:
    hoeveelheid = int(input("Geef de hoeveelheid\n"))
    eenheidsprijs = float(input("Geef de eenheidsprijs in €\n"))
    print(artikelnr, ",", hoeveelheid, "stuks,", eenheidsprijs, "euro per stuk en", eenheidsprijs * hoeveelheid, "euro in totaal.")
    artikelnr = int(input("Geef het artikelnr:\n"))