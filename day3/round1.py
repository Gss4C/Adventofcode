file_hand = open('test.txt', 'r')
file = file_hand.readlines()
numeri_da_sommare = []
#with open('input.txt', 'r') as file:
for n_riga, riga in enumerate(file):
    #print(n_riga)
    riga.rstrip()
    posizioni_caratteri_scelti = []
    for i, carattere in enumerate(riga):
        if i in posizioni_caratteri_scelti:
            continue
        if carattere.isdigit():
            numero_string = carattere

            posizioni_caratteri_scelti.append(i)

            posizioni_numero = []
            posizioni_numero.append(i)
            

            index_caratteri_successivi = 1

            while True:
                if riga[i + index_caratteri_successivi].isdigit():
                    numero_string += riga[i + index_caratteri_successivi]
                    posizioni_caratteri_scelti.append(i + index_caratteri_successivi)
                    posizioni_numero.append(i + index_caratteri_successivi)
                    index_caratteri_successivi += 1
                else:
                    break
            #posizioni_numero.append(i+index_caratteri_successivi)
            #ora ho il numero, devo controllare le caselle adiacenti
            #posizioni numero mi mostra gli indici da controllare sopra e sotto
            riga_sopra = False
            riga_sotto = False
            riga_sx = False
            riga_dx = False

            diagonaleSX = False
            diagonaleDX = False

            # SOPRA E SOTTO #
            for posizione in posizioni_numero:
                #print(i+index_caratteri_successivi) -- Corretto
                if n_riga != 0:
                    if file[n_riga - 1][posizione] != '.':
                        riga_sopra = True
                elif n_riga == 0:
                    riga_sopra = True

                if n_riga != 2:
                    if file[n_riga + 1][posizione] != '.':
                        riga_sotto = True
                elif n_riga == len(file) - 1:
                    riga_sotto = True
                    

            # DIAGONALI #
            if n_riga != 0 and n_riga != len(file)-1:
                
                if i != 0:
                    if file[n_riga - 1][i-1] != '.' or file[n_riga+1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = True
                if i != len(riga):
                    if file[n_riga - 1][i+1] != '.' or file[n_riga +1][i+1]:
                        diagonaleDX = True
                else:
                    diagonaleDX = True
            
            if n_riga == 0:
                
                if i != 0:
                    if file[n_riga+1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = True
                if i != len(riga):
                    if file[n_riga +1][i+1]!= '.':
                        diagonaleDX = True
                else:
                    diagonaleDX = True

            if n_riga == len(file) -1:
                
                if i != 0:
                    if file[n_riga-1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = True
                if i != len(riga):
                    if file[n_riga -1][i+1]!= '.':
                        diagonaleDX = True
                else:
                    diagonaleDX = True




            # DESTRA E SINISTRA #
            if i != 0:
                if riga[i - 1] != '.':
                    riga_sx = True
                    #print('RIGA SX')
            else:
                riga_sx = True
                #print('RIGA SX')
            
            if (i+index_caratteri_successivi) != len(riga)-1:
                if riga[i + index_caratteri_successivi] != '.':
                    riga_dx = True
                    #print('RIGA DX')
            else:
                riga_dx = True
                #print('RIGA DX')
            

            numero_valido = riga_dx or riga_sx or riga_sotto or riga_sopra or diagonaleDX or diagonaleSX
            if numero_valido:
                numeri_da_sommare.append(int(numero_string))

risposta = sum(numeri_da_sommare)
print(risposta)