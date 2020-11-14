from pygame import KEYDOWN, K_BACKSPACE
from pygame.event import EventType

from handler import Handler


class KeyboardBuffer(Handler):
    def __init__(self):
        self.buffer = ''

    def regurgitate(self) -> str:
        result = self.buffer
        self.buffer = ''
        return result

    def handle(self, event: EventType):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.buffer = self.buffer[:-1]
            self.buffer += event.unicode
