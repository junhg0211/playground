from pygame import Surface, draw, K_ESCAPE, K_RETURN, K_KP_ENTER

from handler import KeyboardBuffer
from manager import MouseManager, KeyManager
from objet import Objet
from objet.click_area import UnderlinedClickArea
from screen import Display
from util import TextFormat, lerp, get_lerp_friction


class FixedEntry(Objet):
    """
    가로 폭이 정해진 키보드 입력란
    입력중일 때에 밑줄 애니메이션이 표시되고,
    마우스가 영역 안에 있을 때에는 입력중일 때와 같은 애니메이션이 표시됩니다.
    """

    def __init__(self, x: int, y: int, width: int, text_format: TextFormat, mouse_manager: MouseManager,
                 key_manager: KeyManager, keyboard_buffer: KeyboardBuffer, display: Display,
                 initial_string: str = 'None', string_test=None):
        """
        :param x: 왼쪽 변 좌표
        :param y: 위쪽 변 좌표
        :param width: 가로 폭
        :ivar self.string: 화면에 보일 fixed_entry-에 입력되어 있는 값
        :param initial_string: self.string-의 초기 설정값
        :ivar self.inserting: self.keyboard_buffer-에 의해 self.string-에 입력받고있는지 여부
        :param string_test: 입력이 종료되기 위한 self.string-에 대한 조건
        """

        super().__init__(x, y)
        self.width = width
        self.text_format = text_format
        self.mouse_manager = mouse_manager
        self.key_manager = key_manager
        self.keyboard_buffer = keyboard_buffer
        self.display = display
        self.string = initial_string
        self.string_test = string_test
        self.inserting = False
        self.click_area = UnderlinedClickArea(self.x, self.y, self.width, self.text_format.size, self.start_insert,
                                              self.text_format.color, self.mouse_manager, self.display)
        self.surface = self.refresh_surface()
        self.underline_length = 0
        self.previous_string = self.string
        self.pre_edited_string = self.string

    def set_text(self, text: str):
        self.string = text
        self.refresh_surface()
        return self

    def refresh_surface(self) -> Surface:
        self.surface = self.text_format.render(self.string)
        return self.surface

    def start_insert(self):
        """self.keyboard_buffer-에 의해 self.string-에 입력받기를 시작합니다."""

        self.inserting = True
        self.pre_edited_string = self.string
        self.keyboard_buffer.regurgitate()

    def tick(self):
        self.click_area.tick()

        friction = get_lerp_friction(self.display.fps)
        if self.inserting:
            self.string += self.keyboard_buffer.regurgitate_string()
            if (backspace := self.keyboard_buffer.regurgitate_backspace()) > 0:
                self.string = self.string[:-backspace]
            self.underline_length = lerp(self.underline_length, self.width, friction)
            if self.key_manager.is_start_key(K_ESCAPE) \
                    or self.key_manager.is_start_key(K_RETURN) \
                    or self.key_manager.is_start_key(K_KP_ENTER) \
                    or not self.click_area.mouse_on() and self.mouse_manager.end_left:
                if self.string_test is not None and not self.string_test(self.string):
                    self.string = self.pre_edited_string
                else:
                    self.inserting = False
        else:
            if self.underline_length < 1:
                self.underline_length = 0
            else:
                self.underline_length = lerp(self.underline_length, 0, friction)

        if self.previous_string != self.string:
            self.refresh_surface()

        self.previous_string = self.string

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))
        if self.underline_length:
            draw.line(surface, self.text_format.color,
                      (self.x, self.y + self.text_format.size),
                      (self.x + self.underline_length, self.y + self.text_format.size))
        self.click_area.render(surface)
