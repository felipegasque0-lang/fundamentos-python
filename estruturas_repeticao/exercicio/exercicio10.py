def soma_numeros():
    soma = 0
    inicio = int(input("digite um numero inicial: "))
    fim = int(input("digite um numero final: "))
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma = soma + i
    print(f"O valor total é {soma}")

soma_numeros()