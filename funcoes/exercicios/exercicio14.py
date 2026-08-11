def consumo_de_combuastivel():
    distancia_percorrida = float(input(f"Qual foi sua distancia percorrida em km : "))
    quantidade_combustivel = float(input(f"Qual a quantidade de combustivel em litro: "))
    consumo_medio = distancia_percorrida / quantidade_combustivel
    return consumo_medio

media = consumo_de_combuastivel()
print(f"O consumo médio é de : {media} litros por km")
