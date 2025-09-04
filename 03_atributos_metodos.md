# 03 · Atributos e Métodos

Quando falamos de atributos e métodos dentro de uma classe, estamos basicamente respondendo a duas perguntas: **“o que esse objeto tem?”** e **“o que esse objeto sabe fazer?”**.

Os atributos são as informações guardadas no objeto. é como se cada objeto tivesse sua própria “ficha de dados”. pense numa pessoa: nome, idade, altura… cada pessoa carrega consigo seus próprios valores para essas informações. Se criarmos várias pessoas, cada uma terá suas próprias características.

Já os métodos são as ações, os comportamentos. São como verbos que o objeto sabe executar. Voltando ao exemplo da pessoa: além de ter um nome e uma idade, ela pode falar, andar, comer. Esses comportamentos podem até usar os atributos para fazer sentido — como uma pessoa apresentar-se dizendo seu nome e idade.

Em python, isso se traduz naturalmente quando criamos uma classe. Veja:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

joao = Pessoa("João", 20)
maria = Pessoa("Maria", 25)

joao.apresentar()   # Olá, meu nome é João e tenho 20 anos.
maria.apresentar()  # Olá, meu nome é Maria e tenho 25 anos.
```

Perceba que tanto **joao** quanto **maria** são do mesmo “molde” (a classe Pessoa), mas cada um tem atributos diferentes. E quando chamamos o método, o comportamento é o mesmo, mas o resultado depende das informações que aquele objeto guarda.

Se quiser uma analogia bem simples: imagine que uma classe é como um **molde de bonecos**. Os atributos são as cores e acessórios que cada boneco pode ter (cabelo loiro, roupa azul, sapatos vermelhos). Os métodos são as articulações e botões que permitem que eles façam coisas (levantar o braço, falar uma frase, acender uma luz). Cada boneco sai do mesmo molde, mas pode ter sua própria “personalidade” dependendo dos atributos, e todos sabem os mesmos “truques” por causa dos métodos.
