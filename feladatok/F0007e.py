#!/usr/bin/env python3
print('A program kiírja a számokat a beírt határok között.\n')
also_hatar = int(input('Kérem a tartomány alsó határát: '))
felso_hatar = int(input('Kérem a tartomány felső határát: '))

if also_hatar > felso_hatar:
    seged = also_hatar
    also_hatar = felso_hatar
    felso_hatar = seged

seged = also_hatar

while seged <= felso_hatar:
    print(seged)
    seged += 1
