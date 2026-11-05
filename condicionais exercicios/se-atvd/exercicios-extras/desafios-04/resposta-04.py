quantidade = int(input("Digite a quantidade de esfihas desejadas: "))

if quantidade >= 30:
    preco = 4
else:
    preco = 5

total = quantidade * preco

print("O valor final da compra é: R$", total)