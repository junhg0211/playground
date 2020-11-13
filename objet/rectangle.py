from pygame import Surface, draw

from objet import Objet


class FillRect(Objet):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def render(self, surface: Surface):
        draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


class DrawRect(FillRect):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, thickness: int):
        super().__init__(x, y, width, height, color)
        self.thickness = thickness

    def render(self, surface: Surface):
        draw.lines(surface, self.color, True, ((self.x, self.y),
                                               (self.x + self.width, self.y),
                                               (self.x + self.width, self.y + self.height)), self.thickness)
