file_hand = open('input.txt', 'r')
file = file_hand.readlines()

numeri_da_sommare = []

#with open('input.txt', 'r') as file:
for n_riga, riga in enumerate(file):
    posizioni_caratteri_scelti = []
    for i, carattere in enumerate(riga):
        if i in posizioni_caratteri_scelti:
            continue
        if carattere.isdigit():
            numero_string = carattere

            posizioni_caratteri_scelti.append(i)

            posizioni_numero = []
            posizioni_numero.append(i)
            if i != 0:
                posizioni_numero.append(i-1)

            index_caratteri_successivi = 1

            while True:
                if riga[i + index_caratteri_successivi].isdigit():
                    numero_string += riga[i + index_caratteri_successivi]
                    posizioni_caratteri_scelti.append(i + index_caratteri_successivi)
                    posizioni_numero.append(i + index_caratteri_successivi)
                    index_caratteri_successivi += 1
                else:
                    break
            posizioni_numero.append(i+index_caratteri_successivi + 1)
            #ora ho il numero, devo controllare le caselle adiacenti
            #posizioni numero mi mostra gli indici da controllare sopra e sotto
            riga_sopra = False
            riga_sotto = False
            riga_sx = False
            riga_dx = False
            for posizione in posizioni_numero:
                if n_riga != 0:
                    if file[n_riga - 1][posizione] != '.':
                        riga_sopra = True
                elif n_riga == 0:
                    riga_sopra = True

                if n_riga != 140:
                    if file[n_riga + 1][posizione] != '.':
                        riga_sotto = True
                elif n_riga == len(file):
                    riga_sotto = True

            if i != 0:
                if riga[i - 1] != '.':
                    riga_sx = True
            else:
                riga_sx = True
            
            if i != len(riga):
                if riga[i + 1] != '.':
                    riga_dx = True
            else:
                riga_dx = True
            
            numero_valido = riga_dx and riga_sx and riga_sotto and riga_sopra
            if numero_valido:
                numeri_da_sommare.append(int(numero_string))

risposta = sum(numeri_da_sommare)