input_file = open("input.txt", 'r')

lista_differenze = []

for riga in input_file:
    riga = riga.strip().split()
    differenze = []
    for i in range(len(riga)-1):
        differenze.append(int(riga[i])-int(riga[i+1]))
    lista_differenze.append(differenze)

safe_levels = 0
for level_diffs in lista_differenze:
    level_negativity = list(map(lambda x : x<0 , level_diffs))
    if all(level_negativity) or not any(level_negativity):
        if any(list(map(lambda x : abs(x)>3 or x==0 , level_diffs))): continue #skip level
        safe_levels +=1

print("Safe levels: ", safe_levels)