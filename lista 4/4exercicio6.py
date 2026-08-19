# 6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
# programa deve permitir que notas sejam cadastradas ou removidas (através do seu
# índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
# deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
# avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
# calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
# e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
# com o seu programa:
# Notas
# -----
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 4 - Calcular média
# 0 - Sair
# Opção:

def listar_notas(lista_notas):
    print("Notas:")
    indice = 0
    while indice < len(lista_notas):
        print(" -", lista_notas[indice])
        indice = indice + 1

    if len(lista_notas) == 0:
        print ("- Lista está vazia")

notas = []
total_notas=0 
soma_notas=0
opcao = -1
while opcao != 0:

    print ("""
        1 - Cadastrar
        2 - Excluir
        3 - Listar
        4 - Calcular média
        0 - Sair
        """)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nota = int(input("digite sua nota: "))
        notas.append(nota)
        total_notas = total_notas + 1
        soma_notas += nota

    elif opcao == 2:
        listar_notas(notas)
        excluir_nota = input("digite nota que você deseja excluir: ")
        
        indice =  0
        posicao = -1
        while indice < len(notas):
            if notas[indice] == nota:
                posicao = indice
                break
            indice = indice +1
        if posicao != -1:
            print("removendo posicao")
            notas.pop(posicao)
            print("nota removida!")

    elif opcao == 3:
        listar_notas(notas)

    elif opcao == 4: 
        media = soma_notas/total_notas
        print(media)


        if media >= 6:
            print("aluno aprovado!")
        else: 
            print("reprovado")




