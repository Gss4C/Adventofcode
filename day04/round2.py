import numpy as np

file_hand = open('input.txt', 'r')
file = file_hand.readlines()

carte_possedute = np.ones(len(file))

for i, line in enumerate(file):

    coso = line.split(':')
    cazzi = coso[1].split('|')
    winning = cazzi[0].split()
    mine    = cazzi[1].split()

    n_corrispondenze = 0
    for k in mine:
        if k in winning:
            n_corrispondenze += 1

    if n_corrispondenze == 0:
        continue
    
    for _ in range(int(carte_possedute[i])):
        for indice_successivi in range(n_corrispondenze):
            carte_possedute[i+indice_successivi + 1] += 1
    
print(sum(carte_possedute))    