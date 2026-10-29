saldo = float(input("Digite o saldo de créditos do usuário: "))

if saldo < 20:
    saldo = saldo + 15

print("O saldo atualizado é:", saldo, "créditos")