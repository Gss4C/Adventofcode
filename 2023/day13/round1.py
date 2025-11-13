fileh = open('test.txt', 'r')
file = fileh.readlines()
patterns = []

new_pattern = True
for line in file:
    print(new_pattern, line)
    if new_pattern == True:
        pattern = []
        new_pattern = False
    
    if line == '\n' or line == file[-1]:
        new_pattern = True
        patterns.append(pattern)
        #continue
    else:
        pattern.append(line.strip())

#faccio la pattern matrix e la analizzo
for pattern in patterns:
    pattern_matrix = []
    for riga in pattern:
        riga_smontata = [riga[i] for i in range(len(riga))]
        pattern_matrix.append(riga_smontata)
print(pattern_matrix)