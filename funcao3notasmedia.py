def media(n1, n2 ,n3):
    return (n1 + n2 + n3)/3

def main():
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    n3 = float(input('Terceira nota: '))

    print(f'Média final: {media(n1,n2,n3):.2f}')

if __name__ == '__main__':
    main()
    