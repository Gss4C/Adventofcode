fileh = open('input.txt', 'r')
predictions = []

for riga in fileh:
    livello_zero = [int(riga.split()[j]) for j in range(len(riga.split()))]
    levels_box = [livello_zero]
    
    i = 0
    condition = True

    while condition == True:
        livello_i = []
        for index in range(len(levels_box[i])):
            if index == (len(levels_box[i]) - 1):
                break
            livello_i.append(levels_box[i][index+1] - levels_box[i][index])
        levels_box.append(livello_i)
        if not any(livello_i) != 0:
            condition = False
        else:
            i += 1

    step_up = 0
    for indice in range(1, len(levels_box)):
        step_up = step_up + levels_box[-1-indice][-1]
        
    predictions.append(step_up)
print(sum(predictions))