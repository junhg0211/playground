from pygame import Surface

from objet import Objet
from util import TextFormat


class Text(Objet):
    def __init__(self, x: int, y: int, text: str, text_format: TextFormat):
        super().__init__(x, y)
        self.text = text
        self.text_format = text_format

        self.surface = self.text_format.render(self.text)

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))
