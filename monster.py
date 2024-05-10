import json
from classes import player

class Monster:
    def __init__(monster, name: str, hp: int, description: str, loot: str):
        monster.name = name
        monster.hp = hp
        monster.description = description
        monster.loot = loot
    
class maldachaunians(Monster):
    def __init__(monster, name:str, hp:int, description:str, loot:str, weapon:str):
        super().__init__(name, hp, description, loot)
        monster.weapon = weapon

class elves(maldachaunians):
    def __init__(monster, name:str, hp:int, description:str, loot:str, weapon:str, powers:str):
        super().__init__(name, hp, description, loot, weapon)
        monster.power = powers 
    
class element_spirits(Monster): 
    def __init__(monster, name:str, hp:int, description:str, loot:str, power:str):
        super().__init__(name, hp, description, loot)
        monster.power = power 

