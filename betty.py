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

Betty.first_en_bet()