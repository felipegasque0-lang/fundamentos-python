def classificar_trangulo():
    valor1 = float(input("Insira o valor do primeiro lado do triangulo: "))
    valor2 = float(input("Insira o valor do segundo lado: "))
    valor3 = float(input("Insira o valor do terceiro lado: "))

    if valor1 == valor2 and valor2 == valor3:
        print("Triangulo Equlatero")
    elif valor1 == valor1 or valor2 == valor3 or valor1 == valor3:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")

classificar_trangulo()