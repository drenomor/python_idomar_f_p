#!/usr/bin/env python3

szam = input('Kérek egy egész számot! : ')
szam = int(szam)

if szam >= 0:
    print('A(z)', szam, 'természetes szám!')
else:
    print('A(z)', szam, 'egy negatív egész!')
