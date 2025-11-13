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

file = open('input.txt','r') 
the_matrix = []
for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    the_matrix.append(riga_matrix)
pos_galassie = []
universo = expander(the_matrix)
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
for coppia in coppie_non_ripetute:
    delta_riga = abs(coppia[0][0] - coppia[1][0])
    delta_colonna = abs(coppia[0][1] - coppia[1][1])
    distanze.append(delta_colonna + delta_riga)

print(sum(distanze))