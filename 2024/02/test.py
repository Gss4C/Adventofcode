import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    with open("input.txt", "r") as f:
    
        for line in f:
            print(line.strip().split())
            
    return


@app.cell
def _():
    test_list = [['42', '44', '47', '49', '51', '52', '54', '52'],
    ['24', '27', '30', '31', '32', '35', '36', '36'],
    ['80', '82', '85', '86', '87', '90', '94'],
    ['4', '5', '7', '10', '13', '14', '20'],
    ['38', '41', '40', '42', '45', '47', '50', '52'],
    ['43', '46', '48', '49', '52', '49', '52', '49'],
    ['38', '41', '42', '44', '47', '49', '48', '48'],
    ['60', '62', '61', '63', '67'],
    ['33', '36', '38', '35', '41'],
    ['14', '16', '18'],
    ['31', '32', '32', '35', '37', '38'],
    ['68', '69', '69', '70', '71', '74', '75', '73'],
    ['29', '32', '34', '35', '35', '37', '38', '38'],
    ['83', '84', '85', '88', '88', '90', '93', '97'],
    ['23', '24', '25', '28', '28', '34'],
    ['78', '80', '83', '84', '86', '90', '93', '96'],
    ['43', '46', '47', '51', '52', '51'],
    ['22', '23', '25', '29', '29'],
    ['78', '81', '84', '87', '90', '94', '95', '99'],
    ['-14', '-16', '-18']]

    input_file = open("input.txt", 'r')

    lista_differenze = []
    #for riga in test_list:
    for riga in input_file:
        riga = riga.strip().split()
        differenze = []
        for i in range(len(riga)-1):
            differenze.append(int(riga[i])-int(riga[i+1]))
        #print(differenze, "\n\n")
        lista_differenze.append(differenze)

    print(lista_differenze)
    #print("Lista differenze: " , len(lista_differenze), "\nLista test: ", len(test_list))
    safeness = []
    safe_levels = 0
    for level_diffs in lista_differenze:
        level_safeness   = False
        level_negativity = list(map(lambda x : x<0 , level_diffs))
        #print("Level", lista_differenze.index(level_diffs), "negativity: ", level_negativity)
        if all(level_negativity) or not any(level_negativity):
            #print("Negativity OK")
            if any(list(map(lambda x : abs(x)>3 or x==0 , level_diffs))):
                continue #skip level
            safe_levels +=1
            #level_safeness = True
            #safeness.append(level_safeness)

    #print(safeness)
    print("Safe levels: ", safe_levels)
    return


@app.cell
def _():
    for k in range(3):
        print("K = ", k)
        for l in range(5):
            if l == 2:
                break
            print("L = ", l)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
