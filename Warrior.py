from Character import Character

class Warrior(Character):

    def __init__(self, name):
        self.Sp_attack=30
        super().__init__(
            name,
            life=150,
            attack=15,
            defence=20,
            level=1,
            xp=0
            )