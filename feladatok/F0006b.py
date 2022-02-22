#!/usr/bin/env python3

a = int(input('Kérem az első számot: '))
b = int(input('Kérem a második számot: '))

if a < b:
    szoveg = 'A két szám közül a kisebb: ' + str(a)
elif b < a:
    szoveg = 'A két szám közül a kisebb: ' + str(b)
else:
    szoveg = 'A két szám egyenlő: ' + str(a) + ' = ' + str(b)
print(szoveg)
