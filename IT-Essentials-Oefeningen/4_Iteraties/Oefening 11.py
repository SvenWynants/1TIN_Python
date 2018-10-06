personeelsnummer = int(input("Personeelsnummer\n"))
aantal_mannen = 0
aantal_vrouwen = 0

while personeelsnummer !=0:
    geslacht = int(input("Geslacht: 0 = vrouw; 1 = man\n"))
    leeftijd = int(input("Leeftijd\n"))
    brutoloon = float(input("Brutoloon\n"))
    if geslacht == 1 and leeftijd > 34 or geslacht == 12 and brutoloon >= 1800:
        aantal_mannen += 1
    elif geslacht == 0 and leeftijd < 25:
        aantal_vrouwen += 1

    personeelsnummer = int(input("Personeelsnummer\n"))

print("Aantal mannen die ouder zijn dan 34 jaar of een loon hebben van 1800 euro of meer:", aantal_mannen)
print("Aantal vrouwen die jonger zijn dan 25 jaar:", aantal_vrouwen)