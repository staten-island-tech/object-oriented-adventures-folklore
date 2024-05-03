import json
test = open("item_history.json", encoding = "utf8")
data = json.load(test)

class Items:
    def print():
        for i in data:
            print(i["Description"])
    def item_category():
        x = (input("pick item category: "))
        for i in data:
            if x in i['Item category']:
                print(i["Item name"])
Items.item_category()