import os
import time
import sys
from Entrance import going_into_tower
from Forest import forestman
from classes import format_line
from classes import boxed_msg
from classes import typingInput
from classes import typingPrint

class Go_Where():
    global different_location
    def different_location():
        if Location == "A":
            going_into_tower.asking_to_enter()
        elif Location == "B":
            forestman.forester()
        elif Location == "C":
            print("ya")
        elif Location == "D":
            picking_location()
        else:
            picking_location()

    global picking_location
    def picking_location():
        global Location
        Location = typingInput("Would you like to go?\n A) Tower\n B) Forest\n C) Village\n D)Road \n").upper()
        different_location()
    picking_location()
    

