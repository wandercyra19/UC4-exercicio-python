cargo = input("Digite o cargo (Administrativo ou Operacional): ")
tempo = int(input("Digite o tempo de empresa em anos: "))

if cargo.lower() == "administrativo":
    if tempo >= 5:
        print("Pode receber promoção.")
    else:
        print("Ainda não está apto para promoção.")

elif cargo.lower() == "operacional":
    if tempo >= 3:
        print("Pode receber promoção.")
    else:
        print("Ainda não está apto para promoção.")

else:
    print("Erro: cargo inválido.")