#!/usr/bin/env python3

print('''Ím ezen emlékmű Diophantosz hamva fölött áll,
Élte korát adják művei és ez a kő.
Ifjúként tölté hatod életét isteni kegyből,
Még tizenketted után, gyenge szakálla kiüt.
Egy heted élttel utóbb nászfáklyák égtek előtte,
Öt évvel aztán kisfia megszületett.
Ó, boldogság nélküli ifjú, fél annyi évet
Mint tudós apa élt, s lett hona szürke Hádész.
Még négy esztendőn a tudás könnyíti gyászát,
S hosszú élet után őt is elérte a vég.''')

kor = 0
while kor/7 + kor/12 + kor/7 + 5 + kor/2 + 4 != kor and kor < 200:
    kor += 1
    print(kor)
if kor < 200:
    print('\n',kor, ' évet élet', sep='')
else:
    print('Nem deríthető ki az életkor')