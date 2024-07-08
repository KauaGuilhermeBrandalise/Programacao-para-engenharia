alcool = 4.98
gasolina = 5.57

combustivel = input('Tipo de combustível (A - alcool / G - gasolina): ')
litros = float(input('Quantidade de litros: '))

if combustivel.upper() == 'A' or 'a':
    if litros <= 20:
        valorlitros = litros * (alcool * 0.02)       
    else:
        valorlitros = litros * (alcool * 0.05)

elif combustivel.upper() == 'G' or 'g':
    if litros <= 20:
        valorlitros = litros * (gasolina * 0.04)
    else:
        valorlitros = litros * (gasolina * 0.06)

else:
    print('Tipo de combustível inválido!!')
    exit()
print("Valor a ser pago pelo cliente R$ ",valorlitros)