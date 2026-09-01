def somar_numeros(numeros):
    total = sum(numeros)

    for numero in numeros:
        print(f"Os numeros são: {numero}")
    print(f"A soma desses numeros é: {total}")


lista_notas = [7.2, 6.8, 10, 9.0]

somar_numeros(lista_notas)