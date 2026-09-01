def ordear_nomes(nomes):
    quantidade = sorted(nomes)

    for nome in nomes:
        print(f"A lista de nomes são {nome}")
    print(f"A lista de nomes organizadas em ordem alfabeticas é {quantidade}")


lista_nomes = ["Pedro", "Felipe", "Manoel"]

ordear_nomes(lista_nomes)