import os
import time
import sys
from interface import start
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint
import merhcant

class James:
    global first_en_Jame
    def first_en_Jame():
            os.system('cls')
            typingPrint("\x1B[3mYou decide to turn right.\n As you walk, you find yourself in a town.\n Looking around at the people you notice something.")
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mYou saw a guy with a shady hood over his head.\nHe was walking up to an old lady and sneakly take her purse from her pockets. \nYou followed him behind and he notices you.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("You are not being sneaky following me like that."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("..."))
            time.sleep(1)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("How come I never seen you around here?"))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("I am new to this town."))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("I know you saw what I did.\n So either you join me or I will end you right here and now."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mTraveller:")
            typingPrint(boxed_msg("I guess I would join you."))
            time.sleep(2)
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
                    merhcant.Merchant()

            if PunchJames == "NO":
                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You should never trust a me."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mJames murdered you.")
                os.system('cls')
                typingPrint("You slowly lose your vision.")
                os.system('cls')
                typingPrint("A clock appeared in front of your eyes as it started ticking backwards.")
                os.system('cls')
                typingPrint("A bright light consumed you, sending you back in time.")
                os.system('cls')
                start.run_interface()


