
pessoas = []

for i in range(3):
    nome = input(f'Nome{i+1}: ')
    altura = float(input(f'Altura{i+1}: '))
    peso = float(input(f'Peso{i+1}: '))
    pessoas.append({"nome": nome, "altura": altura, "peso": peso})

menoraltura = min(pessoa['altura'] for pessoa in pessoas)
pesototal = sum(pessoa['peso'] for pessoa in pessoas)
pesomedio = pesototal / len(pessoas)
nomes_ordenados = sorted(pessoa["nome"] for pessoa in pessoas)

print(f"A menor altura do grupo é: {menoraltura} metros")
print(f"O peso médio do grupo é: {pesomedio:.2f} kg")
print("Lista dos nomes das pessoas em ordem alfabética:")

