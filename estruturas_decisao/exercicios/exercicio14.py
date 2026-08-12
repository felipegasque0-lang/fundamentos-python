def sistema_voto():
    idade = int(input("Digite sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade >= 16 and idade < 18:
        print("Voto opcional")
    elif idade >= 18 and idade < 70:
        print("voto obrigatorio")
    else:
        print("voto opcional")

sistema_voto()