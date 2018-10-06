snelste_renner = 0
sec_snelste_renner = 999999999999
percentage_trager = 0.0
teller = 0
aantal_traag = 0
inschrijvingsnr = int(input("Inschrijvingsnr\n"))

while inschrijvingsnr >= 0:
    tijd_sec = int(input("Tijd in seconden over 36km\n"))
    teller += 1

    if tijd_sec > 3600:
        aantal_traag += 1

    if tijd_sec < sec_snelste_renner:
        snelste_renner = inschrijvingsnr
        sec_snelste_renner = tijd_sec
    inschrijvingsnr = int(input("Inschrijvingsnr\n"))

percentage_trager = (aantal_traag / teller) * 100

print("Snelste renner is de renner met inschrijvingsnr:", snelste_renner)
print("Het percentage van de renners dat er langer dan 1 uur over doet:", percentage_trager, "%")