from pygame import QUIT
from pygame.event import EventType

from handler import Handler


class Quit(Handler):
    def __init__(self, function):
        self.function = function

    def handle(self, event: EventType):
        if event.type == QUIT:
            self.function()
