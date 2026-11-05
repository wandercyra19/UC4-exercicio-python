nota = float(input("Digite a nota de Marli: "))
exercicios = int(input("Digite a quantidade de exercícios entregues: "))

if nota >= 7 and exercicios >= 5:
    nota = nota + 2

print("A nota final de Marli é:", nota)