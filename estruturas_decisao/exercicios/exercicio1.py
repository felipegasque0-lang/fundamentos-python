def numero():
    numero_inteiro = int(input("Digite um numero inteiro: "))

    if numero_inteiro >=1:
        print("Seu numero é positivo")
    elif numero_inteiro == 0:
        print("Seu numero é 0")
    elif numero_inteiro < 0:
        print("seu numero é negativo")

numero()
