getal = int(input("Geef een getal tussen 1 en 100\n"))

while getal < 1 or getal > 100:
    if getal < 1:
        print("Fout! Het getal moet groter zijn dan 1!")
        getal = int(input("Geef een getal tussen 1 en 100\n"))
    else:
        print("Fout! Het getal moet kleiner zijn dan 100!")
        getal = int(input("Geef een getal tussen 1 en 100\n"))
        
print(getal)