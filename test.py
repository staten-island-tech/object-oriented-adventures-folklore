# don't import everything, if you only need one function
from random import randint

# option to have a pause, so that the fight lasts a number of seconds
from time import sleep

creatures = {
    1 : ['Maldachaunians',    3, 100],
    2 : ['Ogre',     4, 100],
    3 : ['Shrek', 6, 100],
    4 : ['Water Spirit',  7, 100],
    5 : ['Elves',  8, 100],
    }

players = {
    1 : ['Player name', 0, 100],
    }

weapons = {
    1 : ['sword',  1, 10],
    2 : ['pickaxe',    3, 10],
    3 : ['bow and arrow',     4, 10],
    4 : ['blades', 6, 10],
    5 : ['dagger', 5, 10],
    }
 
# indices
name = 0
damage = 1
health, usage = 2, 2

# get a random player and weapon
player = players.get(randint(1,len(players)))
weapon = weapons.get(randint(1,len(weapons)))
weaponName = weapon[name]
playerDamage = weapon[damage]

# get a random creature
creature = creatures.get(randint(1,len(creatures)))
creatureName = creature[name]
creatureDamage = creature[damage]

print(f"{player[name]}, you have choose {weaponName} and will be fighting a {creatureName}")