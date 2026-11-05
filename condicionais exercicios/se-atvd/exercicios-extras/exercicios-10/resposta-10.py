livros = int(input("Digite a quantidade de livros comprados: "))
jogos = int(input("Digite a quantidade de jogos comprados: "))
valor_compra = float(input("Digite o valor total da compra: R$ "))

if livros >= 2 or jogos >= 3:
    valor_compra = valor_compra - 25

print("O valor final da compra é: R$", valor_compra)