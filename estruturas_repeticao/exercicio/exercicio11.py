def fatorial():
    fatorial = 1

    valor = int(input("Digite um valor: "))
    for i in range (1, valor + 1):
        fatorial = fatorial * i

    print(f"O fatorial de {valor} é: {fatorial}")

fatorial()
