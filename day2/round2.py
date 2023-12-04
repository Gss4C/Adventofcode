file = open('input.txt', 'r')
games = {}

#creo un dizionario utile
for count, line in enumerate(file, start=1):
    line = line.rstrip()
    sline = line.split(':')
    games[str(count)] = sline[1]

risposta = 0
for gameid in games:
    estrazioni_singolo_game = games[gameid].split(';')

    estrazioni_game = []
    for estrazione in estrazioni_singolo_game:
        estrazione_dict = {}
        counts_colors = estrazione.split(',')
        for count_color in counts_colors:
            s_count_color = count_color.split()
            estrazione_dict[s_count_color[1].rstrip()] = int(s_count_color[0].rstrip())
        
        estrazioni_game.append(estrazione_dict)
    
    max_red   = 0
    max_green = 0
    max_blue  = 0
    
    for estrazione in estrazioni_game:
        if 'green' in estrazione:
            if max_green == 0 or estrazione['green'] > max_green:
                max_green = estrazione['green']
        if 'blue' in estrazione:
            if max_blue == 0 or estrazione['blue'] > max_blue:
                max_blue = estrazione['blue']
        if 'red' in estrazione:
            if max_red == 0 or estrazione['red'] > max_red:
                max_red = estrazione['red']

    game_power = max_red * max_green * max_blue
    risposta  += game_power

print(risposta)