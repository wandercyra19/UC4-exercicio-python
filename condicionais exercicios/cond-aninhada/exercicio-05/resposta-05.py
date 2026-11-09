num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

match operador:
    case "+":
        print("Resultado:", num1 + num2)

    case "-":
        print("Resultado:", num1 - num2)

    case "*":
        print("Resultado:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero.")

    case _:
        print("Operador inválido!")