def area_retangulo():
    base = float(input("digite o valor da base: "))
    altura = float(input("digite o valor da altura: "))
    calculararea = (base * altura)
    return calculararea

area = area_retangulo()

print(f"A area do retângulo é {area}")