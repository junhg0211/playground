from basis import Basis
from const import project

from state import GAME_INTRO


class Game(Basis):
    def __init__(self):
        super().__init__(1920, 1080, project.NAME)
        self.state_manager.set_state(GAME_INTRO)

    def shutdown(self):
        self.running = False

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render(self.display.window)
