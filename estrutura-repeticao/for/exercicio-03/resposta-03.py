atividade 3: media de nota

soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 4

print(f"\nMédia final: {media:.2f}")
