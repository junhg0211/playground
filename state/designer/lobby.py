from pygame import Surface

from const import font, color
from manager import MouseManager, ObjetManager
from objet import Text
from objet.text import TextButton
from screen import Display
from state import State, DESIGNER_CHARACTER
from util import TextFormat


class Lobby(State):
    def __init__(self, mouse_manager: MouseManager, state_manager, display: Display):
        self.title = Text(64, 64, '디자이너', TextFormat(font.DALMOORI, 72, color.BLACK))

        button_text_format = TextFormat(font.DALMOORI, 32, color.BLACK)

        self.objet_manager = ObjetManager() \
            .add(TextButton(64, 192, '캐릭터 디자인', button_text_format,
                            lambda: state_manager.set_state(DESIGNER_CHARACTER), mouse_manager, display)) \
            .add(TextButton(64, 256, '맵 디자인', button_text_format, lambda: None, mouse_manager, display)) \
            .add(TextButton(64, 320, '종료', button_text_format, exit, mouse_manager, display))

    def tick(self):
        self.objet_manager.tick()

    def render(self, surface: Surface):
        self.title.render(surface)
        self.objet_manager.render(surface)
