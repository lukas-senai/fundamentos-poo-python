# 08 · Exceções

Quando algo dá errado no nosso programa, chamamos isso de exceção. Por exemplo, tentar dividir por zero ou converter uma palavra em número. Se não tratarmos isso, o programa quebra.  

Em python usamos try e except para lidar com essas situações de forma elegante:

```python
try:
    numero = int("abc")
except ValueError:
    print("não foi possível converter o texto em número")
```

A ideia é parecida com andar de bicicleta com capacete: você não espera cair, mas se acontecer, está protegido.  

Também podemos criar nossas próprias exceções, úteis quando queremos sinalizar erros específicos do nosso sistema. Imagine um caixa eletrônico que não deixa sacar mais dinheiro do que há disponível:

```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("saldo insuficiente!")
```

Desse jeito, conseguimos identificar exatamente o tipo de erro e reagir de forma adequada.
