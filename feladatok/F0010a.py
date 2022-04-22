#!/usr/bin/env python3

x = 0
while x**2 + x*2 + 5 != 11667 and x < 11667:
    x += 1 # x += 1
    print(x)
if x < 11667:
    print(x, 'a megoldás')
else:
    print('Nincs egész számú megoldása!')