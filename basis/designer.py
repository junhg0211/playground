from basis import Basis
from const import project
from handler import Quit
from state import DESIGNER_LOBBY


class Designer(Basis):
    def __init__(self):
        super().__init__(1920, 1080, f'{project.NAME} - Designer')
        self.state_manager.set_state(DESIGNER_LOBBY)
        self.handler_manager.add(Quit(self.shutdown))
