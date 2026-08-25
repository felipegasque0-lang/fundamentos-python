def mostrar_multiplos():
    valor = float(input("Digite um valor: "))
    for i in range (1, 11):
        multiplo = valor * i
        print(f"{valor} x {i} = {multiplo}")

mostrar_multiplos()
