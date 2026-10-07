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
    def __init__ (self, matricula2, nome2, sobrenome2, idade2):
        self.matricula = matricula2
        self.nome = nome2
        self.sobrenome = sobrenome2
        self.idade = idade2

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
        matricula2 = int(input("Digite a matricula do aluno: "))
        nome2  = input("Digite o nome do aluno: ")
        sobrenome2 = input("Digite o sobrenome da pessoa: ")
        idade2 = int(input("Digite a idade do aluno: "))
        
        aluno = Aluno(matricula2, nome2, sobrenome2, idade2)
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





