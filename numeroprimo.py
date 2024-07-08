import math

num = int(input('Digite um número: '))
i = 1
divisor = 0

print(f'Divisores de {num}')
raiz = math.sqrt(num)
print(num)
raiz = math.ceil(raiz)
print(raiz)
while i <= num:
    if num % i == 0:
        divisor += 1   
        #break
        #print(i) 
    i +=1
print(f'{num} tem {divisor} divisores.')
if divisor > 0:
    print(num,'Não é primo.')
else:
    print(num,'É primo.')