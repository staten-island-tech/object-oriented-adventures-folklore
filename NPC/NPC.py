import os
import time
import sys
#from betty import Betty
from chu import MrsChu
from james import James
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

class picking_NPC:
    def picking_friend():
        os.system('cls')
        picking_friends = typingInput("Would you like to go up, straight or down? \nA(Left) W(Straight Foward) S(Down)\n").upper()
        if picking_friends == "A":
            print("Work in Progress")
        elif picking_friends == "W":
            MrsChu.first_en_Chu()
        elif picking_friends == "S":
            James.first_en_Jame()
picking_NPC.picking_friend()
