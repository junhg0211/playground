from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame.event import Event

from handler import Handler


class MouseManager(Handler):
    """마우스의 위치와 누르고 있는지 여부를 저장하는 클래스입니다."""

    def __init__(self):
        """
        :ivar self.x: 마우스의 현재 x좌표
        :ivar self.y: 마우스의 현재 y좌표
        :ivar self.left: 왼쪽 클릭을 하고 있는지에 대한 여부
        :ivar self.wheel: 휠 클릭을 하고 있는지에 대한 여부
        :ivar self.right: 오른쪽 클릭을 하고 있는지에 대한 여부
        :ivar self.previous_left: 이전 프레임에서 왼쪽 클릭을 하고 있었는지에 대한 여부
        :ivar self.previous_wheel: 이전 프레임에서 휠 클릭을 하고 있었는지에 대한 여부
        :ivar self.previous_right: 이전 프레임에서 오른쪽 클릭을 하고 있었는지에 대한 여부
        :ivar self.start_left: 이번 프레임에서 왼쪽 클릭을 시작했는지에 대한 여부
        :ivar self.start_wheel: 이번 프레임에서 휠 클릭을 시작했는지에 대한 여부
        :ivar self.start_right: 이번 프레임에서 오른쪽 클릭을 시작했는지에 대한 여부
        :ivar self.end_left: 이번 프레임에서 왼쪽 클릭을 끝냈는지에 대한 여부
        :ivar self.end_wheel: 이번 프레임에서 휠 클릭을 끝냈는지에 대한 여부
        :ivar self.end_right: 이번 프레임에서 오른쪽 클릭을 끝냈는지에 대한 여부
        """

        self.x = 0
        self.y = 0
        self.left = False
        self.wheel = False
        self.right = False
        self.previous_left = False
        self.previous_wheel = False
        self.previous_right = False
        self.start_left = False
        self.start_wheel = False
        self.start_right = False
        self.end_left = False
        self.end_wheel = False
        self.end_right = False

    def handle(self, event: Event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.left = True
            elif event.button == 2:
                self.wheel = True
            elif event.button == 3:
                self.right = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.left = False
            elif event.button == 2:
                self.wheel = False
            elif event.button == 3:
                self.right = False
        elif event.type == MOUSEMOTION:
            self.x, self.y = event.pos

    def tick(self):
        self.start_left = not self.previous_left and self.left
        self.start_wheel = not self.previous_wheel and self.wheel
        self.start_right = not self.previous_right and self.right
        self.end_left = self.previous_left and not self.left
        self.end_wheel = self.previous_left and not self.wheel
        self.end_right = self.previous_left and not self.right
        self.previous_left = self.left
        self.previous_wheel = self.wheel
        self.previous_right = self.right
