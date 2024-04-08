import os
import time

#\x1B[3m Italic 
#\x1B[0m Normal Text
class Global:
    global picking_friends
class Betty:
    picking_friends = input("Would you like to go up, straight or down? B(Up) C(Straight Foward) J(Down)")
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
        print("Traveller: Mrs.Chu?!? Is that you?")
        print("Mrs.Chu: Oh my gosh, is that you? I suddently woke up in this world a month ago.")
        print("Traveller: I woke up and found myself in the road near the forest. No wonder you were in school for the last month.")
        print("Mrs.Chu: Come on let me show you around, it is hard to survive here.")
        print("As you witness just now, this fountain was a structure that contain a huge healing stone, which heals you as you get sprinkled by the water. You clothes would still get wet though.")