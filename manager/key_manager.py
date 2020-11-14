from pygame import KEYDOWN, KEYUP
from pygame.event import EventType

from handler import Handler


class KeyManager(Handler):
    def __init__(self):
        self.keys = set()
        self.previous_keys = set()
        self.start_keys = set()
        self.end_keys = set()

    def is_key(self, key: int) -> bool:
        return key in self.keys

    def is_start_key(self, key: int) -> bool:
        return key in self.start_keys

    def is_end_key(self, key: int) -> bool:
        return key in self.end_keys

    def handle(self, event: EventType):
        if event.type == KEYDOWN:
            self.keys.add(event.key)
        elif event.type == KEYUP:
            self.keys.remove(event.key)

    def tick(self):
        self.start_keys = self.keys - self.previous_keys
        self.end_keys = self.previous_keys - self.keys

        self.previous_keys = self.keys.copy()
