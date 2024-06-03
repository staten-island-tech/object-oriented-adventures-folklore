#WORK IN PROGRESS (DANIEL)


import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor


class typer():
   global typingPrint
   global typingInput




   def typingPrint(text):
       for character in text:
           sys.stdout.write(character)
           sys.stdout.flush()
           time.sleep(0.01)
  
   def typingInput(text):
       for character in text:
           sys.stdout.write(character)
           sys.stdout.flush()
           time.sleep(0.01)
       value = input() 
       return value 
#\x1B[3m Italic
#\x1B[0m Normal Text


class boxes:
   global format_line
   def format_line(line, max_length):
       half_dif = (max_length - len(line)) / 2 # in Python 3.x float division
       return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'
  
   global boxed_msg
   def boxed_msg(msg):
       lines = msg.split('\n')
       max_length = max([len(line) for line in lines])
       horizontal = '+' + '-' * (max_length + 2) + '+\n'
       res = horizontal
       for l in lines:
           res += format_line(l, max_length)
       res += horizontal
       return res.strip()

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
       water_spirits.name = "Water Spirit"
       water_spirits.hp = 150
       water_spirits.gold = random.randint(5,20)
       water_spirits.silver = random.randint(10,20)
       water_spirits.damage = random.randint(5,15)