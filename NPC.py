import os
import time

from math import ceil, floor

#\x1B[3m Italic 
#\x1B[0m Normal Text
class Box:
    def format_line(line, max_length):
        global format_line 
        half_dif = (max_length - len(line)) / 2 # in Python 3.x float division
        return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'
    
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
            print("\x1B[3m You saw a magnifcent tower. A strong magically energy draws you near. As you apoarched you saw a girl and you ask for her name.")
            time.sleep(5)
            os.system('cls')
            print("Traveller: Hi, I am new to this town. Can you tell me your name?")
            time.sleep(5)
            print("Betty: Hi, I am Betty and I can show you around. This village is known for its fishing ports and advancements in the water way. At the center of the village, we have a huge water fountain, which is like healing sprinkler. Once you get near it, it should heal you completely.")
            time.sleep(5)   
            print("Taveller: Thank you.")
            time.sleep(5)    
            print("Betty: Follow me, I can show you where you can get materials and supplies. The merchant is very nice and the stuff is pretty cheap.")
            time.sleep(5)
            os.system('cls')

class MrsChu:
    picking_friends = input("Would you like to go up, straight or down? B(Up) C(Straight Foward) J(Down)")
    def Chu():
        if picking_friends == "C":
            os.system('cls')
        print("\x1B[3m You saw a fountain. The flowers flew out of the structure like fairies covering the square in a shimmering light. A powerful rejuvenating shock went through you. As you walk up to the fountain, you found your math teacher from your previous world. Mrs. Chu looks shocked and quickly waved to you.")
        time.sleep(5)
        print("Traveller: Mrs.Chu?!? Is that you?")
        time.sleep(5)
        print("Mrs.Chu: Oh my gosh, is that you? I suddently woke up in this world a month ago.")
        time.sleep(5)
        print("Traveller: I woke up and found myself in the road near the forest. No wonder you were in school for the last month.")
        time.sleep(5)
        print("Mrs.Chu: Come on let me show you around, it is hard to survive here.")
        time.sleep(5)
        print("As you witness just now, this fountain was a structure that contain a huge healing stone, which heals you as you get sprinkled by the water. You clothes would still get wet though.")
        time.sleep(5)
        print("Traveller: Do you know how I can get back?")
        time.sleep(5)
        print("Mrs.Chu: Follow me. Look over there. That is the Folklore Forest. There is a huge tower in the center. To get back home, you have to complete the five floors. On the final, you have to defeat a boss and it would grant you a wish, and that is your ticket home. By the markets, you would find Augustine, he is the merchant who you can sell and buy materials from.")
        time.sleep(5)
        os.system('cls')


