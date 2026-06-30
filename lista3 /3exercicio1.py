# 1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
# programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
# apresentar apenas as idades que forem maiores ou iguais a 16.
lista = [0]*6

indice = 0
while indice < 6:
    lista[indice] = int(input("digite idade: "))
    indice = indice + 1

for idade in lista:
    if idade >= 16:
        print (idade) 