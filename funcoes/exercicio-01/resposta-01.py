def verificar_aprovacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Chamando a função com três notas diferentes
nota1 = 8.5
nota2 = 6.0
nota3 = 7.0

print("Estudante 1:", verificar_aprovacao(nota1))
print("Estudante 2:", verificar_aprovacao(nota2))
print("Estudante 3:", verificar_aprovacao(nota3))
