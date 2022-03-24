#!/usr/bin/env python3

# Amanda az olivabogyós pizzát csak akkor eszi meg, ha pepperoni is van rajta,
# ((olivaBogyo and pepperoni) or (not olivaBogyo and not pepperoni))
# Borbála csak pepperonis pizzát és csak sonka nélkül eszi, az olíva mindegy neki,
# (pepperoni and not sonka)
# Cilike pedig csak olyan pizzát hajlandó enni, amin pontosan kétféle feltét van.
# (olivaBogyo and pepperoni and not sonka) or
# (olivaBogyo and not pepperoni and sonka) or
# (not olivaBogyo and pepperoni and sonka)

# igazság táblázat

#   POS|ABC|M
#   ---|+--|-
#   +--|-+-|-
#   -+-|---|-
#   --+|+--|-
#   ++-|+++|+
#   +-+|--+|-
#   -++|--+|-
#   +++|+--|-

olivaBogyo = True if input('Olíva bogyó van rajta (i/n): ') == 'i' else False
pepperoni = True if input('Pepperóni van rajta (i/n): ') == 'i' else False
sonka = True if input('Sonka van rajta (i/n): ') == 'i' else False

if pepperoni and olivaBogyo and not sonka:
    print('Jóllakik mindenki.')
else:
    print('Valaki éhes maradna, így nem rendelnek ilyen pizzát')
