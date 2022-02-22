#!/usr/bin/env python3

gondolt_szam = int(input('Gondolt szám : '))
tipp = int(input('Melyik számra gondolok : '))
if gondolt_szam == tipp:
    print('Eltaláltad, ügyes vagy!')
elif abs(tipp - gondolt_szam) == 1:
    print('Majdnem sikerlült!')
else:
    print('Ez most nem jött össze, talán majd legközelebb.')
print('Viszlát')
