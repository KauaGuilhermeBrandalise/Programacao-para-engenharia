def main():
    num_alunos = 10
    num_notas = 4
    medias = []

    for aluno in range(1, num_alunos + 1):
        notas = []
        print(f"Aluno {aluno}:")
        for nota_num in range(1, num_notas + 1):
            while True:
                    nota = float(input(f"  Nota {nota_num}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
        
        media = sum(notas) / num_notas
        medias.append(media)
        print(f"  Média: {media:.2f}\n")

    num_aprovados = sum(1 for media in medias if media >= 7)
    print(f"Número de alunos com média maior ou igual a 7: {num_aprovados}")

if __name__ == "__main__":
    main()