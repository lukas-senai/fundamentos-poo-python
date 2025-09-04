# 07 · Classes Abstratas

Uma classe abstrata é como um esqueleto: ela define o que precisa existir, mas não diz exatamente como.  
É usada quando queremos garantir que todas as classes filhas tenham certos métodos, mas deixamos para elas a responsabilidade de implementar.

Pense numa “receita base” que diz: *para ser considerado um bolo, você precisa ter massa e cobertura*. Mas cada tipo de bolo (chocolate, cenoura, fubá) prepara isso de um jeito.

Em python, usamos a biblioteca abc para criar classes abstratas:

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
```

Aqui, qualquer forma que criarmos é obrigada a ter um método area. Isso evita inconsistências e garante uma padronização.
