# 06 · Polimorfismo

A palavra parece complicada, mas o conceito é bem simples: polimorfismo é quando diferentes objetos podem “responder” da sua maneira a uma mesma chamada.

Pense em animais. Todos podem emitir um som, mas cada um tem o seu. O cachorro late, o gato mia, o passarinho canta. Se você tiver uma lista de animais e pedir para cada um “falar”, cada um vai responder do seu jeito, sem que você precise se preocupar em saber qual é qual.

Em python:

```python
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

bichos = [Cachorro(), Gato()]
for bicho in bichos:
    print(bicho.falar())
```

A beleza do polimorfismo é justamente essa: você trata tudo de forma genérica (no caso, todos como animais), mas cada um sabe como agir de maneira particular. É como pedir para várias pessoas “se apresentarem”: cada uma vai dizer o que faz sentido para ela.
