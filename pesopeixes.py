
pesopeixes = float(input('Peso dos peixes: '))

limite = 50

if pesopeixes > limite:
    excesso = pesopeixes - limite
    multa = excesso*4.00
    print('João obteve',excesso,'quilos além do limite de peso estabelecido e deverá pagar R$',multa,'de multa.')

else:
    print('João não excedeu o limite de peso estabelecido.')

