def adicionar_notas(notas,nota):
    for numeros in notas:
        print(f"As nota são {numeros}")

    notas.append(nota)



    print(f"A nova nota adicionada é: {nota} e foi inserida em: {notas}")


lista_notas = [7.3, 8.4, 6.7]

nota = float(input("digite uma nota: "))


adicionar_notas(lista_notas,nota)

def remover_notas(notas,nota):
    for numeros in notas:
        print(f"As nota são {numeros}")

    notas.remove(nota)

    print(f"As notas restantes após excluir a nota: {nota} é {notas}")

remover = float(input("digite a nota que deseja remover: "))

remover_notas(lista_notas,remover)


def media_notas(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = (total / quantidade)

    for numeros in notas:
        print(f"Os numeros são {numeros}")
    print(f"A quantidade é: {quantidade}")
    print(f"A media deles é: {media}")

media_notas(lista_notas)