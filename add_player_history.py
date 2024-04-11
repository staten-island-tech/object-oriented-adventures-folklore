import json
import os

class history:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
with open("player_history.json", "r") as f:
    player_data = json.load(f)

name = input("What is your name?\n")
x = history(name)
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