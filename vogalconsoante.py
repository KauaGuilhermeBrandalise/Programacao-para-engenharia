letra = input('Digite uma letra: ')

if letra.isalpha():
    vogais = 'aeiouAEIOU'
    if letra in vogais:
        print('Vogais')

    else:
        print('Consoante')

else:
    print('Não é uma letra')
