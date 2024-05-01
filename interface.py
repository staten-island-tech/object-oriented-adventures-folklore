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

class start:
    def interface():
        print("1. Start Game")
        print("2. How to play")
        print("3. Exit Game")
        pick_option = input("What would you like to do? (ex: 1, 2, or 3): \n")
        os.system('cls')

        if pick_option == "1":
            typingPrint("\x1B[3m You're walking across the street when a truck honks at you.\n You turn your as a blinding light gets closer...\n")
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
            typingPrint("\x1B[3mYou decide to turn right.\n ")

start.interface()
start.left()
start.right()
