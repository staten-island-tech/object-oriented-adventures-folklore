import json
import os

test = open("monster_data.json", encoding="utf8")
monster_data = json.load(test)

class monster_info:
    def monster():
        name = input("Which monster would you like to know about?\n").upper()
        for i in monster_data:
            if name == i['name'].upper():
                print(i)

monster_info.monster()