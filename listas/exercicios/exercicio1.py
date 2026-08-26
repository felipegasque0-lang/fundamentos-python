def adicionar_nomes(nomes,nome):
    for nome in nomes:
        print(f"O nome da lista é {nome}")
    nomes.append(nome)
    print(nomes)

lista_nomes = ["Gabriel", "Manoel", "Murillo"]

adicionar_nomes(lista_nomes,"Kael")