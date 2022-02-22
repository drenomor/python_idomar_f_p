#!/usr/bin/env python3
ujra = 'I'

while ujra == 'I' or ujra == 'i':
    kereszt_nev = input('Kérem a keresztnevet : ')
    vezetek_nev = input('Kérem a vezetéknevet : ')

    neme = input('Nő vagy Férfi (N/F)? : ')
    if neme == 'F' or neme == 'f':
        neme = 'Mr. '
    elif neme == 'N' or neme == 'n':
        hazas = input('Férjezett ? (I/N) : ')
        if hazas == 'I' or hazas == 'i':
            neme = 'Mrs. '
        elif hazas == 'N' or hazas == 'n':
            neme = 'Ms. '
        else:
            print('Családi állapota nem megállapítható!\n')
            neme = 'M?. '
    else:
        print('Ilyen nemet nem ismererek!\n')
        neme = 'M?. '

    napszak = input('Milyen napszak van? (R/DU/E/É) : ')
    if napszak == 'R' or napszak == 'r':
        napszak = 'Morning '
    elif napszak == 'DU' or napszak == 'du':
        napszak = 'Afternoon '
    elif napszak == 'E' or napszak == 'e':
        napszak = 'Evening '
    elif napszak == 'É' or napszak == 'é':
        napszak = 'Night '
    else:
        print('Ilyen napszakot nem ismerek!\n')
        napszak = '(part of the day) '

    print('Good ' + napszak + neme + kereszt_nev + ' ' + vezetek_nev + '!')

    ujra = input('\nSzeretné előröl kezdeni? (I/N): ')
