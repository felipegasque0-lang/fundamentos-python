def ordear_nomes(nomes):
    quantidade = sorted(nomes, reverse=True)

    for nome in nomes:
        print(f"A lista de nomes são {nome}")
    print(f"A lista de nomes invertidas {quantidade}")


lista_nomes = ["Pedro", "Felipe", "Manoel"]

ordear_nomes(lista_nomes)