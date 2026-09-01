notas = [7.5, 6.0, 8.5, 9.0, 5.5]


def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima(notas):
    notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_inversas(notas):
    return list(reversed(notas))


def calcular_soma(notas):
    return sum(notas)


def calcular_media(notas):
    return sum(notas) / len(notas)



adicionar_nota(notas, 10)


inserir_nota(notas, 8.0, 2)


adicionar_varias(notas, [7.0, 9.5])

remover_nota(notas, 6.0)


remover_ultima(notas)


posicao = encontrar_nota(notas, 8.5)


quantidade = quantidade_notas(notas)


ordenadas = ordenar_notas(notas)


inversas = notas_inversas(notas)


soma = calcular_soma(notas)


media = calcular_media(notas)


print("Notas atuais:", notas)
print("Posição da nota 8.5:", posicao)
print("Quantidade de notas:", quantidade)
print("Notas ordenadas:", ordenadas)
print("Notas em ordem inversa:", inversas)
print("Soma das notas:", soma)
print("Média da turma:", media)