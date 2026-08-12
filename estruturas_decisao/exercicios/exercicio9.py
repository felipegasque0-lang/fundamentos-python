def calculadora():
    numero01 = float(input("Digite o primeiro valor: "))
    numero02 = float(input("Digite o segundo valor: "))
    total_soma = numero01 + numero02
    total_subtracao = numero01 - numero02
    total_multiplicacao = numero01 * numero02

    operacao = (input("digite a operacao que deseja (digite: + - * / : ")  )

    if operacao == "+":
        print(f"O resultado da operacao é {total_soma}")
    elif operacao == "-":
        print(f"O resultado da subtracao é {total_subtracao}")
    elif operacao == "*":
        print(f"O total da multiplicação é {total_multiplicacao}")
    elif operacao == "/":
        if numero02 != 0:
            total_division = numero01 / numero02
            print(f"O total da divisao da {total_division}")
        else:
            print("Não é possivel calcular")

calculadora()

