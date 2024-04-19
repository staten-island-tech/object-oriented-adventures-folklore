import json
test = open("item_history.json", encoding = "utf8")
data = json.load(test)

class Item:
    def Item_Description():
        print("1. Start Game")
        print_option = input("What would you like to do? \n")

        if print_option == "1":
            print()
        else:
            print_option == "2"

Item_description = [{
    "Item name": "Sword",
    "Item cateogory": "Weapon/Combat",
    "Description": "Used in combat: Strength is dependent on the sharpness and level of the sword ()",
}, {
    "Item name": "Armor",
    "Item cateogory": "Combat",
    "Description": "A layer of protection that increases the damage needed to be dealt to you in order to lose health",
},{
    "Item name": "Pickaxe",
    "Item cateogory":"Weapon/Combat",
    "Description": "Used in combat: Strength is dependent on the level of the Pickaxe",
},{
    "Item name": "Bow and Arrow",
    "Item cateogory":"Weapon/Combat",
    "Description": "Used in combat: Strength is dependent on level and the use of arrow(s)",
},{
    "Item name": "Health Potion",
    "Item cateogory": "Spell",
    "Description": "By intiating this potion, you gain 2 HP for every second that passes (Note: this potion lasts 10 seconds)",
},{
    "Item name": "Speed Potion",
    "Item cateogory": "Spell",
    "Description": "By intiating this potion, you gain 2x speed for 6 seconds",
},{
    "Item name": "Strength Potion",
    "Item cateogory": "Spell",
    "Description": "By intiating this potion, your increase your chances of crit damage by 15%",
},{
    "Item name": "Defense Potion",
    "Item cateogory": "Spell",
    "Description": "By intiating this potion, all damage dealt to you is reduced by 20%",
},{
    "Item name": "Meat",
    "Item cateogory":"Food",
    "Description": "This item can be consumed. Restores HP for each piece of meat eaten (pork, steak, chicken, lamb)",
},{
    "Item name": "Cake",
    "Item cateogory":"Food",
    "Description": "Can be consumed. Item is made using ingredients: flour, milk, egg, and sugar",
},{
    "Item name": "Apple",
    'Item cateogory':"Food",
    'Description': "Can be consumed. Picked from tree or found on ground.",
},{
    "Item name": "Cabbage",
    "Item cateogory":"Food",
    "Description": "Can be consumed to restore HP. Yummyyyyy",
},{
    "Item name": "Gold",
    "Item cateogory":"Currency",
    "Description": "Used to buy items in the shop.",
},{
    "Item name": "Silver",
    "Item cateogory":"Currency",
    "Description": "Used to buy items in to the shop.",
},{
    "Item name": "Bronze",
    "Item cateogory":"Currency",
    "Description": "Used to buy items in to the shop.",
},{
    "Item name": "Wood",
    "Item cateogory":"Nature",
    "Description": "This can be used to make weapons and houses",
}]

""" 'Item name': "",
'Item cateogory':",
'Description': "", 
 """
if input == ("item.help"):
    print (Item_description)   

json_object = json.dumps(Item_description, indent = 4) 
# Print JSON object
print(json_object) 