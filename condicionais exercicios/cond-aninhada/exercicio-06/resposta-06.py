codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print("Notebook")
    case 2:
        print("Mouse")
    case 3:
        print("Teclado")
    case 4:
        print("Monitor")
    case 5:
        print("Impressora")
    case _:
        print("Código inválido!")