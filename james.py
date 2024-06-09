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
            typingPrint("\x1B[3mYou decide to turn right.\n As you walk, you find yourself in a village.\n Looking around at the people, you notice something.")
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mYou see a guy with a shady hood over his head.\n He was walking up to an old lady and sneakly take her purse from her pockets.\n You followed behind him and he notices you.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("You are not being sneaky following me like that."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("..."))
            time.sleep(1)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("How come I've never seen you around here before?"))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("I'm new here.\n Not really even sure how I got here."))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("I know you saw what I did.\n So either you join me or I will end you right here, right now."))
            time.sleep(4)
            os.system('cls')

            print("\x1B[0mYou:")
            typingPrint(boxed_msg("Seeing as I don't really want to die, I guess I'll join you."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mStranger:")
            typingPrint(boxed_msg("Okay good.\n I'll show you around.\n My names is James by the way."))
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mWhile following James, you both eventually end up in a shady looking area.")
            time.sleep(3)
            os.system('cls')
            
            print("\x1B[0mJames:")
            typingPrint(boxed_msg("This is the underground alley of the village.\n It's basically the black market.\n I have some business to deal with here."))
            time.sleep(5)
            os.system('cls')

            typingPrint("\x1B[3mRealizing how bad this is, you come up with the option to either punch him while he was distracted or just wait and see what happends...")
            PunchJames = typingInput("Would you like to punch james? YES/NO\n").upper()
            os.system('cls')
            
            if PunchJames == "YES":
                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You... You back stabbing mole rat!"))
                time.sleep(2)
                os.system('cls')
                PunchingJames = typingInput("Run or Slaughter him? RUN/SLAUGHTER ").upper()
                if PunchingJames == "RUN":
                    typingPrint("\x1B[3mYou have escaped and you reached the merchant.")
                    time.sleep(2)
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


                elif PunchingJames == "SLAUGHTER":
                    typingPrint("\x1B[3mYou murdered James, and you run to the river to clean yourself up.\n After cleaning you body of James' blood, you run out of the alley and make your way towards the mercahnt to get some materials.")
                    time.sleep(6)
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

            if PunchJames == "NO":
                typingPrint("\x1B[3mAs you contemplate, James turns around and looks at you with a malicious glint in his eyes.")
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mJames:")
                typingPrint(boxed_msg("You know, you should never trust a criminal."))
                time.sleep(2)
                os.system('cls')

                typingPrint("\x1B[3mLooking at James, the only thing you see is a shape knife heading straight for your heart.")
                time.sleep(2)
                os.system('cls')

                typingPrint("\x1B[3mJames murdered you.")
                time.sleep(1)
                os.system('cls')

                typingPrint("\x1B[3mYou slowly lose your vision.\n The world goes black.")
                time.sleep(2)
                os.system('cls')

                typingPrint("\x1B[3mA clock appeared in front of your eyes as it started ticking backwards.")
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mA bright light consumed you, sending you back in time.")
                time.sleep(2)
                os.system('cls')
                start.run_interface()


