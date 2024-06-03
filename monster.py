import json 
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class Monster:
    def __init__(self, name: str, hp: int, loot: str, damage: int, crit: int):
        self.name = name
        self.hp = hp
        self.loot = loot
        self.damage = damage
        self.crit = crit
    
class maldachaunians(Monster):
    def __init__(self, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit)
        self.weapon = weapon

class wimitescu(Monster):
    def __init__(self, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit)
        self.weapon = weapon
    
class elves(maldachaunians):
    def __init__(self, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str, powers:str):
        super().__init__(name, hp, loot, damage, crit, weapon)
        self.power = powers 

class element_spirits(Monster): 
    def __init__(self, name:str, hp:int, loot:str, damage: int, crit: int, power:str, element: str):
        super().__init__(name, hp, loot, damage, crit)
        self.power = power 
        self.element = element

class Floor1_Moonlight_Monarch(Monster):
    def __init__(Floor1_Moonight_Monarch, name:str, hp: int, loot: str, damage: int, crit:int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        Floor1_Moonight_Monarch.power = power

class Floor2_Pchvpxa(Monster):
    def __init__(Floor2_Pchvpxa, name:str, hp: int, loot: str, damage: int, crit:int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        Floor2_Pchvpxa.power = power

class Floor3_Anlliasio_Altosoei(Monster):
    def __init__(Floor3_Annlliasio_Altosoei, name:str, hp: int, loot: str, damage: int, crit:int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        Floor3_Annlliasio_Altosoei.power = power

class Floor4_Chikungunya(Monster):
    def __init__(Floor4_Chikungunya, name:str, hp: int, loot: str, damage: int, crit:int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        Floor4_Chikungunya.power = power

class Pikachu(Monster):
    def __init__(floor, name:str, hp: int, loot: str, damage: int, crit:int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        Pikachu.power = power


