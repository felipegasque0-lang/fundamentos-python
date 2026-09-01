def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 30, 22, 28, 26]

resultado = analisar_temperaturas(temperaturas)

print(f"Quantidade: {resultado[0]}")
print(f"Soma: {resultado[1]}")
print(f"Média: {resultado[2]}")
print(f"Temperaturas ordenadas: {resultado[3]}")