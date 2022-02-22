#!/usr/bin/env python3
kor = -1

while kor < 0:
    kor = int(input('\nKérem adja meg az életkorát : '))
    if kor < 0:
        print('\nAz életkor nem lehet kisebb 0-nál!')

if kor < 6:
    print('\nNézd meg \'A piroska és a farkast\'')
elif 6 <= kor <= 16:
    print('\nNézd meg \'A Zootropolice-t\'')
elif kor > 16:
    print('\nNézz amit szeretnél')
