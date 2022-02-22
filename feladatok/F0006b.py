#!/usr/bin/env python3

a = input('Kérem az első számot: ')
b = input('Kérem a második számot: ')

if a < b:
    szoveg = 'A két szám közül a kisebb: ' + str(a)
elif b < a:
    szoveg = 'A két szám közül a kisebb: ' + str(b)
else:
    szoveg = 'A két szám egyenlő: ' + str(a) + ' = ' + str(b)
print(szoveg)
