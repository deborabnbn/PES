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

amigos_proximos = []   
opcao = -1
while opcao != 0:
    print("escolha uma opcao: ")
    print("""
        1- Cadastrar
        2- Excluir
        3- Listar
        0- Sair
        """)
    opcao = int(input("digite opcao: "))

    if opcao == 1:
        novo_amigo = input("digite o nome do novo amigo: ")
        amigos_proximos.append(novo_amigo)
        print("Deu tudo certo!")

    elif opcao==2:
        excluir_amigo = input("digite o nome do amigo que você deseja excluir:  ")
        posicao = -1
        indice = 0
        while indice < len(amigos_proximos):
            if amigos_proximos[indice] == excluir_amigo:
                posicao = indice

            indice = indice +1
        if posicao != -1:
            print("removendo ex-amigo...")
            amigos_proximos.pop(posicao)

            print("cadastro removido com sucesso!")
        else:
            print("Amigo não encontrado.")

    elif opcao == 3:
        indice = 0 
        while indice < len(amigos_proximos):
            print(amigos_proximos[indice])
            indice = indice +1

        if len(amigos_proximos) == 0:
            print("a lista está vazia")

    
