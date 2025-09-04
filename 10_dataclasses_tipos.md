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

