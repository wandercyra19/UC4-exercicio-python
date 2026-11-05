ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2026- ano_nascimento
if idade  >= 18:
    print("voto obrigatorio")
elif idade < 16:
    print("voto proibido")
else:
    print("voto opcional")