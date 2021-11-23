#!/usr/bin/env python3

Nev = input('Hogy híjják kendet?\n')
AktualisEv = int(input('Milyen évet írunk?\n'))
Kor = int(input('És hány éves kend?\n'))

SZuletesiEv = AktualisEv - Kor

print(Nev, ', kend ', SZuletesiEv, '-ben született.', sep='')
