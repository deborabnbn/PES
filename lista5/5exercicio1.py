# 1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
# notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.

def media_aritmetica(numero1,numero2,numero3):
    media = (numero1+numero2+numero3)/3
    print(media)


v1 = float(input("digite a primeira nota: "))
v2 = float(input("digite a segunda nota: "))
v3 = float(input("digite a terceira nota: "))

media_aritmetica(v1, v2, v3)