from funcs import *
file = open('input.txt','r')

the_matrix = []
for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    the_matrix.append(riga)

riga_i, colonna_j = S_position(the_matrix)
start_riga = riga_i
start_colonna = colonna_j

condition = True
diobestia = []

print('startings r/c: ', start_riga, start_colonna)
while condition == True:
    punto = the_matrix[riga_i][colonna_j]
    if colonna_j != len(the_matrix[riga_i]) - 1:
        right = the_matrix[riga_i][colonna_j + 1]
    else:
        right = 'edge'
    if colonna_j != 0:
        left = the_matrix[riga_i][colonna_j - 1]
    else:
        left = 'edge'
    if riga_i != 0:
        up = the_matrix[riga_i-1][colonna_j]
    else:
        up = 'edge'
    if riga_i != len(the_matrix) - 1:        
        down = the_matrix[riga_i+1][colonna_j]
    else:
        down = 'edge'
    
    azzecco_punto = appiccicosity(punto)
    azzecco_left  = appiccicosity(left)
    azzecco_right = appiccicosity(right)
    azzecco_up    = appiccicosity(up)
    azzecco_down  = appiccicosity(down)

    u_r_d_l = can_i_go(me = azzecco_punto,
                       l = azzecco_left,
                       r = azzecco_right,
                       d = azzecco_down,
                       u = azzecco_up)
    
    if riga_i == start_riga and colonna_j == start_colonna:
        if u_r_d_l[0]:
            riga_i = riga_i - 1
        elif u_r_d_l[1]:
            colonna_j = colonna_j + 1
        elif u_r_d_l[2]:
            riga_i = riga_i + 1
        neopunto = [riga_i, colonna_j]
        diobestia.append(neopunto)

    else:
        if u_r_d_l[0] and not [riga_i - 1 , colonna_j] in diobestia:
            riga_i = riga_i - 1
                
        elif u_r_d_l[1] and not [riga_i , colonna_j + 1] in diobestia:
            colonna_j = colonna_j + 1

        elif u_r_d_l[3] and not [riga_i, colonna_j - 1] in diobestia :
            colonna_j = colonna_j - 1

        elif u_r_d_l[2] and not [riga_i + 1 , colonna_j] in diobestia:
            riga_i = riga_i + 1                
                
        neopunto = [riga_i, colonna_j]
        diobestia.append(neopunto)
    if riga_i == start_riga and colonna_j == start_colonna:
        condition = False

print(len(diobestia)/2)