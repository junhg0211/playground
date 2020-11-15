from pygame import Surface

from const import font, color
from handler import KeyboardBuffer
from manager import MouseManager, ObjetManager, KeyManager
from objet import Text, FixedEntry
from objet.text import TextButton
from screen import Display
from state import State, DESIGNER_CHARACTER
from util import TextFormat


class Lobby(State):
    def __init__(self, mouse_manager: MouseManager, key_manager: KeyManager, keyboard_buffer: KeyboardBuffer,
                 state_manager, display: Display):
        self.title = Text(64, 64, '디자이너', TextFormat(font.DALMOORI, 72, color.BLACK))
        self.state_manager = state_manager

        button_text_format = TextFormat(font.DALMOORI, 32, color.BLACK)

        self.character_name_entry = FixedEntry(
            92 + button_text_format.get_width('캐릭터 디자인:'), 192, 360, button_text_format, mouse_manager, key_manager,
            keyboard_buffer, display, 'Nickname', lambda x: x)

        self.objet_manager = ObjetManager() \
            .add(TextButton(64, 192, '캐릭터 디자인:', button_text_format, self.on_character_pressed, mouse_manager,
                            display)) \
            .add(self.character_name_entry) \
            .add(TextButton(64, 256, '맵 디자인', button_text_format, lambda: None, mouse_manager, display)) \
            .add(TextButton(64, 320, '종료', button_text_format, exit, mouse_manager, display))

    def on_character_pressed(self):
        self.state_manager.set_state(DESIGNER_CHARACTER, self.character_name_entry.string)

    def tick(self):
        self.objet_manager.tick()

    def render(self, surface: Surface):
        self.title.render(surface)
        self.objet_manager.render(surface)
