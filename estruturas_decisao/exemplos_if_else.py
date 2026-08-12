def aluno_aprovado():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    print(f"A media do aluno é: {media} ")

    if media >= 6:
        print("Aluno aprovado!")
    elif media >=5 and media <6:
        print("Aluno de recuperação!")
    else:
        print("Aluno reprovado!")

# aluno_aprovado()

def login():
    e_mail = "felipe@gmail.com"
    senha = "1234"
    codigo_secreto = "#456@"


    e_mail_input = input("Digite seu e-mail: ")
    senha_input = input("Digite sua senha: ")

    if e_mail_input == e_mail and senha_input == senha:
        print("Usuário Logado!")
        acessar_admin = input("Deseja acessar are administrativa (Digite S para ou N)? : ")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite o codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("Acesso adm Líberado!")
            else:
                print("Código secreto errado!")
        elif acessar_admin == "N":
            print("Ok. você acessou "
                  "como usuário comum!")
        else:
            print("Opção invalida!")
    else:
        print("E-mail ou senha incorreto!")

login()
