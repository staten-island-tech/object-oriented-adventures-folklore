import json
from classes import player

class Monster:
    def __init__(self, name, hp, description, loot):
        self.name = name
        self.hp = hp
        self.description = description
        self.loot = loot
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.description}, {self.loot}"
    
class maldachaunians(Monster):
    def __init__(self, name, hp, description, loot, weapon):
        super().__init__(name, hp, description, loot)
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.description}, {self.loot}, {self.weapon}"
    
class elves(maldachaunians):
    def __init__(self, name, hp, description, loot, weapon, powers):
        super().__init__(name, hp, description, loot, weapon)
        self.power = powers 
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.description}, {self.loot}, {self.weapon}, {self.power}"
    
class element_spirits(Monster): 
    def __init__(self, name, hp, description, loot, power):
        super().__init__(name, hp, description, loot)
        self.power = power 
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.description}, {self.loot}, {self.power}"
    
