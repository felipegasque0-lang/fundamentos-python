def faixa_etaria():
    idade = int(input("Digite sua idade: "))

    if idade <13:
        print("Criança")
    elif idade >= 13 and idade < 18:
        print("Adolescente")
    elif idade >= 18 and idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

faixa_etaria()