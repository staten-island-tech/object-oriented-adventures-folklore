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

class monsters:
    def maldachaunians():
        hp = 100
        print("OOGAH BOOGAH!")
    def wimitescu():
        hp = 200
    def elves():
        hp = 100
    def water_spirits():
        hp = 150 

class encounter:
    def enco_monster():
        while True:
            choose = input("What would you like to do? A/B/C\n(Type: 'help' for explanation on encounters)\n").upper()
            while choose == "HELP":
                print("A - Attack")
                print("B - Be a wuss (run away)")
                print("C - Consume potion")
                break
            if choose == "A":
                print("You have attacked!")
                break
            elif choose == "B":
                print("You are a huge wuss! Congrats on running away, YOU COWARD!")
                break
            elif choose == "C":
                print("Which potion would you like to drink\n")
                break

encounter.enco_monster()