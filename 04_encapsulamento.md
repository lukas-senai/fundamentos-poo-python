# 04 · Encapsulamento

Encapsulamento é como se fosse um “controle de acesso” às informações de um objeto.  
Pense em uma conta bancária: você sabe o seu nome como titular, mas o banco não deixa qualquer pessoa acessar diretamente o saldo ou mudar valores na sua conta. Existe um **meio seguro** para isso: extratos, aplicativos, caixas eletrônicos.  

Na programação orientada a objetos, a ideia é a mesma. Os atributos podem ser deixados “protegidos” e só acessados de forma controlada, normalmente por métodos que nós mesmos criamos. Isso evita que alguém de fora bagunce dados importantes sem passar pelas regras certas.  

Exemplo simples em python:

```python
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo   # aviso de que não é para mexer direto

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self._saldo}")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
```

Aqui, qualquer pessoa pode ver o nome do titular, mas o saldo é “meio escondido” (indicado pelo underline). Para mexer nele, oferecemos meios seguros, como o método depositar.  

É como se os atributos fossem **caixas** e os métodos fossem **as chaves** certas para abri-las. Assim, o objeto mantém ordem e segurança.
