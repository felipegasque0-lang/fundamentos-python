def preco_desconto():
    preco = float(input(f"Qual o preco do produto: "))
    desconto = float(input(f"Quantos porcento você tem de desconto do produto: "))
    calcular_desconto = preco * desconto / 100
    calcular_total = preco - calcular_desconto
    return calcular_total

total_desconto = preco_desconto()
print(f"O preço com o desconto ficou {total_desconto}")
