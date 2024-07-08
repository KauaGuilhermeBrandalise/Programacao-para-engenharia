
tamanholista = 10
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Tamanho da lista L: ', tamanholista)
print('L: ',L)

listapares = []
for n in L:
    if n % 2 == 0:
        listapares.append(n)

print('PARES: ',listapares)

listaimpar = []
for n in L:
    if n %2 == 1:
        listaimpar.append(n)

print('IMPARES: ',listaimpar)
