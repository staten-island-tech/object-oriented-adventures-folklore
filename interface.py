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
            typingPrint("You're walking across the street when a truck honks at you.\n You turn your as a blinding light gets closer...")
            typingPrint("You open your eyes to a pounding in your head.\n")
            
        elif pick_option == "2":
            print()
        elif pick_option == "3":
            print("Bye bye!")

