import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    f = open("input.txt", 'r')
    print([line.strip() for line in f])
    for line in f:
        print(line)
    return


@app.cell
def _():
    counter = 0
    dial = [x for x in range(100)]
    index = 50

    with open('input.txt') as input_file:
        for linea in input_file:
            #print(linea)
            direction = linea[0]
            steps = int(linea[1:])
            #print('direction: ', direction, ' -- steps: ', steps)
            if direction == 'L':
                index -= steps % 100
            elif direction == 'R':
                index += steps %100
            
            if index in [0, 100]:
                counter += 1
                index = 0
                #print('Increment counter: ', counter)
            else:
                if index > 99:
                    index -= 100
                index = dial.index(dial[index])
    print(counter)
    return


@app.cell
def _():
    a = 200
    b = 21
    pos_num = 627
    neg_num = -395

    print('Pos: ', a + pos_num % 100)
    print('Neg: ', neg_num % -100)
    print(b%100)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
