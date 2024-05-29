import random
import datetime
import os
import time
import json
import sys
from math import ceil, floor
import Monsters
import Inventory
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


class Players:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.currency = {"Gold": 0, "Silver": 0, "Bronze": 0}
        self.health = {"Health": 100}
        self.sheild = {"Sheild" : 0}
        self.location = [] #Fix this
        self.inventory = Inventory()
        self.potions = {"Health Potion": 0, "Speed Potion": 0, "Defense Potion": 0}
        self.foods = {"Fowl": 0, "Cake": 0, "Apple": 0, "Cabbage": 0}
        self.materials = {"Wood": 0, "Stone": 0, "Iron": 0, "Leather": 0}
    def display_stats(self):
        print("   ")
        print("----Stats/Info----")
        print("Name:", self.name)
        print("Age:", self.age)
    #Might add a magic system
        print("Resources:")
        for resource, value in self.currency.potions():
           print(f" {resource.capitalize()}: {value}")
        for resource, value in self.currency.foods():
           print(f" {resource.capitalize()}: {value}")
        for resource, value in self.currency.materials():
           print(f" {resource.capitalize()}: {value}")


        print("Location:", self.location) #FIX


 #############################################     
    def move(self, location):       
        print("   ")
        print(f"You arrive at {location}.")
 #############################################   
   #else:
       #return False