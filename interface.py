import os
import time
import sys

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
            pick_route = typingInput("\x1B[3m Would you like to move E(left), W(right), or V(straight ahead)?").upper()
            
        elif pick_option == "2":
            print()
        elif pick_option == "3":
            print("Bye bye!")
    
        def left():
            if pick_route == "E":
                os.system('cls')
                typingPrint("\x1B[3mYou decide to turn left.\n You look around and notice that you are in a forest.\n As you go deeper into the forest, you hear a noise coming from the tree...")
                time.sleep(5)
                os.system('cls')
                typingPrint("You look back at the road when you hear a thump in front of you.")
                time.sleep(5)
                os.system('cls')

start.interface()