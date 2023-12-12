import numpy as np

file = open('text.txt','r')

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

the_matrix = []
for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    the_matrix.append(riga)

