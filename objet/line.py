from pygame import Surface, draw

from objet import Objet


class Line(Objet):
    """화면에 보이는 선분입니다."""

    def __init__(self, x: int, y: int, end_x: int, end_y: int, color: tuple):
        """
        :ivar :param x: 선분의 시작 점의 x-좌표
        :ivar :param y: 선분의 시작 점의 y-좌표
        :ivar :param end_x: 선분의 끝 점의 x-좌표
        :ivar :param end_y: 선분의 끝 점의 y-좌표
        :ivar :param color: 선분의 색상
        """

        super().__init__(x, y)
        self.end_x = end_x
        self.end_y = end_y
        self.color = color

    def render(self, surface: Surface):
        draw.aaline(surface, self.color, (self.x, self.y), (self.end_x, self.end_y))
