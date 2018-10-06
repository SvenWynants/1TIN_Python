getala = int(input("Getal 1\n"))
getalb = int(input("Getal 2\n"))

if getala < getalb:
    kleinste_getal = getala
    grootste_getal = getalb
elif getalb < getala:
    kleinste_getal = getalb
    grootste_getal = getala

print("Het kleinste getal is", kleinste_getal)
print("Het kwadraat van het kleinste getal is", kleinste_getal * kleinste_getal)

if getalb == 0 or getala == 0:
    print("De deling kan niet uitgevoerd worden omdat er niet gedeeld kan worden door 0")
else:
    print("Het grootste getal gedeeld door het kleinste getal is", float(grootste_getal / kleinste_getal))
