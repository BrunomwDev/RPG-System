from Character import Character

class Arrow(Character):

    def __init__(self, name):
        self.Sp_attack=30
        super().__init__(
            name,
            life=100,
            attack=20,
            defence=10,
            level=1,
            xp=0
            )
        ##chance critical
        #sp attack flecha precisa