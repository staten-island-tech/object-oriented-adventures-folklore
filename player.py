class player:
    def __init__(self, name: str, hp: int, strength: int, speed: int, inventory: str, damage: int):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = speed
        self.inventory = inventory 
        self.damage = damage

    def __str__(self):
        return f"{self.name}, {self.hp}, {self. strength}, {self.speed}, {self.inventory}, {self.damage}"

