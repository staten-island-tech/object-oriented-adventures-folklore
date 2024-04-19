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

with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    pokemon_list= [Items.__dict__]
    data.append(Items)
    ##Call classes in here

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps()

    # Write the JSON string to the new JSON file
    f.write(json_string)
    f.close()


""" 'Item name': "",
'Item cateogory':",
'Description': "", 
 """  

json_object = json.dumps(Item_description, indent = 4) 
# Print JSON object
print(json_object) 
