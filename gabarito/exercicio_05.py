class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        print(f"{self.nome}, salário: {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def mostrar_dados(self):
        print(f"{self.nome}, gerente do setor {self.setor}, salário: {self.salario}")

f = Funcionario("lucas", 2000)
g = Gerente("leticia", 5000, "TI")
f.mostrar_dados()
g.mostrar_dados()
