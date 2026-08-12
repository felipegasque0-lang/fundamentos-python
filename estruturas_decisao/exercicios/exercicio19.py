def classificacao():
    numero = int(input("Digite um numero inteiro: "))

    if numero % 2 == 0:
         par_impar="O seu numero é par"
    else:
        par_impar = "O seu numero é impar"

    if numero < 0:
        classificar = "Numero negativo"
    elif numero > 0:
        classificar = "Numero positivo"
    else:
        classificar = "Numero zero"

    print(f"numero: {numero}")
    print(f"Classificacao: {classificar}, {par_impar}")

classificacao()