from basis import Basis
from const import project
from handler import Quit


class Designer(Basis):
    def __init__(self):
        super().__init__(1920, 1080, f'{project.NAME} - Designer')
        self.handler_manager.add(Quit(self.shutdown))
