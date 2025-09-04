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

