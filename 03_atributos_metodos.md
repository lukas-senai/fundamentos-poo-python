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

