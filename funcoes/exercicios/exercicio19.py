def consumo_de_energia():
    cosumo_kwh = float(input("Digite o valor consumido de kwh: "))
    preco_kwh = float(input("Quanto é preço do kwh: "))
    calcular_total = cosumo_kwh * preco_kwh
    return calcular_total

total = consumo_de_energia()
print(f"O preço total do consumo de energia é: {total}")