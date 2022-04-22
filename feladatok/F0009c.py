#!/usr/bin/env python3

print('''Majmok játszottak az erdőben.
Nyolcadrészük négyzetre emelve már ugrál a fákon.
A fennmaradó 12 táncolva és nagy zajjal a zöld bokrok között szalad.
Hányan voltak összesen?''')

majmok = 0

while (majmok/8)**2 + 12 != majmok:
    majmok += 1
print(majmok, 'majom volt ott!')