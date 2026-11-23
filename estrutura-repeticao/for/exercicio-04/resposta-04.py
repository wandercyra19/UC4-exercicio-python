atividade 4: pesquisa de satisfaçao

soma = 0

for i in range(1, 6):
    nota = int(input(f"Digite a nota do cliente {i} (1 a 5): "))
    soma += nota

media = soma / 5

print(f"\nSoma das notas: {soma}")
print(f"Média de satisfação: {media:.2f}")
