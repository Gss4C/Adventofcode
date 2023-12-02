file = open('input.txt', 'r')
games = {}

#creo un dizionario utile
for count, line in enumerate(file, start=1):
    line = line.rstrip()
    sline = line.split(':')
    games[str(count)] = sline[1]

#soglie
reds = 12
greens = 13
blues = 14


#controllo game per game
lista_ids = []
for gameid in games:
    gioco_valido = True
    estrazioni_singolo_game = games[gameid].split(';')

    for estrazione in estrazioni_singolo_game:
        estrazione_dict = {}
        counts_colors = estrazione.split(',')
        for count_color in counts_colors:
            s_count_color = count_color.split()
            estrazione_dict[s_count_color[1].rstrip()] = int(s_count_color[0].rstrip())
        
        if 'green' in estrazione_dict:
            if estrazione_dict['green'] > greens:
                gioco_valido = False
        if 'blue' in estrazione_dict:
            if estrazione_dict['blue'] > blues:
                gioco_valido = False
        if 'red' in estrazione_dict:
            if estrazione_dict['red'] > reds:
                gioco_valido = False
        
        #print(estrazione_dict)
    if gioco_valido:
        lista_ids.append(int(gameid))

print(sum(lista_ids))