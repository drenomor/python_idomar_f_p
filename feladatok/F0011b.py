#!/usr/bin/env python3
tobbszorozo = 0
while tobbszorozo < 10:
    oszlop = 0
    while oszlop < 10:
        sor = 0
        while sor < oszlop: # egy sor kiíratása (egy sorban 25 db O van)
            print(' ',end='')
            sor += 1
        print('O')
        oszlop += 1

    oszlop = 8
    while oszlop >= 0:
        sor = 0
        while sor < oszlop: # egy sor kiíratása (egy sorban 25 db O van)
            print(' ',end='')
            sor += 1
        print('+')
        oszlop -= 1
    tobbszorozo += 1