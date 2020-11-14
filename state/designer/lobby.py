from pygame import Surface

from const import font, color
from manager import MouseManager, ObjetManager
from objet import Text
from objet.text import TextButton
from state import State
from util import TextFormat


class Lobby(State):
    def __init__(self, mouse_manager: MouseManager):
        self.mouse_manager = mouse_manager

        self.title = Text(64, 64, '디자이너', TextFormat(font.DALMOORI, 72, color.BLACK))

        button_text_format = TextFormat(font.DALMOORI, 32, color.BLACK)

        self.objet_manager = ObjetManager() \
            .add(TextButton(64, 192, '캐릭터 디자인', button_text_format, lambda: None, self.mouse_manager))

    def tick(self):
        self.objet_manager.tick()

    def render(self, surface: Surface):
        self.title.render(surface)
        self.objet_manager.render(surface)
