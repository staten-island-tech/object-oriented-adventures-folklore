import json
import os

test = open("monster_data.json", encoding = "utf8")
monster_data = json.load(test)

class monster_info:
    def search_monster():
        name = input("Which monster would you like to know about?\n").upper()
        for i in monster_data:
            if name in i['Name'].upper():
                print(i['Name'])
                print(i['Description'])
                print(i['Loot'])