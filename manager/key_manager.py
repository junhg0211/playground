from pygame import KEYDOWN, KEYUP
from pygame.event import Event

from handler import Handler


class KeyManager(Handler):
    """사용자가 누르는 키에 대한 정보를 저장합니다."""

    def __init__(self):
        """
        :ivar self.keys: 현재 누르고 있는 키의 코드를 저장합니다.
        :ivar self.previous_keys: 이전 프레임에서 누르고 있던 키의 코드를 저장합니다.
        :ivar self.start_keys: 현재 프레임에서 누르기 시작한 키의 코드를 저장합니다.
        :ivar self.end_keys: 현재 프레임에서 떼기 시작한 키의 코드를 저장합니다.
        """
        self.keys = set()
        self.previous_keys = set()
        self.start_keys = set()
        self.end_keys = set()

    def is_key(self, key: int) -> bool:
        """
        키가 눌려있는지 확인합니다.

        :param key: 확인할 키의 코드
        :return: 키가 눌려있는지 여부
        """

        return key in self.keys

    def is_start_key(self, key: int) -> bool:
        """
        키가 이번 프레임에서 눌리기 시작했는지 확인합니다.

        :param key: 확인할 키의 코드
        :return: 키가 이번 프레임에서 눌리기 시작했는지 여부
        """

        return key in self.start_keys

    def is_end_key(self, key: int) -> bool:
        """
        키가 이번 프레임에서 떼지기 시작했는지 확인합니다.

        :param key: 확인할 키의 코드
        :return: 키가 이번 프레임에서 떼지기 시작했는지 여부
        """

        return key in self.end_keys

    def handle(self, event: Event):
        if event.type == KEYDOWN:
            self.keys.add(event.key)
        elif event.type == KEYUP:
            self.keys.remove(event.key)

    def tick(self):
        self.start_keys = self.keys - self.previous_keys
        self.end_keys = self.previous_keys - self.keys
        self.previous_keys = self.keys.copy()
