def maior_numero():
    maior = None
    continuar = "s"

    while continuar == "s":
        numero = int(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ")

    print(f"O maior número é: {maior}")


maior_numero()