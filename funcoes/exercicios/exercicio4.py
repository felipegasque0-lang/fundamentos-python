def media():
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    nota3 = float(input("digite a terceira nota: "))
    media_usuraio =(nota1 + nota2 + nota3) / 3
    return media_usuraio

nota_final = media()

print(f"A nota média é {nota_final}")