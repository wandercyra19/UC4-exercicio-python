
def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)
    return media


# Lista de notas
notas = [8, 7, 9, 6, 10]

# Chamando a função e armazenando o resultado
media_final = calcular_media(notas)

# Exibindo a média final
print("A média final da turma é:", media_final)
