import os
import time
import sys
from classes import typingInput
from classes import typingPrint
from player import player
from monster import Floor1_Moonlight_Monarch
from interface import main_character
from interface import interface

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
        first_t_battle = Floor1_Moonlight_Monarch(name= "Monarch", hp= 100, damage= 10, crit= 15, power= "Tornado")
        while main_character > 0 and first_t_battle > 1:
            player.battle(main_character, first_t_battle)
        if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
        elif first_t_battle.hp <=0: 
            typingPrint("You defeated the " + first_t_battle.name + "")
            time.sleep(2)
            os.system('cls')
            Floor1_Exit()

        elif first_t_battle == 1:
            typingPrint("You ran out of the tower, you COWARD! Waiting for you outside was a shadow monster that killed you!")
            time.sleep(3)
            os.system('cls')

            d = typingInput("Would you like to restart? YES/NO\n").upper()
            if d == "YES":
                interface()
            elif d == "NO":
                sys.exit()
        
    global Floor1_Exit
    def Floor1_Exit():
        print("You are now moving on to the second floor")
        time.sleep(1)
        os.system('cls')
FloorOne.Floor1_Beginning


        