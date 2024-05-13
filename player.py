import monster
import random
import item

class player():
    def __init__(self, name: str, hp: int, max_hp: int, strength: int, speed: int, inventory: str, damage: int, crit: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.speed = speed
        self.inventory = inventory 
        self.damage = damage
        self.crit = crit

    def take_damage(self, attack):
        if attack > self.hp:
            self.hp = 0
            print(self.name + ", you have been killed and have 0 hp")
        else:
            self.hp -= attack
            print(self.name + "you have" + str(self.hp) + "hp")

    def gain_hp(self, amount):
        if amount > self.max_hp:
            print("You have" + str(self.max_hp) + "hp")
        else:
            self.hp += amount
            print("You have" + str(self.hp) + "hp")
    
    def damage_w_weapon(self, weapon):
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