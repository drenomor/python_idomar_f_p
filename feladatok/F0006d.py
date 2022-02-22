#!/usr/bin/env python3

helyezes = int(input('Hanyadik helyen végeztél a versenyen? : '))

while helyezes < 1:
    print('\n0 vagy negatív szám nem lehet a helyezés!')
    helyezes = int(input('\nHanyadik helyen végeztél a versenyen? : '))

if helyezes == 1:
    print('Arany érmes vagy!')
elif helyezes == 2:
    print('Ezüst érmes vagy!')
elif helyezes == 3:
    print('Bronz érmes vagy!')
else:
    print('Nem kapsz semmilyen érmet!')
