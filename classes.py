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
            speed = 0.01
            time.sleep(speed)
    def typingInput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            speed = 0.01
            time.sleep(speed)
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

