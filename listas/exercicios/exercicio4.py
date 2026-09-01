def remover_produtos(produtos, produto):
    produtos.remove(produto)
    for item in produtos:
        print(f"A lista é {item}")
    print(f"O produto {produto} foi removido da lista de produtos: {produtos}")




lista_produtos = ["maça", "banana", "pera"]
produto = input("Digite o nome do produto que deseja retirar: ")

remover_produtos(lista_produtos, produto)