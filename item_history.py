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

    if input == ("item.help"):
        print (Item_description)

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
    'Description': "By intiating this potion, you gain 2x speed for 6 seconds",
},{
    'Item name': "Apple",
    'Item cateogory':"Food",
    'Description': "Can be consumed. Found in the wild or can be obtained through tree planting",
}{
    'Item name': "Cake",
    'Item cateogory':"Food",
    'Description': "Can be consumed. Must be made through ingredients: flour, eggs, sugar, and milk",
}{
    'Item name': "Pickaxe",
    'Item cateogory': "Weapon/Combat",
    'Description': "Used in combat: Strength is dependent on the level of the pickaxe",
}{
    'Item name': "Bow",
    'Item cateogory':"Weapon/Combat",
    'Description': "Used in combat: Made with wood and string, and requires an arrow to be intiated",
}]
print(Item_description)