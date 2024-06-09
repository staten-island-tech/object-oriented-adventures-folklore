import os
import time
import sys
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class Betty:
    global first_en_bet
    def first_en_bet():
        global Choosing_Going_to_Betty
        def Choosing_Going_to_Betty():
            global Going_to_Betty
            Going_to_Betty = typingInput("Would you like to appoarch her? YES/NO\n ").upper()
            if Going_to_Betty == "YES":
                Yes_Going_to_Betty()
            elif Going_to_Betty == "NO":
                Yes_Going_to_Betty()
            else:
                typingPrint("Are you stupid?")
                time.sleep(2)
                os.system("cls")
                Choosing_Going_to_Betty()

        global Yes_Going_to_Betty
        def Yes_Going_to_Betty():
            global Climb_Poets_Tower
            os.system('cls')
            typingPrint("\x1B[3mEither way, the stranger approaches you.\n")    
            print("\x1B[0mStranger:")  
            Climb_Poets_Tower = typingInput(boxed_msg("Are you here to climb the Tortured Poets Department? YES/NO \n(You also have the option to ask for information about the tower.)") + "\n").upper()
            os.system('cls')
            if Climb_Poets_Tower == "YES":
                os.system('cls')
                yes_to_climb_poets_tower()
            if Climb_Poets_Tower == "NO":
                os.system('cls')
                not_climb_poet_tower()
                

        def yes_to_climb_poets_tower():
            os.system('cls')
            print("\x1B[0mStranger")
            typingPrint(boxed_msg("You better be careful. \nThe tower belonged to a powerful moonlit witch. \nNo one has ever made it to the top."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("Thank you for the advice."))
            time.sleep(1)

            os.system('cls')
            typingPrint("\x1B[3m You entered through the gates of the tower, knowing full well you have no experience.\n As you arrived to the stairs of the tower, a forced consumed you and you were transported back in time.\n You ended put back in front of the stranger.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("What happened?"))
            time.sleep(1)
            os.system('cls')
            Choosing_Going_to_Betty()
            
        def not_climb_poet_tower():
            print("\x1B[0mYou:")
            typingPrint(boxed_msg("No, not really.\n I'm new here and I'm not really sure what to do."))
            time.sleep(5)
            os.system('cls')
               
            print("\x1B[0mBetty:")
            typingPrint(boxed_msg("Hi, I am Betty. If you want, I can show you around.\nThis village is known for its fishing ports and advancements in the water way.\nAt the center of the village, we have a huge water fountain, which is like healing sprinkler.\nOnce you get near it, it should heal you completely."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("Thank you."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mBetty:")    
            typingPrint(boxed_msg("Follow me, I can show you where you can get materials and supplies.\nThe merchant is very nice and the stuff is pretty cheap."))
            time.sleep(4)
            os.system('cls')

            typingPrint("You have reached the end of your free trial for the Folklore game!\n In order to unlock the rest of the game, you will have to pay $4.99!")
            time.sleep(4)
            os.system('cls')
                
            pay = typingInput("Would you like to pay? YES/NO\n").upper()
            if pay == "YES":
                print("Just kidding!\n The developers have no clue on what to do next in order to complete the game.\n We thank you for playing! The end.")
                time.sleep(5)
                sys.exit()
            if pay == "NO": 
                print("Thanks for trying out our game! The end.")
                time.sleep(3)
                sys.exit()

####################################################
        os.system('cls')
        typingPrint("\x1B[3mYou decide to turn left. \n As you walk, you eventually end up in a village.\n Exploring the village, you find a towering structure in the center.")
        time.sleep(5)
        os.system('cls')
        
        typingPrint("\x1B[3mYou find yourself drawn to the towering structure.\n Its spire reaches up to the sky, beckoning you to come closer.\n As you approach the base of the tower, you notice a young woman sitting on the steps.")
        time.sleep(5)
        os.system('cls')
        Choosing_Going_to_Betty()