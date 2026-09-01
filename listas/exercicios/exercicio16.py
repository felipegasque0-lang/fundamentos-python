def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    print(f"Ranking: {ranking}")


lista_pontuacoes = [8, 5, 10, 7, 9]

criar_ranking(lista_pontuacoes)