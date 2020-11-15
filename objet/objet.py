from pygame import Surface


class Objet:
    """화면에서 위치를 가지는 대부분의 객체를 상속하는 클래스입니다."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def tick(self):
        pass

    def render(self, surface: Surface):
        pass
