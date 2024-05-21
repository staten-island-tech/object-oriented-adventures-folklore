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

#Moonlight Monarch
class FloorOne:
    def Floor1_Beginning():
        typingPrint("You entered the through the halls of a the dark skyscraper.")
        time.sleep(1)
        os.system('cls')
        typingPrint("At the center of the tower, you saw mauve beacon.")
        time.sleep(1)
        os.system('cls')
        typingPrint("You walked up towards the beacon.")
        time.sleep(1)
        os.system('cls')
        typingPrint("As you place your hand on the illuminating light, you black out.")
        time.sleep(1)
        os.system('cls')
        typingPrint("You slowly lose your sight, as the lavender light consumed you.")
        print("Taveller:")
        typingPrint("What just happened?")
        time.sleep(1)
        os.system('cls')
        typingPrint("As you began to wake up, you realized you are surrounded by thounsands glowing creatures.")
        time.sleep(1)
        os.system('cls')
        typingPrint("Suddenly, a magenta light shoot out of the chandelier, pierce through your skin.")
        time.sleep(1)
        os.system('cls')
        typingPrint("Any armor you have on would have no effect on this floor.")
        time.sleep(1)
        os.system('cls')
        typingPrint("As you look up to see what stike you, thousands of butterfly flew across the room.")
        time.sleep(1)
        os.system('cls')
        typingPrint("They illuminated the room with a eerie purple glow.")
        time.sleep(1)
        os.system('cls')
        typingPrint("These butterflies began to glow brighter and brighter, ready to attack.")
        time.sleep(1)
        os.system('cls')
        typingPrint("A streeching sound filled the room.")
        time.sleep(1)
        os.system('cls')
        typingPrint("A mesmerizing musical tune plays from nowhere and echoes everywhere.")
        time.sleep(1)
        os.system('cls')
        typingPrint("Signaling the start of Floor 1.")
        time.sleep(1)
        os.system('cls')
    def Floor1_Battle():
        print("")
    def Floor1_Exit():
        print("You are moving on to floor 2")
        time.sleep(1)
        os.system('cls')


        