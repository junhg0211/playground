from pygame import Surface
from pygame.font import Font


class TextFormat:
    """objet.Text-의 글꼴"""

    def __init__(self, path: str, size: int, color: tuple):
        """
        :ivar :param path: 글꼴 위치. 실제로 저장된 파일의 경로 문자열입니다.
        :param size: 글꼴 높이
        :param color: text 색상
        """

        self.path = path
        self.size = size
        self.color = color

        self.font = Font(self.path, self.size)

    def render(self, text: str) -> Surface:
        """:return: text-가 self(text_format)로 표현된 Surface"""

        return self.font.render(text, True, self.color)

    def get_width(self, text: str) -> int:
        """:return: self(text_format)로 text-를 표현한 것의 가로 폭"""

        return self.render(text).get_width()
