def caixa_eletronico():
    saldo = float(input("Qual o seu saldo?"))
    sacar = float(input("Qual o valor que você quer sacar?"))
    total_sobra = saldo - sacar

    if sacar > saldo:
        print("Saldo insuficiente")
    elif sacar <=0:
        print("valor de saque inválido")
    else:
        print(f"Foi possivel sacar {sacar} do seu saldo")
        print(f"Seu valor restante de saldo é: {total_sobra}")

caixa_eletronico()