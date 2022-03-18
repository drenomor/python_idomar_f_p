#!/usr/bin/env python3

# Amanda az olivabogyós pizzát csak akkor eszi meg, ha pepperoni is van rajta,
# ((olivaBogyo and pepperoni) or (not olivaBogyo and not pepperoni))
# Borbála csak pepperonis pizzát és csak sonka nélkül eszi, az olíva mindegy neki,
# (pepperoni and not sonka)
# Cilike pedig csak olyan pizzát hajlandó enni, amin pontosan kétféle feltét van.
# (olivaBogyo and pepperoni and not sonka) or
# (olivaBogyo and not pepperoni and sonka) or
# (not olivaBogyo and pepperoni and sonka)

olivaBogyo = True if input('Olíva bogyó van rajta (i/n): ') == 'i' else False
pepperoni = True if input('Pepperóni van rajta (i/n): ') == 'i' else False
sonka = True if input('Sonka van rajta (i/n): ') == 'i' else False

if ((olivaBogyo and pepperoni) or (not olivaBogyo and not pepperoni)) and \
    (pepperoni and not sonka) and \
    ((olivaBogyo and pepperoni and not sonka) or \
    (olivaBogyo and not pepperoni and sonka) or \
    (not olivaBogyo and pepperoni and sonka)):
    print('Jóllakik mindenki.')
else:
    print('Valaki éhes maradna, így nem randelnek ilyen pizzát')
