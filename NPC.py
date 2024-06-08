from betty import Betty
from chu import MrsChu
from james import James
from classes import typingInput

class picking_NPC:
    global picking_friend
    def picking_friend():
        picking_friends = typingInput("\x1B[3mWould you like to move B(left), C(right), or J(straight ahead)?\n").upper()
        if picking_friends == "B":
            Betty.first_en_bet()
        elif picking_friends == "C":
            MrsChu.first_en_Chu()
        elif picking_friends == "J":
            James.first_en_Jame()
    def run_NPC():
        picking_friend()

picking_NPC.run_NPC()