# 09 · Métodos Especiais, Iteráveis e Iteradores

Python permite que objetos **se comportem como tipos nativos** por meio de **métodos especiais** (também chamados “dunder methods”).
Com `__str__` e `__repr__`, definimos como o objeto aparece; com `__eq__`, `__lt__` etc., definimos comparações; com `__len__`,
`__contains__`, integramos com `len()` e `in`.

    class Ponto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Ponto(x={self.x}, y={self.y})"

        def __eq__(self, other):
            return (self.x, self.y) == (other.x, other.y)

        def __add__(self, other):
            return Ponto(self.x + other.x, self.y + other.y)

Agora, sobre coleções: um **iterável** é algo que o `for` consegue percorrer. Ele fornece um **iterador** via `__iter__`.
O iterador, por sua vez, sabe entregar elementos um a um com `__next__`.

    class Contador:
        def __init__(self, inicio, fim):
            self.inicio = inicio
            self.fim = fim

        def __iter__(self):
            atual = self.inicio
            while atual <= self.fim:
                yield atual
                atual += 1

    for n in Contador(3, 6):
        print(n)

Acima usamos `yield`, que simplifica muito a criação de iteradores. Se precisarmos da forma “manual”, podemos implementar
um objeto com `__iter__` retornando `self` e `__next__` avançando o estado — mas `yield` costuma ser mais legível.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.

