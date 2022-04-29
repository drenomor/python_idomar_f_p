#!/usr/bin/env python3

# 3x+4y=52

x = 0
while 3*x <=52:
    y = 0
    while 3*x + 4*y <= 52:
        if 3*x + 4*y == 52:
            print('x=', x , 'y=', y, ' az egyik megoldás.')
        y += 1
    x += 1
