#!/us/bin/env python3
gondolt_szam = 4
kitalalta = False
lehetoseg = 3

while not kitalalta and lehetoseg > 0: # Amíg 'kitalálta' egyenlő hamis
    tipp = int(input('Melyik számra gondoltam 1 és 5 között? : '))
    if tipp == gondolt_szam:
        kitalalta = True
    else:
        print('Nem ez az a szám amire gondoltam!')
    lehetoseg -= 1

if not kitalalta and lehetoseg == 0:
    print('Ez most nem sikerült, de majd talán legközelebb!')
else:
    print('Ügyes vagy eltaláltad!')

print('Viszlát!')
