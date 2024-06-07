from monster import Monster
import random
import item
import json
import time
import os
from classes import typingPrint
from Inventory import inventory
from Inventory import player_in
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class player():
    def __init__(self, name: str, hp: int, max_hp: int, inventory: list, damage: int, crit: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
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
            os.system('cls')
            print("1. Attack!")
            print("2. Go into inventory")
            print("3. View player stats")
            global choose
            choose = int(input("What would you like to do?\n"))
            os.system('cls')
            player_attack = random.randint(1,100)
            monster_attack = random.randint(1,100)
            player_crit = random.randint(1,100)
            monster_crit = random.randint(1,100)
            run = random.randint(1,100)
            if choose == 1:
                if player_attack <= 75: 
                    if player_crit <= 99:
                        x.attack(y)
                        if y.hp <= 0:
                            print("You successfully attacked the " + y.name + ". The " + y.name + " is dead!")
                            time.sleep(2)
                            os.system('cls')
                            y.hp == 0 
                        elif y.hp > 0:
                            print("You successfully attacked the " + y.name + ". The " + y.name + " has " + str(y.hp) + " hp now!")
                            time.sleep(2)
                            os.system('cls')
                            if monster_attack <= 75: 
                                if monster_crit <= 99:
                                    x.hp -= y.damage
                                    if x.hp <= 0: 
                                        print("The " + y.name + " successfully attacked you. You are now dead!")
                                        time.sleep(2)
                                        os.system('cls')
                                        x.hp == 0 
                                    elif x.hp > 0:
                                        print("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                        time.sleep(2)
                                        os.system('cls')
                                elif monster_crit == 100:
                                    x.hp -= y.crit
                                    if x.hp <= 0: 
                                        print("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                                        time.sleep(2)
                                        os.system('cls')
                                        x.hp == 0 
                                    elif x.hp > 0:
                                        print("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(player.hp) + " hp now!")
                                        time.sleep(2)
                                        os.system('cls')
                                    return x.hp
                                return x.hp
                            elif monster_attack > 75 and monster_attack <= 100:
                                print("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                                return x.hp
                    elif player_crit == 100:
                        x.attack_crit(y)
                        if y.hp <= 0:
                            print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " is dead!")
                            time.sleep(2)
                            os.system('cls')
                            y.hp == 0 
                        elif y.hp > 0:
                            print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " has " + str(y.hp) + "hp now!")
                            time.sleep(2)
                            os.system('cls')
                        if monster_attack <= 75: 
                            if monster_crit <= 99:
                                x.hp -= y.damage
                                if x.hp <= 0: 
                                    print("The " + y.name + " successfully attacked you. You are now dead!")
                                    time.sleep(2)
                                    os.system('cls')
                                    x.hp == 0 
                                elif x.hp > 0:
                                    print("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                    time.sleep(2)
                                    os.system('cls')
                            elif monster_crit == 100:
                                x.hp -= y.crit
                                if x.hp <= 0: 
                                    print("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                                    time.sleep(2)
                                    os.system('cls')
                                    x.hp == 0 
                                elif x.hp > 0:
                                    print("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(player.hp) + " hp now!")
                                    time.sleep(2)
                                    os.system('cls')
                                return x.hp
                        elif monster_attack > 75 and monster_attack <= 100:
                            print("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                            return x.hp
                elif player_attack > 75 and player_attack <= 100:
                    print("Your attack was unsucessful! The " + y.name + " still has " + str(y.hp) + " hp!")
                    time.sleep(2)
                    os.system('cls')
                    if monster_attack <= 75: 
                        if monster_crit <= 99:
                            x.hp -= y.damage
                            if x.hp <= 0: 
                                print("The " + y.name + " successfully attacked you. You are now dead!")
                                time.sleep(2)
                                os.system('cls')
                                x.hp == 0 
                            elif x.hp > 0:
                                print("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                time.sleep(2)
                                os.system('cls')
                        elif monster_crit == 100:
                            x.attack_crit(y)
                            if y.hp <= 0:
                                print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " is dead!")
                                time.sleep(2)
                                os.system('cls')
                                y.hp == 0 
                            elif y.hp > 0:
                                print("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " has " + str(y.hp) + "hp now!")
                                time.sleep(2)
                                os.system('cls')
                                return x.hp
                    elif monster_attack > 75 and monster_attack <= 100:
                        print("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                        return x.hp
                    return x.hp and y.hp
                return x.hp and y.hp
            if choose == 2:
                print("You are poor right now! You have no money!")
                time.sleep(3)
                inventory.display_inventory(x)
            if choose == 3:
                player_in.display_stats(x)
            