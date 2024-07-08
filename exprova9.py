d = {}

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
endereco = input('Digite seu endereço: ')
telefone = int(input('Digite seu telefone: '))
d.update({'Nome': nome,'Idade': idade,'Endereço': endereco,'Telefone': telefone})
print(d)