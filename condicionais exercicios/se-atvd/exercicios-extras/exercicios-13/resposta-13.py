laboratorios = int(input("Digite a quantidade de laboratórios visitados: "))

pontos = laboratorios * 10

if laboratorios >= 4:
    pontos = pontos + 20

print("A pontuação final é:", pontos)