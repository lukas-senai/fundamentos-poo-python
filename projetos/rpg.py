import random

# classe base para qualquer personagem do jogo
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida  # encapsulamento: vida não deve ser alterada diretamente

    @property
    def esta_vivo(self):
        return self._vida > 0

    def levar_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nome} sofreu {dano} de dano (vida: {self._vida})")

    def atacar(self, outro):
        raise NotImplementedError("cada personagem deve implementar o ataque")


# guerreiro: personagem com ataque físico
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100)

    def atacar(self, outro):
        dano = random.randint(10, 20)
        print(f"{self.nome} ataca com espada!")
        outro.levar_dano(dano)


# mago: personagem que usa magia, mas tem menos vida
class Mago(Personagem):
    def __init__(self, nome, mana=50):
        super().__init__(nome, vida=70)
        self._mana = mana

    def atacar(self, outro):
        if self._mana >= 10:
            dano = random.randint(15, 25)
            self._mana -= 10
            print(f"{self.nome} lança magia! (mana: {self._mana})")
            outro.levar_dano(dano)
        else:
            print(f"{self.nome} não tem mana suficiente!")


# inimigo genérico
class Inimigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=60)

    def atacar(self, outro):
        dano = random.randint(5, 15)
        print(f"{self.nome} ataca ferozmente!")
        outro.levar_dano(dano)


# --- exemplo de batalha ---
heroi = Guerreiro("Professor Lucas")
vilao = Inimigo("ORC")

while heroi.esta_vivo and vilao.esta_vivo:
    heroi.atacar(vilao)
    if vilao.esta_vivo:
        vilao.atacar(heroi)

print("fim da batalha!")
