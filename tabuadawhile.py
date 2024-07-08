num = int(input('Qual o número voce deseja mostrar a tabuada: '))

print (f'Tabuada de {num}')

for i in range(1,11):
    print(f'{num} * {i} = {num*i}')

i = 1
while i <= 10:
    print(f'{num} * {i} = {num*i}')
    i = i+1