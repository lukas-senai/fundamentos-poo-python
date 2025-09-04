class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

formas = [Quadrado(2), Retangulo(3, 4), Circulo(5)]
for f in formas:
    print(f"área: {f.area()}")
