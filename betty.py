import os
import time
import merhcant
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class Betty:
    global first_en_bet
    def first_en_bet():
        global Choosing_Going_to_Betty
        def Choosing_Going_to_Betty():
            global Going_to_Betty
            Going_to_Betty = typingInput("Would you like to appoarch her? Y/N\n ").upper()
            Try_Again_Choosing_Going_to_Betty()
        global Try_Again_Choosing_Going_to_Betty
        def Try_Again_Choosing_Going_to_Betty():
            if Going_to_Betty == "Y":
                Yes_Going_to_Betty()
            if Going_to_Betty == "N":
                Yes_Going_to_Betty()
            else:
                typingPrint("Are you stupid?")
                Choosing_Going_to_Betty()
        global Yes_Going_to_Betty
        def Yes_Going_to_Betty():
            os.system('cls')
            print("\x1B[0mStranger:")    
            global Climb_Poets_Tower
            Climb_Poets_Tower = typingInput(boxed_msg("Either way, Betty approaches you. Are you here to climb the Tortured Poets Department?\n (yes/no)\n(You also have the option to ask for information about the tower.)")).upper()
            time.sleep(2)
            os.system('cls')

        
        global Input_Climb_Poets_Tower
        def Input_Climb_Poets_Tower():
            if Climb_Poets_Tower == "YES":
                os.system('cls')
                yes_to_climb_poets_tower()
            if Climb_Poets_Tower == "NO":
                os.system('cls')
                not_climb_poet_tower()
                

        def yes_to_climb_poets_tower():
            os.system('cls')
            print("Stranger")
            typingPrint(boxed_msg("You better be careful. \nThe tower belonged to a powerful moonlit witch. \nNo one has ever made it to the top."))
            time.sleep(5)
            os.system('cls')

            print("Travler:")
            typingPrint(boxed_msg("Thank you for the advice."))
            time.sleep(1)

            os.system('cls')
            typingPrint("\x1B[3m You entered through the gates of the tower, knowing full well you have no experience.\n As you arrived to the stairs of the tower, a forced consumed you and you were transported back in time.\n You ended put back in front of Betty.")
            time.sleep(5)
            os.system('cls')

            print("Travler:")
            typingPrint(boxed_msg("\x1B[0mWhat happened?"))
            time.sleep(1)
            os.system('cls')
            Choosing_Going_to_Betty()
            
        def not_climb_poet_tower():
            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("No, not really.\n I am new to this town."))
            time.sleep(5)
            os.system('cls')
               
            print("\x1B[0mBetty:")
            typingPrint(boxed_msg("Hi, I am Betty and I can show you around.\nThis village is known for its fishing ports and advancements in the water way.\nAt the center of the village, we have a huge water fountain, which is like healing sprinkler.\nOnce you get near it, it should heal you completely."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("Thank you."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mBetty:")    
            typingPrint(boxed_msg("Follow me, I can show you where you can get materials and supplies.\nThe merchant is very nice and the stuff is pretty cheap."))
            time.sleep(5)
            os.system('cls')
            merhcant.Merchant()

        


####################################################
        os.system('cls')
        typingPrint("\x1B[3mYou decide to turn left. \n As you walk, you eventually end up in a city.\n Exploring the city, you find a towering structure in the center of the city.")
        time.sleep(5)
        os.system('cls')
        typingPrint("\x1B[3mYou find yourself drawn to the towering structure.\n Its spire reaches up to the sky, beckoning you to come closer.\n As you approach the base of the tower, you notice a young woman sitting on the steps.")
        time.sleep(5)
        os.system('cls')
        Choosing_Going_to_Betty()