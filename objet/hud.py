from pygame import Surface, draw

from const import font, color
from manager import HandlerManager
from objet import Objet
from util import TextFormat


class HUD(Objet):
    def __init__(self, handler_manager: HandlerManager):
        """
        :ivar self.surfaces: 화면에 띄울 HUD-의 한줄한줄의 Surface-를 포함합니다.
        """

        super().__init__(0, 0)
        self.handler_manager = handler_manager
        self.text_format = TextFormat(font.DALMOORI, 16, color.WHITE)
        self.surfaces = list()

    def tick(self):
        string = f'핸들러 수 {len(self.handler_manager.handlers)}개'

        self.surfaces = [self.text_format.render(line) for line in string.split('\n')]

    def render(self, surface: Surface):
        for i in range(len(self.surfaces)):
            y = self.y + self.text_format.size * i
            draw.rect(surface, color.BLACK, ((self.x, y), (self.surfaces[i].get_width(), self.text_format.size)))
            surface.blit(self.surfaces[i], (self.x, y))
