dinheiro = float(input("Quanto dinheiro Mikaelly possui? R$ "))

ingresso = 750
passagem = 300

total = ingresso + passagem

if dinheiro >= total:
    dinheiro = dinheiro + 100

print("Mikaelly possui após o possível bônus: R$", dinheiro)