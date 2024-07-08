lista = []

x = int(input('Digite um número inteiro x: '))
y = int(input('Digite um número inteiro y: '))

if x < y:
    for i in range(x,y +1):
        lista.append(i)
    print(lista)

else:
    print('Erro, o x deve ser menor que o y.')

