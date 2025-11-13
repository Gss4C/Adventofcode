file = open('input.txt', 'r')
reds = 12
greens = 13
blues = 14

#creo un dizionario utile
games = {}
for count, line in enumerate(file, start=1):
    line = line.rstrip()
    splitted = line.split(':')
    games[str(count)] = splitted[1]

#controllo game per game
good_games_id = []
for gameid in games:
    goodgame = True
    estrazioni_singolo_game = games[gameid].split(';')

    for estrazione in estrazioni_singolo_game:
        estrazione_dict = {}
        counts_colors = estrazione.split(',')
        for count_color in counts_colors:
            s_count_color = count_color.split()
            estrazione_dict[s_count_color[1].rstrip()] = int(s_count_color[0].rstrip())
        
        if 'green' in estrazione_dict:
            if estrazione_dict['green'] > greens:
                goodgame = False
        if 'blue' in estrazione_dict:
            if estrazione_dict['blue']  > blues:
                goodgame = False
        if 'red' in estrazione_dict:
            if estrazione_dict['red']   > reds:
                goodgame = False
    if goodgame:
        good_games_id.append(int(gameid))

print(sum(good_games_id))