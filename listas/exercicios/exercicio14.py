def adicionar_produtos(compras,produtos):
    print(f"A lista de compras é {compras}")

    compras.extend(produtos)

    print(f"Os novos produtos {produtos}foram adicionados a lista de compras:{compras}")


lista_compras = ["maça", "banana", "pera"]
lista_produtos = ["controle", "teclado", "mouse"]

adicionar_produtos(lista_compras,lista_produtos)


def cancelar_produtos(compras,produto):

    print(f"A lista total de produtos é {compras}")

    compras.remove(produto)


    print(f"O produto {produto} foi cancelado da lista de compras:{compras}")

produto = input(f"Qual o nome do produto que deseja cancelar?")

cancelar_produtos(lista_compras, produto)