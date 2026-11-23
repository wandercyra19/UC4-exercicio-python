atividade 7:contagem de numeros positivos e negativos


positivos = 0
negativos = 0

for i in range(8):
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
