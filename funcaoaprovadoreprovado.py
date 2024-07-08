
def cmedia(n1, n2 ,n3):
    return (n1 + n2 + n3)/3

def verifica(media):
    
    if media > 6:
        print('APROVADO.')

    elif media < 4:
        print('REPROVADO.')

    else:
        print('VERIFICAÇÃO SUPLEMENTAR.')

def main():
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))

    print(f'Media final: {cmedia(n1,n2,n3):.2f}')

    media = cmedia(n1,n2,n3)
    verifica(media)
main()
