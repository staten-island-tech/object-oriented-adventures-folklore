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

class MrsChu:
    def first_en_Chu():
            os.system('cls')
            typingPrint("\x1B[3m You walked to the center of the charming village, nestled in a lush valley.\n")
            typingPrint("Thatched cottages with blooming gardens lined the cobblestone streets.\n")
            typingPrint("The air was filled with the sweet scent of flowers and freshly baked bread.\n")
            typingPrint("You stumbled towards a fountain in the center of the village, its waters shimmering with a soft, golden glow.\n")
            typingPrint("As I cupped my hands and drank, a soothing warmth spread through me, easing the fatigue and confusuion.\n")
            typingPrint("You turn around a saw a fimaliar figure sitting by a lake reading a book.\n")
            time.sleep(10)
            os.system('cls')

            print("\x1B[0mTraveller:")
            print(boxed_msg(" Mrs.Chu?!?\nIs that you? \nWHat are you doing here?"))
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3m She was dressed in elegant, flowing robes adorned with intricate patterns that seemed to shift and change with the light.\n")
            typingPrint("Her usual stern demeanor was softened by an aura of calming authority, yet there was something in her eyes that I couldn't quite place.\n")
            typingPrint("In her hands there was a book, called A Court of Attor and Feyre: A Love Story.\n")
            time.sleep(10)
            os.system('cls')

            print("\x1B[0mMrs.Chu:")
            print(boxed_msg("Oh my gosh, is that you?\nI suddently woke up in this world a month ago."))
            time.sleep(5)
            os.system('cls')

            print("Traveller:")
            print(boxed_msg("I woke up and found myself in the road near the forest.\nNo wonder you were in school for the last month."))
            time.sleep(5)
            os.system('cls')

            print("Mrs.Chu:")
            print(boxed_msg("Come on let me show you around, it is hard to survive here.\nAs you witness just now, this fountain was a structure that contain a huge healing stone.\n This heals you as you get sprinkled by the water.\nYou clothes would still get wet though."))
            time.sleep(8)
            os.system('cls')

            print("Traveller:")
            print(boxed_msg("Do you know how I can get back?"))
            time.sleep(3)
            os.system('cls')

            print("Mrs.Chu:")
            print(boxed_msg("This place is called Alcina Dimitrescu. \nIt was named after the swamp monsters, which you would find more information on later on."))
            time.sleep(3)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("This fountain is called the Heart of Dimitrescu."))
            time.sleep(2)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("Its waters can heal and rejuvenate."))
            time.sleep(2)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("The villagers here are mostly artisans and merchants, and they play a crucial role in maintaining the balance of magic."))
            time.sleep(5)
            os.system('cls')

            print("Traveller:")
            print(boxed_msg("This place is incredible. \nIt feels so alive."))
            time.sleep(2)
            os.system('cls')

            print("Mrs.Chu:")
            print(boxed_msg("However this balance is distrubed."))
            time.sleep(2)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("The balance of magic and reality is tipping dangerously."))
            time.sleep(2)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("If it continues, both Dimitrescu and our wrold will suffer catastrophic consequences."))
            time.sleep(3)
            os.system('cls')

            print("\x1B[3m She grestured towards a massive tree with luminous leaves stood. \nBeneath it, villagers gathered, their faces etched with worry and hope.\n The tree's glow seemed to dim and brighten, as if breathing.")
            time.sleep(5)
            os.system('cls')
            print("There was a hint of steel in her voice now, a reminder of the gravity of our mission.\n Yet, the way she spoke of forces seeking to tip the balance made me wonder if she knew more about these threats than she was leeting on.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0m Mrs.Chu:")
            print(boxed_msg("Come, there is someone you need to meet."))
            time.sleep(2)
            os.system('cls')
            print("Mrs.Chu:")
            print(boxed_msg("A merchant named Alaric. He can provide us with supplies and perhaps more informaion about your quest."))
            time.sleep(5)
            os.system('cls')

MrsChu.first_en_Chu()