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
        return ("Nome: " + self.nome + " Idade: " + str(self.idade) + " Altura: " + str(self.altura) + " Peso: " + str(self.peso))


lista_pessoa = []

print ("""
      1- Cadastrar
      2- Listar
      3- Excluir
      4- Atualizar
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

    elif opcao == 3:
        excluir_pessoa = input("Digite o nome da pessoa que você deseja excluir: ")
        indice_porcurando = -1
        indice = 0

        while indice < len(lista_pessoa):
            if lista_pessoa[indice].nome == excluir_pessoa:
                indice_porcurando = indice
            indice = indice + 1

        if indice_porcurando == -1:
            print("Pessoa não encontrada.")
        else:
            lista_pessoa.pop(indice_porcurando)
            print("Pessoa removida com sucesso!")

    elif opcao == 4:
        atualizar_pessoa = input("Digite o nome da pessoa que você deseja atualizar: ")
        indice_porcurando = -1
        indice = 0

        while indice < len(lista_pessoa):
            if lista_pessoa[indice].nome == atualizar_pessoa:
                indice_porcurando = indice
            indice = indice + 1

        if indice_porcurando == -1:
            print("Pessoa não encontrada.")
        else:
            lista_pessoa[indice_porcurando].idade = int(input("Digite a nova idade: "))
            lista_pessoa[indice_porcurando].altura = float(input("Digite a nova altura: "))
            lista_pessoa[indice_porcurando].peso = float(input("Digite o novo peso: "))
            print("Pessoa atualizada com sucesso!")

    elif opcao == 0:
        print ("encerrando sistema")
        
