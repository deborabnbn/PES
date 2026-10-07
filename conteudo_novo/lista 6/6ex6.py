# 6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
# funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
# conforme abaixo:
# Cadastro de Pessoas
# -------------------
# 1 – Cadastrar
# 2 – Listar
# 0 – Sair
# Opção:

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def dados (self):
        return ("Nome: " + self.nome + "Idade: " + str(self.idade) + "altura:" + str(self.altura) + "Peso: " + str(self.peso))


lista_pessoa = []

print ("""
      1- Cadastrar
      2- Listar
      0- Sair
""")

opcao = -1
while opcao != 0:
    opcao = int(input("digite uma opação: "))

    if opcao == 1:
        nome  = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))
        peso = float(input("Digite o peso da pessoa: "))

        pessoa = Pessoa(nome, idade, altura, peso)
        lista_pessoa.append(pessoa)

        print ("Pessoa cadastrada com sucesso!")

    elif opcao == 2:
        for pessoa in lista_pessoa:
            print (pessoa.dados())
        
    elif opcao == 0:
        print ("encerrando sistema")
