import math

raio_maior = float(input('Digite valor do raio maior'))
raio_menor = float(input('Digite valor do raio menor'))

area_coroa = math.pi * (raio_maior**2 - math.pow(raio_menor, 2))

print(f"Area da coroa circular é {area_coroa:.2f}")