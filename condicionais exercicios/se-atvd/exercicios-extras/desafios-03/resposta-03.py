dinheiro = float(input("Quanto dinheiro Mikaelly possui? R$ "))

ingresso = 900
passagem = 600
hospedagem = 400

custo_total = ingresso + passagem + hospedagem

if dinheiro >= custo_total:
    sobra = dinheiro - custo_total
    print("Mikaelly vai realizar seu sonho!")
    print("Dinheiro que sobrará: R$", sobra)
else:
    falta = custo_total - dinheiro
    print("Ainda falta economizar!")
    print("Dinheiro que falta: R$", falta)