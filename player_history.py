import json
import os

test = open("history.json", encoding = "utf8")
player_data = json.load(test)

class history:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"{self.name},{self.age}, {self.gender}"
    
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)


x = history(name,age,gender)
data.append(x.__dict__)

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")