def montati_il_numero(file, n_riga_digit, i_digit, from_where):
    numero_sringoso = []
    if from_where == 'L':
        while file[n_riga_digit][i_digit].isdigit():
            numero_sringoso.insert(0, file[n_riga_digit][i_digit])
            i_digit = i_digit - 1
        numero_montato = ''
        for cifra in numero_sringoso:
            numero_montato += cifra
        numero_di_merda = int(numero_montato)

    elif from_where == 'R':
        while file[n_riga_digit][i_digit].isdigit():
            numero_sringoso.append(file[n_riga_digit][i_digit])
            i_digit = i_digit + 1
        numero_montato = ''
        for cifra in numero_sringoso:
            numero_montato += cifra
        numero_di_merda = int(numero_montato)

    elif from_where == 'C':
        AAA = i_digit
        BBB = i_digit+1
        #print('Parto dal numero: ', file[n_riga_digit][AAA])
        while file[n_riga_digit][AAA].isdigit():
            numero_sringoso.insert(0, file[n_riga_digit][AAA])
            AAA = AAA - 1
            #print(numero_sringoso)
        
        while file[n_riga_digit][BBB].isdigit():
            numero_sringoso.append(file[n_riga_digit][BBB])
            BBB = BBB + 1
        
        numero_montato = ''
        for cifra in numero_sringoso:
            numero_montato += cifra
        numero_di_merda = int(numero_montato)

    return numero_di_merda




def conta_rigaup_rigadown(updown, i, file, n_riga, left, right):
    conteggio_BASTARDO = 0
    numeri_di_merda = []
    if updown == 'UP':
        if not(file[n_riga - 1][i].isdigit()):
            if not left:
                if file[n_riga - 1][i-1].isdigit():
                    conteggio_BASTARDO += 1
                    numeroadiacente = montati_il_numero(file, n_riga-1, i-1, "L")
                    numeri_di_merda.append(numeroadiacente)
            if not right:
                if file[n_riga - 1][i+1].isdigit():
                    conteggio_BASTARDO += 1
                    numeroadiacente = montati_il_numero(file, n_riga-1, i+1, "R")
                    numeri_di_merda.append(numeroadiacente)
        else:
            conteggio_BASTARDO += 1
            numeroadiacente = montati_il_numero(file, n_riga-1, i, "C")
            numeri_di_merda.append(numeroadiacente)

    if updown == 'DOWN':
        if not(file[n_riga + 1][i].isdigit()):
            if not left:
                if file[n_riga + 1][i-1].isdigit():
                    conteggio_BASTARDO += 1
                    numeroadiacente = montati_il_numero(file, n_riga+1, i-1, "L")
                    numeri_di_merda.append(numeroadiacente)
            if not right:
                if file[n_riga + 1][i+1].isdigit():
                    conteggio_BASTARDO += 1
                    numeroadiacente = montati_il_numero(file, n_riga+1, i+1, "R")
                    numeri_di_merda.append(numeroadiacente)
        else:
            conteggio_BASTARDO += 1
            numeroadiacente = montati_il_numero(file, n_riga+1, i, "C")
            numeri_di_merda.append(numeroadiacente)

    if updown == 'FANCULO':
        if not left:
            if file[n_riga][i-1].isdigit():
                conteggio_BASTARDO += 1
                numeroadiacente = montati_il_numero(file, n_riga, i-1, "L")
                numeri_di_merda.append(numeroadiacente)
        if not right:
            if file[n_riga][i+1].isdigit():
                conteggio_BASTARDO += 1
                numeroadiacente = montati_il_numero(file, n_riga, i+1, "R")
                numeri_di_merda.append(numeroadiacente)
    return conteggio_BASTARDO, numeri_di_merda

def conteggia_adiacenti(i, file , n_riga, left, right):
    adiacentenza = 0
    merda_sopra,numeri_sopra = conta_rigaup_rigadown(updown = 'UP',
                                        i      = i,
                                        file   = file,
                                        n_riga = n_riga,
                                        left   = left,
                                        right  = right)
    merda_sotto,numeri_sotto = conta_rigaup_rigadown(updown = 'DOWN',
                                        i      = i,
                                        file   = file,
                                        n_riga = n_riga,
                                        left   = left,
                                        right  = right)
    merda_bastarda,numeri_delcazzo = conta_rigaup_rigadown(updown = 'FANCULO',
                                        i      = i,
                                        file   = file,
                                        n_riga = n_riga,
                                        left   = left,
                                        right  = right)
    adiacentenza = merda_sopra + merda_sotto + merda_bastarda
    merdosi = numeri_sopra+ numeri_sotto+ numeri_delcazzo
    return adiacentenza, merdosi

def edge_finder(index, riga):
    right = False
    left = False
    if index == 0:
        left = True
    if index == len(riga)-1:
        right = True
    return left, right


file_hand = open('input.txt', 'r')
file = file_hand.readlines()

lista_risposta = []

for n_riga, riga in zip(range(len(file)), file):
    riga = riga.rstrip()
    for i, carattere in zip(range(len(riga)), riga):
        if carattere == '*':
            left_edge, right_edge = edge_finder(i, riga)
            n_adiacenti = 0
            if n_riga != 0 and n_riga != len(file)-1:
                n_adiacenti, numeri_merdosi = conteggia_adiacenti(i=i, 
                                                  file   = file, 
                                                  n_riga = n_riga, 
                                                  left   = left_edge,
                                                  right  = right_edge) 
            elif n_riga == 0:
                adiacenti_sopra, numeri_sopra = conta_rigaup_rigadown(updown='UP', i=i, file=file,n_riga=n_riga,left=left_edge,right=right_edge)
                adiacenti_lato, numeri_lato  = conta_rigaup_rigadown(updown='FANCULO', i=i, file=file,n_riga=n_riga,left=left_edge,right=right_edge)
                numeri_merdosi = numeri_sopra + numeri_lato
                n_adiacenti = adiacenti_lato+adiacenti_sopra
            elif n_riga == len(file)-1:
                adiacenti_sotto, numeri_sotto = conta_rigaup_rigadown(updown='DOWN', i=i, file=file,n_riga=n_riga,left=left_edge,right=right_edge)
                adiacenti_lato, numeri_lato  = conta_rigaup_rigadown(updown='FANCULO', i=i, file=file,n_riga=n_riga,left=left_edge,right=right_edge)
                numeri_merdosi = numeri_sotto + numeri_lato
                n_adiacenti = adiacenti_lato+adiacenti_sotto

            if n_adiacenti == 2:
                print(numeri_merdosi[0],'; ' ,numeri_merdosi[1])
                schifezza = numeri_merdosi[0]*numeri_merdosi[1]
                lista_risposta.append(schifezza)
risposta = sum(lista_risposta)
print(risposta)