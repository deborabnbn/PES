# Crie uma classe chamada Livro com:
# • Atributos: titulo e autor.
# • Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
# Teste criando um objeto e chamando o método para exibir a descrição.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        print("O livro", self.titulo, "foi ecrito por", self.autor)

    
Livro1 = Livro("Todas as suas imperfeições", "Colen Hover")

print(f"{Livro1.titulo} foi escrito por {Livro1.autor}.")
