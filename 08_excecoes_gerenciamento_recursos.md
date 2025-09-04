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

