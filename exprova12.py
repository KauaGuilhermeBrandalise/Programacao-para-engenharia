lista1 = []
lista2 = []

print('Digite os elementos da primeira lista.')
for i in range(6):
    elementos = int(input('Digite um número: '))
    lista1.append(elementos)

print('Digite os elementos da segunda lista.')
for i in range(6):
    elementos = int(input('Digite um número: '))
    lista2.append(elementos)

lista3 = []
for i in range(6):
    soma = lista1[i] + lista2[i]
    lista3.append(soma)

print(lista1)
print(lista2)
print(lista3)
