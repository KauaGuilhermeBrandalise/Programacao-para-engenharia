def funcao(nome, salario = 9000):
    print('Nome: ', nome)
    print('Salário: ', salario)

def main():
    nome = input('Nome do funcionário: ')
    salario = 9000
    print(f'Funcionario {nome} e salario de R${salario:.2f}')
main()    
