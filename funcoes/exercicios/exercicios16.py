def IMC():
    ler_peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    IMC = ler_peso / (altura ** 2)
    return IMC

IMC_total = IMC()
print(f"O seu IMC é: {IMC_total}")