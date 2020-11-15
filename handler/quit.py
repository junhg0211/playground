from pygame import QUIT
from pygame.event import Event

from handler import Handler


class Quit(Handler):
    """프로그램 종료를 위한 Handler-입니다."""

    def __init__(self, function):
        self.function = function

    def handle(self, event: Event):
        if event.type == QUIT:
            self.function()
