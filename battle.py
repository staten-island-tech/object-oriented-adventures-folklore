import random 
import time
import os
import json
from classes import typingPrint
from monster import Monster
from monster import maldachaunians
from monster import elves
from monster import element_spirits
from player import player 
test = open("monster_data.json", encoding="utf8")
data = json.load(test)

class battle_system:
    global attack_maldachaunians
    global attack_elves
    global attack_element_spirits
    global crit_attack_maldachaunians
    global crit_attack_elves
    global crit_attack_element_spirits
    global fight_monster
    def attack_maldachaunians(self, maldachaunians):
        new_monster_hp = maldachaunians.hp - self.damage
        maldachaunians.hp = new_monster_hp
        return maldachaunians.hp 
    
    def attack_elves(self, elves):
        new_elf_hp = elves.hp - self.damage
        elves.hp = new_elf_hp
        return elves.hp
    
    def attack_element_spirits(self, element_spirits):
        new_spirit_hp = element_spirits.hp - self.damage
        element_spirits.hp = new_spirit_hp
        return element_spirits.hp 
    
    def crit_attack_maldachaunians(self, maldachaunians):
        new_monster_hp = maldachaunians.hp - self.crit
        maldachaunians.hp = new_monster_hp
        return maldachaunians.hp
    
    def crit_attack_elves(self, elves):
        new_elf_hp = elves.hp - self.crit
        elves.hp = new_elf_hp
        return elves.hp
    
    def crit_attack_element_spirits(self, element_spirits):
        new_spirit_hp = element_spirits.hp - self.crit
        element_spirits.hp = new_spirit_hp
        return element_spirits.hp 

    def choose_to_attack():
        player("", 100, 100, 10, 10, [], 5, 10)
        maldachaunians("", 20, "", 5, 10, "")
        print("1. Attack!")
        print("2. Go into inventory")
        print("3. Run away... (you wuss)")
        global choose
        choose = int(input("What would you like to do?\n"))
        x = random.randint(1,100)

        if choose == 1:
            if fight_monster == "MALDACHAUIANS":
                if x < 100:
                    attack_maldachaunians(player, maldachaunians)
                elif x == 100:
                    crit_attack_maldachaunians(player, maldachaunians)
            if fight_monster == "ELVES":
                if x < 100:
                    attack_elves(player, elves)
                elif x == 100:
                    crit_attack_elves(player, elves)
            if fight_monster == "ELEMENT_SPIRIT":
                if x < 100:
                    attack_element_spirits(player, element_spirits)
                if x == 100:
                    crit_attack_element_spirits(player, element_spirits)

fight_monster = "MALDACHAUIANS"
battle_system.choose_to_attack()