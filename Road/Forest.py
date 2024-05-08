import time
import sys
import os

global typingPrint
global typingspeed
typingspeed = 0.01
global typingInput
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(typingspeed)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(typingspeed)
        value = input()  
        return value  
class forestman():
    def forester():
        while True:
            player = input("ON/OFF: ").upper()
            if player == 'ON':
                typingPrint("You have spawned in your last saved position.")
                time.sleep(2)
                os.system('cls')
                typingPrint("You are in the forest right now. As a side note, this is a great place to obtain wood so that you can craft weapons.")
                time.sleep(3)
                os.system('cls')
                typingPrint("Let's continue walking up ahead. There is the Maldachaunians Camps(left), lakes(foward), and the Wimitescu Swampland(right). Which direction would you like to go?")
                time.sleep(5)
                os.system('cls')
                direction = input("Left/Foward/Backward/Right").upper()
                if direction == "LEFT":
                    typingPrint("You have reached the Maldachaunian Camps. Once human beings who lived in the empire ruled by malevolent deities.")
                    time.sleep(3)
                    os.system('cls')
                    typingPrint("Under the tyrannical rule of these godly beings, humans were forced to work in underground mines. One of these mines was the Chasm of Carcassona. The people of this mine were directed to collect beryl crystals, terribly hard to acquire, with many casualties.")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("A plot to escape was quickly formed. A false explosion created a perfect distraction for an escape. However, the plan failed and they were cursed to be made and violent creatures.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("But nevermind that. This place is not used to earn more loot by defeating enemies. Think of it as a training ground for you to get stronger.")
                    time.sleep(4)
                    os.system('cls')
                elif direction == "FOWARD":
                    typingPrint("You have reached the lakes. If you walk in far enough you can reach either the village ports or water spirit Fjord. ")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("..*you walk for another 5 min*....")
                    time.sleep(2)
                    os.system('cls')
                    direction = input("Left/Right").upper()
                elif direction == "BACKWORD":
                    typingPrint("You choose to go backward. This means that you will go back through the forest and arrive somewhere else")
                    time.sleep(4)
                    os.system('cls')
                    direction = input("Left/Foward/Backward/Right").upper()
                    #right direction for else
                else:
                    typingPrint("You have arrived at the Wimitescu Swampland. If you didn't know this is where sassy shrek lives. Try not to run into sassy shrek or things could get really bad for you.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("A long time ago, when this world was first created, there was a mutation in some of the monsters causing them to act weirdly and grow to a huge size.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("")
            else:
                print("....")
