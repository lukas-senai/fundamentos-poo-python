# Programação Orientada a Objetos em Python (Guia Completo)

Este repositório contém um material **super didático** sobre POO em Python, organizado em módulos.
O conteúdo foi escrito de forma **fluida**, sem listas engessadas do tipo "o que é / para que serve",
e recheado de exemplos e analogias. Sempre que aparecer código, ele estará em **blocos com 4 espaços de recuo**
(em vez de cercas ```), para evitar erros de renderização.

## Estrutura

1. 01_introducao.md  
2. 02_classes_objetos.md  
3. 03_atributos_metodos.md  
4. 04_encapsulamento_properties.md  
5. 05_heranca_composicao.md  
6. 06_polimorfismo_ducktyping.md  
7. 07_abstratas_protocols.md  
8. 08_excecoes_gerenciamento_recursos.md  
9. 09_metodos_especiais_iteradores.md  
10. 10_dataclasses_tipos.md  
11. 11_padroes_solid_exemplos.md  
12. 12_exercicios_projetos.md  

Se preferir tudo em um único arquivo, use **POO_Python_Completo.md**.

---
>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



# 01 · Introdução à POO em Python

Começar pela ideia central ajuda: em Programação Orientada a Objetos, organizamos o programa como um conjunto
de **objetos** que representam coisas do mundo (reais ou conceituais), cada um com **dados** (atributos) e **comportamentos**
(métodos). É como montar uma mini “cidade” dentro do programa: existem moradores, veículos, prédios; cada um sabe fazer certas
coisas e mantém seus próprios estados.

Python é especialmente simpático a essa abordagem, porque praticamente **tudo é objeto**: números, strings, listas, funções e, claro,
as próprias classes. Isso significa que a sintaxe tende a ser enxuta, e a curva de aprendizado, agradável.

Para sentir a diferença, compare um pequeno trecho sem POO com outro usando uma classe. No primeiro, apenas guardamos dados soltos;
no segundo, reunimos dados e comportamento em um único lugar, o que facilita entender e evoluir o código.

    # Sem POO
    nome = "João"
    idade = 20
    print(f"{nome} tem {idade} anos")

    # Com POO
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1 = Pessoa("João", 20)
    print(f"{p1.nome} tem {p1.idade} anos")

Ao adotar POO, ganhamos **organização**, **reuso** e **manutenção** mais tranquila. Em projetos maiores, isso faz diferença:
fica mais fácil localizar onde certas regras vivem e trocar comportamentos sem bagunçar outras partes do sistema.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



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



# 03 · Atributos e Métodos

Dentro de uma classe, **atributos** guardam dados e **métodos** guardam comportamentos. Há dois tipos principais de atributos:
os **de instância**, que pertencem a cada objeto, e os **de classe**, compartilhados por todas as instâncias. É como ter um nome
próprio (instância) e uma espécie em comum (classe).

    class Pessoa:
        especie = "Humano"   # atributo de classe (compartilhado)
        def __init__(self, nome):
            self.nome = nome  # atributo de instância (próprio de cada objeto)

Para comportamentos, escrevemos métodos. Por padrão, os **métodos de instância** recebem `self`. Já **métodos de classe** recebem `cls`
e costumam ser criadores alternativos ou utilitários relacionados à classe inteira. **Métodos estáticos** são funções colocadas dentro
da classe por organização, mas não recebem nada automaticamente.

    class Calculadora:
        def soma(self, a, b):           # método de instância
            return a + b

        @classmethod
        def identidade(cls):            # método de classe
            return f"Sou a classe {cls.__name__}"

        @staticmethod
        def dobro(x):                   # método estático
            return x * 2

Em geral, use métodos de instância para lidar com dados do objeto, métodos de classe para fábricas e configuração global,
e estáticos quando quiser apenas agrupar uma função útil junto da classe para manter a organização.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



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



# 05 · Herança e Composição

Herança é quando uma classe “filha” reaproveita e estende o comportamento de uma classe “pai”. É como herdar o DNA:
a filha nasce sabendo coisas básicas da mãe e pode especializar comportamentos.

    class Pessoa:
        def __init__(self, nome):
            self.nome = nome

    class Estudante(Pessoa):
        def __init__(self, nome, curso):
            super().__init__(nome)   # chama o construtor da classe mãe
            self.curso = curso

    e = Estudante("Bia", "ADS")
    print(e.nome, e.curso)

Python também permite **herança múltipla**, mas use com parcimônia. Quando várias classes entram na linha de herança,
o Python usa a **MRO (Method Resolution Order)** para decidir a ordem de busca por métodos.

Composição é uma alternativa muito valiosa: ao invés de “é um”, dizemos “tem um”. Por exemplo, um carro **tem** um motor.
Isso costuma reduzir acoplamento e aumentar flexibilidade.

    class Motor:
        def ligar(self):
            print("Motor ligado")

    class Carro:
        def __init__(self):
            self.motor = Motor()  # composição

        def ligar(self):
            self.motor.ligar()
            print("Carro pronto para andar")

Herança é útil para especializar um comportamento comum; composição é ótima para **construir objetos a partir de peças**.
Uma regra prática: prefira composição quando a relação não for um “é um” claro.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



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



# 07 · Classes Abstratas e Protocols

Quando queremos definir um “contrato” claro, usamos **classes abstratas** (ABC – Abstract Base Classes). Elas não podem
ser instanciadas diretamente e exigem que as classes filhas implementem certos métodos. É como uma ficha com campos obrigatórios.

    from abc import ABC, abstractmethod

    class Forma(ABC):
        @abstractmethod
        def area(self):
            pass

    class Quadrado(Forma):
        def __init__(self, lado):
            self.lado = lado

        def area(self):
            return self.lado ** 2

Já os **Protocols** (do módulo `typing`) permitem declarar interfaces por **estrutura**: se um objeto tem certos métodos/atributos,
ele é compatível, independentemente da herança. É uma forma tipada de duck typing.

    from typing import Protocol

    class TemArea(Protocol):
        def area(self) -> float: ...

    def imprime_area(figura: TemArea) -> None:
        print(figura.area())

    # Qualquer objeto com método area() -> float serve,
    # mesmo sem herdar de uma base comum.

Use ABCs quando quiser um ponto comum de herança e mecanismos em tempo de execução.
Use Protocols quando quiser descrever capacidades para checagem estática (type checkers) com liberdade de implementação.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



# 08 · Exceções e Gerenciamento de Recursos

Erros acontecem, e tudo bem. O importante é **tratá-los de forma previsível**. Com `try/except`, capturamos problemas e damos
respostas amigáveis. Se algo deve acontecer **sempre** (como fechar um arquivo), podemos usar `finally` ou um **context manager**.

    try:
        x = int("abc")
    except ValueError as e:
        print("Erro de conversão:", e)

Às vezes precisamos criar **exceções personalizadas** para sinalizar condições do nosso domínio.

    class SaldoInsuficienteError(Exception):
        pass

    def sacar(saldo, valor):
        if valor > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente!")

Para recursos que precisam de abertura/fechamento (arquivos, conexões), o padrão com `with` evita vazamentos:

    class ArquivoSeguro:
        def __init__(self, caminho):
            self.caminho = caminho
            self._f = None

        def __enter__(self):
            self._f = open(self.caminho, "w", encoding="utf-8")
            return self._f

        def __exit__(self, tipo, valor, traceback):
            if self._f:
                self._f.close()
            # retornar False re-propaga exceções, True as suprime
            return False

    with ArquivoSeguro("saida.txt") as f:
        f.write("Olá, mundo!")

Isso transmite a ideia de “peguei a chave, usei a sala, devolvi a chave”. O `with` garante o retorno seguro da chave,
mesmo se algo der errado lá dentro.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



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



# 10 · `dataclasses` e Anotações de Tipo

Quando a classe é basicamente um “pacote de dados” com pouca lógica, `dataclasses` reduzem a verbosidade ao gerar
automáticamente `__init__`, `__repr__`, `__eq__` e outros conforme configurado.

    from dataclasses import dataclass

    @dataclass
    class Pessoa:
        nome: str
        idade: int

    p = Pessoa("Rafa", 22)
    print(p)  # Pessoa(nome='Rafa', idade=22)

Se quiser valores padrão, campos imutáveis ou pós-processamento, há opções:

    from dataclasses import dataclass, field

    @dataclass(frozen=True)
    class Config:
        host: str = "localhost"
        portas: list[int] = field(default_factory=lambda: [80, 443])

As **anotações de tipo** (typing) documentam intenções e ajudam ferramentas a apontar problemas com antecedência.
Python continua dinâmico em tempo de execução, mas editores e analisadores estáticos (mypy, pyright) agradecem.

    from typing import Iterable

    def soma_todos(numeros: Iterable[int]) -> int:
        return sum(numeros)

Use tipos para **comunicar** seu design. Você não está escrevendo burocracia; está deixando pistas para o futuro você e para sua equipe.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



# 11 · Padrões de Projeto e Princípios (na prática Python)

Em Python, os padrões se adaptam ao estilo dinâmico da linguagem. Dois exemplos diretos ajudam muito:

• **Strategy**: troque comportamentos em tempo de execução passando funções/objetos intercambiáveis.

    class Frete:
        def __init__(self, estrategia):
            self.estrategia = estrategia

        def calcular(self, valor):
            return self.estrategia(valor)

    def frete_normal(v): return v * 0.05
    def frete_express(v): return v * 0.10

    f = Frete(frete_normal)
    print(f.calcular(200))
    f.estrategia = frete_express
    print(f.calcular(200))

• **Observer**: objetos se inscrevem para serem notificados quando algo acontece.

    class Evento:
        def __init__(self):
            self._ouvintes = []

        def inscrever(self, f):
            self._ouvintes.append(f)

        def disparar(self, dados):
            for f in self._ouvintes:
                f(dados)

    evento = Evento()
    evento.inscrever(lambda d: print("Recebi:", d))
    evento.disparar({"ok": True})

Sobre **SOLID**, não precisamos decorar leis; o ponto é guiar decisões. Em especial:
- Responsabilidade Única (SRP): cada classe tem um papel claro.
- Aberto/Fechado (OCP): novas variações entram sem mexer no que já funciona (ex.: Strategy).
- Substituição de Liskov (LSP): subclasses honram as expectativas da base.
- Segregação de Interfaces (ISP): não force métodos inúteis; prefira pequenos contratos.
- Inversão de Dependência (DIP): dependa de abstrações, não de detalhes concretos.

Traduzindo: mantenha classes focadas, permita variações por composição e contratos, e evite “fios” diretos entre tudo e todos.

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



# 12 · Exercícios e Projetos Guiados

Aprender POO é principalmente **praticar**. Aqui vão desafios graduais, com dicas do que observar.

## Aquecimento (básico)
1) Crie uma classe `Carro` com `marca` e `ano`. Instancie dois objetos e imprima informações amigáveis.
2) Modele `Aluno` com método `media(n1, n2)` e um método que diz se está aprovado.

## Intermediário
3) Implemente `ContaBancaria` com `depositar`, `sacar`, `saldo` (usar `@property`). Dispare exceção própria ao sacar sem saldo.
4) Modele `Livro` com `preco` validado por `@property` e método `aplicar_desconto(percentual)`.

## Herança e Polimorfismo
5) Crie `Funcionario` (nome, salário base) e duas subclasses (`Gerente`, `Dev`) que calculam bônus de forma diferente. Faça uma função que recebe uma lista heterogênea e soma a folha.
6) Crie `Forma` abstrata e implementações `Quadrado`, `Circulo`, `Triangulo`. Escreva uma função que imprime a área de qualquer forma (duck typing).

## Projetinho 1: Catálogo de Itens (composição + dataclasses)
- Use `dataclasses` para `Item` (nome, preço).
- Faça `Carrinho` que guarda itens (composição) e calcula total. Adicione cupom por Strategy.

## Projetinho 2: Sistema de Notificações (Observer)
- Um `Publicador` dispara eventos; `AssinanteEmail` e `AssinanteSMS` reagem.
- Permita adicionar/remover assinantes em tempo de execução.

## Dicas de Avaliação (para professores)
- Observe se o aluno separa responsabilidades (sem classes “faz-tudo”).
- Veja se validam entradas com `property` e tratam erros com exceções próprias.
- Procure por nomes autoexplicativos e `__repr__` úteis para depuração.
- Estimule o uso de testes simples (mesmo que `assert` em scripts).

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.



