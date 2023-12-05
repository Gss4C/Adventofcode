file = open('input.txt', 'r')

cacca = []
for line in file:
    print(line)
    coso = line.split(':')
    cazzi = coso[1].split('|')
    winning = cazzi[0].split()
    mine = cazzi[1].split()
    
    contacazzi = 0
    for i in mine:
        if i in winning:
            contacazzi += 1
    if contacazzi > 0:
        if contacazzi == 1:
            card_score = 1
        if contacazzi > 1:
            card_score = 2**(contacazzi-1)
    else:
        card_score = 0
    cacca.append(card_score)
print(sum(cacca))