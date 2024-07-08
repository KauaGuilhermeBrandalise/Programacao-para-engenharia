
lista = []

for i in range(10):
    num = float(input('Digite um número: '))
    lista.append(num)

print(lista)
lista.reverse()  #reverse
print(lista)
                    #ou 
print()
print(lista[::-1]) #reverse [::-1]