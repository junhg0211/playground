from pygame import display


class Display:
    def __init__(self, width: int, height: int, caption: str):
        self.width = width
        self.height = height

        self.window = display.set_mode((self.width, self.height))
        display.set_caption(caption)
