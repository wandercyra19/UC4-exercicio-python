valor_compra = float(input("digite o valor da compra:"))
if valor_compra > 200:
    desconto = valor_compra - 30
else:
    desconto = valor_compra

print("O valor da compra com desconto é:", desconto)