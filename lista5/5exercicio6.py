# 6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
# que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
# # usuário para inserir as horas e minutos, e exiba o tempo total em minutos.

def tempo_total (h, m):
    total = (h*60) + m
    return total

horas = int(input("Digite o total de horas: "))
minutos = int(input("Digite o total de minutos: "))
resultado = tempo_total(horas, minutos)
print ("O tempo total foi: ",resultado)