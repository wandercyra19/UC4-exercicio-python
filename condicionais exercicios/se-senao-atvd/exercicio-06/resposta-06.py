quantidade = int(input("Digite a quantidade de maçãs: "))
if quantidade <= 12:
    preco = 0.30
else:
    preco = 0.25
total = quantidade * preco
print("O valor total da compra é: R$", total)