class Items():
    def __init__(self, item:str):
        self.item = item

class weapon(Items):
    def __init__(weapon, item: str, description:str, damage:int):
        super().__init__(item, description)
        weapon.damage = damage

class armor(Items):
    def __init__(armor, item: str, description: str, protection:int):
        super().__init__(item, description)
        armor.protection = protection

class potion(Items):
    def __init__(potion, item: str, description: str, effect: str):
        super().__init__(item, description)
        potion.effect = effect
    
class food(Items):
    def __init__(food, item: str, description: str, add_hp: int):
        super().__init__(item, description)
        food.add_hp = add_hp

class currency(Items):
    def __init__(currency, item: str, description: str, value: int):
        super().__init__(item, description)
        currency.value = value
    
