class Persona():
    def __init__(self,life = 50):
        self._life = life

    def get_life(self):
        return self._life

    def set_life(self,life):
        self._life = life