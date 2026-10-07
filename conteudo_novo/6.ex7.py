# 7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
# para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
# peso, baseado, também, no nome informado.

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
      3- Excluir
      0- Sair
""")

opcao = -1
while opcao != 0:
    opcao = int(input("digite uma opção: "))

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
        
    elif opcao ==3:
        remover_pessoa = input("Digite o nome da pessoa que vc quer remover: ")
        remove = False
        for pessoa in lista_pessoa:
            if pessoa.nome == remover_pessoa:
                lista_pessoa.remove(remover_pessoa)
                remove = True
            
        if remove:
             print("Pessoa removida!")
        else:
            print("pessoa não encontrada")
    elif opcao == 0:
        print ("encerrando sistema")

        
