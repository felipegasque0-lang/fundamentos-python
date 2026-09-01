def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = (total / quantidade)

    for nota in notas:
        print(f"As notas são: {nota}")
    print(f"A quantidade de notas são: {quantidade}")
    print(f"A média das notas é: {media}")



lista_notas = [7.2, 6.8, 10, 9.0]


calcular_media(lista_notas)