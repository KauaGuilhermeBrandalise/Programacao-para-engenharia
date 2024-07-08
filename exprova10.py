funcionarios = {
    1: {"nome": "Alice", "funcao": "Programador", "tempo_servico": 4},
    2: {"nome": "Bruno", "funcao": "Designer", "tempo_servico": 2},
    3: {"nome": "Carlos", "funcao": "Gerente", "tempo_servico": 5},
    4: {"nome": "Diana", "funcao": "Programador", "tempo_servico": 2},
}


print("Funcionários:")
for id, info in funcionarios.items():
    print(f"{id}: Nome: {info['nome']}, Função: {info['funcao']}, Tempo de serviço: {info['tempo_servico']} anos")

numero_cadastro = int(input("\nDigite o número de cadastro do funcionário a ser demitido: "))

if numero_cadastro in funcionarios:
    funcionario = funcionarios[numero_cadastro]
    if funcionario["funcao"] == "Programador" and funcionario["tempo_servico"] >= 3:
        print(f"\nErro: O funcionário {funcionario['nome']} é um programador com 3 anos ou mais de serviço e não pode ser demitido.")
    else:
        del funcionarios[numero_cadastro]
        print(f"\nFuncionário {funcionario['nome']} demitido com sucesso.")
else:
    print("\nErro: Número de cadastro não encontrado.")

print("\nFuncionários restantes:")
for id, info in funcionarios.items():
    print(f"{id}: Nome: {info['nome']}, Função: {info['funcao']}, Tempo de serviço: {info['tempo_servico']} anos")

