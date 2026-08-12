def preco_ingresso():
    idade = int(input("Digite sua idade: "))

    if idade < 6:
        print("Ingresso gratuito")
    elif idade >= 6 and idade < 13:
        print("Ingresso R$ 10")
    elif idade >= 13 and idade < 60:
        print("Ingresso R$ 20")
    else:
        print("Ingresso R$ 10")

preco_ingresso()
