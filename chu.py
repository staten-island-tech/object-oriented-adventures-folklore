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
            typingPrint("\x1B[3mAs you cup your hands and drank, a soothing warmth spreads through you, easing the fatigue and confusuion.\n")
            typingPrint("\x1B[3mYou turn around to see a fimaliar figure sitting by a lake reading a book.\n")
            time.sleep(10)
            os.system('cls')


            Approaching_Chu = typingInput("Would you like to approach her? YES/NO\n").upper()
            if Approaching_Chu == "NO":
                os.system('cls')
                typingPrint("\x1B[3mShe was dressed in elegant, flowing robes adorned with intricate patterns that seemed to shift and change with the light.\n")
                typingPrint("\x1B[3mHer demeanor seem to be softened by an aura of calming authority, yet there was something in her eyes that you couldn't quite place.\n")
                typingPrint("\x1B[3mIn her hands there was a book, called A Court of Attor and Feyre: A Love Story.\n")
                time.sleep(15)
                os.system('cls')

                typingPrint("\x1B[3mSuddenly, the stranger walked up to you...\n")
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Oh my gosh, is that you, " + main_character.name + "!?"))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Mrs.Chu?!?\nIs that you?\n What are you doing here?"))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("I could ask the same for you!\n I suddently woke up in this world a month ago."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Same!\n I woke up and found myself in the road near the forest.\n No wonder you haven't been in school for the last month."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come on let me show you around. It's hard to survive here."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Do you know how I can get back?"))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mIgnoring your question, Mrs.Chu continues to talk about the village.")
                time.sleep(2)
                os.system("cls")

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This place is called Alcina Dimitrescu. \nIt was named after the swamp monsters.\n You'll probably find more information on them later."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This fountain is called the Heart of Dimitrescu.\n It contains a huge healing stone."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("As you've just seen, its waters can heal and rejuvenate.\n However, your clothes will still get wet though."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The villagers here are mostly artisans and merchants.\n They play a crucial role in maintaining the balance of magic."))
                time.sleep(4)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("This place is incredible.\n It feels so alive."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("However, the balance is in discord at the moment."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The balance of magic and reality is tipping dangerously."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("If it continues, both Dimitrescu and our world will suffer catastrophic consequences."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mShe grestured towards a massive tree with luminous leaves stood. \nBeneath it, villagers gathered, their faces etched with worry and hope.\n The tree's glow seemed to dim and brighten, as if breathing.")
                time.sleep(5)
                os.system('cls')

                typingPrint("\x1B[3mThere was a hint of steel in her voice now, a reminder of the gravity of the situation.\n Yet, the way she spoke of forces seeking to tip the balance made you wonder if she knew more about these threats than she was letting on.")
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come, there is someone you need to meet."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("A merchant named Alaric. He can provide us with supplies and perhaps more informaion about why you are here."))
                time.sleep(5)
                os.system('cls')

            elif Approaching_Chu == "YES":
                typingPrint("\x1B[3mShe was dressed in elegant, flowing robes adorned with intricate patterns that seemed to shift and change with the light.\n")
                typingPrint("\x1B[3mHer demeanor seemed to be softened by an aura of calming authority, yet there was something in her eyes that you couldn't quite place.\n")
                typingPrint("\x1B[3mIn her hands there was a book, called A Court of Attor and Feyre: A Love Story.\n")
                time.sleep(15)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Oh my gosh, is that you, Mrs.Chu?\nWhat are you doing here?."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Oh my gosh, is that you, " + main_character.name + "?\nI suddently woke up in this world a month ago."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you weren't in school for the last month."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come on, let me show you around.\nIt's hard to survive here."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("Do you know how I can get back?"))
                time.sleep(2)
                os.system('cls')

                typingPrint("\x1B[3mIgnoring your question, Mrs.Chu continues to talk about the village.")
                time.sleep(2)
                os.system("cls")

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This place is called Alcina Dimitrescu. \nIt was named after the swamp monsters.\n You'll probably find more information on them later."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("This fountain is called the Heart of Dimitrescu.\n It contains a huge healing stone."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("As you've just seen, its waters can heal and rejuvenate.\n However, your clothes will still get wet though."))
                time.sleep(3)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The villagers here are mostly artisans and merchants.\n They play a crucial role in maintaining the balance of magic."))
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mYou:")
                typingPrint(boxed_msg("This place is incredible. \nIt feels so alive."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("However, the balance is in discord at the moment."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("The balance of magic and reality is tipping dangerously."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("If it continues, both Dimitrescu and our world will suffer catastrophic consequences."))
                time.sleep(3)
                os.system('cls')

                typingPrint("\x1B[3mShe grestured towards a massive tree with luminous leaves stood. \nBeneath it, villagers gathered, their faces etched with worry and hope.\n The tree's glow seemed to dim and brighten, as if breathing.")
                time.sleep(5)
                os.system('cls')

                typingPrint("\x1B[3mThere was a hint of steel in her voice now, a reminder of the gravity of the situation.\n Yet, the way she spoke of forces seeking to tip the balance made you wonder if she knew more about these threats than she was letting on.")
                time.sleep(5)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("Come, there is someone you need to meet."))
                time.sleep(2)
                os.system('cls')

                print("\x1B[0mMrs.Chu:")
                typingPrint(boxed_msg("A merchant named Alaric. He can provide us with supplies and perhaps more informaion about why you are here."))
                time.sleep(5)
                os.system('cls')