def contar_dez():
    valor = int(input("Digite um valor inteiro: "))
    for i in range (1, valor + 1):
        if i % 2 != 0:
            print(i)

contar_dez()