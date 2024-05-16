class Monster:
    def __init__(monster, name: str, hp: int, loot: str, damage: int, crit: int):
        monster.name = name
        monster.hp = hp
        monster.loot = loot
        monster.damage = damage
        monster.crit = crit
    
class maldachaunians(Monster):
    def __init__(monster, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit)
        monster.weapon = weapon

    

class elves(maldachaunians):
    def __init__(monster, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str, powers:str):
        super().__init__(name, hp, loot, damage, crit, weapon)
        monster.power = powers 

class element_spirits(Monster): 
    def __init__(monster, name:str, hp:int, loot:str, damage: int, crit: int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        monster.power = power 