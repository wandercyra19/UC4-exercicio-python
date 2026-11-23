atividade 4: controle de aprovação

notas = [8, 5, 9, 4, 7]

aprovados = 0
reprovados = 0

print("Notas registradas:")

for nota in notas:
    print(nota)

    if nota >= 7:
        print("Aprovado")
        aprovados = aprovados + 1
    else:
        print("Reprovado")
        reprovados = reprovados + 1

print("Quantidade de aprovados:", aprovados)
print("Quantidade de reprovados:", reprovados)
