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
    
    def add_weapon_damage(self, weapon):
        new_damage = self.damage + weapon.damage
        self.damage = new_damage
        return self.damage 

    def attack_enemy(self, monster):
        d = random.randint(1,20)
        if d < 20:
            monster.hp -= self.damage
            print("You did" + self.damage + "to the" + monster.name)

        elif d == 20:
            monster.hp -= self.crit
            print("You did" + self.crit + "to the" + monster.name)
        return monster.hp
    
    def get_attacked(self, monster):
        a = random.randint(1,20)
        if a < 20:   
            self.hp -= monster.damage
            print("You were attacked! You took" + monster.damage + "and now have" + self.hp + "hp!")

        elif a == 20:
            self.hp -= monster.crit
            print("You were attacked! It was a critical hit! You took" + monster.crit + "and now have" + self.hp + "hp!")
    
    def dead(self):
        if self.hp == 0:
            print(self.name + ", you have 0 hp left and have just died!")
        else:
            print(self.name + "you have" + str(self.hp) + "hp!")