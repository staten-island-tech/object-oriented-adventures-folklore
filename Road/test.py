class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        self.shield = 0

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points
    def selectWeapon(self):
        choice = int(input("Choose your weapon 1-Sword, 2-Pickaxe or 3-Bow and arrow:  "))
        self.weapon = choice - 1
    def selectShield(self):
        choice = int(input("Press 1 to seletct a shield"))
        self.shield = choice - 1
    def selectShield(self):
        choice = random.randint(1, 3)
        self.shield = choice - 1
        self.sheild = 
