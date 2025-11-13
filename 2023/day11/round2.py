import numpy as np

def aggiungi_righe_universo(universo_matrix):
    universo_espanso_verticale = []
    for i, riga in enumerate(universo_matrix):
        if '#' in riga:
            universo_espanso_verticale.append(riga)
        else:
            universo_espanso_verticale.append(['.' for j in range(len(riga))])
            universo_espanso_verticale.append(['.' for j in range(len(riga))])
    return universo_espanso_verticale
    
def aggiungi_colonne_universo(universo_da_espandere):
    universo_trasposto = np.transpose(universo_da_espandere)
    universo_espanso = aggiungi_righe_universo(universo_trasposto)
    universo_espanso_finale = np.transpose(universo_espanso)
    return universo_espanso_finale

def expander(universo):
    universo_espanso_h = aggiungi_righe_universo(universo)
    universo_finale = aggiungi_colonne_universo(universo_espanso_h)
    return universo_finale

def N_righe_vuote(universo, n_riga_A, n_riga_B):
    righe_vuote = 0
    if n_riga_A == n_riga_B:
        return righe_vuote
    else:
        for index_riga in range(min(n_riga_A, n_riga_B), max(n_riga_A, n_riga_B) ):
            if '#' not in universo[index_riga]:
                righe_vuote += 1
    return righe_vuote

def N_colonne_vuote(universo, n_colonna_A, n_colonna_B):
    colonne = 0
    neoverso = np.transpose(universo)
    if n_colonna_A == n_colonna_B:
        return colonne
    else:
        for index_colonna in range(min(n_colonna_A, n_colonna_B), max(n_colonna_A, n_colonna_B) ):
            if '#' not in neoverso[index_colonna]:
                colonne += 1
    return colonne

file = open('input.txt','r')
moltiplicatore = 1000000

universo = []
for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    universo.append(riga_matrix)

pos_galassie = []

for i_riga in range(len(universo)):
    for j_col in range(len(universo[i_riga])):
        if universo[i_riga][j_col] == '#':
            pos_galassie.append([i_riga,j_col])

coppie_non_ripetute = []
for index in range(len(pos_galassie)):
    for ondex in range(index):
        if pos_galassie[index] != pos_galassie[ondex]:
            coppia = [pos_galassie[index], pos_galassie[ondex]]
            coppie_non_ripetute.append(coppia)

distanze = []
for k,coppia in enumerate(coppie_non_ripetute):
    if k%200 == 0:
        print('Completamento: ', round(k/len(coppie_non_ripetute)*100, 2), '%')
    N_righe = N_righe_vuote(universo = universo,
                            n_riga_A = coppia[0][0],
                            n_riga_B = coppia[1][0])
    N_colon = N_colonne_vuote(universo = universo,
                              n_colonna_A = coppia[0][1],
                              n_colonna_B = coppia[1][1])
    delta_riga    = abs(coppia[0][0] - coppia[1][0]) + moltiplicatore * N_righe - N_righe
    delta_colonna = abs(coppia[0][1] - coppia[1][1]) + moltiplicatore * N_colon - N_colon
    distanze.append(delta_colonna + delta_riga)

print(sum(distanze))