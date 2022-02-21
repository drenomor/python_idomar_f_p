#!/usr/bin/env python3

evszak = input('Melyik évszak van? (ny/ő) : ')
esik_az_eso = input('Esik az eső? (i/n) : ')
fuj_a_szel = input('Fúj a szél? (i/n) : ')

if evszak == 'ny' and fuj_a_szel == 'n':
    print('Megyünk ki!')
elif evszak == 'ő' and esik_az_eso == 'n' and fuj_a_szel == 'n':
    print('Megyünk ki!')
else:
    print('Maradunk otthon!')