# Faça um programa que funcionará como um cadastro de códigos de produtos de uma
# loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
# os elementos da lista com -1, este valor indicará que o elemento está vago para o
# cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
# código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
# listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
# na hora de cadastrar um novo código e também não deve ser possível cadastrar um
# produto com o código -1. No momento do cadastro, não deve ser informado o valor do
# índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
lista = [-1]*3
opcao = -1
while opcao != 0:
    print("""
        Escolha uma das opções:
          [1] - Cadastrar novo código
          [2] - Listar códigos cadastrados
          [0] - Sair
    """)
    opcao = int(input("Digite: "))
    if opcao == 1:
        novo_codigo = input("Digite novo código: ")
        
        foi_possivel_inserir_na_lista = "não"

        indice = 0
        while indice < len(lista):
            if lista[indice] == -1:
                lista[indice] = novo_codigo
                foi_possivel_inserir_na_lista = "sim"
                break
            indice = indice + 1

        if foi_possivel_inserir_na_lista == "sim":
            print("Deu tudo certinho!")
        else:
            print("Deu tudo errado")

        # novo_codigo = input("Digite novo código: ")

        # espacos_disponiveis = 0
        # for espaco in lista:
        #     if espacos_disponiveis == -1:
        #         espacos_disponiveis = espacos_disponiveis + 1

        # if espacos_disponiveis == 0:
        #     print("não existe espaço disponível")
        # else:

        #     indice = 0
        #     while indice < len(lista):
        #         if lista[indice] == -1:
        #             lista[indice] = novo_codigo
        #             foi_possivel_inserir_na_lista = True
        #             break
        #         indice = indice + 1
                
        #     print("deu tudo certo!")


    if opcao == 2:
        for codigo in lista:
            print (codigo)

