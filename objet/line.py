from pygame import Surface, draw

from objet import Objet


class Line(Objet):
    def __init__(self, x: int, y: int, end_x: int, end_y: int, color: tuple):
        super().__init__(x, y)
        self.end_x = end_x
        self.end_y = end_y
        self.color = color

    def render(self, surface: Surface):
        draw.aaline(surface, self.color, (self.x, self.y), (self.end_x, self.end_y))
