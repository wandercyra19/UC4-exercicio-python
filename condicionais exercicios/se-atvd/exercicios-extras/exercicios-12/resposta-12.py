distancia = float(input("Digite a distância que Milena irá percorrer em km: "))

valor_servico = 180

if distancia > 10:
    valor_servico = valor_servico + 25

print("O total a pagar é: R$", valor_servico)