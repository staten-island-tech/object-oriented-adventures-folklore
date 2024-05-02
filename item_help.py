import json
import os
test = open("item_history.json", encoding = "utf8")
data = json.load(test)

class Items_info:
    def name():
        y = input("Enter in an item name: ").capitalize()
        for i in data:
            if y in i['Item name']:
                print(i["Description"])
                print()
    def item_category():
        x = input("What items are in the item category: ").capitalize()
        for i in data:
            if x in i['Item category']:
                print(i["Item name"])
                print(i["Description"])
                print()

item_help = input("Item help (Y/N):\n").upper()

if item_help == "Y":
    os.system("cls")
    h = input("How would you like to find information about an item? (Ex: NAME, CATEGORY)\n").upper()
    if h == "NAME": 
        os.system("cls")
        Items_info.name()
    if h == "CATEGORY":
        os.system("cls")
        Items_info.item_category()

