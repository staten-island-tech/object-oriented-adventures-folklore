import os
import time
import sys
import betty
import chu
import james
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

class Global:
    global picking_friend
    def picking_friend():
        global picking_friends
        picking_friends = typingInput("Would you like to go up, straight or down? \nA(Left) W(Straight Foward) S(Down)\n").upper()

class Betty():
    os.system('cls')
    if picking_friends == "A":
        #Going to Betty.
        os.system('cls')
        typingPrint("\x1B[3m You find yourself drawn to the towering structure in the center of the city.\n Its spire reaches up to the sky, beckoning you to come closer.\n As you approach the base of the tower, you notice a young woman sitting on the steps.")
        time.sleep(5)
        os.system('cls')
        betty()

class Chu():
    os.system('cls')
    if picking_friends == "W":
        chu()

class James():
    os.system('cls')
    if picking_friends == "S":
        james()