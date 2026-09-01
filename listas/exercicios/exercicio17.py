def vender_produtos(estoque,produto):

    if produto not in estoque:
        print("Esse produto não existe na lista")
    else:
        estoque.remove(produto)
        print(f"O produto: {produto} foi removido a lista atualiza é {estoque}")

estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

pergunta = input("Qual o nome do produto: ")

vender_produtos(estoque, pergunta)