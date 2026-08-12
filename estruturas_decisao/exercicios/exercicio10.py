def desconto():
    valor = float(input("Qual o valor da compra: "))
    DESCONTO_PRECO10 = 0.10
    DESCONTO_PRECO15 = 0.15

    if valor <101:
        print(f"Sem desconto o valor da compra ainda sera {valor}")
    elif valor >100 and valor <=500:
        calcular_procento = valor * DESCONTO_PRECO10
        total10 = valor - calcular_procento
        print(f"O desconto sera {calcular_procento}")
        print(f"O valor da compra sera {total10}")
    else:
        calcular_procento = valor * DESCONTO_PRECO15
        total15 = valor - calcular_procento
        print(f"O desconto sera {calcular_procento}")
        print(f"O valor da compra sera {total15}")

desconto()