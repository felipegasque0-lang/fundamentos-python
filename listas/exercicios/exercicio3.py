def adicionar_convidados(convidados, nome_convidados):

    for nome in convidados:
        print(f"A lista de convidado é {nome}")

    convidados.extend(nome_convidados)

    print(f"Os novos nomes {nome_convidados}  foram inseridos na lista {convidados}")

lista_convidados = ["Manoel", "Murillo", "Eduardo"]
nome_convidados = ["Manoel", "Kael"]

adicionar_convidados(lista_convidados, nome_convidados)