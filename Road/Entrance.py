import os
import time
import sys
import TowerFloor1
from TowerFloor2 import FloorTwo
from TowerFloor3 import FloorThree
from TowerFloor4 import FloorFour
from TowerBossBattle import FinalBoss
#System Typing
#########################################################################################################################################################
class typer():
    global typingPrint
    global typingInput
    global typingspeed
    typingspeed = 0.01
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
from math import ceil, floor
#\x1B[3m Italic 
#\x1B[0m Normal Text
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
#########################################################################################################################################################
class going_into_tower:
    def asking_to_enter():
        os.system('cls')
        typingPrint("You walked up to the steps of the dark tower, a breeze send shivers down your swine. You walk up to the huge gates of the tower.")
        time.sleep(2)
        os.system('cls')
        Enter_Tower = typingInput("Would you like to go up the tower?").upper()
        os.system('cls')

        def Picking_Floor():
            if Enter_Tower == "YES":
                Picking_Floor = typingInput("Which floor would you like to go to? (1,2,3,4,5, or leave)").upper
                if Picking_Floor == "1".upper:
                    TowerFloor1.FloorOne.Floor1_Beginning()
                elif Picking_Floor == "2".upper:
                    FloorTwo.Floor2_Beginning()
                elif Picking_Floor == "3".upper:
                    FloorThree.Floor3_Beginning()
                elif Picking_Floor == "4".upper:
                    FloorFour.Floor4_Beginning()
                elif Picking_Floor == "5".upper:
                    FinalBoss.FinalBoss_Beginning()
                else:
                    Picking_Floor()
        Picking_Floor()

            

        if Enter_Tower == "NO":
            print("ya")
going_into_tower.asking_to_enter()