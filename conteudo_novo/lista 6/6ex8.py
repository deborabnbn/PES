# 8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
# deve ter um menu com as seguintes opções:
# Sistema de Cadastro
# -------------------
# 1 – Cadastrar estudante
# 2 – Cadastrar professor
# 3 – Listar estudantes
# 4 – Listar professores
# 5 – Alterar estudante pela matrícula
# 6 – Alterar estudante pelo nome
# 7 – Alterar professor pela matrícula
# 8 – Alterar professor pelo nome
# 9 – Excluir estudante pela matrícula
# 10 – Excluir professor pela matrícula
# 0 – Sair
# Opção: 

class Professor:
    def __init__ (self, matricula, nome, sobrenome, idade, especializacao):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao

    def dados_professor (self):
        return (" Matricula: " + str(self.matricula) + " Nome: " + self.nome + " Sobrenome: " + self.sobrenome + " Idade: " + str(self.idade) + " Especialização: " + self.especializacao)

class Aluno:
    def __init__ (self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados_aluno (self):
        return ("Matricula: " + str(self.matricula) + " Nome: " + self.nome + " Sobrenome: " + self.sobrenome + " Idade: " + str(self.idade))


lista_alunos = []
lista_professores = []
        
print("""
Sistema de Cadastro
-------------------
1 – Cadastrar estudante
2 – Cadastrar professor
3 – Listar estudantes
4 – Listar professores
5 – Alterar estudante pela matrícula
6 – Alterar estudante pelo nome
7 – Alterar professor pela matrícula
8 – Alterar professor pelo nome
9 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
0 – Sair
      """)

opcao = -1
while opcao != 0:
    opcao = int(input("digite uma opção: "))

    if opcao == 1:
        matricula = int(input("Digite a matricula do aluno: "))
        nome = input("Digite o nome do aluno: ")
        sobrenome = input("Digite o sobrenome da pessoa: ")
        idade = int(input("Digite a idade do aluno: "))
        
        aluno = Aluno(matricula, nome, sobrenome, idade)
        lista_alunos.append(aluno)

        print ("Aluno cadastrado com sucesso!")

    elif opcao == 2:
        matricula = int(input("Digite a matricula do professor: "))
        nome  = input("Digite o nome do professor: ")
        sobrenome = input("Digite o sobrenome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        especializacao =  input("Digite a especialização do professor: ")
        
        professor = Professor(matricula, nome, sobrenome, idade, especializacao)
        lista_professores.append(professor)

        print ("Professor cadastrado com sucesso!")

    elif opcao == 3:
        for aluno in lista_alunos:
            print (aluno.dados_aluno())

    elif opcao == 4:
        for professor in lista_professores:
            print (professor.dados_professor())

    elif opcao == 5:
        alterar_estudante = int(input("Digite a matrícula do estudante que você está procurando: "))
        indice_procurando = -1
        indice = 0

        while indice < len(lista_alunos):
            if lista_alunos[indice].matricula == alterar_estudante:
                indice_procurando = indice
            indice = indice + 1

        if indice_procurando == -1:
            print("Pessoa não encontrada.")
        else:
            lista_alunos[indice_procurando].matricula = int(input("Digite a nova matrícula: "))
            lista_alunos[indice_procurando].nome = input("Digite o novo nome: ")
            lista_alunos[indice_procurando].sobrenome = input("Digite o novo sobrenome: ")
            lista_alunos[indice_procurando].idade = int(input("Digite a nova idade: "))
            print("Aluno atualizado com sucesso!")

    elif opcao == 6:
        alterar_estudante = input("Digite o nome do estudante que você está procurando: ")
        indice_procurando = -1
        indice = 0

        while indice < len(lista_alunos):
            if lista_alunos[indice].nome == alterar_estudante:
                indice_procurando = indice
            indice = indice + 1

        if indice_procurando == -1:
            print("Aluno não encontrada.")
        else:
            lista_alunos[indice_procurando].matricula = int(input("Digite a nova matrícula: "))
            lista_alunos[indice_procurando].nome = input("Digite o novo nome: ")
            lista_alunos[indice_procurando].sobrenome = input("Digite o novo sobrenome: ")
            lista_alunos[indice_procurando].idade = int(input("Digite a nova idade: "))
            print("Aluno atualizado com sucesso!")

    elif opcao == 7:
        alterar_professor = int(input("Digite a matrícula do professor que você está procurando: "))
        indice_procurando = -1
        indice = 0

        while indice < len(lista_professores):
            if lista_professores[indice].matricula == alterar_professor:
                indice_procurando = indice
            indice = indice + 1

        if indice_procurando == -1:
            print("Professor não encontrado.")
        else:
            lista_professores[indice_procurando].matricula = int(input("Digite a nova matrícula: "))
            lista_professores[indice_procurando].nome = input("Digite o novo nome: ")
            lista_professores[indice_procurando].sobrenome = input("Digite o novo sobrenome: ")
            lista_professores[indice_procurando].idade = int(input("Digite a nova idade: "))
            lista_professores[indice_procurando].especializacao = (input("Digite a nova especializacao: "))
            print("Professor atualizado com sucesso!")

    elif opcao == 8:
        alterar_professor = input("Digite o nome do professor que você está procurando: ")
        indice_procurando = -1
        indice = 0

        while indice < len(lista_professores):
            if lista_professores[indice].nome == alterar_professor:
                indice_procurando = indice
            indice = indice + 1

        if indice_procurando == -1:
            print("Professor não encontrado.")
        else:
            lista_professores[indice_procurando].matricula = int(input("Digite a nova matrícula: "))
            lista_professores[indice_procurando].nome = input("Digite o novo nome: ")
            lista_professores[indice_procurando].sobrenome = input("Digite o novo sobrenome: ")
            lista_professores[indice_procurando].idade = int(input("Digite a nova idade: "))
            lista_professores[indice_procurando].especializacao = (input("Digite a nova especializacao: "))
            print("Professor atualizado com sucesso!")

    elif opcao == 9:
        excluir_aluno = input("Digite o nome do aluno que você deseja excluir: ")
        indice_porcurando = -1
        indice = 0

        while indice < len(lista_alunos):
            if lista_alunos[indice].nome == excluir_aluno:
                indice_porcurando = indice
            indice = indice + 1

        if indice_porcurando == -1:
            print("Aluno não encontrada.")
        else:
            lista_alunos.pop(indice_porcurando)
            print("Aluno removido com sucesso!")

    elif opcao == 10:
        excluir_professor = input("Digite o nome do professor que você deseja excluir: ")
        indice_porcurando = -1
        indice = 0

        while indice < len(lista_professores):
            if lista_professores[indice].nome == excluir_professor:
                indice_porcurando = indice
            indice = indice + 1

        if indice_porcurando == -1:
            print("Professor não encontrado.")
        else:
            lista_professores.pop(indice_porcurando)
            print("Professor removido com sucesso!")
        
    
    elif opcao == 0:
        print ("encerrando sistema")


        






