# 02 · Classes e Objetos

Uma **classe** é como o “molde” de um objeto. Pense em uma forma de fazer biscoitos: a forma define como os biscoitos serão,
mas cada biscoito é uma **instância** diferente. No código, criamos a classe e, ao “usar o molde”, obtemos o objeto.

    class Pessoa:
        pass

Acima há uma classe mínima. Para torná-la útil, damos a ela um **construtor** (o método `__init__`), que prepara cada novo objeto
com valores iniciais. O parâmetro `self` é a forma de o método enxergar “quem eu sou” — a própria instância.

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1 = Pessoa("Ana", 25)
    p2 = Pessoa("Luis", 30)
    print(p1.nome, p2.nome)

Cada objeto tem seu próprio estado (os atributos). Embora p1 e p2 sejam da mesma classe, eles podem ter valores diferentes.
Isso permite modelar o mundo real: pessoas distintas, com dados individuais, mas “fabricadas” a partir do mesmo molde.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.

