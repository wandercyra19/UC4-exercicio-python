pontuacao = int(input("Digite a pontuação do participante: "))
vitorias = int(input("Digite o número de vitórias: "))

if pontuacao >= 500 and vitorias >= 3:
    print("Classificado para a final!")
else:
    print("Continue treinando para o próximo campeonato!")