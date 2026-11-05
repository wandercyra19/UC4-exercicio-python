reproducoes = int(input("Digite o número de reproduções: "))
curtidas = int(input("Digite a quantidade de curtidas: "))
valor_arrecadado = float(input("Digite o valor já arrecadado: R$ "))

if reproducoes > 1000 or curtidas > 200:
    valor_arrecadado = valor_arrecadado + 150

print("O valor final arrecadado é: R$", valor_arrecadado)