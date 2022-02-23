#!/us/bin/env python3
gondolt_szam = 4
kitalalta = False

while not kitalalta:
    tipp = int(input('Melyik számra gondoltam 1 és 5 között? : '))
    if tipp == gondolt_szam:
        kitalalta = True
print('Viszlát!')