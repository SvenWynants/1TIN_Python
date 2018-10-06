gemiddelde = 0.0
hoogste = -10000

for i in range(0, 10):
    temperatuur = float(input("temperatuur in °C\n"))
    gemiddelde += temperatuur
    if temperatuur > hoogste:
        hoogste = temperatuur

gemiddelde = gemiddelde / 10

print("De hoogste temperatuur voor deze 10 dagen is: " + str(hoogste) + "°C")
print("De gemiddelde temperatuur voor deze 10 dagen is: " + str(gemiddelde) + "°C")