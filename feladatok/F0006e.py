#!/usr/bin/env python3

a = int(input('\'a\' oldal: '))
b = int(input('\'b\' oldal: '))
c = int(input('\'c\' oldal: '))

if (a - b) < c and (b - c) < a and (c - a) < b:
    print('A Háromszög megszerkeszthető!')
else:
    print('Ebből soha nem lesz háromszög!')
