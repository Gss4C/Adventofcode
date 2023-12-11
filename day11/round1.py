file = open('text.txt','r')

def expander(universo_matrix):
    for i, riga in enumerate(universo_matrix):
        if '#' not in riga:
            universo_matrix.insert(i-1, ['.' for j in range(len(riga))])


the_matrix = []
for riga in file:
    riga_matrix = [riga[j] for j in range(len(riga.strip()))]
    the_matrix.append(riga)

