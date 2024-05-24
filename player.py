from monster import Monster
import random
import item
import json
from classes import typingPrint
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
    
    def add_weapon_damage(self, weapon):
        new_self_damage = self.damage + weapon.damage 
        self.damage = new_self_damage
        return self.damage
    
    def add_weapon_to_crit(self, weapon):
        new_self_damage = self.crit + weapon.damage
        self.damage = new_self_damage
        return self.damage
    
    def attack(self, enemy) -> None:
        enemy.hp -= self.damage
        enemy.hp = max(enemy.hp, 0)
        if enemy.hp <= 0:
            print("You successfully attacked " + str(enemy.name) + " . The " + str(enemy.name) + " is dead!")
        elif enemy.hp > 0:
            print("You successfully attacked " + str(enemy.name) + " . The " + str(enemy.name) + " has " + str(enemy.hp) + "hp now!")
            return enemy.hp 

    def attack_crit(self, enemy) -> None:
        enemy.hp -= self.crit
        enemy.hp = max(enemy.hp, 0)
        if enemy.hp <= 0:
            print("You successfully attacked " + str(enemy.name) + " . It was a critical hit! The " + str(enemy.name) + " is dead!")
        elif enemy.hp > 0:
            print("You successfully attacked " + str(enemy.name) + " . It was a critical hit! The " + str(enemy.name) + " has " + str(enemy.hp) + "hp now!")
            return enemy.hp 

    def battle(x, y):
        print("1. Attack!")
        print("2. Go into inventory")
        print("3. Run away... (you wuss)")
        global choose
        choose = int(input("What would you like to do?\n"))
        random = random.randint(1,100)
        if choose == 1:
            if random <= 99:
                x.attack(y)
            elif random == 100:
                x.attack_crit(y)
        elif choose == 2:
            print()
        elif choose == 3:
            if "elf" in y:
                typingPrint("The elf just shot you. You are now dead!")
            



