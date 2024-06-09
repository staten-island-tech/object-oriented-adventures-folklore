from classes import typingInput
from betty import first_en_bet
from chu import first_en_Chu
from james import first_en_Jame

class picking_NPC:
    def picking_friend():
        picking_friends = typingInput("\x1B[3mWould you like to move A(left), D(right), or W(straight ahead)?\n").upper()
        if picking_friends == "A":
            first_en_bet()
        elif picking_friends == "W":
            first_en_Chu()
        elif picking_friends == "D":
            first_en_Jame()

picking_NPC.picking_friend()