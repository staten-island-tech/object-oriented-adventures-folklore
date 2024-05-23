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
#Dueling twins Anlliasio &  Altosoei
class FloorThree:
    def Floor3_Beginning():
        typingPrint("You have now reached floor 3.\n This floor consists of the two dueling twins called Anlliasio and Altosoei")
        time.sleep(2)
        os.system('cls')
        typingPrint("They have no empathy for humans, and especially those that come from the oustide world \n")
        typingPrint("Anlliasio an Altosoei were created by the leader of the tower, who is over course still unknown.")
        time.sleep(4)
        os.system('cls')
        typingPrint("In order to defeat them, find a way to hit them at the same time")
        time.sleep(2)
        os.system('cls')
        typingPrint("If you wait too long to hit one of them, they will start to regain health. \n There is also a 2:30 timer for you to complete the challenge.")
        time.sleep(2)
        os.system('cls')
        typingPrint("* If you fail to complete the challenge you will have to restart *")
        time.sleep(1)
        os.system('cls')
        typingPrint("Signaling floor three to start*")
        time.sleep(1)
        os.system('cls')
    def Floor3_Battle():
        print("")
    def Floor3_Exit():
        print("You are moving on to floor 4")
        time.sleep(1)
        os.system('cls')
    def Floor3_Ending():
        typingPrint("The butterflies slowly dissipate.")
        time.sleep(1)
        os.system('cls')
        typingPrint("The beacon glowed ever more brightly.")
        time.sleep(1)
        os.system('cls')
        typingPrint("Being distracted by the light, the butterflies reappeared and striked through you.")
        time.sleep(1)
        os.system('cls')
        typingPrint("The pain caused you to fall in a deep sleep.")
        time.sleep(1)
        os.system('cls')
        typingPrint("You wake up at the entrance of the tower, once again.")
        time.sleep(1)
        os.system('cls')
        going_into_tower.asking_to_enter()
