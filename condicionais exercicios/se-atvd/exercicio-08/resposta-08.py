consumo = float(input("Digite o consumo de energia elétrica em kWh: "))

if consumo > 200:
    consumo = consumo + 25

print("O consumo atualizado é:", consumo, "kWh")