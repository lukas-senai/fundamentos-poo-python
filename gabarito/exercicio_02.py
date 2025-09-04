class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"olá, meu nome é {self.nome}")

class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def apresentar(self):
        print(f"sou {self.nome} e estudo {self.curso}")

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"sou {self.nome} e ensino {self.disciplina}")

a = Aluno("lucas", "programação")
p = Professor("aline", "banco de dados")
a.apresentar()
p.apresentar()
