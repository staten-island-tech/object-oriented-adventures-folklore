from monster import Monster
import random
import item
import json
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class player():
    def __init__(self, name: str, hp: int, max_hp: int, strength: int, speed: int, inventory: list, damage: int, crit: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.speed = speed
        self.inventory = inventory 
        self.damage = damage
        self.crit = crit
    
    def add_weapon_damage(a,b):
        #a is the player's original damage, b is the weapon amount
        d = a + b
        n = d
        return n
    
    def add_weapon_to_crit(a,b):
        #a is the player's crit, b is the weapon amount 
        c = a + b
        n = c
        return n


