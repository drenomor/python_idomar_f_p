#!/usr/bin/env python3

a = input('Kérem az első számot: ')
b = input('Kérem a második számot: ')

if a < b:
    print('A két szám közül a kisebb: ', a)
elif b < a:
    print('A két szám közül a kisebb: ', b)
else:
    print('A két szám egyenlő: ' + a + ' = ' + b)
