import random 
import time
import os
from classes import typingPrint
class battle_system:
    def battle(a,b,c,d,e,f): 
        os.system('cls')
        typingPrint("Commence Battle!")
        time.sleep(1)
        os.system('cls')
        global m 
        global y
        def attack_enemy(a,b,c):
            #a is the monter's hp, b is how much damage the player does, c is the player's crit attack amount
            d = random.randint(1,90)
            if d < 90:
                m = a - b
                typingPrint("You did " + str(b) + " damage! It only has " + str(m) + " hp now!")
                time.sleep(3)
                os.system('cls')
            elif d >= 90:
                m = a - c
                typingPrint("Your attack was a critical hit! You did " + str(c) + " damage! It only has " + str(m) + " hp now!")
                time.sleep(3)
                os.system('cls')
            return m
             
        def get_attacked(d,e,f):
            #d is player hp, e is how much damage the monster does, f is a critical hit
            x = random.randint(1,100)
            if x < 90:   
                y = d - e
                typingPrint("You were attacked! You took " + str(e) + " damage and now have " + str(y) + " hp!")
                time.sleep(3)
                os.system('cls')
            elif x >= 90:
                y = d - f 
                typingPrint("You were attacked! It was a critical hit! You took " + str(f) + " and now have " + str(y) + " hp!")
                time.sleep(3)
                os.system('cls')
            return y 
    
        m = attack_enemy(a,b,c)
        y = get_attacked(d,e,f)

        while m and y > 0: 
            attack_enemy(a,b,c)
            get_attacked(d,e,f)
            return m and y 
        
        if m <= 0:
            typingPrint("Congradulations! You won the batttle!")
            time.sleep(2)
            os.system('cls')
        elif y <= 0:
            typingPrint("It has killed you...\nYou are dead...")
            time.sleep(2)
            os.system('cls')

battle_system.battle(50,5,10,50,5,10)