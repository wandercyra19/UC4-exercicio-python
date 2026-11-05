participantes = int(input("Digite a quantidade de participantes inscritos: "))
orcamento = float(input("Digite o orçamento disponível: R$ "))

if participantes >= 20 and orcamento >= 500:
    orcamento = orcamento + 200
    print("Festival aprovado!")
    print("Orçamento final: R$", orcamento)
else:
    print("Festival não aprovado.")
    print("Orçamento final: R$", orcamento)