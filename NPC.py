import os
import time

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
    global picking_friends
    picking_friends = input("Would you like to go up, straight or down? B(Up) C(Straight Foward) J(Down)")

class Betty:
    def bet():
                #After arriving in the village for the first time and you pick Betty as your friend.
        if picking_friends == "B":
                    #Betty's Lines
            os.system('cls')
            print("\x1B[3m You saw a magnifcent tower.\nA strong magically energy draws you near.\nAs you apoarched you saw a girl and you ask for her name.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print("Hi, I am new to this town.\nCan you tell me your name?")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mBetty:")
            print("Hi, I am Betty and I can show you around.\nThis village is known for its fishing ports and advancements in the water way.\nAt the center of the village, we have a huge water fountain, which is like healing sprinkler.\nOnce you get near it, it should heal you completely.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print("Thank you.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mBetty:")    
            print("Follow me, I can show you where you can get materials and supplies.\nThe merchant is very nice and the stuff is pretty cheap.")
            time.sleep(5)
            os.system('cls')

class MrsChu:
    
    def Chu():
        if picking_friends == "C":
            os.system('cls')
            print("\x1B[3mYou saw a fountain.\nThe flowers flew out of the structure like fairies covering the square in a shimmering light.\nA powerful rejuvenating shock went through you.\nAs you walk up to the fountain, you found your math teacher from your previous world.\nMrs. Chu looks shocked and quickly waved to you.")
            time.sleep(7)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print(boxed_msg(" Mrs.Chu?!?\nIs that you?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            print(boxed_msg("Oh my gosh, is that you?\nI suddently woke up in this world a month ago."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you were in school for the last month."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            print(boxed_msg("Come on let me show you around, it is hard to survive here.\nAs you witness just now, this fountain was a structure that contain a huge healing stone.\n This heals you as you get sprinkled by the water.\nYou clothes would still get wet though."))
            time.sleep(8)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print(boxed_msg("Do you know how I can get back?"))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            print(boxed_msg("Follow me.\nLook over there.\nThat is the Folklore Forest.\nThere is a huge tower in the center.\nTo get back home, you have to complete the five floors.\nOn the final, you have to defeat a boss and it would grant you a wish, and that is your ticket home.\nBy the markets, you would find Augustine, he is the merchant who you can sell and buy materials from."))
            time.sleep(10)
            os.system('cls')


MrsChu.Chu()
Betty.bet()