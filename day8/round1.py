from itertools import cycle

file = open('input.txt', 'r')
elenco_punti = file.readlines()
istruzioni_str = elenco_punti[0].strip()

istruzioni = [istruzioni_str[i] for i in range(len(istruzioni_str))]
istruzioni_cicliche = cycle(istruzioni)
punti = [elenco_punti[j].strip() for j in range(len(elenco_punti)) if j >1]


contapassi = 0
punto_i = None
A = True

while A == True:
    if contapassi == 0:
        punto_i = 'AAA'
    for riga in punti:
        if riga.startswith(punto_i):
            if punto_i == 'ZZZ':
                print('Trovato punto finale')
                A = False
                break
            
            pezzetti_riga = riga.split()
            left  = pezzetti_riga[2].removeprefix('(').removesuffix(',')
            right = pezzetti_riga[3].removesuffix(')')

            direzione = next(istruzioni_cicliche)
            if direzione == 'L':
                punto_i = left
                contapassi += 1
            else:
                punto_i = right
                contapassi += 1

print(contapassi)