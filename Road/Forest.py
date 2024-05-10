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
            player = input("CONTINUE/OFF").upper()
            if player == 'CONTINUE':
                typingPrint("You have reached the forest.\n As a side note, this is a great place to obtain wood so that you can craft weapons.")
                time.sleep(4)
                os.system('cls')
                typingPrint("Let's continue walking up ahead. There is the Maldachaunians Camps(left), lakes(foward), and the Wimitescu Swampland(right). Which direction would you like to go?")
                time.sleep(5)
                os.system('cls')
                direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
                if direction == "LEFT":
                    typingPrint("You have reached the Maldachaunian Camps.\n Once human beings who lived in the empire ruled by malevolent deities.")
                    time.sleep(3)
                    os.system('cls')
                    typingPrint("Under the tyrannical rule of these godly beings, humans were forced to work in underground mines.\n One of these mines was the Chasm of Carcassona.\nThe people of this mine were directed to collect beryl crystals, terribly hard to acquire, with many casualties.")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("A plot to escape was quickly formed. A false explosion created a perfect distraction for an escape.\nHowever, the plan failed and they were cursed to be made and violent creatures.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("But nevermind that. This place is used to earn more loot by defeating enemies.\nThink of it as a training ground for you to get stronger.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("Watch out! You already entered their territory so you might get targeted! Look over there... somethings coming...")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("You squint your eys. Something is franticaly running towards you. \nIts a Maldachuanian!")
                    time.sleep(5)
                    os.system('cls')     
                    typingPrint("Maldachuanian: OoooOO.. Look whos here. I delcious human waiting for me to gobble up!\nThat's what you get for being in our territory.")
                    time.sleep(5)
                    os.system('cls')              
                    typingPrint("You: Huh?! Your gonna gobble me? Let's see about that!")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("Maldachuanian: This is maldachuaian land.\nYOU ASKED FOR THIS!")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("You take out your weapon.\n You then attack the Maldachuian before it can even blink.")
                elif direction == "FOWARD":
                    typingPrint("You have reached the lakes. If you walk in far enough you can reach either the village ports or water spirit Fjord. ")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("..*you walk for another 5 min*....")
                    time.sleep(2)
                    os.system('cls')
                    typingPrint("If you choose to go see the water spirit you can try defeatin it.\nLegend says that by defeating them, you can increase the amount of power you have by almost double.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("On the other hand, if you go to the village ports, you can get a chance to gain new items.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("Which way would you like to go? Village Ports(Left) or to the water spirit(Right)?")
                    direction = input("LEFT/RIGHT").upper()
                    if direction == 'LEFT':
                        print("")
                elif direction == "RIGHT":
                    typingPrint("You have arrived at the Wimitescu Swampland. If you didn't know this is where sassy shrek lives. Try not to run into sassy shrek or things could get really bad for you.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("A long time ago, there was a mutation in some of the monsters causing them to act weirdly and grow to a huge size.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("No one has ever defeated Shrek before so nobody knows what happens if you do. \nMaybee.... ... ... ")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("Maybe... you could be the first to meet him. And possibly defeat him???")
                    time.sleep(4)
                    os.system('cls')
                #else is going backward: leaving the forest
                else:
                    typingPrint("You choose to go backward. This means that you will go back through the forest and arrive somewhere else")
                    time.sleep(4)
                    os.system('cls')
                    direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
            else:
                input("You choose off. This means you are quiting the game. Are you sure?")
                if input == 'YES':
                    print("Loading.... Game is turning off")
                else:
                    return 
                
forestman.forester