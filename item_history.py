import json
test = open("item_history.json", encoding = "utf8")
data = json.load(test)

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
        data_collection(data)
        for i in data:
            print(i)
    data_collection()

    
    if input == 10:
        x = input("(YES/NO)").upper()
        if x == 'YES':
            world = return_home()
            #The vars() function returns the __dict__ attribute of an object
            data.append(vars(world))
        elif x == 'NO':
            print(data)
            break
        else:
            print("Invalid option. Please enter 'YES' or 'NO'")
        data_collection(data)
        for i in data:
            print(i)