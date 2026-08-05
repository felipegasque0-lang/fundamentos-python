def exibir_mensagem():
    print("Hello World!!!!!!!!!")

def somar():
    valor1 =50
    valor2 =60
    total = valor1 + valor2
    print(f"O resultado da soma é {total}")


def calcular_media():
    nota1 = float(input("digite a nota da primeira prova: "))
    nota2 = float(input("digite a nota da segunda prova: "))
    media = (nota1 + nota2) / 2
    return media

exibir_mensagem()
somar()

nota_final = calcular_media()
print(f"A nota final é {nota_final}")