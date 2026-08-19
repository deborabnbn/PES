# 4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
# resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
# números ao usuário, chamar a função e exibir o resultado da soma na tela.

def soma_numeros(n1, n2, n3, n4):
    soma = n1 + n2 + n3 + n4
    print(soma)

num1 = int(input("digite o n1: "))
num2 = int(input("digite o n2: "))
num3 = int(input("digite o n3: "))
num4 = int(input("digite o n4: "))
soma_numeros(num1, num2, num3, num4)

