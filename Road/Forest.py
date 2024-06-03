import time
import sys
import os
from Fighting import Attacks
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

global left
global right
global straight_ahead

class forestman():
    #CLASS/FUNCTIONS TO MOVE THROUGH AND NAVIGATE THROUGH THE FOREST
    def forester():
        while True:
            player = input("COUNTINE/STOP").upper()
            if player == 'CONTINUE':
                typingPrint("\x1B[2mYou have reached the forest.\n *As a side note, this is a great place to obtain wood so that you can craft weapons*")
                time.sleep(4)
                os.system('cls')
                typingPrint("Let's continue walking up ahead. There is the Maldachaunians Camps(left), lakes(foward), and the Wimitescu Swampland(right). Which direction would you like to go?")
                time.sleep(5)
                os.system('cls')
                direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
                #LEFT DIRECTION *MALDACHUANIANS CAMP*
                if direction == "LEFT":
                    typingPrint("\x1B[2mYou have reached the Maldachaunian Camps.\n A long time ago human beings who lived in the empire ruled by malevolent deities.")
                    time.sleep(3)
                    os.system('cls')
                    typingPrint("\x1B[2mUnder the tyrannical rule of these godly beings, humans were forced to work in underground mines.\n One of these mines was the Chasm of Carcassona.\nThe people of this mine were directed to collect beryl crystals, terribly hard to acquire, with many casualties.")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("\x1B[2mA plot to escape was quickly formed. A false explosion created a perfect distraction for an escape.\nHowever, the plan failed and they were cursed to be mad and violent creatures.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mBut nevermind that. This place is used to earn more loot by defeating enemies.\nThink of it as a training ground for you to get stronger.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mYou already entered their territory so you might get targeted. Look over there... somethings coming...")
                    time.sleep(5)
                    os.system('cls')
                    typingPrint("\x1B[2mYou squint your eyes. Something is frantically running towards you. \nWATCH OUT!! Its a Maldachuanian!")
                    time.sleep(5)
                    os.system('cls')     
                    typingPrint("Maldachuanian: OoooOO.. Look whos here. A delcious human waiting for me to gobble up!\nThat's what you get for being in our territory.")
                    time.sleep(5)
                    os.system('cls')              
                    typingPrint("You: Huh?! You? Gobble me? Let's see about that!")
                    time.sleep(2)
                    os.system('cls')
                    typingPrint("Maldachuanian: This is maldachuaian land.\nYOU ASKED FOR THIS!")
                    time.sleep(3)
                    os.system('cls')
                    Attacks.Maldachaunians()

                    #Might change:   typingPrint("You take out your weapon.\n [ Quickly press the enter key to intiate a damage with your weapon ]")
                #FOWARD DIRECTION *LAKES*
                elif direction == "FOWARD":
                    typingPrint("\x1B[2mYou have reached the lakes. If you walk in far enough you can reach either the village ports or water spirit Fjord. ")
                    time.sleep(3)
                    os.system('cls')
                    typingPrint("..*you walk for another 5 min*....")
                    time.sleep(2)
                    os.system('cls')
                    typingPrint("\x1B[2mIf you choose to go see the water spirit you can try defeat it.\n")
                    typingPrint("\x1B[2mLegend says that by defeating it, you can increase the amount of power you have by almost double.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mOn the other hand, if you go to the village ports, you can get a chance to gain new items.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("Which way would you like to go? Village Ports(Left) or to the water spirit(Right)?")
                    direction = input("LEFT/RIGHT").upper()
                    #VILLAGE PORTS
                    if direction == 'LEFT':
                        typingPrint("\x1B[2mYou have reached the Village Ports")
                        time.sleep(1)
                        os.system('cls')
                        typingPrint("\x1B[2mThe people here are pretty nice so if you ask for food they will most likely give you some.")
                        time.sleep(2)
                        os.system('cls')
                        typingPrint("")
                        time.sleep(2)
                        os.system('cls')
                    #WATER SPIRIT
                    else:
                        typingPrint("\x1B[2mYou have reached the land where the Water Spirit is.\n")
                        typingPrint("\x1B[2mThere are two spirits in total the water spirit and the fire spirit.\n")
                        typingPrint("\x1B[2mThere is no specific territory for the fire spirit since it roams the forest freely\n")
                        typingPrint("\x1B[2mBy defeating both of them, you will earn a reward bag with extra loot.")
                        time.sleep(8)
                        os.system('cls')
                        typingPrint("\x1B[2mIf you would like to battle the Water Spirit press the up arrow, if not press the down arrow")
                        time.sleep(2)
                        os.system('cls')
                        up_down = input("UP/DOWN").upper()
                        if up_down == 'UP':
                            typingPrint("You have entered battle with the Water Spirit ")
                            time.sleep(3)
                            os.system('cls')
                            typingPrint("\x1B[2mFight!!")
                        elif up_down == 'DOWN':
                            print("You choose not to fight, and walked back to the end of the forest")
                            typingPrint("Which way would you like to go? Village Ports(Left) or to the water spirit(Right)?")
                            direction = input("LEFT/RIGHT").upper()
                        else:
                            print("Invalid Input\n Remember that you your chocies are UP or DOWN")
                            direction = input("LEFT/RIGHT").upper()                     
                #RIGHT DIRECTION *WIMITESCU SWAMPLAND*
                elif direction == "RIGHT":
                    typingPrint("\x1B[2mYou have arrived at the Wimitescu Swampland. If you didn't know, this is where sassy shrek lives. Try not to run into sassy shrek or things could get really bad for you.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mBack then, there was a mutation in some of the monsters causing them to act weirdly and grow to a huge size.")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mNo one has ever defeated Shrek before so nobody knows what happens if you do. \nMaybee.... ... ... ")
                    time.sleep(4)
                    os.system('cls')
                    typingPrint("\x1B[2mMaybe... you could be the first to meet him. And possibly defeat him???")
                    time.sleep(3)
                    os.system('cls')
                    typingPrint("\x1B[2mBut please keep in mind that the lakes here are pousinous, so make sure you don't touch.")
                    time.sleep(3)
                    os.system('cls')
                    Attacks.Wimitescu()
                #BACKWARD DIRECTION *LEAVING THE FOREST*
                elif direction == "BACKWARD":
                    typingPrint("You chose to go backward. This means that you will go back through the forest and arrive somewhere else")
                    time.sleep(4)
                    os.system('cls')
                    direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
            
                #else is ERROR MESSAGE or INVALID INPUT
                else:
                    input("Invalid Input: Remember that your input should be either , LEFT/FOWARD/BACKWARD/RIGHT")
                    direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
            else:
                input("You choose off. This means you are quiting the game. Are you sure? YES/NO")
                if input == 'YES':
                    print("Loading.... Game is turning off")
                    return 
                else:
                    print("You choose NO. The game will continue")
                    time.sleep(2)
                    os.system('cls')
                    direction = input("LEFT/FOWARD/BACKWARD/RIGHT").upper()
                    
forestman.forester()
