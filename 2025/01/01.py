if __name__ == "__main__":
    counter = 0
    index = 50
    dial = [x for x in range(100)]

    with open('input.txt') as input_file:
        for line in input_file:
            direction = line[0]
            steps = int(line[1:])
            match direction:
                case 'L':
                    index -= steps % 100
                case 'R':
                    index += steps % 100

            if index in [0, 100]:
                counter += 1
                index = 0
            else:
                if index > 99:
                    index -= 100
                index = dial.index(dial[index])
    print('Part one solution: ',counter)