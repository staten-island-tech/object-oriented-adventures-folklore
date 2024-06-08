import os
import time
import sys
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint
import merhcant
from interface import main_character

class MrsChu:
    global first_en_Chu
    def first_en_Chu():  
            os.system('cls')

            typingPrint("\x1B[3mYou decided to walk straight ahead.\n As you walk, you find yourself in a village.")
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mYou walked to the center of the charming village, nestled in a lush valley.\n")
            typingPrint("\x1B[3mThatched cottages with blooming gardens lined the cobblestone streets.\n")
            typingPrint("\x1B[3mThe air was filled with the sweet scent of flowers and freshly baked bread.\n")
            time.sleep(10)
            os.system('cls')

            typingPrint("\x1B[3mYou stumbled towards a fountain in the center of the village, its waters shimmering with a soft, golden glow.\n")
            typingPrint("\x1B[3mAs I cupped my hands and drank, a soothing warmth spread through me, easing the fatigue and confusuion.\n")
            typingPrint("\x1B[3mYou turn around a saw a fimaliar figure sitting by a lake reading a book.\n")
            time.sleep(10)
            os.system('cls')


            Approaching_Chu = typingInput("Would you like to approach her? Y/N\n").upper()
            if Approaching_Chu == "N":
                os.system('cls')
                typingPrint("\x1B[3mShe was dressed in elegant, flowing robes adorned with intricate patterns that seemed to shift and change with the light.\n")
                typingPrint("\x1B[3mHer usual stern demeanor was softened by an aura of calming authority, yet there was something in her eyes that I couldn't quite place.\n")
                typingPrint("\x1B[3mIn her hands there was a book, called A Court of Attor and Feyre: A Love Story.\n")
                time.sleep(10)
                os.system('cls')

                typingPrint("\x1B[3mSuddenly, the stranger walked up to you...\n")
                time.sleep(10)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Oh my gosh, is that you, " + main_character.name + "!\nI suddently woke up in this world a month ago."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg(" Mrs.Chu?!?\nIs that you? \nWhat are you doing here?"))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Oh my gosh, is that you?\nI suddently woke up in this world a month ago."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you were in school for the last month."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come on let me show you around, it is hard to survive here.\nAs you witness just now, this fountain was a structure that contain a huge healing stone.\n This heals you as you get sprinkled by the water.\nYou clothes would still get wet though."))
                time.sleep(8)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Do you know how I can get back?"))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This place is called Alcina Dimitrescu. \nIt was named after the swamp monsters, which you would find more information on later on."))
                time.sleep(3)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This fountain is called the Heart of Dimitrescu."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Its waters can heal and rejuvenate."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The villagers here are mostly artisans and merchants, and they play a crucial role in maintaining the balance of magic."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("This place is incredible. \nIt feels so alive."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("However this balance is distrubed."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The balance of magic and reality is tipping dangerously."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("If it continues, both Dimitrescu and our wrold will suffer catastrophic consequences."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mShe grestured towards a massive tree with luminous leaves stood. \nBeneath it, villagers gathered, their faces etched with worry and hope.\n The tree's glow seemed to dim and brighten, as if breathing.")
                time.sleep(5)
                os.system('cls')
                typingPrint("\x1B[3mThere was a hint of steel in her voice now, a reminder of the gravity of our mission.\n Yet, the way she spoke of forces seeking to tip the balance made me wonder if she knew more about these threats than she was leeting on.")
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come, there is someone you need to meet."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("A merchant named Alaric. He can provide us with supplies and perhaps more informaion about your quest."))
                time.sleep(5)
                os.system('cls')


            elif Approaching_Chu == "Y":
                typingPrint("\x1B[3m She was dressed in elegant, flowing robes adorned with intricate patterns that seemed to shift and change with the light.\n")
                typingPrint("\x1B[3mHer usual stern demeanor was softened by an aura of calming authority, yet there was something in her eyes that I couldn't quite place.\n")
                typingPrint("\x1B[3mIn her hands there was a book, called A Court of Attor and Feyre: A Love Story.\n")
                time.sleep(10)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Oh my gosh, is that you, " + main_character.name + "!\nWhat are you doing here?."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Oh my gosh, is that you?\nI suddently woke up in this world a month ago."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you were in school for the last month."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come on let me show you around, it is hard to survive here.\nAs you witness just now, this fountain was a structure that contain a huge healing stone.\n This heals you as you get sprinkled by the water.\nYou clothes would still get wet though."))
                time.sleep(8)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Do you know how I can get back?"))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This place is called Alcina Dimitrescu. \nIt was named after the swamp monsters, which you would find more information on later on."))
                time.sleep(3)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This fountain is called the Heart of Dimitrescu."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Its waters can heal and rejuvenate."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The villagers here are mostly artisans and merchants, and they play a crucial role in maintaining the balance of magic."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("This place is incredible. \nIt feels so alive."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("However this balance is distrubed."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The balance of magic and reality is tipping dangerously."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("If it continues, both Dimitrescu and our wrold will suffer catastrophic consequences."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mShe grestured towards a massive tree with luminous leaves stood. \nBeneath it, villagers gathered, their faces etched with worry and hope.\n The tree's glow seemed to dim and brighten, as if breathing.")
                time.sleep(5)
                os.system('cls')
                typingPrint("\x1B[3mThere was a hint of steel in her voice now, a reminder of the gravity of our mission.\n Yet, the way she spoke of forces seeking to tip the balance made me wonder if she knew more about these threats than she was leeting on.")
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come, there is someone you need to meet."))
                time.sleep(2)
                os.system('cls')
                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("A merchant named Alaric. He can provide us with supplies and perhaps more informaion about your quest."))
                time.sleep(5)
                os.system('cls')
                merhcant.Merchant()