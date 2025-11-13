from itertools import cycle
import numpy as np

file = open('input.txt', 'r')
elenco_punti = file.readlines()
istruzioni_str = elenco_punti[0].strip()

istruzioni = [istruzioni_str[k] for k in range(len(istruzioni_str))]
istruzioni_cicliche = cycle(istruzioni)
punti = [elenco_punti[j].strip() for j in range(len(elenco_punti)) if j >1]

punti_i = []
A = True

for riga in punti:
    pezzetti_riga = riga.split()
    puntino_i = pezzetti_riga[0]
    if puntino_i.endswith('A'):
        punti_i.append(riga.split()[0])

passicontati = []
for PUNTONE in punti_i:
    contapassi = 0
    punto_i = PUNTONE
    print('Ora faccio: ', PUNTONE)
    A = True
    while A == True:
        for riga in punti:
            if riga.startswith(punto_i):
                if punto_i.endswith('Z'):
                    print('Trovato punto finale')
                    A = False
                    break
                
                left  = riga.split()[2].removeprefix('(').removesuffix(',')
                right = riga.split()[3].removesuffix(')')

                direzione = next(istruzioni_cicliche)
                if direzione == 'L':
                    punto_i = left
                    contapassi += 1
                else:
                    punto_i = right
                    contapassi += 1

    passicontati.append(contapassi)
print(passicontati)
passinteri = [int(passicontati[l]) for l in range(len(passicontati))]
print(np.lcm.reduce(passinteri))