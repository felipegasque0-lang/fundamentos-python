def imc():
    peso = float(input("Qual o seu peso?"))
    altura = float(input("Qual a sua altura?"))
    calculo = peso / (altura **2 )

    if calculo < 19:
        print("Abaixo do peso")
    elif 18.5 >= calculo <= 24.9:
        print("Peso normal")
    elif 25 >= calculo <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

imc()