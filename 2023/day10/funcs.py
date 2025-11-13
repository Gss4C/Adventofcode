def S_position(matrice):
    #restituisce le coordinate di S nella matrice: riga i, colonna j.
    for i, riga in enumerate(matrice):
        if 'S' not in riga:
            continue
        else:
            for j, colonna in enumerate(riga):
                if colonna == 'S':
                    indice_riga = i
                    indice_colonna = j
    return indice_riga, indice_colonna

def appiccicosity(punto):
    appiccicanza = {}
    if punto == 'edge' or '.':
        appiccicanza['up']    = False
        appiccicanza['down']  = False
        appiccicanza['left']  = True
        appiccicanza['right'] = True
    if punto == '-':
        appiccicanza['up']    = False
        appiccicanza['down']  = False
        appiccicanza['left']  = True
        appiccicanza['right'] = True
    if punto == '|':
        appiccicanza['up']    = True
        appiccicanza['down']  = True
        appiccicanza['left']  = False
        appiccicanza['right'] = False
    if punto == 'L':
        appiccicanza['up']    = True
        appiccicanza['down']  = False
        appiccicanza['left']  = False
        appiccicanza['right'] = True
    if punto == 'J':
        appiccicanza['up']    = True
        appiccicanza['down']  = False
        appiccicanza['left']  = True
        appiccicanza['right'] = False
    if punto == '7':
        appiccicanza['up']    = False
        appiccicanza['down']  = True
        appiccicanza['left']  = True
        appiccicanza['right'] = False
    if punto == 'F':
        appiccicanza['up']    = False
        appiccicanza['down']  = True
        appiccicanza['left']  = False
        appiccicanza['right'] = True
    if punto == 'S':
        appiccicanza['up']    = True
        appiccicanza['down']  = True
        appiccicanza['left']  = True
        appiccicanza['right'] = True
    return appiccicanza

def can_i_go(me, l, r, u, d):
    can_i_go_l = me['left'] and l['right']
    can_i_go_r = me['right'] and r['left']
    can_i_go_u = me['up'] and u['down']
    can_i_go_d = me['down'] and d['up']
    where_can_i_go = [can_i_go_u, can_i_go_r, can_i_go_d, can_i_go_l]
    return where_can_i_go