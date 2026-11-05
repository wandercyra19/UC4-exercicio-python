gasto_anna = float(input("Digite o valor gasto por Anna Beatriz: R$ "))
gasto_giuliany = float(input("Digite o valor gasto por Giuliany: R$ "))

total = gasto_anna + gasto_giuliany

if total > 80:
    total = total + 20

print("O valor final é: R$", total)