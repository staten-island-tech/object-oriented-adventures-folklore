import os
import time
import sys
from classes import typingInput
from classes import typingPrint
from player import player
from monster import Floor2_Pchvpxa
from interface import main_character
from interface import interface

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
        second_t_battle = Floor2_Pchvpxa(name= "Pchvpxa", hp= 150, damage= 15, crit= 20, power= "Gunner")
        while main_character > 0 and second_t_battle> 1:
            player.battle(main_character, second_t_battle)
        if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
        elif second_t_battle.hp <=0: 
            typingPrint("You defeated the " + second_t_battle.name + "")
            time.sleep(2)
            os.system('cls')
            Floor2_Exit()

        elif second_t_battle == 1:
            typingPrint("You ran out of the tower, you COWARD! Waiting for you outside was a shadow monster that killed you!")
            time.sleep(3)
            os.system('cls')

            d = typingInput("Would you like to restart? YES/NO\n").upper()
            if d == "YES":
                interface()
            elif d == "NO":
                sys.exit()
    global Floor2_Exit
    def Floor2_Exit():
        print("You are now moving on to the thrid floor")
        time.sleep(1)
        os.system('cls')
FloorTwo.Floor2_Beginning