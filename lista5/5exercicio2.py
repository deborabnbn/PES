# 2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
# ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
# resultado na tela.

def impar_ou_par(valor):
    if (valor % 2) != 0:
        print("é impar")
    else:
        print("é par")

numero = int(input("digite um número: "))
impar_ou_par(numero)