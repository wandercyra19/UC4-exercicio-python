mensalidade = float(input("Digite o valor da mensalidade do curso: "))

if mensalidade >= 500:
    mensalidade = mensalidade - 50

print("O valor atualizado da mensalidade é: R$", mensalidade)