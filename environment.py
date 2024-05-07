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
            typingPrint("You are forest right now. Try obtaining wood and creating a weapon just in case you come across enemies")
            time.sleep(4)
            os.system('cls')
            typingPrint("")
        else:
            print("....")
environment()
        
