from math import inf
from time import time

from pygame import display


class Display:
    def __init__(self, width: int, height: int, caption: str):
        self.width = width
        self.height = height

        self.window = display.set_mode((self.width, self.height))
        display.set_caption(caption)

        self.fps = 0
        self.previous_time = time()

    def tick(self):
        now = time()

        try:
            self.fps = 1 / (now - self.previous_time)
        except ZeroDivisionError:
            self.fps = inf

        self.previous_time = now
