from pygame import image, Surface, transform

from objet import Objet


class Image(Objet):
    """화면에 이미지를 표시합니다."""

    def __init__(self, x: int, y: int, photo=None):
        """
        :param x: 왼쪽 변 좌표
        :param y: 위쪽 변 좌표
        :ivar :param photo:
        -   만약 photo-가 str 객체일 때에는 이미지의 경로로 인식하고 이미지 읽기를 시도합니다.
        -   만약 photo-가 Surface 객체일 때에는 self.photo-에 저장합니다.
        -   self.photo-는 언제나 Surface 객체입니다.
        """
        super().__init__(x, y)
        if photo is None:
            raise TypeError("missing 1 required positional argument: 'photo'")
        elif isinstance(photo, str):
            self.surface = image.load(photo)
        elif isinstance(photo, Surface):
            self.surface = photo
        else:
            raise TypeError(f"invalid image type: '{photo}'")

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))

    def scale(self, width: int, height: int):
        """
        이미지의 가로 폭과 세로 높이를 변경해 self.surface-에 저장합니다.

        :param width: 가로 폭
        :param height: 세로 높이
        :return: 크기가 변경된 이미지를 포함하는 Image 객체
        """

        self.surface = transform.scale(self.surface, (width, height))
        return self

    def smooth_scale(self, width: int, height: int):
        """
        이미지의 가로 폭과 세로 높이를 부드럽게 변경해 self.surface-에 저장합니다.

        :param width: 가로 폭
        :param height: 세로 높이
        :return: 크기가 부드럽게 변경된 이미지를 포함하는 Image 객체
        """

        self.surface = transform.smoothscale(self.surface, (width, height))
        return self

    def crop(self, x: int, y: int, width: int, height: int):
        """
        이미지의 일부분을 잘라 self.surface-에 저장합니다.

        :param x: 자를 부분의 왼쪽 변 좌표
        :param y: 자를 부분의 위쪽 변 좌표
        :param width: 자를 부분의 가로 폭
        :param height: 자를 부분의 세로 높이
        :return: 잘린 일부분의 이미지를 포함하는 Image 객체
        """

        surface = Surface((width, height))
        surface.blit(self.surface, (-x, -y))
        self.surface = surface
        return self
