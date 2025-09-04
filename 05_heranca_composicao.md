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

