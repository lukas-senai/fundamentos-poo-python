class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "au au"

class Gato(Animal):
    def falar(self):
        return "miau"

class Pato(Animal):
    def falar(self):
        return "quack"

bichos = [Cachorro(), Gato(), Pato()]
for bicho in bichos:
    print(bicho.falar())
