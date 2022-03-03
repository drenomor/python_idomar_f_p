#!/usr/bin/env python3
gondolt_szam = 4
kitalalta = False
lehetoseg = 3

while not kitalalta and lehetoseg > 0:
    tipp = int(input('Melyik számra gondoltam 1 és 5 között? : '))
    if tipp == gondolt_szam:
        kitalalta = True
    else:
        print('Nem ez az a szám amire gondoltam! Az eltérés : ', abs(gondolt_szam - tipp))
    lehetoseg -= 1

print('Viszlát!')
