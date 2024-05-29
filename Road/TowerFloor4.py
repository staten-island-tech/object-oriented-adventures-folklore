import os
import time
import sys

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
# Beaste
class FloorFour:
    def Floor4_Beginning():
        print("You have reached the fourth floor. ")
        time.sleep(2)
        os.system('cls')
        typingPrint("For this floor, you will be battling Chikungunya, a giant beast that was quite literally named after a disease by the village people\n")
        typingPrint("This is because of the large quantities of venom it produces every few seconds\n It leaves a trail whereever it goes, and if you aren't careful you are going to slowly lose HP")
        time.sleep(4)
        os.system('cls')
        typingPrint("By completing this floor, you will obtain the last and final stone needed, the 'gold light stone'")
        time.sleep(2)
        os.system('cls')
        typingPrint("Initiating the fourth floor to start")
        time.sleep(1)
        os.system('cls')
        typingPrint("Entering...")
        time.sleep(1)
        os.system('cls')
    def Floor4_Battle():
        print("")
    def Floor4_Exit():
        print("You are moving on to the Boss Battle :>")
        time.sleep(1)
        os.system('cls')
