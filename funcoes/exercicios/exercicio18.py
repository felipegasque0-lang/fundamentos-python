def valor_prestacao():
    valor_produto = float(input("Digite o valor do produto: "))
    quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
    calcular_valor_parcelas = valor_produto / quantidade_parcelas
    return calcular_valor_parcelas

valor_final_parcelas = valor_prestacao()
print(f"O valor de cada parcela é: {valor_final_parcelas}")