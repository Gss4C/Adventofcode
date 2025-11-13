import numpy as np

def delta(tf, d):
    discr = tf*tf - 4*d
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
tempostringa = ''
for i in tempini:
    tempostringa += i

distanze = distances[1].rstrip()
distanzine = distanze.split()
distanzostringa = ''
for j in distanzine:
    distanzostringa += j

print('Utilizzo la coppia tempino/distanzino: ', tempostringa, distanzostringa)
tempo = int(tempostringa)
distanza = int(distanzostringa)
x1, x2 = x12(tempo, distanza)
differenza = int(x1) - int(x2)
print(differenza)