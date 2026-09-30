# Exercício A: Altere o algoritmo para representar 3 colegas de
# turma. O algoritmo também deve, ao final, exibir o nome e a
# idade de cada um deles.

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Luis = Aluno("Luiz", 16)
Vi = Aluno("Vitória", 17)
Vitor = Aluno("Vitor", 16)

alunos = [Luis, Vi, Vitor]

for aluno in alunos:
    print ("Aluno: ", aluno.nome,",", "Idade: ", aluno.idade)