execucoes = int(input("Digite a quantidade de execuções: "))
musicas = int(input("Digite o número inicial de músicas disponíveis: "))

if execucoes >= 10:
    musicas = musicas + 5

print("A quantidade final de músicas disponíveis é:", musicas)