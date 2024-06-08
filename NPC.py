from betty import Betty
from chu import MrsChu
from james import James
from classes import typingInput

class picking_NPC:
    def picking_friend():
        picking_friends = typingInput("\x1B[3m Would you like to move A(left), D(right), or W(straight ahead)?\n").upper()
        if picking_friends == "A":
            Betty.first_en_bet()
        elif picking_friends == "W":
            MrsChu.first_en_Chu()
        elif picking_friends == "D":
            James.first_en_Jame()

picking_NPC.picking_friend()