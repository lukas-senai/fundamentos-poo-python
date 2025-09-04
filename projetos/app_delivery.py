# classe base para qualquer produto do cardápio
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco  # preço encapsulado

    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f"{self.nome} - R$ {self._preco:.2f}"


# restaurantes genéricos
class Restaurante:
    def __init__(self, nome, aberto=True):
        self.nome = nome
        self.aberto = aberto
        self.cardapio = []

    def adicionar_produto(self, produto):
        self.cardapio.append(produto)

    def listar_cardapio(self):
        for p in self.cardapio:
            print(p)

    def calcular_tempo_entrega(self):
        # pode ser sobrescrito em subclasses
        return 30


# pizzaria com regra de tempo diferente
class Pizzaria(Restaurante):
    def calcular_tempo_entrega(self):
        return 40  # pizzas demoram mais


# lanchonete com regra de tempo diferente
class Lanchonete(Restaurante):
    def calcular_tempo_entrega(self):
        return 20  # lanches saem rápido


# pedido feito por um cliente
class Pedido:
    def __init__(self, cliente, restaurante):
        if not restaurante.aberto:
            raise Exception("restaurante fechado!")
        self.cliente = cliente
        self.restaurante = restaurante
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        return sum(p.preco for p in self.itens)

    def resumo(self):
        print(f"pedido de {self.cliente} no {self.restaurante.nome}:")
        for item in self.itens:
            print(f"- {item}")
        print(f"total: R$ {self.calcular_total():.2f}")
        print(f"tempo estimado: {self.restaurante.calcular_tempo_entrega()} minutos")


# --- exemplo de uso ---
pizzaria = Pizzaria("pizza boa")
pizzaria.adicionar_produto(Produto("mussarela", 30))
pizzaria.adicionar_produto(Produto("calabresa", 35))

pedido = Pedido("joão", pizzaria)
pedido.adicionar_item(pizzaria.cardapio[0])
pedido.adicionar_item(pizzaria.cardapio[1])
pedido.resumo()
