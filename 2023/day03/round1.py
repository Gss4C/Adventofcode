file_hand = open('input.txt', 'r')
file = file_hand.readlines()
numeri_da_sommare = []

for n_riga, riga in zip(range(len(file)), file):
    riga = riga.rstrip()
    posizioni_caratteri_scelti = []

    for i, carattere in zip(range(len(riga)), riga):
        if i in posizioni_caratteri_scelti:
            continue

        if carattere.isdigit():
            posizioni_numero = []

            numero_string = carattere
            posizioni_caratteri_scelti.append(i)
            posizioni_numero.append(i)
            next_index = 1

            cond = True
            while cond == True:
                if riga[i+next_index].isdigit():

                    numero_string += riga[i + next_index]
                    posizioni_caratteri_scelti.append(i + next_index)
                    posizioni_numero.append(i + next_index)

                    if i+next_index != len(riga)-1:
                        next_index += 1
                    else:
                        break
                else:
                    break

            riga_sopra = False
            riga_sotto = False
            riga_sx = False
            riga_dx = False
            diagonaleSX = False
            diagonaleDX = False

            # DIAGONALI #
            if n_riga != 0 and n_riga != len(file)-1:
                
                if i != 0:
                    if file[n_riga - 1][i-1] != '.' or file[n_riga+1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = False
                if i != len(riga):
                    if file[n_riga - 1][i+next_index] != '.' or file[n_riga +1][i+next_index] != '.':
                        diagonaleDX = True
                else:
                    diagonaleDX = False
            
            if n_riga == 0:
                
                if i != 0:
                    if file[n_riga+1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = False
                if i != len(riga):
                    if file[n_riga +1][i+next_index]!= '.':
                        diagonaleDX = True
                else:
                    diagonaleDX = False

            if n_riga == len(file)-1:
                
                if i != 0:
                    if file[n_riga-1][i-1] != '.':
                        diagonaleSX = True
                else:
                    diagonaleSX = False
                if i != len(riga):
                    if file[n_riga -1][i+next_index]!= '.':
                        diagonaleDX = True
                else:
                    diagonaleDX = False
            

            # SOPRA E SOTTO #
            for posizione in posizioni_numero:
                if n_riga != 0:
                    if file[n_riga - 1][posizione] != '.':
                        riga_sopra = True
                        
                elif n_riga == 0:
                    riga_sopra = False
                    

                if n_riga != len(file)-1:
                    if file[n_riga + 1][posizione] != '.':
                        riga_sotto = True
                elif n_riga == len(file) - 1:
                    riga_sotto = False
            
            # DESTRA E SINISTRA #
            if i != 0:
                if riga[i - 1] != '.':
                    riga_sx = True
            else:
                riga_sx = False
            
            if (i+next_index) != len(riga)-1:
                if riga[i + next_index] != '.':
                    riga_dx = True
            else:
                riga_dx = False

            numero_valido = riga_dx or riga_sx or riga_sotto or riga_sopra or diagonaleDX or diagonaleSX
            if numero_valido:
                numeri_da_sommare.append(int(numero_string))
                #print(numero_string)
risposta = sum(numeri_da_sommare)
print(risposta)