#!/usr/bin/env python3

# A Tesód születésnapi pitéjét csinálod.
# A tesód szerint akkor jó egy almás pite, ha:

# Nincsen benne egyszerre szegfűbors és szerecsendió.
# (not (szegFubors and szerecsenDio))

# Ha pitébe tettünk fahéjat, akkor kell bele szerecsendió is.
# Ha nem tettünk fahéjat akkor nem lehet benne szerecsendió sem.
# ((szerecsenDio and faHej) or (not szerecsenDio and not faHej))

# Írj programot a pite jóságának eldöntésére!

szegfuBors = True if input('Van benne szegfűbors? (i/n): ') == 'i' else False
szerecsenDio = True if input('Van benne szerecsendió? (i/n): ') == 'i' else False
faHej = True if input('Van benne fahéj? (i/n): ') == 'i' else False

if (not (szegfuBors and szerecsenDio)) and \
    ((szerecsenDio and faHej) or (not szerecsenDio and not faHej)):
    print('\nEz a pite finom lesz!')
else:
    print('\nEbből tuti nem fogok enni!')
    