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
        typingPrint("\x1B[2mYou have reached the final boss. Congrats on being the first to reach this far.")
        time.sleep(3)
        os.system('cls')
        typingPrint("\x1B[2mSomeone's approaching from the dark...")
        time.sleep(1)
        os.system('cls')
        typingPrint("Unknown: Welcome welcome my partner! I am the leader and rule of this tower and you didn't event notice.\n")
        typingPrint("I am surprised you even it made it this far. Even then, you won't be able to defeat me\n")
        typingPrint("Try all you can. Show me what you are made of.")
        time.sleep(8)
        os.system('cls')
        typingPrint("You: Who are you? Partner?? Come out so I can see you!")
        time.sleep(2)
        os.system('cls')
        typingPrint("You: CHU?!!")
        time.sleep(1)
        os.system('cls')
        typingPrint("Chu: Surprised eh?\n")
        typingPrint("But now that you know, stop the chit chat. I didn't come her to reminisce, I came here to fight.")
        time.sleep(5)
        os.system('cls')
        typingPrint("You: You underestimate me. You'll regret betraying me...")
        time.sleep(2)
        typingPrint(" * intiating the final battle to begin * \n")
        typingPrint("\x1B[5mBattle starting...")
        time.sleep(3)
        os.system('cls')



        print("This is the last floor for the tower! Congratulations on completeing the game")