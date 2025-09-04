# 04 · Encapsulamento e `property`

Encapsular é **proteger e organizar o acesso aos dados** de um objeto. Em Python, confiamos muito em **convenções** ao invés
de proibições rígidas. Um atributo público pode ser lido de fora normalmente; um atributo com **um sublinhado** (por exemplo,
`_saldo`) sinaliza “use com cuidado”; com **dois sublinhados** (`__segredo`), o nome é “ofuscado” (name mangling) para desencorajar
acessos diretos.

    class ContaBancaria:
        def __init__(self, titular, saldo):
            self.titular = titular    # público
            self._saldo = saldo       # protegido por convenção
            self.__senha = "1234"     # privado (name mangling)

        def get_saldo(self):
            return self._saldo

Embora possamos escrever getters e setters “manualmente”, Python tem um atalho elegante: o decorador `@property`. Ele permite que
um método se comporte como atributo, com validação na escrita. Assim, quem usa a classe tem uma experiência simples, enquanto
você mantém o controle interno.

    class Produto:
        def __init__(self, preco):
            self._preco = preco

        @property
        def preco(self):
            return self._preco

        @preco.setter
        def preco(self, novo_preco):
            if novo_preco <= 0:
                raise ValueError("Preço deve ser positivo.")
            self._preco = novo_preco

    p = Produto(10.0)
    p.preco = 12.5
    print(p.preco)

A ideia é parecida com janelas com cortinas: por fora tudo parece um “vidro” simples (um atributo), mas por dentro há mecanismos
que controlam luz e privacidade (validação e lógica adicional).

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.

