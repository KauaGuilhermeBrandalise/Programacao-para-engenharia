pv = float(input("Valor presente R$ "))
n = int(input("Quantidade de meses: "))
i = float(input("Taxa anual de juros: "))

fv = pv * (1 + (i/100.0)/12)**n

print(f"Montante final R$ {fv:,.2f}")