# 4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
# um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
# lista. Seu programa deve ter um menu com a seguinte estrutura:
# 1 – Cadastrar
# 2 - Excluir
# 3 - Listar
# 0 - Sair
# A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
# houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
# disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
# nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
# simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
# um espaço vago na lista.
Automoveis = [-1]*15

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
        nova_placa = input("Digite nova placa: ")
        
        foi_possivel_inserir_na_lista = "não"

        indice = 0
        while indice < len(Automoveis):
            if Automoveis[indice] == -1:
                Automoveis[indice] = nova_placa
                    
                foi_possivel_inserir_na_lista = "sim"
                break
            indice = indice + 1

        if foi_possivel_inserir_na_lista == "sim":
            print("Deu tudo certinho!")
        else:
            print("Não há espaço disponível")
    elif opcao == 2:
        
        placa = input("digite placa: ")
        posicao = -1
        indice = 0 
        while indice < len(Automoveis): 
            if Automoveis[indice] == placa:
                posicao = Automoveis[indice]
            indice = indice +1

        if posicao != -1:
            print("removendo placa")
            posicao = -1
        else:
            print("placa não encontrada.")

    elif opcao == 3:
        indice = 0 
        while indice < len(Automoveis):
            
            if Automoveis[indice] != -1:
                print(Automoveis[indice])
                
            indice = indice +1
            