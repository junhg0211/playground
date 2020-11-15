from pygame import Surface, draw, K_ESCAPE, K_RETURN, K_KP_ENTER

from handler import KeyboardBuffer
from manager import MouseManager, KeyManager
from objet import Objet
from objet.click_area import UnderlinedClickArea
from screen import Display
from util import TextFormat, lerp, get_lerp_friction


class FixedEntry(Objet):
    def __init__(self, x: int, y: int, width: int, text_format: TextFormat, mouse_manager: MouseManager,
                 key_manager: KeyManager, keyboard_buffer: KeyboardBuffer, display: Display,
                 initial_string: str = 'None'):
        super().__init__(x, y)
        self.width = width
        self.text_format = text_format
        self.mouse_manager = mouse_manager
        self.key_manager = key_manager
        self.keyboard_buffer = keyboard_buffer
        self.display = display
        self.string = initial_string
        self.inserting = False
        self.click_area = UnderlinedClickArea(self.x, self.y, self.width, self.text_format.size, self.start_insert,
                                              self.text_format.color, self.mouse_manager, self.display)
        self.previous_string = self.string
        self.surface = self.refresh_surface()
        self.underline_length = 0

    def refresh_surface(self) -> Surface:
        self.surface = self.text_format.render(self.string)
        return self.surface

    def start_insert(self):
        self.inserting = True
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
