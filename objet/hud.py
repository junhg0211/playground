from pygame import Surface, draw

from const import font, color
from manager import HandlerManager
from objet import Objet
from util import TextFormat


class HUD(Objet):
    def __init__(self, handler_manager: HandlerManager):
        super().__init__(0, 0)
        self.handler_manager = handler_manager
        self.height = 16
        self.text_format = TextFormat(font.DALMOORI, self.height, color.WHITE)
        self.surfaces = list()

    def tick(self):
        string = f'핸들러 수 {len(self.handler_manager.handlers)}개'

        self.surfaces = [self.text_format.render(line) for line in string.split('\n')]

    def render(self, surface: Surface):
        for i in range(len(self.surfaces)):
            y = self.y + self.height * i
            draw.rect(surface, color.BLACK, ((self.x, y), (self.surfaces[i].get_width(), self.height)))
            surface.blit(self.surfaces[i], (self.x, y))
