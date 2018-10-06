brutoloon = float(input("Geef het brutoloon van een werknemer in: "))

vakantiegeld = brutoloon * 0.05

if vakantiegeld > 350:
    jaarlijkse_bijdrage = 0.08 * 350
else:
    jaarlijkse_bijdrage = vakantiegeld * 0.08

print("Het brutoloon is €" + str(brutoloon))
print("Het vakantiegeld is €" + str(vakantiegeld))
print("De jaarlijkse bijdrage is €" + str(jaarlijkse_bijdrage))
