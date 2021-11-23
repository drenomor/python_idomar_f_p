#!/usr/bin/env python3

MagyarMerfold = int(input('Hány Magyar mérföldre van a sárkány barlangja? : '))

TengeriMerfold = MagyarMerfold * 8.353

Kilometer = MagyarMerfold / 1.852

print('A sárkány barlangja', TengeriMerfold, 'NM-re vagy', Kilometer, 'km-re található!')