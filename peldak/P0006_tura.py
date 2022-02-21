#!/usr/bin/env python3

evszak = input('Melyik évszak van? (ny/ő) : ')
esik_az_eso = input('Esik az eső? (i/n) : ')
fuj_a_szel = input('Fúj a szél? (i/n) : ')

if fuj_a_szel == 'n' and (evszak == 'ny' or (evszak == 'ő' and esik_az_eso == 'n')):
    print('Megyünk ki!')
else:
    print('Maradunk otthon!')