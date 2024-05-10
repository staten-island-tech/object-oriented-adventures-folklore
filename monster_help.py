import json

test = open("monster_data.json", encoding = "utf8")
monster_data = json.load(test) 

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