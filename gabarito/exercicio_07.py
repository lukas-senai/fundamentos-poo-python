class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def aplicar_desconto(self, percentual):
        novo_preco = self._preco * (1 - percentual/100)
        if novo_preco > 0:
            self._preco = novo_preco

    def mostrar_preco(self):
        print(f"{self.nome}: r$ {self._preco:.2f}")

p = Produto("camisa", 100)
p.aplicar_desconto(10)
p.mostrar_preco()
