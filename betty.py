import os
import time
import sys
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

class Betty:
    os.system('cls')
    def first_en_bet():
        os.system('cls')
        typingPrint("\x1B[3m You find yourself drawn to the towering structure in the center of the city.\n Its spire reaches up to the sky, beckoning you to come closer.\n As you approach the base of the tower, you notice a young woman sitting on the steps.")
        time.sleep(5)
        os.system('cls')
            
        def bet_Continue():
            print("\x1B[0mStranger:")    
            Climb_Poets_Tower = typingInput(boxed_msg("Are you here to climb the Tortured Poets Department?\n (yes/no)\n(You also have the option to ask for information about the tower.)")).upper()
            time.sleep(2)
            os.system('cls')

            if Climb_Poets_Tower == "YES":
                os.system('cls')
                def yes_to_climb_poets_tower():
                    os.system('cls')
                    print("Stranger")
                    typingPrint(boxed_msg("You better be careful. \nThe tower belonged to a powerful moonlit witch. \nNo one has ever made it to the top."))
                    time.sleep(5)
                    os.system('cls')

                    print("Travler:")
                    typingPrint(boxed_msg("Thank you for the advice."))
                    time.sleep(1)
                    os.system('cls')

                    typingPrint("\x1B[3m You entered through the gates of the tower, knowing full well you have no experience.\n As you arrived to the stairs of the tower, a forced consumed you and you were transported back in time.\n You ended put back on the fork in the world. \nThe place your journey began.")
                    time.sleep(5)
                    os.system('cls')

                    print("Travler:")
                    typingPrint(boxed_msg("\x1B[0mWhat happened?"))
                    time.sleep(1)
                    os.system('cls')
                    yes_to_climb_poets_tower()

                elif Climb_Poets_Tower == "NO":
                    os.system('cls')
                    not_climb_poet_tower()

                    def continuing_to_otrtued_poets():
                                os.system('cls')
                                print("\x1B[0mStranger:")    
                                Continue_to_climb_poet = typingInput(boxed_msg("Are you still going to climb the Tortured Poets Department?\n (yes/no)")).upper()
                                time.sleep(2)
                                os.system('cls')

                                if Continue_to_climb_poet == "NO":
                                    not_climb_poet_tower()
                                elif Continue_to_climb_poet == "YES":
                                    yes_to_climb_poets_tower()
                                else:
                                    os.system('cls')
                                    typingPrint("\x1B[3m That isn't an option.")
                                    time.sleep(5)
                                    os.system('cls')
                                    continuing_to_otrtued_poets()
                else:
                    os.system('cls')
                    print("Betty:")
                    typingPrint(boxed_msg(Climb_Poets_Tower))

                    os.system('cls')
                    print("Betty:")
                    typingPrint(boxed_msg("It was said that this tower belong to a powerful witch. \nHowever she wasn't the one who built this tower. \nLegends said that this was a mental asylum. \nPeople who have gone in, never came back. \nOnly one person ever made it out alive, and he came out insane."))
                    continuing_to_otrtued_poets()

                    


                def not_climb_poet_tower():
                    print("\x1B[0mTraveller:")
                    typingPrint(boxed_msg("No, not really.\n I am new to this town."))
                    time.sleep(5)
                    os.system('cls')

                    print("\x1B[0mBetty:")
                    typingPrint(boxed_msg("Hi, I am Betty and I can show you around.\nThis village is known for its fishing ports and advancements in the water way.\nAt the center of the village, we have a huge water fountain, which is like healing sprinkler.\nOnce you get near it, it should heal you completely."))
                    time.sleep(5)
                    os.system('cls')

                    print("\x1B[0mTraveller:")
                    typingPrint(boxed_msg("Thank you."))
                    time.sleep(5)
                    os.system('cls')

                    print("\x1B[0mBetty:")    
                    typingPrint(boxed_msg("Follow me, I can show you where you can get materials and supplies.\nThe merchant is very nice and the stuff is pretty cheap."))
                    time.sleep(5)
                    os.system('cls')
                
                


            going_to_Betty = typingInput("\x1B[3m Would you like to approach her? (yes/no)").upper()
            if going_to_Betty == "YES":
                bet_Continue()
                
            if going_to_Betty == "NO":
                encountering_characters()


Betty.first_en_bet()