from pygame import Surface

from state import INTRO, Intro


class StateManager:
    def __init__(self):
        self.state = None

    def tick(self):
        if self.state is not None:
            self.state.tick()

    def render(self, surface: Surface):
        if self.state is not None:
            self.state.render(surface)

    def set_state(self, code: int, *args):
        if code == INTRO:
            self.state = Intro()

        return self
