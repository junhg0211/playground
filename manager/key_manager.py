from pygame import KEYDOWN, KEYUP
from pygame.event import EventType

from handler import Handler


class KeyManager(Handler):
    def __init__(self):
        self.keys = set()
        self.previous_keys = set()

    def handle(self, event: EventType):
        if event.type == KEYDOWN:
            self.keys.add(event.key)
        elif event.type == KEYUP:
            self.keys.remove(event.key)

    def is_key(self, key: int) -> bool:
        return key in self.keys
