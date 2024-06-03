from monster import Monster
import random
import item
import json
import time
import os
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

    def attack_crit(self, enemy) -> None:
        enemy.hp -= self.crit
        enemy.hp = max(enemy.hp, 0) 
    
    def battle(x, y):
        while x.hp and y.hp > 0:
            print("1. Attack!")
            print("2. Go into inventory")
            print("3. Run away... (you wuss)")
            global choose
            choose = int(input("What would you like to do?\n"))
            r = random.randint(1,100)
            if choose == 1:
                if r <= 99:
                    x.attack(y)
                    if y.hp <= 0:
                        print("You successfully attacked the " + y.name + ". The " + y.name + " is dead!")
                    elif y.hp > 0:
                        print("You successfully attacked the " + y.name + ". The " + y.name + " has " + str(y.hp) + " hp now!")
                        if r <= 99:
                            x.hp -= y.damage
                            if x.hp <= 0: 
                                print("The " + y.name + " successfully attacked you. You are now dead!")
                            elif x.hp > 0:
                                print("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                        elif r == 100:
                            x.hp -= y.crit
                            if x.hp <= 0: 
                                print("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                            elif x.hp > 0:
                                print("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(player.hp) + " hp now!")
                            return x.hp
                        return y.hp
                elif r == 100:
                    x.attack_crit(y)
                    if y.hp <= 0:
                        print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " is dead!")
                    elif y.hp > 0:
                        print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " has " + str(y.hp) + "hp now!")
                        if r <= 99:
                            x.hp -= y.damage
                            if x.hp <= 0: 
                                print("The " + y.name + " successfully attacked you. You are now dead!")
                            elif x.hp > 0:
                                print("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                        elif r == 100:
                            x.hp -= y.crit
                            if x.hp <= 0: 
                                print("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                            elif x.hp > 0:
                                print("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(player.hp) + " hp now!")
                            return x.hp
                    return y.hp 
                return x.hp and y.hp
        if choose == 2:
            print()
        if choose == 3:
            if r <= 50:
                if "elf" in y:
                    typingPrint("The elf just shot you. You are now dead!")
                    time.sleep(3)
                if "maldachaunians" in y:
                    typingPrint("The maldachaunians threw a dagger at you. It hits you right in the heart. You are now dead!")
                    time.sleep(5)
                if "wimitescu" in y:
                    typingPrint("The wimitescu smashed your head in with a " + y.weapon + ". You are now dead!")
                    time.sleep(4)
                if "spirit" in y: 
                    typingPrint("The " + y.element + " spirit threw " + y.power + " at you. You are now dead!")
                    time.sleep(4)
            elif r > 50: 
                if "elf" in y:
                    typingPrint("The elf shot an arrow at you. It flys right past your head! You successfully ran away (COWARD)!")
                    time.sleep(5)
                if "maldachaunians" in y:
                    typingPrint("The maldachaunians threw " + y.weapon + " at you. It missed! You successfully ran away (COWARD)! ")
                    time.sleep(5)
                if "wimitescu" in y:
                    typingPrint("The wimitescu tries to attack you with a " + y.weapon + " but hits the ground instead. You successfully ran away (COWARD)!")
                    time.sleep(6)
                if "spirit" in y: 
                    typingPrint("The " + y.element + " spirit threw " + y.power + " at you. The " + y.name + "missed! You successfully ran away (COWARD)!")
                    time.sleep(6)