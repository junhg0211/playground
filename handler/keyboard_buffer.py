from pygame import KEYDOWN, K_BACKSPACE
from pygame.event import Event

from handler import Handler


class KeyboardBuffer(Handler):
    """사용자가 입력한 문자열 정보를 저장하는 Handler-입니다."""

    def __init__(self):
        self.buffer = ''
        self.backspaces = 0

    def regurgitate(self) -> tuple:
        return self.regurgitate_string(), self.regurgitate_backspace()

    def regurgitate_string(self) -> str:
        """
        self.buffer-를 비우고, self.buffer-에 저장되어 있던 정보를 반환합니다.
        self.buffer-에는 이전 keyboard_buffer.regurgitate_string() 호출 이후로 입력받은 문자열 정보가 저장됩니다.

        :return: keyboard_buffer.buffer-에 저장되어있던 문자열 정보
        """

        result = self.buffer
        self.buffer = ''
        return result

    def regurgitate_backspace(self) -> int:
        """
        self.backspaces-를 0으로 설정하고, self.backspaces-에 저장되어 있던 정수를 반환합니다.
        self.backspaces-는 이전 keyboard_buffer.regurgitate_backspace() 호출 이후로 감지한
        백스페이스 입력의 횟수가 저장됩니다.

        :return: backspace 키 입력의 횟수
        """

        result = self.backspaces
        self.backspaces = 0
        return result

    def handle(self, event: Event):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(self.buffer) <= 0:
                    self.backspaces += 1
                else:
                    self.buffer = self.buffer[:-1]
            self.buffer += event.unicode
