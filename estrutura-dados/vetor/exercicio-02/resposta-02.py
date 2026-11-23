atividade 2: controle de passageiro

passageiros = ["Miguel", "Giuliany", "Rhaldney", "Mikaelly", "Kauany"]

print("Passageiros iniciais:", passageiros)

passageiros.append("Cauã")

if "Jonatha" in passageiros:
    passageiros.remove("Jonatha")

passageiros[3] = "Anna"

print("Quantidade atual de passageiros:", len(passageiros))

print("Lista atualizada de passageiros:")

for passageiro in passageiros:
    print(passageiro)
