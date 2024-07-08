valor_original = float(input('Valor original do produto: R$ '))
desconto = float(input('Desconto (em %) para esse produto: '))

desconto = desconto / 100

print('Valor original do produto: R%',valor_original)
print('Voçe ganhou R$',valor_original * desconto,'% de desconto')
print('Valor do produto com desconto: R%',valor_original * (1-desconto))