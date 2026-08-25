def tabuada():
    soma = 0

    valor = int(input("Digite um numero inteiro: "))

    for i in range(1, valor + 1):
        soma = soma + i
    print(f"A soma é: {soma}")

tabuada()

