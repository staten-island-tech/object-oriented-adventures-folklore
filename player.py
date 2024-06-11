import random
import json
import time
import os
from classes import typingPrint
from Inventory import inventory, player_in
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class player():
    def __init__(self, name: str, hp: int, damage: int, crit: int, gold: int, silver: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.crit = crit
        self.gold = gold
        self.silver = silver
    
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
        while x.hp > 0 and y.hp > 1:
            os.system('cls')
            print("1. Attack!")
            print("2. Go into inventory")
            """ print("3. View player stats") """
            print("3. Run away") #should actually be option 4
            global choose
            choose = int(input("What would you like to do?\n"))
            os.system('cls')
            player_attack = random.randint(1,100)
            monster_attack = random.randint(1,100)
            player_crit = random.randint(1,100)
            monster_crit = random.randint(1,100)
            run = random.randint(1,100)
            text_duration = 2
            if choose == 1:
                if player_attack <= 80: #chances of sucessful player attack
                    if player_crit <= 90: #chance of normal player attack
                        x.attack(y)
                        if y.hp <= 0:
                            typingPrint("You successfully attacked the " + y.name + ". The " + y.name + " is dead!")
                            time.sleep(text_duration)
                            os.system('cls')
                            y.hp == 0 
                        elif y.hp > 0:
                            typingPrint("You successfully attacked the " + y.name + ". The " + y.name + " has " + str(y.hp) + " hp now!")
                            time.sleep(text_duration)
                            os.system('cls')
                            if monster_attack <= 75: #chance of successful monster attack
                                if monster_crit <= 95: #chance of normal monster attack
                                    x.hp -= y.damage
                                    if x.hp <= 0: 
                                        typingPrint("The " + y.name + " successfully attacked you. You are now dead!")
                                        time.sleep(text_duration)
                                        os.system('cls')
                                        x.hp = 0 
                                    elif x.hp > 0:
                                        typingPrint("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                        time.sleep(text_duration)
                                        os.system('cls')
                                elif monster_crit > 95 and monster_crit <= 100: #chance of crit monster attack
                                    x.hp -= y.crit
                                    if x.hp <= 0: 
                                        typingPrint("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                                        time.sleep(text_duration)
                                        os.system('cls')
                                        x.hp = 0 
                                    elif x.hp > 0:
                                        typingPrint("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(x.hp) + " hp now!")
                                        time.sleep(text_duration)
                                        os.system('cls')
                                    return x.hp
                                return x.hp
                            elif monster_attack > 75 and monster_attack <= 100: #chance of unsuccessful monster attack
                                typingPrint("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                                time.sleep(text_duration)
                                os.system('cls')
                                return x.hp
                    elif player_crit > 90 and player_crit <= 100: #chance of player crit attack
                        x.attack_crit(y)
                        if y.hp <= 0:
                            typingPrint("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " is dead!")
                            time.sleep(text_duration)
                            os.system('cls')
                            y.hp = 0 
                        elif y.hp > 0:
                            typingPrint("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " has " + str(y.hp) + "hp now!")
                            time.sleep(text_duration)
                            os.system('cls')
                        if monster_attack <= 75: #chance of sucessful monster attack
                            if monster_crit <= 95: #chance of monster normal attack 
                                x.hp -= y.damage
                                if x.hp <= 0: 
                                    typingPrint("The " + y.name + " successfully attacked you. You are now dead!")
                                    time.sleep(text_duration)
                                    os.system('cls')
                                    x.hp = 0 
                                elif x.hp > 0:
                                    typingPrint("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                    time.sleep(text_duration)
                                    os.system('cls')
                            elif monster_crit > 95 and monster_crit <= 100: #chance of monster crit attack 
                                x.hp -= y.crit
                                if x.hp <= 0: 
                                    typingPrint("The " + y.name + " successfully attacked you. It was a critical hit! You are now dead!")
                                    time.sleep(text_duration)
                                    os.system('cls')
                                    x.hp = 0 
                                elif x.hp > 0:
                                    typingPrint("The " + y.name + " successfully attacked you. It was a critical hit! You have " + str(x.hp) + " hp now!")
                                    time.sleep(text_duration)
                                    os.system('cls')
                                return x.hp
                        elif monster_attack > 75 and monster_attack <= 100: #chance of unsuccessful monster attack 
                            typingPrint("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                            time.sleep(text_duration)
                            os.system('cls')
                            return x.hp
                elif player_attack > 80 and player_attack <= 100: #chance of unsuccessful player attack 
                    typingPrint("Your attack was unsucessful! The " + y.name + " still has " + str(y.hp) + " hp!")
                    time.sleep(text_duration)
                    os.system('cls')
                    if monster_attack <= 75: #chance of successful monster attack 
                        if monster_crit <= 95: #chance of normal monster attack
                            x.hp -= y.damage
                            if x.hp <= 0: 
                                typingPrint("The " + y.name + " successfully attacked you. You are now dead!")
                                time.sleep(text_duration)
                                os.system('cls')
                                x.hp = 0 
                            elif x.hp > 0:
                                typingPrint("The " + y.name + " successfully attacked you. You have " + str(x.hp) + " hp now!")
                                time.sleep(text_duration)
                                os.system('cls')
                        elif monster_crit > 95 and monster_crit <= 100: #chance of monster crit attack 
                            x.attack_crit(y)
                            if y.hp <= 0:
                                typingPrint("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " is dead!")
                                time.sleep(text_duration)
                                os.system('cls')
                                y.hp = 0 
                            elif y.hp > 0:
                                typingPrint("You successfully attacked the " + y.name + ". It was a critical hit! The " + y.name + " has " + str(y.hp) + "hp now!")
                                time.sleep(text_duration)
                                os.system('cls')
                                return x.hp
                    elif monster_attack > 75 and monster_attack <= 100: #chance of unsuccessful monster attack 
                        typingPrint("The " + y.name + " attacked you unsuccessfully. You still have " + str(x.hp) + " hp!") 
                        time.sleep(text_duration)
                        os.system('cls')
                        return x.hp
                    return x.hp and y.hp
                return x.hp and y.hp
            if choose == 2:
                inventory.display_inventory(x)
                """if x.gold == 0 and x.silver == 0:
                    typingPrint("You are poor right now! You have no money or items!")
                    time.sleep(3)
                else: 
                    print()"""
                    #daniel has to figure out inventory system
                
            if choose == 3:
                player_in.display_stats(x)
            if choose == 3:
                if run <= 50:
                    if "Elf" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " just shot you. You are now dead!")
                        time.sleep(3)
                        os.system('cls')
                        x.hp = 0 
                        return x.hp
                    if "Maldachaunians" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " threw a dagger at you. It hits you right in the heart. You are now dead!")
                        time.sleep(5)
                        os.system('cls')
                        x.hp = 0
                        return x.hp
                    if "Wimitescu" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " smashed your head in with a " + y.weapon + ". You are now dead!")
                        time.sleep(4)
                        os.system('cls')
                        x.hp = 0
                        return x.hp 
                    if "Spirit" in y.name: 
                        os.system('cls')
                        typingPrint("The " + y.name + " threw " + y.power + " at you. You are now dead!")
                        time.sleep(4)
                        os.system('cls')
                        x.hp = 0
                        return x.hp
                elif run > 50 and run <= 100: 
                    if "Elf" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " shot an arrow at you. It flys right past your head! You successfully ran away (COWARD)!")
                        time.sleep(5)
                        os.system('cls')
                        y.hp = 1
                        return y.hp 
                    if "Maldachaunians" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " threw " + y.weapon + " at you. It missed! You successfully ran away (COWARD)! ")
                        time.sleep(5)
                        os.system('cls')
                        y.hp = 1
                        return y.hp 
                    if "Wimitescu" in y.name:
                        os.system('cls')
                        typingPrint("The " + y.name + " tries to attack you with a " + y.weapon + " but hits the ground instead. You successfully ran away (COWARD)!")
                        time.sleep(6)
                        os.system('cls')
                        y.hp = 1
                        return y.hp
                    if "Spirit" in y.name: 
                        os.system('cls')
                        typingPrint("The " + y.name + " threw " + y.power + " at you. The " + y.name + " missed! You successfully ran away (COWARD)!")
                        time.sleep(6)
                        os.system('cls')
                        y.hp = 1
                        return y.hp
            