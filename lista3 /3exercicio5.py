# 5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
# programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
# sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
# ser através de um menu com as seguintes opções:
# 1 – Cadastrar
# 2 - Excluir
# 3 - Alterar
# 4 - Listar
# 0 - Sair
# A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
# excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
# solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
# da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
# das pessoas cadastradas. 


nomes = []
idades = []
alturas = []
pesos = []

opcao = -1

while opcao != 0:
    print("""
        Escolha uma das opções:
          [1] - Cadastrar
          [2] - Excluir
          [3] - Alterar
          [4] - Listar
          [0] - Sair
    """)

    opcao = int(input("Digite opcao: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

        print("Deu tudo certinho!")

    elif opcao == 2:

        nome = input("Digite o nome que deseja excluir: ")

        posicao = -1
        indice = 0

        while indice < len(nomes):
            if nomes[indice] == nome:
                posicao = indice
                break

            indice = indice + 1

        if posicao != -1:
            print("Removendo cadastro...")

            nomes.pop(posicao)
            idades.pop(posicao)
            alturas.pop(posicao)
            pesos.pop(posicao)

            print("Cadastro removido com sucesso!")

        else:
            print("Pessoa não encontrada.")

    elif opcao == 3:

        nome = input("Digite o nome que deseja alterar: ")

        posicao = -1
        indice = 0

        while indice < len(nomes):
            if nomes[indice] == nome:
                posicao = indice
                break

            indice = indice + 1

        if posicao != -1:
            print("Digite as novas informações:")

            idades[posicao] = int(input("Digite a nova idade: "))
            alturas[posicao] = float(input("Digite a nova altura: "))
            pesos[posicao] = float(input("Digite o novo peso: "))

            print("Cadastro alterado com sucesso!")

        else:
            print("Pessoa não encontrada.")

    elif opcao == 4:

        indice = 0

        while indice < len(nomes):

            print("-------------------------")
            print("Nome:", nomes[indice])
            print("Idade:", idades[indice])
            print("Altura:", alturas[indice])
            print("Peso:", pesos[indice])

            indice = indice + 1

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")

