class Character:

    def __init__(self, name, life, attack, defence, level, xp):
        self.name = name
        self.life = life
        self.attack = attack
        self.defence = defence
        self.level = level
        self.xp = xp

    def attack_target(self, targed):
        targed.attack_targed(self.attack)
        pass

    def receive_damage(self, damage, life):
        self.damage = damage-self.defence
        self.life -= self.damage
        pass

    def is_alive(self):
        return self.life > 0
        pass

    def xp_gain(self, xp):
        self.xp += xp
        return self.xp
        pass

    def up_level(self, xp):
        while xp >= 100:
            self.level += 1
            self.life += 20
            self.xp -= 100
        else: print("Not enough experience to level up")
        
