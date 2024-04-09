class Items():
    def __init__(self, item, description)-> None:
        self.item = item
        self.description = description

def input_items():
    Item_name = input("Enter item: ")
    Item_description = input("Enter description: ")
    new_item = Items(Item_name, Item_description)
    return new_item

def data_collection():
    data = []
    while True:
        x = input("New item:(YES/NO): ").upper()
        if x == 'YES':
            new_item =  input_items()
            #The vars() function returns the __dict__ attribute of an object
            data.append(vars(new_item))
        elif x == 'NO':
            print(data)
            break
        else:
            print("Invalid option. Please enter 'YES' or 'NO'")

if __name__ == "__main__":
    data_collection()

Item_description = [{
    'Item name': "Sword",
    'Item cateogory': "Weapon/Combat",
    'Description': "Used in combat: Strength is dependent on the sharpness and level of the sword ()",
}, {
    'Item name': "Armor",
    'Item cateogory': "Combat",
    'Description': "A layer of protection that increases the damage needed to be dealt to you in order to lose health",
},{
    'Item name': "Health Potion",
    'Item cateogory': "Spell",
    'Description': "By intiating this potion, you gain 2 HP for every second that passes (Note: this potion lasts 10 seconds)",
},{
    'Item name': "Speed Potion",
    'Item cateogory': "Spell",
    'Description': "",
},{
    'Item name': "Meat",
    'Item cateogory':"Food",
    'Description': "This item can be consumed. Restores HP for each piece of meat eaten (pork, steak, chicken, lamb)",
},{
    'Item name': "Pickaxe",
    'Item cateogory':"Weapon/Combat",
    'Description': "Used in combat: Strength is dependent on the level of the Pickaxe",
},{
    'Item name': "Cake",
    'Item cateogory':"Food",
    'Description': "Can be consumed. Item is made using ingredients: flour, milk, egg, and sugar",
},{
    'Item name': "Bow and Arrow",
    'Item cateogory':"Weapon/Combat",
    'Description': "Used in combat: Strength is dependent on level and the use of arrow(s)",
}]

if input == ("item.help"):
    print (Item_description)   
