# 6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
# baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
# o nome da pessoa como critério de busca.

nomes = []
idades = []
alturas = []
pesos = []
codigo = []

opcao = 1

while opcao != 0:
    print("""
        Escolha uma das opções:
          [1] - Cadastrar
          [2] - Excluir
          [3] - Alterar
          [4] - Listar
          [5] - Pesquisar
          [0] - Sair
    """)

    opcao = int(input("Digite opcao: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        cod = input("Digite o código: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        nomes.append(nome)
        codigo.append(cod)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

        print("Deu tudo certinho!")

    elif opcao == 2:

        cod = input("Digite o código da pessoa que vocẽ deseja excluir: ")

        posicao = -1
        indice = 0

        while indice < len(nomes):
            if codigo[indice] == cod:
                posicao = indice
                break

            indice = indice + 1

        if posicao != -1:
            print("Removendo cadastro...")

            nomes.pop(posicao)
            codigo.pop(posicao)
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

            print("Nome:", nomes[indice])
            print("Idade:", idades[indice])
            print("Altura:", alturas[indice])
            print("Peso:", pesos[indice])

            indice = indice + 1

    elif opcao == 5:

        nome = input("Digite o nome da pessoa que deseja pesquisar: ")

        posicao = -1
        indice = 0

        while indice < len(nomes):
            if nomes[indice] == nome:
                posicao = indice
                break

            indice = indice + 1

        if posicao != -1:
            print("Pessoa encontrada!")
            print("Nome:", nomes[posicao])
            print("Código:", codigo[posicao])
            print("Idade:", idades[posicao])
            print("Altura:", alturas[posicao])
            print("Peso:", pesos[posicao])

        else:
            print("Pessoa não encontrada.")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")

