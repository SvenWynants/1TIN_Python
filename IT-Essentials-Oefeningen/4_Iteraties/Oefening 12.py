familienaam = input("Familienaam:\n")
hoogste_premie = 0
totale_premie = 0

while familienaam != "*" and familienaam != "/":
    voornaam = input("Voornaam:\n")
    aantal_dienstjaren = int(input("Aantal dienstjaren\n"))

    while aantal_dienstjaren < 0 or aantal_dienstjaren > 40:
        aantal_dienstjaren = int(input("Geef het aantal jaren tussen 1 en 40 jaar\n"))

    if aantal_dienstjaren > 5:
        huidige_premie = aantal_dienstjaren * 25
    elif aantal_dienstjaren < 5:
        huidige_premie = 0

    if huidige_premie > hoogste_premie:
        hoogste_premie = huidige_premie

    totale_premie += huidige_premie

    print(" Familienaam:", familienaam, "\n Voornaam:", voornaam, "\n Aantal dienstjaren:", aantal_dienstjaren, "\n De premie:", huidige_premie)
    familienaam = input("Familienaam:\n")

print("De hoogste premie was:", hoogste_premie)
print("De totale premie te betalen is:", totale_premie)