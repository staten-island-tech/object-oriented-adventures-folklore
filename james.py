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
        typingPrint("\x1B[3m You decided to back to the road.")
        time.sleep(2)
        os.system('cls')
        James.first_en_Jame()

class James:
    def first_en_Jame():

        picking_friend()
        if picking_friends == "S":
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
                if PunchingJames == "RUN":
                    typingPrint("\x1B[0mYou have escaped and you reached the merchant.")
                if PunchingJames == "SLAUGHTER":
                    typingPrint("\x1B[0mYou murdered James, and you run to the river to clean yourself up. Then you ran towards the mercahnt to get other materials.")
                os.system('cls')

            if PunchJames == "NO":
                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You should never trust a me."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mJames murdered you.")

James.first_en_Jame()
