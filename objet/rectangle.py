from pygame import Surface, draw

from objet import Objet


class FillRect(Objet):
    """속이 찬 사각형 Objet-입니다."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        """
        :ivar :param x: 왼쪽 변 좌표
        :ivar :param y: 위쪽 변 좌표
        """

        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def render(self, surface: Surface):
        draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


class DrawRect(FillRect):
    """속이 빈 사각형 Objet-입니다."""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, thickness: int):
        super().__init__(x, y, width, height, color)
        self.thickness = thickness

    def render(self, surface: Surface):
        draw.lines(surface, self.color, True, ((self.x, self.y),
                                               (self.x + self.width, self.y),
                                               (self.x + self.width, self.y + self.height)), self.thickness)
