#WORK IN PROGRESS (DANIEL)

import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor
import Monsters
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





class Inventory:
       #The amount of items in the player's inventory
       def __init__(self):
           self.potions = {"Health Potion": 0, "Speed Potion": 0, "Defense Potion": 0}
           self.foods = {"Fowl": 0, "Cake": 0, "Apple": 0, "Cabbage": 0}
           self.materials = {"Wood": 0, "Stone": 0, "Iron": 0, "Leather": 0}
      
       #Shows the amount of items
       def display_inventory(self):
           print("  ")
           print("---ɪɴᴠᴇɴᴛᴏʀʏ---")
           for item, quantity in self.potions():
               print(f"{item.capitalize()}: {quantity}")
           for item, quantity in self.foods():
               print(f"{item.capitalize()}: {quantity}")
           for item, quantity in self.materials():
               print(f"{item.capitalize()}: {quantity}")


       #Adding items to the player's inventory
       def add_potion(self, potion, quantity):
           self.potions[potion] += quantity
           print(f"You have acquired {quantity} {potion}(s).")
       def add_food(self, food, quantity):
           self.foods[food] += quantity
           print(f"You have acquired {quantity} {food}(s).")
       def add_material(self, material, quantity):
           self.materials[material] += quantity
           print(f"You have acquired {quantity} {material}(s).")
      
       #Using(Removing) items from the player's inventory
       def remove_potion(self, potion, quantity):
           if self.potions[potion] < quantity:
               print("You don't have enough of this potion.")
           else:
               self.potions[potion] -= quantity
               print("\n")
               print(f"You have used this {potion}.")
       def remove_food(self, food, quantity):
           if self.foods[food] < quantity:
               print("You don't have enough of this food.")
           else:
               self.potions[food] -= quantity
               print("\n")
               print(f"You ate a {food}.")
       def remove_materials(self, material, quantity):
           if self.materials[material] < quantity:
               print("You don't have enough of this material.")
           else:
               self.potions[material] -= quantity
               print("\n")
               print(f"You have used this {material}.")