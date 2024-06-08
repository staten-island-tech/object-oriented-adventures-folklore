import os
import time
import sys
from betty import Betty
from chu import MrsChu
from james import James
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class picking_NPC:
    def picking_friend():
        picking_friends = typingInput("Would you like to go up, straight or down? \nA(Left) W(Straight Foward) S(Down)\n").upper()
        if picking_friends == "A":
            Betty.first_en_bet()
        elif picking_friends == "W":
            MrsChu.first_en_Chu()
        elif picking_friends == "S":
            James.first_en_Jame()
picking_NPC.picking_friend()
