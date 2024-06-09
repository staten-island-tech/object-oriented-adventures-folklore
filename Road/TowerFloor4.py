import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

# Beaste
class FloorFour:
    def Floor4_Beginning():
        print("You have reached the fourth floor. ")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mFor this floor, you will be battling Chikungunya, a giant beast that was quite literally named after a disease by the village people\n")
        typingPrint("\x1B[2mThis is because of the large quantities of venom it produces every few seconds\n It leaves a trail whereever it goes, and if you aren't careful you are going to slowly lose HP")
        time.sleep(4)
        os.system('cls')
        typingPrint("\x1B[2mBy completing this floor, you will obtain the last and final stone needed, the 'gold light stone'")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mBut do not take this floor lightly, as it is only one level below the final boss  ")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mThe final boss and Chikungunya have been together for thousands of years -- lots of taming, meals together, and friendly pets....")
        time.sleep(2)
        os.system('cls')
        typingPrint("Initiating the fourth floor to start")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[5mEntering...")
        time.sleep(1)
    def Floor4_Battle():
        print("")
    def Floor4_Exit():
        print("You are moving on to the Boss Battle :>")
        time.sleep(1)
        os.system('cls')
FloorFour.Floor4_Beginning