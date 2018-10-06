gewicht_aarde = float(input("Geef je gewicht:  "))

while gewicht_aarde!=0:
    print("Aarde:", gewicht_aarde)
    gewicht_maan = gewicht_aarde * 0.165
    print("Maan:", gewicht_maan)
    gewicht_jupiter = gewicht_aarde * 2.537
    print("Jupiter:", gewicht_jupiter)
    gewicht_mars = gewicht_aarde * 0.378
    print("Mars:", gewicht_mars)
    gewicht_aarde = float(input("Geef je gewicht op aarde:    "))