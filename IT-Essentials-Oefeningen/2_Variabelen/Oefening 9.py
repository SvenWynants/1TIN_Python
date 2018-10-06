twee_euro = int(input("Hoeveel stukken van 2€ heb je? "))
een_euro = int(input("Hoeveel stukken van 1€ heb je? "))
vijftig_cent = int(input("Hoeveel stukken van 50cent heb je? "))
twintig_cent = int(input("Hoeveel stukken van 20cent heb je? "))
tien_cent = int(input("Hoeveel stukken van 10cent heb je? "))
vijf_cent = int(input("Hoeveel stukken van 5cent heb je? "))
twee_cent = int(input("Hoeveel stukken van 2cent heb je? "))
een_cent = int(input("Hoeveel stukken van 1cent heb je? "))

aantal_centen = (twee_euro * 200) + (een_euro * 100) + (vijftig_cent * 50) + (tien_cent * 10) + (vijf_cent * 5) + (twee_cent * 2) + een_cent

print( str(aantal_centen) + "centen = " , twee_euro, "X 2 euro,", een_euro, "X 1 euro,", vijftig_cent, "X 50cent,", twintig_cent , "X 20 cent,", tien_cent, "X 10 cent,", vijf_cent, "X 5cent,", twee_cent, "X 2cent,", een_cent, "X 1cent.")