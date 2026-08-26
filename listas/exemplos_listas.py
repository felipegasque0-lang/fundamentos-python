def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é {nome}")

lista_de_nomes = ["Renan", "Moises", "Rafael", "Ana", "Clayton"]
mostrar_nomes(lista_de_nomes)

# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(lista_de_nomes, "Manoel")

# Adicionando novo nome em uma posição específica
def adicionar_nome_posição(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lísta:{nomes}")

adicionar_nome_posição(lista_de_nomes, "Rogério", 2)

# Jnutando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes}  foram inseridos na lista {nomes}")

novos_nomes = ["Francisco", "Márcio"]

juntar_nomes(lista_de_nomes, novos_nomes)

# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido da lista {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "Márcio")

# Removendo nome pelo indice
def remover_anome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} é {nomes[posicao]}, foi removido!")

remover_anome_pelo_indice(lista_de_nomes, 4)

# Descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")

encontrar_posicao_pelo_valor(lista_de_nomes, "Moises")

# contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"Quantidade de nomes é: {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# Ordenando os ewlementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista de nomes ordenada é {lista_de_nomes_ordenados}")

ordenar_nomes(lista_de_nomes)

# Operações matemáticas
# Calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = (total / quantidade)
    print(f"A média das notas é {media}")

notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]


calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media =  sum(notas) / len(notas)

    return ordenadas, media

notas_ordenas, media = gerenciar_notas(notas_semestre, 3.5)
print(f"notas ordenadas = {notas_ordenas}")
print(f"A média das notas media = {media}")

#Lista de listas
def adicionar_produtos(produtos, produto):
    produtos.append(produto)
    print(f"Minha lista de produtos: {produtos[0][2]}")


lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50]
]
novo_produto = ["Café",2, 28.00]
adicionar_produtos(lista_produtos, novo_produto)

def quantidade_total_produtos(produtos):
    quantidades = []

    for produto in produtos:
        quantidades.append(produto[1])

    return sum(quantidades)


quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"Quantidade total de produtos é {quantidade_produtos}")

def valor_total_produtos(produtos):
    valores = []
    for produto in produtos:
        valores.append(produto[2] * produto[1])


    return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f"O valor total dos produtos é {preco_total_produtos}")
