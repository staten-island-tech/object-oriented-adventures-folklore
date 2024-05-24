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
        
    def stats():
        maldachaunians = maldachaunians()
        maldachaunians.name = "maldachaunians"
        maldachaunians.hp = 100
        maldachaunians.loot = ""
        maldachaunians.damage = 10
        maldachaunians.crit = 20
        maldachaunians.weapon = "dagger"
    return {maldachaunians.name}, {maldachaunians.hp}, {maldachaunians.loot}, {maldachaunians.damage}, {maldachaunians.crit}, {maldachaunians.weapon} 
    
class elves(maldachaunians):
    def __init__(elves, name:str, hp:int, loot:str, damage: int, crit: int, weapon:str, powers:str):
        super().__init__(name, hp, loot, damage, crit, weapon)
        elves.power = powers 

class element_spirits(Monster): 
    def __init__(element_spirits, name:str, hp:int, loot:str, damage: int, crit: int, power:str):
        super().__init__(name, hp, loot, damage, crit)
        element_spirits.power = power 
