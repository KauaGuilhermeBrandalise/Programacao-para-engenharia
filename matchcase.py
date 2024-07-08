dia = int(input('Numero do dia da semana: '))
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case _:
        print(f"Valor {dia} inválido!")