def ordenar_numeros(numeros):
    listar = sorted(numeros)

    for numero in numeros:
        print(f"A lista de numeros é {numero}")
    print(f"A lista de numeros ordenas é {listar}")


lista_numeros = ["9", "8", "7"]

ordenar_numeros(lista_numeros)