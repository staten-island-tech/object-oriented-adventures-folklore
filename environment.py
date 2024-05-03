import time
import sys
import os

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
        player = input("(ON/OFF): ").upper()
        if player == 'ON':
            typingPrint("You have spawned in your last saved position. Press enter to continue with your journey.")
            time.sleep(4)
            os.system('cls')
            typingPrint("You are forest right now. Try obtaining wood and creating a weapon just in case you come across enemies")
            time.sleep(4)
            os.system('cls')
        else:
            print("....")
environment()
        
