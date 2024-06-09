import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor
import Monsters
import Inventory
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class Attacks:
    def attack(self):
        Inventory()
        def Maldachaunians():    
                player_attack_power = random.randint(5,50)
                Monsters.Maldachaunians()
                attack_chance_Maldachaunian = random.randint(1,10)

                while Monsters.maldachaunians.hp > 0:
                    if attack_chance_Maldachaunian <= 6:
                        typingPrint("You attack the Maldachaunian.")
                        Monsters.madachaunians.hp -= {player_attack_power}
                    elif attack_chance_Maldachaunian <=8:
                        typingPrint("The Maldachaunian attacked you.")
                        self.health -= {Monsters.maldachaunians.damage}
                        if random.randint(1, 10) == 9:
                            print("The strength of the Maldachaunian surprises you. \nThey delt a crit attack.")
                            self.health -= 15
                    else:
                        print("You did a crit attack.")
                        Monsters.maldachaunians.hp -= 15
                    break
                if Monsters.maldachaunians.hp == 0:
                    print(f"You attack a Maldachaunian.\n (+ golds)\n (+ silvers) \n(+ Cabbage) \n(+ Fowl)")
                    self.currency["Gold"] += {Monsters.maldachaunians.gold}
                    self.currency["Silver"] += {Monsters.maldachaunians.silver}
                    self.foods["Cabbage"] += 1
                    self.foods["Fowl"] += 1
                    

        #Wimitescu
        def Wimitescu_Attack():
                player_attack_power = random.randint(5,50)
                Monsters.Wimitescu()
                attack_chance_Wimitescu = random.randint(1,20)

                while Monsters.wimitescu.hp > 0:
                    if attack_chance_Wimitescu <= 6:
                        typingPrint("You attack the Wimitescu.")
                        Monsters.wimitescu.hp -= {player_attack_power}
                    elif attack_chance_Wimitescu <= 13:
                        typingPrint("The Wimitescu attacked you.")
                        self.health -= {Monsters.wimitescu.damage}
                        if random.randint(1, 10) == 9:
                            print("The strength of the Wimitescu surprises you. \nThey delt a crit attack.")
                            self.health -= 15
                    else:
                        print("You did a crit attack.")
                        Monsters.wimitescu.hp -= 40
                    break
                if Monsters.wimitescu.hp == 0:
                    print(f"You defeated a Wimitescu.\n (+ golds)\n (+ silvers) \n(+ Cabbage) \n(+ Fowl)")
                    self.currency["Gold"] += {Monsters.wimitescu.gold}
                    self.currency["Silver"] += {Monsters.wimitescu.silver}
                    self.foods["Wood"] += 1
                    self.foods["Stone"] += 1
        
        #Elves
        def Elves():
                player_attack_power = random.randint(5,25)
                Monsters.Elves()
                attack_chance_Elves = random.randint(1,15)

                while Monsters.evles.hp > 0:
                    if attack_chance_Elves <= 6:
                        typingPrint("You attack the Elf.")
                        Monsters.elves.hp -= {player_attack_power}
                    elif attack_chance_Elves <= 10:
                        typingPrint("The Elf attacked you.")
                        self.health -= {Monsters.elves.damage}
                        if random.randint(1, 10) == 9:
                            print("The strength of the Elf surprises you. \nThey delt a crit attack.")
                            self.health -= 15
                    else:
                        print("You did a crit attack.")
                        Monsters.elves.hp -= 40
                    break
                if Monsters.elves.hp == 0:
                    print(f"You defeated a elf.\n (+ golds)\n (+ silvers) \n(+ Cabbage) \n(+ Fowl)")
                    self.currency["Gold"] += {Monsters.elves.gold}
                    self.currency["Silver"] += {Monsters.elves.silver}
                    self.foods["Apple"] += 1
                    self.foods["Leather"] += 1
                    if random.randint(1,20) == 13:
                        typingPrint("You gain something some else.")
                        self.potions["Health Potion"] += 1
        

        #Water Spirits
        def Water_Spirits():
                player_attack_power = random.randint(5,25)
                Monsters.Water_Spirits()
                attack_chance_Water_Spirits = random.randint(1,15)

                while Monsters.water_spirits.hp > 0:
                    if attack_chance_Water_Spirits <= 6:
                        typingPrint("You attack the Water Spirit.")
                        Monsters.water_spirits.hp -= {player_attack_power}
                    elif attack_chance_Water_Spirits <= 10:
                        typingPrint("The Water Spirit attacked you.")
                        self.health -= {Monsters.water_spirits.damage}
                        if random.randint(1, 10) == 9:
                            print("The strength of the Water Spirit surprises you. \nThey delt a crit attack.")
                            self.health -= 15
                    else:
                        print("You did a crit attack.")
                        Monsters.water_spirits.hp -= 40
                    break
                if Monsters.water_spirits.hp == 0:
                    print(f"You defeated a Water Spirit.\n (+ golds)\n (+ silvers) \n(+ Cabbage) \n(+ Fowl)")
                    self.currency["Gold"] += {Monsters.water_spirits.gold}
                    self.currency["Silver"] += {Monsters.water_spirits.silver}
                    self.foods["Iron"] += 1
                    self.foods["Stone"] += 1            
