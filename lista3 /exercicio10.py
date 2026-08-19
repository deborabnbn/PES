# 10 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os
# números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
# números digitados, assim como a soma e a média aritmética.
numero = 10
n = 0
soma = 0
while numero != 0:
    numero = int(input("numero: "))
    soma = soma + numero
    print (n)
    n = n + 1
media = soma/(n-1)
print (media)
print (soma)
