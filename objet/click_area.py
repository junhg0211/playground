from pygame import Surface, draw

from manager import MouseManager
from objet import Objet
from util import limit, lerp


class ClickArea(Objet):
    def __init__(self, x: int, y: int, width: int, height: int, runnable, mouse_manager: MouseManager):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.runnable = runnable
        self.mouse_manager = mouse_manager

    def mouse_on(self):
        return limit(self.mouse_manager.x, self.x, self.x + self.width) == self.mouse_manager.x \
               and limit(self.mouse_manager.y, self.y, self.y + self.height) == self.mouse_manager.y

    def tick(self):
        if self.mouse_manager.end_left:
            if self.mouse_on():
                self.runnable()


class UnderlinedClickArea(ClickArea):
    def __init__(self, x: int, y: int, width: int, height: int, runnable, color: tuple, mouse_manager: MouseManager):
        super().__init__(x, y, width, height, runnable, mouse_manager)
        self.color = color

        self.length = 0.0

    def tick(self):
        super().tick()

        if self.mouse_on():
            self.length = lerp(self.length, self.width)
        else:
            if self.length < 1:
                self.length = 0
            else:
                self.length = lerp(self.length, 0)

    def render(self, surface: Surface):
        draw.line(surface, self.color, (self.x, self.y + self.height), (self.x + self.length, self.y + self.height))
