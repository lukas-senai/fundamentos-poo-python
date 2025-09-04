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

