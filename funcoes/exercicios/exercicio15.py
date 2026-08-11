def conversao_de_idade():
    idade = int(input("digite sua idade: "))
    calcular_meses = idade * 12
    calcular_dias_ano = idade * 365
    print(f"sua idade em meses sao: {calcular_meses}. E sua idade em dias sao : {calcular_dias_ano}")

conversao_de_idade()