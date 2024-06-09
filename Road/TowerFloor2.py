import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

#Group of villains called 'Pchvpxa'
class FloorTwo:
    def Floor2_Beginning():
        typingPrint("\x1B[3You have reached floor level two!")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[3The villains on this floor are called the Pchvpxa, are they wield weapons of great power. ")
        time.sleep(3)
        os.system('cls')
        typingPrint("\x1B[3Some carry rifles/guns powered by the element they are trained for while others carry hammers.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[3The best way to defeat them is to crit shot a whole bunch of them at the same time.")
        time.sleep(2)
        os.system('cls')
        typingPrint("All things aside, its time to battle.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[5Entering Floor 2....")
    def Floor2_Battle():
        print("")
    def Floor2_Exit():
        print("You are now moving on to the thrid floor")
        time.sleep(1)
        os.system('cls')
FloorTwo.Floor2_Beginning