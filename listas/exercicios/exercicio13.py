def adicionar_cliente(fila, cliente):
    fila.append(cliente)


fila_cliente = []

while True:
    cliente = input("Digite o nome do cliente ou digite 'sair': ")

    if cliente == 'sair':
        break

    adicionar_cliente(fila_cliente, cliente)


def atender_cliente(fila):
    clientes = fila.pop(0)
    return clientes


if len(fila_cliente) > 0:
    cliente_atendido = atender_cliente(fila_cliente)
    print(f"O cliente atendido foi: {cliente_atendido}")
else:
    print("Não há clientes na fila.")