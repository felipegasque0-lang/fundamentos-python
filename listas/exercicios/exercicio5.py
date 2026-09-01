def remover_item(itens, posicao):
    item_removido = itens.pop(posicao)

    for iten in itens:
        print(f"A lista de produtos é {iten}")
    print(f"O item removido foi {item_removido}")

    return item_removido




lista_itens = ["garrafa", "celular", "controle"]
posicao = int(input("Digite a posicção que deseja retirar: "))

remover_item(lista_itens, posicao)