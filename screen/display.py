from math import inf
from time import time

from pygame import display


class Display:
    """basis-의 창(window) 클래스입니다."""

    def __init__(self, width: int, height: int, caption: str):
        """
        :param caption: 창의 캡션
        :ivar self.fps: 이전 프레임에서의 프레임레이트
        :ivar self.previous_time: 이전 프레임의 시각
        """

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
