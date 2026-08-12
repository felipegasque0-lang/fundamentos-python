def calcular_frete():
    compra = float(input("Qual o valor da compra?"))
    FRETE100 = 20
    total100 = compra + FRETE100
    FRETE101 = 10
    total101 = compra + FRETE101

    if compra < 101:
        print("Você terá R$20 de frete")
        print(f"O total com o frete fica {total100}")
    elif compra > 100 and compra <301:
        print(f"Você terá R$10 de frete")
        print(f"O total com o frete fica {total101}")
    else:
        print("Sua compra nao terá frete gratis")

calcular_frete()