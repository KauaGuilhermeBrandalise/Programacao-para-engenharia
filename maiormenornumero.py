n1 = float(input('Digite primeiro número: '))
n2 = float(input('Digite segundo número: '))
n3 = float(input('Digite terceiro número: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('Número maior: ',maior)
print('Número menor: ',menor)