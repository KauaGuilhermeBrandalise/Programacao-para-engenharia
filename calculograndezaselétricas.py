def calcular_resistencia():
    print("Você escolheu calcular resistência.")
    # Aqui você pode adicionar o código para calcular a resistência

def calcular_corrente():
    print("Você escolheu calcular corrente.")
    # Aqui você pode adicionar o código para calcular a corrente

def calcular_tensao():
    print("Você escolheu calcular tensão.")
    # Aqui você pode adicionar o código para calcular a tensão

while True:
    print("************************************************")
    print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("************************************************")
    print("Escolha uma opção:")
    print("1. Calcular Resistência")
    print("2. Calcular Corrente")
    print("3. Calcular Tensão")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        calcular_resistencia()
    elif escolha == "2":
        calcular_corrente()
    elif escolha == "3":
        calcular_tensao()
    elif escolha == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")