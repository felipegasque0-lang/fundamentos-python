def quantidade_elementos(lista):
    quantidade = len(lista)

    for iten in lista:
        print(f"os itens da lista são {iten}")
    print(f"Quantidade de itens da lista {quantidade}")
    return quantidade



lista_produtos = ["banana", "maça", "melancia"]


quantidade_elementos(lista_produtos)