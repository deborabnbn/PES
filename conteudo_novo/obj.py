# class Empresa:
#     nome = ""
#     ano_de_criacao = 0
#     funcionarios = []

# print("Criar empresa de churrasco")
# quintalChurrasco = Empresa()
# print(quintalChurrasco.nome)



class Empresa:
    nome = ""
    ano_de_criacao = 0
    funcionarios = []
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo
print("Criar empresa de churrasco")
quintalChurrasco = Empresa("Quintal", 2000)
print(quintalChurrasco.nome)