import time
import sys
import os
import Player
global typingPrint
global typingspeed
typingspeed = 0.01
global typingInput
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(typingspeed)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(typingspeed)
        value = input()  
        return value  
    
class Merchant:
    Player.Players()
    def __init__(self, name, potions, foods, materials):
        self.name = name
        self.potions = potions
        self.foods = foods
        self.materials = materials
              
    def display_items(self):
        typingPrint("\nYou walk towards the lovely shop centered in the middle of a market.")
        time.sleep(1)
        os.system('cls')
        print("Merchant:")
        typingPrint(f"Welcome traveler to {self.name}!")
        time.sleep(1)
        os.system('cls')
        print("Take a look at my stick. Let me know if anything catches your eye.")
        time.sleep(1)
        os.system('cls')
        for item, price in self.potions.potions():
            print(f"{item.capitalize()}: {price} gold")
        for item, price in self.foods.foods():
            print(f"{item.capitalize()}: {price} gold")
        for item, price in self.materials.materials():
            print(f"{item.capitalize()}: {price} gold")
                
    def sell_item(self, item, quantity, buyer):
        if item not in self.potions or self.foods or self.materials:
            print(f"Appologies traveler, we currently don't sell {item}s.")
            print("You exit the store and make your way back to town with a visible look of disappointment at the news they didnt have your requested item.")
        elif (self.potions[item] or self.foods[item] or self.materials[item]) * quantity > buyer.currency["Gold"]:
            print("  ")
            print("The old man stares at you questioning if your serious with your offer.")
            print("  ")
            print("Old man: You insult my shop with your offer. Come again once you have enough gold to afford my wares.")
            print("  ")
            print("You exit his shop and make your way back to the town.")
        elif buyer.potions[item] -= quantity or buyer.materials[item] -= quantity or buyer.foods[item] -= quantity:
            #might change to self.currency
            Player.Players.currency["Gold"] -= self.potions[item] * quantity
            buyer.inventory.add_item(item, quantity)
            print("  ")
            print(f"Old man: Ahh, exelent choice. Here is your {item} that will be {self.potions[item] * quantity} gold.")
            print("  ")
            print(f"The old man holds one hand out expecting gold holding the {item} in the other. As you drop the gold into his hand he gives you the blood vial. You walk out the door and back towards the town, satisfied with your purchase.")

    # create a new instance of the Merchant class with some items for sale
        merchant = Merchant("Fangs & Favors", {"blood vial": 25, "artifact": 140, "ancient text": 200})
        merchant.display_items()
        print("  ")
        choice = input("Looking for anything in particular?: ")

         # display the items for sale
        merchant.display_items()

        # sell an item to the player
        #might change to self.currency
        if choice == "blood vial": 
            merchant.sell_item("blood vial", 1, Player.Players)
        elif choice == "artifact": 
            merchant.sell_item("artifact", 1, Player.Players)
        elif choice == "ancient text": 
            merchant.sell_item("ancient text", 1, Player.Players)
        else:
            print("  ") 
            print("My appologies traveler, we do not currently have that item. However we do get new shipments weekly so check back soon!")
            print("You exit the store and make your way back to town with a visible look of disappointment at the news they didnt have your requested item.")
