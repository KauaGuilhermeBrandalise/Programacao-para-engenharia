tupla1 = (6.4, 7.5, 10.0, 6.5, 9.5)
tupla2 = (7.0, 8.4, 9.5, 6.6, 7.3)

media1 = sum(tupla1)/len(tupla1)

soma = 0
for nota in tupla2:
    soma = soma + nota

media2 = soma/len(tupla2)

print(f'Média turma 1 = {media1:.2f}')
print(f'Média turma 2 = {media2:.2f}')

if media1 > media2:
    print('A turma obteve a melhor média na prova 1.')
else:
    print('A turma obteve a melhor média na prova 2.')
