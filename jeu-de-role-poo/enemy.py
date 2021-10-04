from persona import Persona
import random

class Enemy(Persona):
    def __init__(self, life=50):
        super().__init__(life=life)

    def damage(self):
        return random.randint(5,15)