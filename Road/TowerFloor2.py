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

#Pchvpxa  &  Anlliasio
class FloorTwo:
    def Floor2_Beginning():
        typingPrint("You have reached floor level two!\n Here, you will have to go against the ")
        time.sleep(2)
        os.system('cls')
        typingPrint("These villians are called the Pchvpxa, are they wield weapons of great power. ")
        time.sleep(1)
        os.system('cls')
        typingPrint("Some carry rifles/guns powered by the element they are trained for while others carry hammers.")
        time.sleep(2)
        os.system('cls')
        typingPrint("The best way to defeat them is to crit shot a whole bunch of them at the same time.")
        time.sleep(2)
        os.system('cls')
        typingPrint("All things aside, its time to fight.")
        time.sleep(1)
        os.system('cls')
        input = ("START")

    def Floor2_Battle():
        print("")
    def Floor2_Exit():