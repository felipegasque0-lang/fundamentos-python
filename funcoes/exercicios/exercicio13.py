def comissao_vendendor():
    salario = float(input(f"Qual o seu salario fixo : "))
    vendas = float(input(f"Quanto arrecadou de vendas : "))
    comissao_vendas = float(input(f"Qual a procentagem voce recebe da comissao: "))
    calcula_comussao = comissao_vendas * vendas / 100
    salario_final = salario + calcula_comussao
    return salario_final

final = comissao_vendendor()
print(f"O seu salaria final é: {final}")