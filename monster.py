import json 
import random
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class Monster:
    def __init__(self, name: str, hp: int, loot: str, damage: int, crit: int, gold: int, silver: int):
        self.name = name
        self.hp = hp
        self.loot = loot
        self.damage = damage
        self.crit = crit
        self.gold = gold
        self.silver = silver
    
class maldachaunians(Monster):
    def __init__(maldachaunians, name:str, hp:int, loot:str, damage: int, crit: int, gold: int, silver: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit, gold, silver)
        maldachaunians.gold = random.randint(2,5)
        maldachaunians.silver = random.randint(3,10)
        maldachaunians.weapon = weapon

class wimitescu(Monster):
    def __init__(wimitescu, name:str, hp:int, loot:str, damage: int, crit: int, gold: int, silver: int, weapon:str):
        super().__init__(name, hp, loot, damage, crit, gold, silver)
        wimitescu.gold = random.randint(3,8)
        wimitescu.silver = random.randint(8,15)
        wimitescu.weapon = weapon
    
class elves(maldachaunians):
    def __init__(elves, name:str, hp:int, loot:str, damage: int, crit: int, gold: int, silver: int, weapon:str, powers:str):
        super().__init__(name, hp, loot, damage, crit, gold, silver, weapon)
        elves.gold = random.randint(5,15)
        elves.silver = random.randint(10,20)
        elves.power = powers 

class water_spirit(Monster): 
    def __init__(water_spirit, name:str, hp:int, loot:str, damage: int, crit: int, gold: int, silver: int, power:str):
        super().__init__(name, hp, loot, damage, crit, gold, silver)
        water_spirit.gold = random.randint(5,20)
        water_spirit.silver = random.randint(10,20)
        water_spirit.power = power 

class fire_spirit(Monster): 
    def __init__(fire_spirit, name:str, hp:int, loot:str, damage: int, crit: int, gold: int, silver: int, power:str):
        super().__init__(name, hp, loot, damage, crit, gold, silver)
        fire_spirit.gold = random.randint(5,20)
        fire_spirit.silver = random.randint(10,20)
        fire_spirit.power = power 

class Floor1_Moonlight_Monarch(Monster):
    def __init__(Floor1_Moonight_Monarch, name:str, hp: int, damage: int, crit:int, power:str):
        super().__init__(name, hp, damage, crit) 
        Floor1_Moonight_Monarch.power = power
        
class Floor2_Pchvpxa(Monster):
    def __init__(Floor2_Pchvpxa, name:str, hp: int, damage: int, crit:int, power:str):
        super().__init__(name, hp, damage, crit)
        Floor2_Pchvpxa.power = power

class Floor3_Anlliasio_Altosoei(Monster):
    def __init__(Floor3_Annlliasio_Altosoei, name:str, hp: int, damage: int, crit:int, power:str):
        super().__init__(name, hp, damage, crit)
        Floor3_Annlliasio_Altosoei.power = power

class Floor4_Chikungunya(Monster):
    def __init__(Floor4_Chikungunya, name:str, hp: int, damage: int, crit:int, power:str):
        super().__init__(name, hp, damage, crit)
        Floor4_Chikungunya.power = power

class Pikachu(Monster):
    def __init__(pikachu, name:str, hp: int, damage: int, crit:int, power:str):
        super().__init__(name, hp, damage, crit)
        pikachu.power = power 


