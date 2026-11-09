tipo_usuario = input("Digite o tipo de usuário (Administrador, Supervisor ou Operador): ")
status_conta = input("Digite o status da conta (Ativa ou Bloqueada): ")

if status_conta.lower() == "ativa":
    if tipo_usuario.lower() == "administrador":
        print("Acesso total.")
    elif tipo_usuario.lower() == "supervisor":
        print("Acesso gerencial.")
    else:
        print("Acesso operacional.")

elif status_conta.lower() == "bloqueada":
    print("Acesso negado. Conta bloqueada.")

else:
    print("Status da conta inválido.")