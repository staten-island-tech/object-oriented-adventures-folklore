class player:
    def __init__(self, name: str, hp: int, strength: int, speed: int, inventory: str):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.inventory = inventory 

    def __str__(self):
        return f"{self.name}, {self.hp}, {self. strength}, {self.speed}, {self.inventory}"