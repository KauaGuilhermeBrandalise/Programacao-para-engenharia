n = int(input('Tamanho da turma: '))

p1 = []
for i in range(n):
    nota = float(input(f'Nota{i+1}: '))
    p1.append(nota)

p2 = []
for i in range(n):
    nota = float(input(f'Nota{i+1}: '))
    p2.append(nota)

mediap1 = sum(p1)/n
mediap2 = sum(p2)/n

print('Notas prova 1: ', p1)
print('Notas prova 2: ', p2)
print(f'Média da turma na prova 1: {mediap1:.2f}')
print(f'Média da turma na prova 2: {mediap2:.2f}')
if mediap1 > mediap2:
    print('A turma obteve a melhor média na prova 1.')
else:
    print('A turma obteve a melhor média na prova 2.')