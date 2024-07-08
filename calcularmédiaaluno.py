nome = input('Nome do aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

media = (n1+n2+n3) /3

if media >= 6:
    print(media,'Parabens sua média é alta.')
elif media >= 5:
    print(media,'Sua média é rasoável.')

else:
    print(media,'Sua média é baixa.É uma boa oportunidade para melhorar.')