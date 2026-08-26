def inserir_alunos(alunos, nome, posicao):


    alunos.insert(posicao, nome)

    for nome in alunos:
        print(f"O nome da lista é {nome}")
    print(f"O nome {nome} foi inserido na posição {posicao} da lísta:{alunos}")



lista_nomes = ["Gabriel", "Manoel", "Murillo"]
nome = input("Digite o nome: ")
posicao = int(input("digite a posição que ele ficara:"))

inserir_alunos(lista_nomes, nome, posicao)



