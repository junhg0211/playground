from pygame import QUIT
from pygame.event import Event

from handler import Handler


class Quit(Handler):
    def __init__(self, function):
        self.function = function

    def handle(self, event: Event):
        if event.type == QUIT:
            self.function()
