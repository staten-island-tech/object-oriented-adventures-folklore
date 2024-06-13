import os
import time
import sys
from classes import typingInput
from classes import typingPrint
from player import player
from monster import Pikachu
from interface import main_character
from interface import interface

global FinalBoss_Begninning
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
    def Boss_Battle():
        final_t_battle = Pikachu(name= "Pikachu", hp= 200, damage= 35, crit= 50, power= "LIGHTNING BOLT")
        while main_character > 0 and final_t_battle > 1:
            player.battle(main_character, final_t_battle)
        if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
                    
        elif final_t_battle.hp <=0: 
            typingPrint("You defeated the " + final_t_battle.name + "")
            time.sleep(2)
            os.system('cls')
            go_home_exit()

        elif final_t_battle == 1:
            typingPrint("You ran out of the tower, you COWARD! Waiting for you outside was a shadow monster that killed you!")
            time.sleep(3)
            os.system('cls')

            d = typingInput("Would you like to restart? YES/NO\n").upper()
            if d == "YES":
                interface()
            elif d == "NO":
                sys.exit()
        global go_home_exit
        def go_home_exit():
            print("This is the last floor for the tower!\n ")
            print("This means that you have offically defeated the game!")
        
