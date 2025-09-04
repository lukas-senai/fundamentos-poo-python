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

