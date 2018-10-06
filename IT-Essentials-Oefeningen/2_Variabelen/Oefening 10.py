getalx = int(input("Geef een geheel getal x: "))
getaly = int(input("Geef een geheel getal y: "))

getalx = getalx + getaly
#getal y is nog altijd hetzelfde, getal x is nu yx

getaly = getalx - getaly
#getal y is nu xy - x

getalx = getalx - getaly

print(getalx, "is getal x,", getaly, "is getal y nu.")

""" x = 5
    y = 10
    x = 5 + 10 = 15
    y = 15 - 10 = 5
    x = 15 - 5 = 10"""