class Items():
    def __init__(self, item:str, description:str):
        self.item = item
        self.description = description

class weapon(Items):
    def __init__(self, item: str, description:str, damage:int):
        super().__init__(item, description)
        self.damage = damage
    def __str__(self):
        return f"{self.item},{self.description},{self.damage}"

class armor(Items):
    def __init__(self, item: str, description: str, protection:int):
        super().__init__(item, description)
        self.protection = protection
    def __str__(self):
        return f"{self.item},{self.description},{self.protection}"
    
class potion(Items):
    def __init__(self, item: str, description: str, effect: str):
        super().__init__(item, description)
        self.effect = effect
    def __str__(self):
        return f"{self.item},{self.description},{self.effect}"
    
class food(Items):
    def __init__(self, item: str, description: str, hp: int):
        super().__init__(item, description)
        self.hp = hp
    def __str__(self):
        return f"{self.item},{self.description},{self.hp}"
    
