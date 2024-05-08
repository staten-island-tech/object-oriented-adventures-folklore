import os
import time
import sys
from classes import boxed_msg
from classes import typingPrint
from classes import typingInput
from player import player

class start:
    def interface():
        print("Welcome to the Folklore Game!")
        player(name= input("What is your name?\n"))
        os.system('cls')

        print("1. Start Game")
        print("2. How to play")
        print("3. Exit Game")
        pick_option = input("What would you like to do? (ex: 1, 2, or 3): \n")
        os.system('cls')

        if pick_option == "1":
            typingPrint("\x1B[3m You're walking across the street when a truck honks at you.\n You turn your as a blinding light gets closer...")
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3m You open your eyes to a pounding in your head.\n The surrounding is very different from where you were before.\n Your blurry vision starts to focus on a fork in the road...")
            time.sleep(5)
            os.system('cls')
            global pick_route
            pick_route = typingInput("\x1B[3m Would you like to move E(left), W(right), or V(straight ahead)?\n").upper()
            
            
        elif pick_option == "2":
            print()
        elif pick_option == "3":
            print("Bye bye!")
    
    def left():
        if pick_route == "E":
            os.system('cls')
            typingPrint("\x1B[3mYou decide to turn left.\n You look around and notice that you are in a forest.\n As you go deeper into the forest, you hear a noise coming from the trees...")
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3mYou look back at the road when you hear a thump in front of you.\n You wip your head around to see a tall, pointed-ear creature.")
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("You filthy human!\nWhat are you doing in our territory!?"))
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mTraveler: ")
            typingPrint(boxed_msg("I...wha-"))
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("You are in the land of the elves.\nHOW DARE YOU VIOLATE OUR SOIL WITH YOUR DISGUSTING FEET!?"))
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3mYou turn around and start running as fast as you can away from the elf.\nIt shoots an arrow at your head and it barely misses.")

    def right():
        if pick_route == "W":
            os.system('cls')
            typingPrint("\x1B[3mYou decide to turn right.\n As you continue walking, you start to hear running water.")
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3mYou make it to a large opening and see a large lake with a waterfall.\n Moving closer to the lake, you see something lurking underneath the surface.")
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3mAs you put your head above the water, something jumps out at you!\n Screaming, you fall onto the ground and scramble back away from the... the... weird creature thing!")
            time.sleep(7)
            os.system('cls')
            print("\x1B[0mTraveler: ")
            typingPrint(boxed_msg("AHHHHHHHH!"))
            time.sleep(5)
            os.system('cls')
            typingPrint("\x1B[3mCrawling closer to you, the creature hisses...")
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Huuuuman...\n Oh, I haven't seen a live human in sooooo long...\n You smell absolutely deliciousssssss..."))
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mTraveler: ")
            typingPrint(boxed_msg("Wh-...\n What are you!?"))
            time.sleep(3)
            os.system('cls')
            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Whyyyyyy... \n How rude of youuuuuuu...\n I'll tear you to shredsssss..."))
            time.sleep(5)
            os.system('cls')
            print("\x1B[0mTraveler: ")
            typingPrint(boxed_msg("Wait wait wait!\n Please!\n I meant no offense!\n I was just confused!"))
            time.sleep(3)
            os.system('cls')
            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Poor little humannnn...\n It seems that its time for you to dieeee..."))


start.interface()
start.left()
start.right()