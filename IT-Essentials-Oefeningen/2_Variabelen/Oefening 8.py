afgelegde_km = float(input("Hoeveel km leg je jaarlijks af? "))
verbruik = float(input("Hoeveel liter verbruik je per 100km? "))
prijs_per_liter = float(input("Hoeveel kost brandstof per liter? "))

totale_kosten = afgelegde_km * (verbruik/100) * prijs_per_liter
kostprijs_km = verbruik / 100 * prijs_per_liter

print("De totale kosten per jaar voor het opgegeven aantal km is: €" + str(totale_kosten), "en de kostprijs per km is: €" + str(kostprijs_km))