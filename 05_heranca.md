# 05 · Herança

Imagine que você já tem uma classe que descreve algo geral, como uma Pessoa. Agora você quer criar uma classe mais específica, como Estudante. Ao invés de reescrever tudo do zero, você “herda” da classe Pessoa.  

Herança é isso: permitir que uma classe aproveite código de outra. É como se fosse a relação entre pais e filhos: o filho já nasce herdando características dos pais, mas também pode ter suas próprias.  

Em python:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Oi, eu sou {self.nome}")

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # reaproveita a inicialização da classe mãe
        self.curso = curso

    def apresentar(self):
        print(f"Oi, eu sou {self.nome} e estudo {self.curso}")
```

A classe Estudante ganhou tudo que Pessoa já tinha, mas ainda acrescentou seu próprio detalhe. É como dizer: *sou uma Pessoa, mas com algumas habilidades extras*.  

A herança facilita a vida porque evita repetição e ajuda a organizar o código em níveis de generalização (do mais genérico para o mais específico).
