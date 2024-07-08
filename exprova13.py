produtos = {}

for i in range(3):
    descricao = input(f"Digite a descrição do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[descricao] = preco

produto_mais_caro = max(produtos)

print(f"O produto mais caro é: {produto_mais_caro}")
