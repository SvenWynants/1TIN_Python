toegangsprijs_volwassene = 11
toegangsprijs_kinderen = 6

aantal_volwassenen = int(input("Hoeveel volwassenen gaan er naar de dierentuin? "))
aantal_kinderen = int(input("Hoeveel kinderen gaan er naar de dierentuin? "))

prijs_kinderen = aantal_kinderen * toegangsprijs_kinderen
prijs_volwassenen = aantal_volwassenen * toegangsprijs_volwassene

totaal_prijs = prijs_kinderen + prijs_volwassenen

print("De totaalprijs bedraagt ", totaal_prijs, "euro.")