quantidade_jogos = int(input("Digite a quantidade de jogos comprados: "))
valor_compra = float(input("Digite o valor total da compra: R$ "))
pontuacao = int(input("Digite a pontuação inicial do cliente: "))

if quantidade_jogos >= 3 and valor_compra > 500:
    pontuacao = pontuacao + 200

print("A pontuação final do cliente é:", pontuacao)