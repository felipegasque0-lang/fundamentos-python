def temperatura():
    graus_celsius = float(input("Qual a temperatura em graus celsius? "))

    if graus_celsius < 15:
        print("frio")
    elif graus_celsius >= 15 and graus_celsius <= 25:
        print("Agradavel")
    else:
        print("Quente")

temperatura()