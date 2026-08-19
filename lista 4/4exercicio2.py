# 2 – Crie um programa que registrará as notas de um estudante. O programa deve
# perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
# notas e, ao final, exibir todas as notas digitadas na tela

notas = []

total_notas = int(input("digite o total de notas: "))

indice = 0
while indice < total_notas:
    nota = input("digite sua nota: ")
    notas.append(nota)
    indice = indice + 1
indice = 0 
while indice < len(notas):
    print(notas[indice])
    indice = indice + 1
    
