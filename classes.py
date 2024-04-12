import json
import os

class player:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

test = open("monster_data.json", encoding = "utf8")
monster_data = json.load(test)

class start:
    def interface():
        print("1. Start Game")
        print("2. How to play")
        print("3. Exit Game")
        pick_option = input("What would you like to do? (ex: 1, 2, or 3): \n")
        os.system('cls')

        if pick_option == "1":
            print()
        elif pick_option == "2":
            print()
        elif pick_option == "3":
            print("Bye bye!")

class monster_info:
    def search_name():
        name = input("Which monster would you like to know about?\n").upper()
        for i in monster_data:
            if name in i['Name'].upper():
                print(i['Name'])
                print(i['Description'])
                print(i['Loot'])
                print(i['Hp'])
    def search_loot():
        loot = input("What monsters drop the loot:\n").upper()
        for i in monster_data:
            if loot in i['Loot'].upper():
                print(i['Name'])
    def search_hp(): 
        h = int(input("What monsters have an hp of:\n(Reminder: Monsters only have hps of: 50, 100, 150, or 200)\n"))
        for x in monster_data:
            if h == x["Hp"]:
                print(x['Name'])   

class encounter:
    def Maldachaunians():
        hp = 100
        print("OOOGA BOOGA!!")

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
