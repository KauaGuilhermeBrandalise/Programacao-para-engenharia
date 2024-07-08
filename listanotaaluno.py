notas = []

for i in range(0,3):
    notas.append(float(input('Digite a nota: ')))

media = sum(notas) / 3

print(f'Primeira nota: {notas[0]}')
print(f'Segunda nota: {notas[1]}')
print(f'Terceira nota: {notas[2]}')
print(f'Menor nota: {min(notas)}')
print(f'Maior nota: {max(notas)}')
print(f'Média de notas: {media:.2f}')