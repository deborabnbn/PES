# 5 – Crie uma classe chamada Pessoa com:
# • Atributos: nome, idade, altura e peso;
# • Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
# pessoa;
# • Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
# • Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
# Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
# estão corretos.

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def dados (self):
        print ("Nome: ",self.nome,  "Idade :", self.idade,  "altura:", self.altura,  "Peso: ", self.peso)

    def IMC (self):
        self.imc = (self.peso / self.altura) / self.altura
        return self.imc
    
    def nome_imc (self):
        nome_imc = f"Nome: {self.nome}: {self.imc}"
        return nome_imc
    
Maria = Pessoa("Maria", 16, 1.74, 55)
Pedro = Pessoa("Pedro", 17, 1.84, 70)
Thiago = Pessoa("Thiago", 8, 1.60, 40)

lista = [Maria, Pedro, Thiago]

for pessoa in lista:
    pessoa.IMC()
    print(pessoa.nome_imc())






    