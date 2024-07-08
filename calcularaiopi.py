pi = 3.14159

# Lendo o número de unidades de comprimento (raio)
raio = float(input("Digite o raio do círculo (em unidades): "))

# Verificando se o raio é positivo
if raio < 0:
    print("Erro: valores negativos não são permitidos.")
else:
    # Calculando a área do círculo
    area = pi * raio**2

    # Exibindo a área do círculo
    print("A área do círculo de raio", raio, "unidades é", area, "unidades.")