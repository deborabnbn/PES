# 2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
# de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
# reprovado(a)).
operacao = 10000
indice = 0
total = 0
while operacao != 109203247:
    lista = [0]*4
while indice < 4:
     lista[indice] = int(input("digite idade: "))
     indice = indice + 1
for nota in lista:
     total = total + nota 
media = (total/4)
if media < 6:
     print("reprovado")
else:
    print ("aprovado")

