compra = float(input('Valor da compra: '))
desconto = float(input('Percentual de desconto: ')) /100
desconto = 1 - desconto 
pagar = (compra * desconto) 
print('Valor a ser pago R$ ',pagar)