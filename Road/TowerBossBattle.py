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

class FinalBoss:
    def FinalBoss_Beginning():
        typingPrint("You finally emerge onto a platform at the very top of the tower.")
        time.sleep(1)
        os.system('cls')
        typingPrint("From here, you can see the entire forest, a sprawling metropolis that seems to stretch on forever.")
        time.sleep(1)
        os.system('cls')
        typingPrint("A gust of wind knocked you to your knees and a you turned around to see if anyone was there.")
        time.sleep(1)
        os.system('cls')
        typingPrint("A gust of wind knocked you to your knees and a you turned around to see if anyone was there.")
        time.sleep(1)
        os.system('cls')
        typingPrint("You saw a familiar figure standing right behind you.")
        time.sleep(1)
        os.system('cls')

        print("Traveller:")
        typingPrint("Mrs.Chu?")
        time.sleep(1)
        os.system('cls')
        print("Traveller:")
        typingPrint("What are you doing here?")
        time.sleep(1)
        os.system('cls')
        print("Traveller:")
        typingPrint("What are you doing here?")
        time.sleep(1)
        os.system('cls')