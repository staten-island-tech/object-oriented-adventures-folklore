import monster

class player():
    def __init__(self, name: str, hp: int, max_hp: int, strength: int, speed: int, inventory: str, damage: int, KO):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.speed = speed
        self.inventory = inventory 
        self.damage = damage
        self.KO = KO

    def ko(self):
        self.KO = True
        print(self.name + ", you have been killed.")

    def take_damage(self, attack):
        if attack > self.hp:
            print(self.name + ", you have been killed and have 0 hp")
            self.hp = 0
            self.KO = True
        else:
            self.hp -= attack
            print(self.name + "you have" + str(self.hp) + "hp")

    def gain_hp(self, amount):
        if amount > self.max_hp:
            print("You have" + str(self.max_hp) + "hp")
        else:
            self.hp += amount
            print("You have" + str(self.hp) + "hp")
    
