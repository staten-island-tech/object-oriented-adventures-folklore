import os
import time
import sys
from classes import typingInput
from classes import typingPrint
from monster import Floor4_Chikungunya
from interface import main_character, interface
from player import player
# Beast
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
        fourth_t_battle = Floor4_Chikungunya(name= "Chikungunya", hp= 250, damage= 25, crit= 45, power= "Drop of Death")
        while main_character > 0 and fourth_t_battle > 1:
            player.battle(main_character, fourth_t_battle)
        if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
        elif fourth_t_battle.hp <=0: 
            typingPrint("You defeated the " + fourth_t_battle.name + "")
            time.sleep(2)
            os.system('cls')
            Floor4_Exit()

        elif fourth_t_battle == 1:
            typingPrint("You ran out of the tower, you COWARD! Waiting for you outside was a shadow monster that killed you!")
            time.sleep(3)
            os.system('cls')

            d = typingInput("Would you like to restart? YES/NO\n").upper()
            if d == "YES":
                interface()
            elif d == "NO":
                sys.exit()
                
    global Floor4_Exit
    def Floor4_Exit():
        print("You are moving on to the Boss Battle :>")
        time.sleep(1)
        os.system('cls')
FloorFour.Floor4_Beginning