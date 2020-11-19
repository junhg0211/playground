from basis import Basis
from const import project
from handler import Quit
from state import DESIGNER_LOBBY


class Designer(Basis):
    """Playground-에서 사용하는 캐릭터의 모습과, 맵을 디자인하는 프로그램의 Basis-입니다."""

    def __init__(self):
        super().__init__(1920, 1080, f'{project.NAME} - Designer')
        self.state_manager.set_state(DESIGNER_LOBBY)
        self.handler_manager.add(Quit(self.shutdown))
