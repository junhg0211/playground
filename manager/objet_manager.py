from pygame import Surface

from manager import KeyManager
from objet import Objet


class ObjetManager:
    def __init__(self, key_manager: KeyManager):
        self.key_manager = key_manager
        self.objets = list()

    def add(self, objet: Objet):
        self.objets.append(objet)
        return self

    def remove(self, objet: Objet):
        self.objets.remove(objet)
        return self

    def tick(self):
        for objet in self.objets:
            objet.tick()

    def render(self, surface: Surface):
        for objet in self.objets:
            objet.render(surface)
