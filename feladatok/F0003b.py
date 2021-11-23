#!/usr/bin/env python3

# Bővítsd az előző programot úgy,
# hogy a kiírás előtt kérdezze meg a születési évedet
# és a csillagjegyedet, és az előző feladatban megadott
# mondat után ezt is közölje veled.

VezetekNev = input('Kérlek add meg a vezeték neved : ')
KeresztNev = input('Kérlek add meg a kereszt neved : ')
SzuletesiEv = input('Kérlek add meg a születési évedet : ')
CsillagJegy = input('Kérlek add meg milyen csillagjegyben születtél : ')

print('A te neved ', VezetekNev, ' ', KeresztNev, '.', sep='')
print(SzuletesiEv, ' -(ban/ben) születtél és a/az ', CsillagJegy, ' csillag jegyében.', sep='')
