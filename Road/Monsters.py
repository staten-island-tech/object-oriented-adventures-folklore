import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class Maldachaunians():
   def __init__(maldachaunians, name:str, hp:int, gold: int, silver: int, damage: int):
       super().__init__(name, hp, gold, silver, damage)
       maldachaunians.name = "Maldachaunian"
       maldachaunians.hp = 100
       maldachaunians.gold = random.randint(2,5)
       maldachaunians.silver = random.randint(3,10)
       maldachaunians.damage = random.randint(5, 10)


class Wimitescu():
   def __init__(wimitescu , name:str, hp:int, gold: int, silver: int, damage: int):
       super().__init__(name, hp, gold, silver, damage)
       wimitescu.name = "Wimitescu"
       wimitescu.hp = 200
       wimitescu.gold = random.randint(3,8)
       wimitescu.silver = random.randint(8,15)
       wimitescu.damage = random.randint(10,20)


class Elves():
   def __init__(elves, name:str, hp:int, gold: int, silver: int, damage: int):
       super().__init__(name, hp, gold, silver, damage)
       elves.name = "Elves"
       elves.hp = 100
       elves.gold = random.randint(5,15)
       elves.silver = random.randint(10,20)
       elves.damage = random.randint(5,10)


class Water_Spirits():
   def __init__(water_spirits, name:str, hp:int, gold: int, silver: int, damage: int):
       super().__init__(name, hp, gold, silver, damage)
       water_spirits.name = "Maldachaunian"
       water_spirits.hp = 150
       water_spirits.gold = random.randint(5,20)
       water_spirits.silver = random.randint(10,20)
       water_spirits.damage = random.randint(5,15)
