def perimetro_retangulo():
    base = float(input("digite o valor da base: "))
    altura = float(input("digite o valor da altura: "))
    calculperimetro = 2 * (base + altura)
    return calculperimetro

area = perimetro_retangulo()

print(f"O perimetro do retângulo é: {area}")