dinheiro = float(input("Digite quantos R$ você quer gastar em combustível: "))

litros = dinheiro/4.95
quilometros = 20*litros

print(f"Com o valor {dinheiro:,.2f}, você pode abastecer {litros:,.2f} litros de combustível e percorrer {quilometros:,.2f} quilometros.")