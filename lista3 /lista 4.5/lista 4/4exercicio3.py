# 3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
# formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
# deve fazer isso de duas formas: com while e com for.
# Exibição com while:
# Nota: 9.0
# Nota: 7.5
# Nota: 8.0
# Exibição com for:
# Nota: 9.0
# Nota: 7.5
# Nota: 8.0

# notas = []

# total_notas = int(input("digite o total de notas: "))

# indice = 0
# while indice < total_notas:
#     nota = input("digite sua nota: ")
#     notas.append(nota)
#     indice = indice + 1
# indice = 0 
# while indice < len(notas):
#     print("Nota:", float(notas[indice]))
#     indice = indice + 1


notas = []

total_notas = int(input("digite o total de notas: "))

indice = 0
while indice < total_notas:
    nota = input("digite sua nota: ")
    notas.append(nota)
    indice = indice + 1
# o nota no "for nota in notas" pode ser qualquer palavra
for nota in notas:
    print("Nota:", float(nota))
    indice = indice + 1