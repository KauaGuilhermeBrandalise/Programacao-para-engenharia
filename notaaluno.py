medias = list()

i = 0

while i < 3:
    soma = 0
    for k in range(4):
        nota = float(input(f'Aluno {i}, nota {k + 1}:'))
        soma += nota
        medias.append(soma/4)

print(medias)
alunos = 0
for m in medias:
    if m >= 7:
        alunos += 1

print(f'{alunos} alunos aprovados com média maior ou igual 7.')