class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for l in self.livros:
            print(f"{l.titulo}, de {l.autor}")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(Livro("1984", "george orwell"))
biblioteca.adicionar_livro(Livro("o hobbit", "j.r.r. tolkien"))
biblioteca.listar_livros()
