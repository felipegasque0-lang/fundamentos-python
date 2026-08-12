def classificar_velocidade():
    velocidade = float(input("Insira a velocidade do veiculo: "))

    if velocidade <60:
        print("Velocidade permitida")
    elif velocidade > 60 and velocidade < 81:
        print("Atenção: veocidade acima do permitido")
    else:
        print("Multa por excesso de velocidade")

classificar_velocidade()