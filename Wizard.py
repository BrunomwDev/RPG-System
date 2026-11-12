from Character import Character

class Wizard(Character):

    def __init__(self, name):
        self.Sp_attack=30
        super().__init__(
            name,
            life=80,
            attack=30,
            defence=5,
            level=1,
            xp=0
            )
        #tem mana
        #sp attack bola de fogo