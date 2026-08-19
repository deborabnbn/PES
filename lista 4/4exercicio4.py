# 4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
# cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
# na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
# remoção dela e imprima a lista novamente.

cidades = []

total_cidades = int(input("digite o total de cidades: "))
indice = 0 
while indice < total_cidades:
    cidade = input("digite o nome da cidade: ")
    cidades.append(cidade)
    indice = indice + 1 
indice = 0 
while indice < len(cidades):
    print(cidades[indice])
    indice = indice + 1

remover = input("digite o nome da cidade que você deseja remover: ")

posicao = -1
indice = 0 
while indice < len(cidades):
    if cidades[indice] == remover:
        posicao = indice
    indice = indice + 1 
       
if posicao != -1:
    print("Removendo cidade...")
    cidades.pop(posicao)
else: 
    print("cidade não encontrada.")
   