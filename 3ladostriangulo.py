lados = input('Dê três valores para o triangulo abaixo.')
l1 = int(input('Primeiro: '))
l2 = int(input('Segundo: '))
l3 = int(input('Terceiro: '))


if (l1 == l2) and (l2 == l3):
    print('Triangulo Equilátero: três lados iguais.')

elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    print('Triangulo isoceles: quaisquer dois lados iguais.')

else:
    print('Triangulo Escaleno: três lados diferentes.')
   