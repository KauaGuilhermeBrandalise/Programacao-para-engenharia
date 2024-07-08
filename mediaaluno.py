nome = input('Digite nome do aluno: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 4: '))
nota3 = float(input('Nota 3: '))

media = (nota1 + nota2 + nota3) /3


if media == 10:
    print(nome,'Aprovado com distinção')
elif media >=7:
    print(nome,'Aprovado')
else:
    print(nome,'Reprovado')