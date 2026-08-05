def conversao_temperatura():
    celsius = float(input(f"Digite a temperatura em Celsius: "))
    converter = celsius * 1.8 + 32
    return converter

convertido = conversao_temperatura()
print(f"A conversão para fahrenheit dara: {convertido}")