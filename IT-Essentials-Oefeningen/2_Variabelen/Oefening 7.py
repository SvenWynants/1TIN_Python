lengte_tapijt = float(input("Geef de lengte van je tapijt in m "))
breedte_tapijt = float(input("Geef de breedte van je tapijt in m "))
prijs_vierm = float(input("Geef de prijs per vierkante meter in "))
prijs_plaatsingskost = float(input("Geef de plaatsingskosten per vierkante meter in "))

opp_tapijt = lengte_tapijt * breedte_tapijt
prijs_tapijt = prijs_vierm * opp_tapijt
prijs_plaatsing = prijs_plaatsingskost * opp_tapijt

totaal_prijs = prijs_tapijt + prijs_plaatsing

print("Het tapijt kost €" + str(prijs_tapijt), ", de kostprijs van de plaatsing is €" + str(prijs_plaatsing), "en de totaal prijs is €" + str(totaal_prijs) + "." )