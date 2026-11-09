gols_a = int(input("Digite os gols do time A: "))
gols_b = int(input("Digite os gols do time B: "))

if gols_a > gols_b:
    print("O time A venceu!")
elif gols_b > gols_a:
    print("O time B venceu!")
else:
    print("Empate!")