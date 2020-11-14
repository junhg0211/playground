from pygame import Surface

from manager import MouseManager
from objet import Objet
from objet.click_area import UnderlinedClickArea
from screen import Display
from util import TextFormat


class Text(Objet):
    def __init__(self, x: int, y: int, text: str, text_format: TextFormat):
        super().__init__(x, y)
        self.text = text
        self.text_format = text_format

        self.surface = self.text_format.render(self.text)

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))


class TextButton(Text):
    def __init__(self, x: int, y: int, text: str, text_format: TextFormat, runnable, mouse_manager: MouseManager,
                 display: Display):
        super().__init__(x, y, text, text_format)

        self.click_area = UnderlinedClickArea(x, y, self.surface.get_width(), self.surface.get_height(), runnable,
                                              self.text_format.color, mouse_manager, display)

    def tick(self):
        self.click_area.tick()

    def render(self, surface: Surface):
        super().render(surface)
        self.click_area.render(surface)
