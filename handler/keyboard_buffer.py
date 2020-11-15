from pygame import KEYDOWN, K_BACKSPACE
from pygame.event import Event

from handler import Handler


class KeyboardBuffer(Handler):
    def __init__(self):
        self.buffer = ''
        self.backspaces = 0

    def regurgitate(self) -> tuple:
        return self.regurgitate_string(), self.regurgitate_backspace()

    def regurgitate_string(self) -> str:
        result = self.buffer
        self.buffer = ''
        return result

    def regurgitate_backspace(self) -> int:
        result = self.backspaces
        self.backspaces = 0
        return result

    def handle(self, event: Event):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(self.buffer) <= 0:
                    self.backspaces += 1
                else:
                    self.buffer = self.buffer[:-1]
            self.buffer += event.unicode
