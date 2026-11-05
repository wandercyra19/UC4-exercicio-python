inscritos = int(input("Digite a quantidade de inscritos: "))
cadeiras = int(input("Digite a quantidade de cadeiras disponíveis: "))

if inscritos > 80 and cadeiras < inscritos:
    cadeiras = cadeiras + 30

print("A quantidade final de cadeiras é:", cadeiras)