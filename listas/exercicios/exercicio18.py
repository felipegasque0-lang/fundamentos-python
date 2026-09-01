def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 30, 22, 28, 26]

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)

print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Temperaturas ordenadas: {ordenadas}")