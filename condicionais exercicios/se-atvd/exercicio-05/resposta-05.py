estoque = int(input("Digite a quantidade do produto em estoque: "))

if estoque < 20:
    estoque = estoque + 50

print("A quantidade atualizada do estoque é:", estoque)