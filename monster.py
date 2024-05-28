import json 
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class Monster:
    def __init__(monster, name: str, hp: int, loot: str, damage: int, crit: int):
        monster.name = name
        monster.hp = hp
        monster.loot = loot
        monster.damage = damage
        monster.crit = crit
    
class maldachaunians(Monster):
    def __init__(maldachaunians, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit)
        maldachaunians.weapon = weapon
    
class elves(maldachaunians):
    def __init__(elves, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str, powers:str):
        super().__init__(name, hp, loot, damage, crit, weapon)
        elves.power = powers 

class element_spirits(Monster): 
    def __init__(element_spirits, name:str, hp:int, loot:str, damage: int, crit: int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        element_spirits.power = power 

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


