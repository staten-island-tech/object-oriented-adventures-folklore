import json
import os

class history:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"{self.name},{self.age}, {self.gender}"
    
with open("player_history.json", "r") as f:
    player_data = json.load(f)

name = input("What is your name?\n")
age = input("How old are you?\n")
gender = input("What gender do you identify as?\n")
x = history(name,age,gender)
player_data.append(x.__dict__)

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(player_data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("player_history.json")
os.rename(new_file, "player_history.json")