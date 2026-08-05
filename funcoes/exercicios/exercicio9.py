def conversão_centimetros():
    metros = float(input("digite a quantidade de metros: "))
    converter = metros * 100
    return converter

convercao = conversão_centimetros()
print(f"O valor em centimetros é: {convercao}")