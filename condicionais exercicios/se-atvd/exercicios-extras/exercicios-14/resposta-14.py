total_alunos = int(input("Digite a quantidade total de alunos: "))
presentes = int(input("Digite a quantidade de alunos presentes: "))
media = float(input("Digite a média geral da turma: "))

if presentes == total_alunos and media >= 8:
    custo = total_alunos * 5
    print("O custo total das esfihas é: R$", custo)
else:
    print("A condição não foi atendida. Não haverá compra de esfihas.")