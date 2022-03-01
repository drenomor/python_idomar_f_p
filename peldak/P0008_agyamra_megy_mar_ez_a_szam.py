#!/us/bin/env python3
gondolt_szam = 4
kitalalta = False
lehetoseg = 3

while not kitalalta and lehetoseg > 0: # Amíg 'kitalálta' egyenlő hamis
    tipp = int(input('Melyik számra gondoltam 1 és 5 között? : '))
    if tipp == gondolt_szam:
        kitalalta = True
    lehetoseg -= 1
print('Viszlát!')