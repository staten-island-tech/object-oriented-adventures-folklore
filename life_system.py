class hp:
    def __init__(self,full_hp,hp_history):
        self.full_hp = full_hp
        self.hp_history = hp_history
    
    def __str__(self):
        return f"{self.full_hp},{self.hp_history}"
    
    full_hp = 100
    hp_history = []

