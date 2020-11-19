from state import State


class Character(State):
    """캐릭터 디자인을 위한 State-입니다."""

    def __init__(self, character_name: str):
        self.character_name = character_name
        print(self.character_name)

