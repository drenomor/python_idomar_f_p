#!/usr/bin/env python3

# Nev = input('Hogy híjják kendet?\n')
Nev = 'Vicc Elek'
AktualisEv = int(input('Milyen évet írunk?\n'))
Kor = int(input('És hány éves kend?\n'))

SZuletesiEv = AktualisEv - Kor

print(Nev, ', kend ', SZuletesiEv, '-ben született.', sep='')

ErettsegiEv = SZuletesiEv + 18

print(Nev, ', kend ', ErettsegiEv, '-ben fog érettségizni.', sep='')
