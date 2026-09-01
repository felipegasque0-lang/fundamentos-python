def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)

    for achar in produtos:
        print(f"A lista de produtos é {achar}")
    print(f"A posição do produto {produto} é {posicao}")

    return posicao


lista_produtos = ["abacate", "maça", "banana"]
produto = input("Digite o nome do produto: ")



encontrar_produto(lista_produtos, produto)