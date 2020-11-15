from state import State


class Character(State):
    def __init__(self, character_name: str):
        self.character_name = character_name
        print(self.character_name)

