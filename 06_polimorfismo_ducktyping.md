# 06 · Polimorfismo e Duck Typing

Polimorfismo é a ideia de que objetos diferentes podem responder ao **mesmo conjunto de mensagens** (mesma interface),
cada um à sua maneira. Um cachorro e um gato “falam”, mas com sons distintos. O código que chama `falar` não precisa saber
quem é cachorro ou gato—apenas confia que existe o método certo.

    class Animal:
        def falar(self):
            raise NotImplementedError

    class Cachorro(Animal):
        def falar(self):
            return "Au Au!"

    class Gato(Animal):
        def falar(self):
            return "Miau!"

    for a in (Cachorro(), Gato()):
        print(a.falar())

Em Python, falamos muito de **duck typing**: “se anda como um pato e grasna como um pato, é um pato”.
Isso significa que o que importa é a **capacidade** (ter o método certo), não a árvore de herança. Se um objeto tem `falar()`,
pode ser tratado como um falante, mesmo sem herdar de `Animal`.

Essa flexibilidade é poderosa, mas exige **boas convenções** e **testes** para garantir que aquilo que prometemos realmente existe.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.

