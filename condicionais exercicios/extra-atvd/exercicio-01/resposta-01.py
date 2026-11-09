cor = input("Digite a cor da pulseira: ")

if cor == "Vermelha":
    print("Emergência - Atendimento imediato.")
elif cor == "Amarelo":
    print("urgente - Atendimento rápido.")
elif cor == "Verde":
    print("pouco urgente - Aguade sua vez.")
elif cor == "Azul":
    print("não urgente - encaminhado para o posto.")
else:
    print("cor inválida. procure a recepção")