class Estudante:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return(f"Olá sou {self.nome} tenho {self.idade} anos")

lista_alunos = []
lista_alunos.append(Estudante("Ryan", 23))
lista_alunos.append(Estudante("Alberto", 35))

for aluno in lista_alunos:
    print(aluno.apresentar())