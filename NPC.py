from betty import Betty
from chu import MrsChu
from james import James
from classes import typingPrint

class picking_NPC:
    def picking_friend():
        typingPrint("\x1B[3mWould you like to move B(left), C(right), or J(straight ahead)?\n").upper()
        picking_friends = input().upper()
        if picking_friends == "B":
            Betty.first_en_bet()
        elif picking_friends == "C":
            MrsChu.first_en_Chu()
        elif picking_friends == "J":
            James.first_en_Jame()

picking_NPC.picking_friend()