from pygame import Surface

from handler import KeyboardBuffer
from manager import MouseManager, KeyManager
from screen import Display
from state import GAME_INTRO, DESIGNER_LOBBY, DESIGNER_CHARACTER
from state.designer import Lobby
from state.designer.character import Character
from state.game import Intro


class StateManager:
    """현재 state-의 객체를 저장하고, transition-을 구현합니다."""

    def __init__(self, mouse_manager: MouseManager, key_manager: KeyManager, keyboard_buffer: KeyboardBuffer,
                 display: Display):
        self.mouse_manager = mouse_manager
        self.key_manager = key_manager
        self.keyboard_buffer = keyboard_buffer
        self.display = display
        self.state = None

    def tick(self):
        if self.state is not None:
            self.state.tick()

    def render(self, surface: Surface):
        if self.state is not None:
            self.state.render(surface)

    def set_state(self, code: int, *args):
        """
        state-를 변경합니다.
        state-를 변경할 필요가 있는 곳에서 State-객체를 만들기에는 파일 구조가 너무 복잡하기 때문에,
        State-객체의 생성은 모두 state_manager 안에서 일어납니다.
        대신, 만들어질 state-가 추가적인 정보를 필요로 할 때 *args-를 통해 정보를 전달합니다.

        :param code: 변경할 state-의 code
        :param args: 변경될 state-가 필요로 하는 추가적인 정보
        """

        if code == GAME_INTRO:
            self.state = Intro()
        elif code == DESIGNER_LOBBY:
            self.state = Lobby(self.mouse_manager, self.key_manager, self.keyboard_buffer, self, self.display)
        elif code == DESIGNER_CHARACTER:
            self.state = Character(*args)

        return self
