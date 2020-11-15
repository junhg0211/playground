from pygame import Surface, draw

from manager import MouseManager
from objet import Objet
from screen import Display
from util import limit, lerp, get_lerp_friction


class ClickArea(Objet):
    """특정한 장소에서 사용자가 마우스 클릭을 통한 상호작용을 시도했는지를 감지합니다."""

    def __init__(self, x: int, y: int, width: int, height: int, runnable, mouse_manager: MouseManager):
        """
        :ivar :param x: click_area-의 왼쪽 변 좌표
        :ivar :param y: click_area-의 위쪽 변 좌표
        :ivar :param width: click_area-의 가로 폭
        :ivar :param height: click_area-의 세로 높이
        :ivar :param runnable: click_area-가 invoke-되었을 때에 실행할 Runnable
        """

        super().__init__(x, y)
        self.width = width
        self.height = height
        self.runnable = runnable
        self.mouse_manager = mouse_manager

    def mouse_on(self) -> bool:
        """click_area-의 영역 안에 마우스 커서가 있는지를 확인합니다."""

        return limit(self.mouse_manager.x, self.x, self.x + self.width) == self.mouse_manager.x \
            and limit(self.mouse_manager.y, self.y, self.y + self.height) == self.mouse_manager.y

    def tick(self):
        if self.mouse_manager.end_left:
            if self.mouse_on():
                self.runnable()


class UnderlinedClickArea(ClickArea):
    """click_area.mouse_on()일 때 아래에 밑줄 애니메이션이 표시되는 ClickArea-입니다."""

    def __init__(self, x: int, y: int, width: int, height: int, runnable, color: tuple, mouse_manager: MouseManager,
                 display: Display):
        """:ivar :param color: 아래에 추가될 밑줄의 색상"""

        super().__init__(x, y, width, height, runnable, mouse_manager)
        self.color = color
        self.display = display

        self.length = 0.0

    def tick(self):
        super().tick()

        if self.mouse_on():
            self.length = lerp(self.length, self.width, get_lerp_friction(self.display.fps))
        else:
            if self.length < 1:
                self.length = 0
            else:
                self.length = lerp(self.length, 0, get_lerp_friction(self.display.fps))

    def render(self, surface: Surface):
        if self.length:
            draw.line(surface, self.color, (self.x, self.y + self.height), (self.x + self.length, self.y + self.height))
