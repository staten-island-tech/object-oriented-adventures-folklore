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

    def attack_enemy(a,b,c):
        #a is the monter's hp, b is how much damage the player does, c is the player's crit attack amount
        d = random.randint(1,20)
        if d < 20:
            a - b
            print("You did " + str(a) + " damage!")

        elif d == 20:
            a - c
            print("You did " + str(c) + " damage!")
        return a
    
    def get_attacked(a,b,c):
        #a is player hp, b is how much damage the monster does, c is a critical hit
        x = random.randint(1,20)
        if x < 20:   
            h = a - b
            print("You were attacked! You took " + str(b) + " damage and now have " + str(h) + " hp!")

        elif x == 20:
            h = a - c
            print("You were attacked! It was a critical hit! You took " + str(c) + " and now have" + str(h) + " hp!")
        return h