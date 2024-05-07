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

def environment():
    while True:
        player = input("ON/OFF: ").upper()
        if player == 'ON':
            typingPrint("You have spawned in your last saved position.")
            time.sleep(3)
            os.system('cls')
            typingPrint("You are forest right now. As a side note, this is a great place to obtain wood so that you can craft weapons")
            time.sleep(4)
            os.system('cls')
            direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
            typingPrint("Let's continue walking up ahead. There is the Maldachaunians Camps(left), lakes(foward), and the Wimitescu Swampland(right). Which direction would you like to go?")
            time.sleep(4)
            os.system('cls')
            if direction == "LEFT":
                typingPrint("You have reached the Maldachaunian Camps. Once human beings who lived in the empire ruled by malevolent deities.")
                time.sleep(4)
                os.system('cls')
                typingPrint("Under the tyrannical rule of these godly beings, humans were forced to work in underground mines. One of these mines was the Chasm of Carcassona. The people of this mine were directed to collect beryl crystals, terribly hard to acquire, with many casualties.")
                time.sleep(6)
                os.system('cls')
                typingPrint("A plot to escape was quickly formed. A false explosion created a perfect distraction for an escape. However, the plan failed and they were cused to be made and violent creatures.")
                time.sleep(6)
                os.system('cls')
                typingPrint("Here you can earn more loot by defeating enemies. Think of it as a training ground for you to get stronger.")
                time.sleep(4)
                os.system('cls')
            elif direction == "FOWARD":
                typingPrint("Yes")
            else:
                typingPrint("Yes")
        else:
            print("....")
environment()
        
