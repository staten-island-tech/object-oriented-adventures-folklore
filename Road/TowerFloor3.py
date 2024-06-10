import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint
from interface import main_character, interface
from monster import Floor3_Anlliasio_Altosoei
from player import player

#Dueling twins Anlliasio &  Altosoei
class FloorThree:
    def Floor3_Beginning():
        typingPrint("\x1B[2mYou have now reached floor 3.\n This floor consists of the two dueling twins called Anlliasio and Altosoei")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mThey have no empathy for humans, and especially those that come from the oustide world \n")
        typingPrint("\x1B[2mAnlliasio an Altosoei were created by the leader of the tower, who is over course still unknown.")
        time.sleep(5)
        os.system('cls')
        typingPrint("\x1B[2mIn order to defeat them, find a way to hit them at the same time")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mIf you wait too long to hit one of them, they will start to regain health. \n There is also a 2:30 timer for you to complete the challenge.")
        time.sleep(3)
        os.system('cls')
        typingPrint("* If you fail to complete the challenge you will have to restart *")
        time.sleep(2)
        os.system('cls')
        typingPrint("Signaling floor three to start*")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[5mEntering...")
        time.sleep(1)
        os.system('cls')
    def Floor3_Battle():
        third_t_battle = Floor3_Anlliasio_Altosoei(name= "Altosoei", hp= 200, damage= 20, crit= 40, power= "Duplication_Blast")
        while main_character > 0 and third_t_battle > 1:
            player.battle(main_character, third_t_battle)
        if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
        elif third_t_battle.hp <=0: 
            typingPrint("You defeated the " + third_t_battle.name + "")
            time.sleep(2)
            os.system('cls')
            Floor3_Exit()

        elif third_t_battle == 1:
            typingPrint("You ran out of the tower, you COWARD! Waiting for you outside was a shadow monster that killed you!")
            time.sleep(3)
            os.system('cls')

            d = typingInput("Would you like to restart? YES/NO\n").upper()
            if d == "YES":
                interface()
            elif d == "NO":
                sys.exit()

    global Floor3_Exit
    def Floor3_Exit():
        print("You are moving on to floor 4")
        time.sleep(1)
        os.system('cls')
    def Floor3_Ending():
        typingPrint("\x1B[2mThe butterflies slowly dissipate.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2mThe beacon glowed ever more brightly.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2mBeing distracted by the light, the butterflies reappeared and striked through you.")
        time.sleep(2)
        os.system('cls')
        typingPrint("\x1B[2mThe pain caused you to fall in a deep sleep.")
        time.sleep(1)
        os.system('cls')
        typingPrint("\x1B[2mYou wake up at the entrance of the tower, once again.")
        time.sleep(1)
        os.system('cls')
FloorThree.Floor3_Beginning
