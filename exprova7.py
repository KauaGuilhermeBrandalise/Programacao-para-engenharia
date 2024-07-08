import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

n = len(Vendas)

soma = sum(Vendas)
media = soma / n

soma_diferencas_quadrado = sum((venda - media) ** 2 for venda in Vendas)
variancia = soma_diferencas_quadrado / n

desvio_padrao = math.sqrt(variancia)

menor_valor = min(Vendas)
maior_valor = max(Vendas)


print(f"Média: {media:.2f}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}")
print(f"Menor Valor: {menor_valor}")
print(f"Maior Valor: {maior_valor}")