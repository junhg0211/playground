from manager import MouseManager
from objet import Objet
from util import limit


class ClickArea(Objet):
    def __init__(self, x: int, y: int, width: int, height: int, runnable, mouse_manager: MouseManager):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.runnable = runnable
        self.mouse_manager = mouse_manager

    def tick(self):
        if self.mouse_manager.end_left:
            if limit(self.mouse_manager.x, self.x, self.x + self.width) == self.mouse_manager.x\
                    and limit(self.mouse_manager.y, self.y, self.y + self.height) == self.mouse_manager.y:
                self.runnable()
