import math

num = 0
soma = 0
n = 0
maior = -1
menor = 9999999
num = 0

while num !=-1:
    num = int(input('Digite um número positivo (-1 para sair): '))
    if num >= 0:
        soma = soma + num
        n = n + 1
        if menor > num:
            menor = num
        if maior < num:
            maior = num

print(f"Você digitou {n} números")
print(f"soma: {soma}")
if n > 0:
    print(f"Média {soma/n:,.2f}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
