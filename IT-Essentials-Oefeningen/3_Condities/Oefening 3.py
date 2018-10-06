vertrek_uur = int(input("Vertrekuur: "))
vertrek_min = int(input("Verktrekminuut: "))
duur = int(input("De duur in minuten: "))
vertrek_totaal = vertrek_uur * 60 + vertrek_min

tussentijd = vertrek_totaal + duur

aankomst_uur = int(tussentijd / 60)
aankomst_min = tussentijd % 60

if aankomst_uur > 24:
    aankomst_uur = aankomst_uur - 24
else:
    if aankomst_uur > 48:
        aankomst_uur = aankomst_uur - 48

print("Het aankomstuur is:", aankomst_uur , "uur en", aankomst_min, "minuten.")
