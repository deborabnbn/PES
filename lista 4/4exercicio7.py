# 7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
# informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
# não existam notas cadastradas, seu programa deve informar “Erro: não há notas
# cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
# programa:
# Notas
# -----
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 4 - Calcular média
# 5 – Mostrar maior nota
# 6 – Mostrar menor nota
# 0 - Sair
# Opção:
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
        5 – Mostrar maior nota
        6 – Mostrar menor nota
        0 - Sair
        """)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nota = int(input("digite sua nota: "))
        notas.append(nota)
        total_notas = total_notas + 1
        soma_notas += nota

    elif opcao == 2:
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

        indice = 0
        while indice < len(notas):
            print(notas[indice])
            indice = indice + 1

        if len(notas) == 0:
            print ("a lista está vazia")

    elif opcao == 4: 
        media = soma_notas/total_notas
        print(media)


        if media >= 6:
            print("aluno aprovado!")
        else: 
            print("reprovado")
        
    elif opcao == 5:
        maior_nota = notas[0]
        indice = 1
        while indice <len(notas):
            if notas[indice] > maior_nota:
                maior_nota = notas[indice]
            indice = indice+1
        
        print(maior_nota)

    elif opcao == 6:
        menor_nota = notas[0]
        indice = 1
        while indice < len(notas):
            if notas[indice] < menor_nota:
                menor_nota = notas[indice]
            indice = indice+1
        
        print(menor_nota)

    if len(notas) == 0:
        print("Erro: não há notas cadastradas")