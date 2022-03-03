#!/usr/bin/env python3
# Egy szendvicsben legalább legyen egy fajta hús,
# (pulyka or marha or sonka)

# Egy szendvicsben legyen marha vagy sonka, de együtt ne,
# ((marha and not sonka) or (sonka and not marha))

# Ha a szendvicsben van pulykahús, akkor legyen benne sajt is.
# ((pulyka and sajt) or (not pulyka))

marha = sonka = pulyka = sajt = False

valasz = input('Van benne pulyka? (i/n): ')
if valasz == 'i':
    pulyka = True

valasz = input('Van benne marha? (i/n): ')
if valasz == 'i':
    marha = True

valasz = input('Van benne sonka? (i/n): ')
if valasz == 'i':
    sonka = True

valasz = input('Van benne sajt? (i/n): ')
if valasz == 'i':
    sajt = True

if (pulyka or marha or sonka) and \
    ((marha and not sonka) or (sonka and not marha)) and \
    ((pulyka and sajt) or (not pulyka)):
    print('\nEz a szendvics finom lesz!')
else:
    print('\nEbből inkább nem ennék!')
