import os
import time
import sys
#from betty import Betty
from chu import MrsChu
from james import James
from classes import typingInput

class picking_NPC:
    def picking_friend():
        os.system('cls')
        picking_friends = typingInput("Would you like to go up, straight or down? \nA(Left) W(Straight Foward) S(Down)\n").upper()
        if picking_friends == "A":
            print("Work in Progress")
        elif picking_friends == "W":
            MrsChu.first_en_Chu()
        elif picking_friends == "S":
            James.first_en_Jame()
picking_NPC.picking_friend()
