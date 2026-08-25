def calcular_media():
    soma = 0
    quantidade = 0
    numero = 1

    while numero != 0:
        numero = float(input("Digite um número (0 para parar): "))

        if numero != 0:
            soma = soma + numero
            quantidade = quantidade + 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"A média é: {media}")
    else:
        print("Nenhum número foi informado.")


calcular_media()