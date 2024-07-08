import math
x1 = float(input('Digite a distancia do x no ponto 1: '))
y1 = float(input('Digite a distancia do y no ponto 1: '))

x2 = float(input('Digite a distancia do y no ponto 2: '))
y2 = float(input('Digite a distancia do y no ponto 2: '))

d = math.sqrt((x2 + x1)**2+(y2 - y1))

print ('A distância entre o ponto 1 e ponto 2 é de:',d)