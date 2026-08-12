def numero_maior():
    numero01 = float(input("Digite o primeiro numero: "))
    numero02 = float(input("Digite o segundo numero: "))

    if numero01 > numero02:
        print(f"O numero {numero01} é maior")
    elif numero02 > numero01:
        print(f"O numero {numero02} é maior")
    else:
        print("Os numeros são iguais")

numero_maior()