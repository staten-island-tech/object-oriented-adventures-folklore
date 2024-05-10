import json
from classes import player

class Monster:
    def __init__(self, name: str, hp: int, description: str, loot: str):
        self.name = name
        self.hp = hp
        self.description = description
        self.loot = loot
    
class maldachaunians(Monster):
    def __init__(self, name:str, hp:int, description:str, loot:str, weapon:str):
        super().__init__(name, hp, description, loot)
        self.weapon = weapon

class elves(maldachaunians):
    def __init__(self, name:str, hp:int, description:str, loot:str, weapon:str, powers:str):
        super().__init__(name, hp, description, loot, weapon)
        self.power = powers 
    
class element_spirits(Monster): 
    def __init__(self, name:str, hp:int, description:str, loot:str, power:str):
        super().__init__(name, hp, description, loot)
        self.power = power 

