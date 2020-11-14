from pygame import Surface

from manager import MouseManager
from screen import Display
from state import GAME_INTRO, DESIGNER_LOBBY
from state.designer import Lobby
from state.game import Intro


class StateManager:
    def __init__(self, mouse_manager: MouseManager, display: Display):
        self.mouse_manager = mouse_manager
        self.display = display
        self.state = None

    def tick(self):
        if self.state is not None:
            self.state.tick()

    def render(self, surface: Surface):
        if self.state is not None:
            self.state.render(surface)

    def set_state(self, code: int, *args):
        if code == GAME_INTRO:
            self.state = Intro()
        elif code == DESIGNER_LOBBY:
            self.state = Lobby(self.mouse_manager, self.display)

        return self
