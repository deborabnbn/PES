# 5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
# Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
# conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
# amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
# Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
# Amigos Próximos
# ---------------
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 0 - Sair

lista = []
opcao = 1
while opcao != 0:  
    print("""
        Escolha uma das opções:
          [1] - Cadastrar 
          [2] - Excluir
          [3] - Listar 
          [0] - Sair
    """)
    opcao = int(input("digite opcao: "))
    if opcao == 1:
        novo_amigo = input("Digite novo amigo: ")
        
        lista.append(novo_amigo)
        
    elif opcao == 2:
        
        amigo = input("digite amigo: ")
        posicao = -1
        indice = 0 
        while indice < len(lista): 
            if lista[indice] == amigo:
                posicao = lista[indice]
            indice = indice +1

        if posicao != -1:
            print("removendo amigo")
            posicao = -1
        else:
            print("amigo não encontrada.")

    elif opcao == 3:
        if len(lista) != 0:

            indice = 0 
            while indice < len(lista):
                
                if lista[indice] != -1:
                    print(lista[indice])
                    
                indice = indice +1
            else:
                print("a lista esta vazia.")

    