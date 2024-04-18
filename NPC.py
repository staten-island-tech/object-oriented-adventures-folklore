import os
import time
import sys
class typer():
    global typingPrint
    global typingInput


    def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    
    def typingInput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        value = input()  
        return value  

from math import ceil, floor

#\x1B[3m Italic 
#\x1B[0m Normal Text

class boxes:
    global format_line 
    def format_line(line, max_length):
        half_dif = (max_length - len(line)) / 2 # in Python 3.x float division
        return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'
    
    global boxed_msg
    def boxed_msg(msg): 
        lines = msg.split('\n')
        max_length = max([len(line) for line in lines])
        horizontal = '+' + '-' * (max_length + 2) + '+\n'
        res = horizontal
        for l in lines:
            res += format_line(l, max_length)
        res += horizontal
        return res.strip()

class Global:
    global picking_friend
    def picking_friend():
        global picking_friends
        picking_friends = typingInput("Would you like to go up, straight or down? A(Left) W(Straight Foward) S(Down)\n").upper()
    global encountering_characters
    def encountering_characters():
        global Meeting_Another_Character
        Meeting_Another_Character = typingInput("\x1B[3m You decided to back to the road.")
        time.sleep(5)
        os.system('cls')
        ###work from here




class Betty:
    def first_en_bet():
                #After arriving in the village for the first time and you pick Betty as your friend.
        picking_friend()
        if picking_friends == "A":
                    #Betty's Lines
            os.system('cls')
            typingPrint("\x1B[3m You find yourself drawn to the towering structure in the center of the city.\n Its spire reaches up to the sky, beckoning you to come closer.\n As you approach the base of the tower, you notice a young woman sitting on the steps.")
            time.sleep(5)
            os.system('cls')

            going_to_Betty = typingInput("\x1B[3m Would you like to approach her? (yes/no)").upper()
            if going_to_Betty == "YES":
                bet_Continue()
            
            if going_to_Betty == "NO":
                bet_notcontinue()
            time.sleep(5)
            os.system('cls')
            
            global bet_Continue
            def bet_Continue():
                print("\x1B[0mStranger:")    
                typingPrint(boxed_msg("Are you here to climb the tower?"))
                time.sleep(2)
                os.system('cls')

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

            def bet_notcontinue():
                encountering_characters()



class MrsChu:
    def first_en_Chu():
        picking_friend()
        if picking_friend == "W":
            os.system('cls')
            typingPrint("\x1B[3mYou saw a fountain.\nThe flowers flew out of the structure like fairies covering the square in a shimmering light.\nA powerful rejuvenating shock went through you.\nAs you walk up to the fountain, you found your math teacher from your previous world.\nMrs. Chu looks shocked and quickly waved to you.")
            time.sleep(7)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg(" Mrs.Chu?!?\nIs that you?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            typingPrint(boxed_msg("Oh my gosh, is that you?\nI suddently woke up in this world a month ago."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you were in school for the last month."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            typingPrint(boxed_msg("Come on let me show you around, it is hard to survive here.\nAs you witness just now, this fountain was a structure that contain a huge healing stone.\n This heals you as you get sprinkled by the water.\nYou clothes would still get wet though."))
            time.sleep(8)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("Do you know how I can get back?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            typingPrint(boxed_msg("Follow me.\nLook over there.\nThat is the Folklore Forest.\nThere is a huge tower in the center.\nTo get back home, you have to complete the five floors.\nOn the final, you have to defeat a boss and it would grant you a wish, and that is your ticket home.\nBy the markets, you would find Augustine, he is the merchant who you can sell and buy materials from."))
            time.sleep(10)
            os.system('cls')

class James:
    def first_en_Jame():
        picking_friend()
        if picking_friend == "S":
            os.system('cls')
            typingPrint("\x1B[3mYou saw a guy with a shady hood over his head.\nHe was walking up to a old lady and sneakly take her purse from her pockets. \nYou followed him behind and noticed you.")

           
            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("You are not being sneaky following me like that."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("..."))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("How come I never seen you around here?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("I am new to this town."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("I know you saw what I did.\n So either you join me or I will end you right here and now."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("I guess I would join you."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("Okay great. \nI will show you around. \nMy names is James by the way. \nThis is the underground alley of this town.\nThis is basically the black market."))
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mYou have the option to punch him, while he is distracted or just wait and see what happends...")
            PunchJames = typingInput("Would you like to punch games? (yes/no)").upper()
            if PunchJames == "YES":
                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You back stabbing mole rat!"))
                time.sleep(3)
                os.system('cls')

                PunchingJames = typingInput("Run or Slaughter him? (run/slaughter)").upper()
                if PunchingJames == "Run":
                    typingPrint("\x1B[0mYou have escaped and you reached the merchant.")
                else:
                    typingPrint("\x1B[0mYou murdered James, and you run to the river to clean yourself up. Then you ran towards the mercahnt to get other materials.")
                os.system('cls')

            if PunchJames == "NO":
                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You should never trust a me."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[0mJames murdered you.")



James.first_en_Jame()
MrsChu.first_en_Chu()
Betty.first_en_bet()