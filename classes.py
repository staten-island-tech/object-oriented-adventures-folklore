import json
import os
import time
import sys
from math import ceil, floor

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
    
class player:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
    def __str__(self):
        return f"{self.name}"
    

test = open("monster_data.json", encoding = "utf8")
monster_data = json.load(test)

class monster_info:
    def search_name():
        name = input("Which monster would you like to know about?\n").upper()
        for i in monster_data:
            if name in i['Name'].upper():
                print(i['Name'])
                print(i['Description'])
                print(i['Loot'])
                print(i['Hp'])
    def search_loot():
        loot = input("What monsters drop the loot:\n").upper()
        for i in monster_data:
            if loot in i['Loot'].upper():
                print(i['Name'])
    def search_hp(): 
        h = int(input("What monsters have an hp of:\n(Reminder: Monsters only have hps of: 50, 100, 150, or 200)\n"))
        for x in monster_data:
            if h == x["Hp"]:
                print(x['Name'])   

class start:
    def interface():
        print("Welcome to the Folklore Game!")
        name = input("What is your name?\n")
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