def verificar_primo():
    valor = int(input("Digite um numero"))

    if valor < 2:
        return False

    for i in range(2, valor):
        if valor % i == 0:
            return False

    return True


resultado = verificar_primo()

print(resultado)