from pygame import Surface

from objet import Objet


class ObjetManager:
    def __init__(self):
        self.objets = list()

    def add(self, objet: Objet):
        self.objets.append(objet)
        return self

    def remove(self, objet: Objet):
        if objet in self.objets:
            self.objets.remove(objet)
        return self

    def tick(self):
        for objet in self.objets:
            objet.tick()

    def render(self, surface: Surface):
        for objet in self.objets:
            objet.render(surface)
