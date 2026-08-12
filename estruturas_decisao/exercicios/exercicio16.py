def sistema_login():
    usuario = "admin"
    senha = "1234"

    usuario_input = input("Digite o usuario: ")
    senha_input = input("Digite a senha: ")

    if usuario_input == usuario and senha_input == senha:
        print("Login realizado com sucesso")
    elif usuario_input == usuario and senha_input != senha:
        print("Senha incorreta")
    elif usuario_input != usuario and senha_input == senha:
        print("Usuario incorreto")

sistema_login()