import os
import time
import json
import sys
from classes import boxed_msg
from classes import typingPrint
from classes import typingInput
from player import player
from monster import elves
from monster import water_spirit
from Inventory import inventory
from Inventory import player_in
import random

class start:
    global interface
    global left
    global right
    global straight_ahead
    def interface():
        os.system('cls')
        print("-‘๑’-Wҽʅƈσɱҽ ƚσ Fσʅƙʅσɾҽ Gαɱҽʂ-`‘๑’-")
        global main_character
        main_character = player(name= input("What is your name?\n"), hp= 100, damage= 5, crit= 10, gold= 0, silver= 0)
        os.system('cls')

        print("1. Start Game")
        print("2. Exit Game")
        pick_option = input("What would you like to do? (ex: 1 or 2): \n")
        os.system('cls')

        if pick_option == "1":
            typingPrint("\x1B[3m You're walking across the street when a truck honks at you.\n You turn your as a blinding light gets closer...")
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3m You open your eyes to a pounding in your head.\n The surrounding is very different from where you were before.\n Your blurry vision starts to focus on a fork in the road...")
            time.sleep(6)
            os.system('cls')
            route = typingInput("\x1B[3m Would you like to move E(left), W(right), or V(straight ahead)?\n").upper()
            if route == "E":
                left()
            elif route == "W":
                right()
            elif route == "V":
                straight_ahead()
            
        elif pick_option == "2":
            print("Bye bye!")
            sys.exit()

    def left():
            os.system('cls')
            typingPrint("\x1B[3mYou decide to turn left.\n You look around and notice that you are in a forest.\n As you go deeper into the forest, you hear a noise coming from the trees...")
            time.sleep(5)
            os.system('cls')

            typingPrint("\x1B[3mYou look back at the road when you hear a thump in front of you.\n You wip your head around to see a tall, pointed-ear creature.")
            time.sleep(4)
            os.system('cls')

            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("You filthy human!\nWhat are you doing in our territory!?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("I...wha-"))
            time.sleep(2)
            os.system('cls')

            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("You are in the land of the elves.\nHOW DARE YOU VIOLATE OUR SOIL WITH YOUR DISGUSTING FEET!?"))
            time.sleep(4)
            os.system('cls')

            typingPrint("\x1B[3mYou turn around and start running as fast as you can away from the elf.\nIt shoots an arrow at your head and it barely misses.")
            time.sleep(5)
            os.system('cls')

            typingPrint("\x1B[3mYou can feel the elf getting closer and closer with each shot it takes.\nWhen you feel it right behind you, you turn around and punch it!")
            time.sleep(5)
            os.system('cls')

            beginning_elf = elves(name="Elf", hp= 20, loot="", damage= 5, crit= 10, gold= random.randint(5,15), silver= random.randint(10,20), weapon= "bow and arrow", powers="N/A")
            typingPrint("BATTLE!!!")
            time.sleep(2)
            os.system('cls')

            while main_character.hp > 0 and beginning_elf.hp > 1:
                player.battle(main_character,beginning_elf)
            if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()
# FIXXXXX
            elif beginning_elf.hp <= 0: 
                print(f"You defeated a elf.\n (+ golds)\n (+ silvers)")
                player_in.currency["Gold"] += {elves.gold}
                player_in.currency["Silver"] += {elves.silver}
                if random.randint(1,20) == 13:
                    typingPrint("You gain something some else.")
                    inventory.adding_items.potions["Health Potion"] += 1
                
                typingPrint("After winning the battle against the " + beginning_elf.name + ", you decide to try and find other people.\n On your way, you end up encountering another fork in the road.")
                time.sleep(5)
                os.system('cls')

            elif beginning_elf.hp == 1:
                os.system('cls')
                typingPrint("After running away from the " + beginning_elf.name +  " like a complete wuss, you decide to try and find other people.\n On your way, you end up encountering another fork in the road.")
                time.sleep(5)
                os.system('cls')
                
    def right():
            os.system('cls')
            typingPrint("\x1B[3mYou decide to turn right.\n As you continue walking, you start to hear running water.")
            time.sleep(3)
            os.system('cls')

            typingPrint("\x1B[3mYou make it to a large opening and see a large lake with a waterfall.\n Moving closer to the lake, you see something lurking underneath the surface.")
            time.sleep(5)
            os.system('cls')

            typingPrint("\x1B[3mAs you put your head above the water, something jumps out at you!\n Screaming, you fall onto the ground and scramble back away from the... the... weird creature thing!")
            time.sleep(6)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("AHHHHHHHH!"))
            time.sleep(2)
            os.system('cls')

            typingPrint("\x1B[3mCrawling closer to you, the creature hisses...")
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Huuuuman...\n Oh, I haven't seen a live human in sooooo long...\n You smell absolutely deliciousssssss..."))
            time.sleep(4)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("Wh-...\n What are you!?"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Whyyyyyy... \n How rude of youuuuuuu...\n I'll tear you to shredsssss..."))
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("Wait wait wait!\n Please!\n I meant no offense!\n I was just confused!"))
            time.sleep(3)
            os.system('cls')

            print("\x1B[0mCreature: ")
            typingPrint(boxed_msg("Poor little humannnn...\n It seems that its time for you to dieeee..."))
            time.sleep(3)
            os.system('cls')

            beginning_water_spirit = water_spirit(name= "Water Spirit", hp= 20, loot= "", damage= 5, crit= 10, gold = random.randint(5,20), silver= random.randint(5,20), power= "Water Blast")
            while main_character.hp > 0 and beginning_water_spirit.hp > 1:
                player.battle(main_character,beginning_water_spirit)
            if main_character.hp <= 0:
                d = typingInput("Would you like to restart? YES/NO\n").upper()
                if d == "YES":
                    interface()
                elif d == "NO":
                    sys.exit()

            elif beginning_water_spirit.hp <= 0: 
                main_character.gold += beginning_water_spirit.gold
                main_character.silver += beginning_water_spirit.silver 

                os.system('cls')
                typingPrint("The " + beginning_water_spirit.name + " dropped " + str(beginning_water_spirit.gold) + " gold and " + str(beginning_water_spirit.silver) + " silver.\n You decide to collect your winnings.")
                time.sleep(5)
                os.system('cls')

                typingPrint("After winning the battle against the " + beginning_water_spirit.name + ", you decide to try and find other people.\n On your way, you end up encountering another fork in the road.")
                time.sleep(5)
                os.system('cls')

            elif beginning_water_spirit.hp == 1:
                os.system('cls')
                typingPrint("After running away from the " + beginning_water_spirit.name +  " like a complete wuss, you decide to try and find other people.\n On your way, you end up encountering another fork in the road.")
                time.sleep(5)
                os.system('cls')
            
    def straight_ahead():
            os.system('cls')
            typingPrint("\x1B[3mYou decide to keep walking straight.\n Soon you find yourself in a bustling village.\n You decided to try and ask someone where you are.")
            time.sleep(5)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("Um, hi-"))
            time.sleep(1)
            os.system('cls')

            typingPrint("\x1B[3mThe villager speeds off away to before you can finish greeting them.\n You decided to try again and approach a new villager.")
            time.sleep(4)
            os.system('cls')

            print("\x1B[0mYou: ")
            typingPrint(boxed_msg("Hello, I-"))
            time.sleep(1)
            os.system('cls')

            typingPrint("\x1B[3mAgain, the villager quickly walks away.\n You keep trying but none of your attempts are sucessful.")
            time.sleep(3)
            os.system('cls')
            
            typingPrint("\x1B[3mDetermined to figure out where you are, you decide to explore the village on your own.\n Eventually you find another fork in the road that seems promising.")
            time.sleep(3)
            os.system('cls')

    def run_interface():
        interface()

start.run_interface()