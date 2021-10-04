from persona import Persona
import random

class MyPlayer(Persona):
    def __init__(self,life=50,potion=3):
        super().__init__(life=life)
        self._potion = potion
        

    def recover_life(self):
        self._life += random.randint(15,50)

    def damage(self):
        return random.randint(5,10)

    def get_potion(self):
        return self._potion

    def set_potion(self,potion):
        self._potion = potion


    
