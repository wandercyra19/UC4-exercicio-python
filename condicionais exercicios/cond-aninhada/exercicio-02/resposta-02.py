situacao = input("Informe a situação do cliente (cadastrado ou não cadastrado): ")
cidade = input("Informe a cidade de entrega: ")
matriz = input("Informe a cidade da matriz: ")

if situacao.lower() == "cadastrado":
    if cidade.lower() == matriz.lower():
        print("Entrega liberada.")
    else:
        print("Vai para análise logística.")

elif situacao.lower() == "não cadastrado" or situacao.lower() == "nao cadastrado":
    if cidade.lower() == matriz.lower():
        print("Solicitar cadastro antes da entrega.")
    else:
        print("Entrega não permitida.")

else:
    print("Erro: situação do cliente inválida.")