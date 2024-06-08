import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor
import Monsters
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

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