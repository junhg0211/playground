from pygame import Surface


class Objet:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def tick(self):
        pass

    def render(self, surface: Surface):
        pass
