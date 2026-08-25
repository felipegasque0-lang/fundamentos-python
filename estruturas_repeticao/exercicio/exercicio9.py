def contar_pares():
    inicio = int(input("digite um numero inicial: "))
    fim = int(input("digite um numero final: "))
    for i in range (inicio, fim+1):
        if i % 2 == 0:
            print(i)


contar_pares()