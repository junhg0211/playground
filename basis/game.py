from basis import Basis
from const import project

from handler import Quit
from manager import HUDManager
from state import INTRO


class Game(Basis):
    def __init__(self):
        super().__init__(1920, 1080, project.NAME)
        self.state_manager.set_state(INTRO)
        self.handler_manager \
            .add(Quit(self.shutdown)) \
            .add(self.key_manager) \
            .add(self.mouse_manager) \
            .add(self.keyboard_buffer) \
            .add(HUDManager(self.handler_manager, self.objet_manager))

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
