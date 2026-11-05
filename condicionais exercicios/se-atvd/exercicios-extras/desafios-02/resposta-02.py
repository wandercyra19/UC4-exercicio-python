valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 200:
    valor_compra = valor_compra - 40
else:
    valor_compra = valor_compra - 10

print("O valor final a pagar é: R$", valor_compra)