import os
import time
import sys
from Entrance import going_into_tower
from Forest import forestman

#System Typing
#########################################################################################################################################################
class typer():
    global typingPrint
    global typingInput
    global typingspeed
    typingspeed = 0.01
    def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(typingspeed)
    
    def typingInput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(typingspeed)
        value = input()
        return value
from math import ceil, floor
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
#########################################################################################################################################################
class Go_Where():
    global different_location
    def different_location():
        if Location == "A":
            going_into_tower.asking_to_enter()
        elif Location == "B":
            forestman.forester()
        elif Location == "C":
            print("ya")
        elif Location == "D":
            picking_location()
        else:
            picking_location()

    global picking_location
    def picking_location():
        global Location
        Location = typingInput("Would you like to go?\n A) Tower\n B) Forest\n C) Village\n D)Road \n").upper()
        different_location()
    picking_location()
    

