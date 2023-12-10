from funcs import *
file = open('test.txt','r')

the_matrix = []

for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    the_matrix.append(riga)

riga_i, colonna_j = S_position(the_matrix)

condition = True

start_riga = riga_i
start_colonna = colonna_j

prev_riga = riga_i
prev_colonna = colonna_j

contapassi = 0

print('startings r/c: ', start_riga, start_colonna)
while condition == True:
#for steps in range(15):
    punto = the_matrix[riga_i][colonna_j]

    if colonna_j != len(the_matrix[riga_i]) - 1:
        right = the_matrix[riga_i][colonna_j + 1]
    else:
        right = 'edge'

    if colonna_j != 0:
        left = the_matrix[riga_i][colonna_j - 1]
    else:
        left = 'edge'

    if riga != 0:
        up = the_matrix[riga_i-1][colonna_j]
    else:
        up = 'edge'

    if riga != len(the_matrix) - 1:        
        down = the_matrix[riga_i+1][colonna_j]
    else:
        down = 'edge'
    
    azzecco_punto = appiccicosity(punto)
    azzecco_left  = appiccicosity(left)
    azzecco_right = appiccicosity(right)
    azzecco_up    = appiccicosity(up)
    azzecco_down  = appiccicosity(down)

    #print(azzecco_up)
    u_r_d_l = can_i_go(me = azzecco_punto,
                       l = azzecco_left,
                       r = azzecco_right,
                       d = azzecco_down,
                       u = azzecco_up)
    
    if riga_i == start_riga and colonna_j == start_colonna:
        if u_r_d_l[0]:
            prev_riga = riga_i
            riga_i = riga_i - 1
        
        if u_r_d_l[1] and not u_r_d_l[0]:
            prev_colonna = colonna_j
            colonna_j = colonna_j + 1
        
        if u_r_d_l[2] and not u_r_d_l[0] and not u_r_d_l[1]:
            prev_riga = riga_i
            riga_i = riga_i + 1

    else:
        for index in range(len(u_r_d_l)):
            if not u_r_d_l[index]:
                continue
            else:
                if index == 0:
                if index == 1:
                    if (colonna_j + 1) != prev_colonna and not (colonna_j - 1) != prev_colonna:
                        u_r_d_l[3] = False
                    else:
                        u_r_d_l[1] =

                if index == 2:
                if index == 3:
        #print(u_r_d_l)

        if u_r_d_l[0]:
            if (riga_i - 1) != prev_riga:
                prev_riga = riga_i
                riga_i = riga_i - 1
                
        if u_r_d_l[2]:
            if (riga_i + 1) != prev_riga:
                prev_riga = riga_i
                riga_i = riga_i + 1
                

        if u_r_d_l[1]:
            if (colonna_j + 1) != prev_colonna:
                prev_colonna = colonna_j
                colonna_j = colonna_j + 1
                

        if u_r_d_l[3]:
            if (colonna_j - 1) != prev_colonna:
                prev_colonna = colonna_j
                colonna_j = colonna_j - 1
                

    contapassi += 1
    print(the_matrix[riga_i][colonna_j])
    
    if riga_i == start_riga and colonna_j == start_colonna:
        condition = False

print(contapassi)