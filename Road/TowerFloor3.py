import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

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
        print("")
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
