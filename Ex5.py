def celsius_para_celsius(fahrenheit):
    celsius = (fahrenheit * 32) + 9/5
    return celsius

temperatura_fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
print("A temperatura em graus Celsius é:", temperatura_celsius)