lista1 = []
lista2 = []

print ('Digite 5 elementos para a primeira lista')

for i in range (5):
    elemento = input(f'Elemento{i+1}: ')
    lista1.append(elemento)

for i in range (5):
    elemento = input(f'Elemento{i+1}: ')
    lista2.append(elemento)

lista3 = []
for i in range (5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print("Lista 1:", lista1)
print('Lista 2:', lista2)
print('Lista 3', lista3)



