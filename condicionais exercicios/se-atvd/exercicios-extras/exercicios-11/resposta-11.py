curtidas = int(input("Digite a quantidade de curtidas: "))
comentarios = int(input("Digite a quantidade de comentários: "))
pontos = int(input("Digite a pontuação inicial: "))

if curtidas >= 100 and comentarios >= 30:
    pontos = pontos + 50

print("A pontuação final é:", pontos)