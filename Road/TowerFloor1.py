import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

#Moonlight Monarch
global Floor1_Beginning
class FloorOne:
    def Floor1_Beginning():
        typingPrint("\x1B[2mWelcome to the tower! Here you will show that you are worthy of the skills you have gained along the way\n")
        typingPrint("\x1B[2mThere are a total of five floors in this tower.\n Each floor you complete you gain a nessesary stone for the engraved rock from the final floor \n")
        typingPrint("\x1B[2mUsing the stones you gained you will place them into the rock to indicate you have completed the tower")
        time.sleep(8)
        os.system('cls')
        typingPrint("\x1B[2mAfter the rock is complete you will be given the choice to either stay in the village or return to the real world")
        time.sleep(2)
        os.system('cls')
        print("Now, let the games begin")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[5Entering...")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2You entered the through the halls of a the dark skyscraper.")
        typingPrint("\x1B[2At the center of the tower, you saw mauve beacon.")
        time.sleep(5)
        os.system('cls')
        typingPrint("\x1B[2You walked up towards the beacon.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2As you place your hand on the illuminating light, you black out.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2You slowly lose your sight, as the lavender light consumed you.")
        time.sleep(2)
        os.system('cls')
        print("Taveller:")
        typingPrint("What just happened?")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2As you began to wake up, you realized you are surrounded by thounsands glowing creatures.")
        typingPrint("\x1B[2Suddenly, a magenta light shoot out of the chandelier, pierce through your skin.")
        time.sleep(8)
        os.system('cls')
        typingPrint("\x1B[2Any armor you have on would have no effect on this floor.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2As you look up to see what stike you, thousands of butterfly flew across the room.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2They illuminated the room with a eerie purple glow.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2These butterflies began to glow brighter and brighter, ready to attack.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2A streeching sound filled the room.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2A mesmerizing musical tune plays from nowhere and echoes everywhere.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[3Signaling the start of Floor 1.")
        time.sleep(1)
        os.system('cls')
    def Floor1_Battle():
        print("")
    def Floor1_Exit():
        print("You are now moving on to the second floor")
        time.sleep(1)
        os.system('cls')
FloorOne.Floor1_Beginning


        