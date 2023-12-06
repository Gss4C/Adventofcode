import numpy as np

def delta(tf, d):
    discr = tf*tf - 4*d
    #print(discr)
    return discr
def x12(tf, d):
    print('calcolo soluzioni con: ', tf, d)
    x1 = (tf + np.sqrt(delta(tf, d)))/2
    x2 = (tf - np.sqrt(delta(tf, d)))/2
    return x1, x2

fileh = open('input.txt', 'r')
file = fileh.readlines()

times = file[0].split(':')
distances = file[1].split(':')

tempi = times[1].rstrip()
tempini = tempi.split()

distanze = distances[1].rstrip()
distanzine = distanze.split()

schifonumerini = []
for tf, d in zip(tempini, distanzine):
    tempaccio = int(tf)
    distanzaccia = int(d)
    x1, x2 = x12(tempaccio, distanzaccia)
    #print(int(x1), int(x2))
    #print(x1, x2)
    if x1%int(x1) == 0:
        schifonumerini.append(int(x1)-int(x2+1))
    else:
        schifonumerini.append(int(x1)-int(x2))

cazzo=1
for i in schifonumerini:
    cazzo *= i
print(cazzo)