salario_funcionario = float(input("digite o salario do funcionario:"))
if salario_funcionario < 1500:
    aumento = salario_funcionario + 200
else:
    aumento = salario_funcionario 

print("O salariio do funcionario com aumento é:", aumento)