valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra > 150:
    valor_compra = valor_compra - 30

print("O valor que o cliente deverá pagar é: R$", valor_compra)