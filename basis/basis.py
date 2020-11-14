from pygame import Surface, init as pygame_init, display
from pygame.event import get as event_get

from const import color
from handler import KeyboardBuffer
from manager import KeyManager, MouseManager, StateManager, ObjetManager, HandlerManager
from screen import Display


class Basis:
    def __init__(self, width: int, height: int, title: str):
        pygame_init()
        self.running = False
        self.display = Display(width, height, title)
        self.key_manager = KeyManager()
        self.mouse_manager = MouseManager()
        self.state_manager = StateManager()
        self.objet_manager = ObjetManager(self.key_manager)
        self.keyboard_buffer = KeyboardBuffer()
        self.handler_manager = HandlerManager()

    def shutdown(self):
        self.running = False

    def handle(self):
        for event in event_get():
            self.handler_manager.handle(event)

    def tick(self):
        self.mouse_manager.tick()
        self.state_manager.tick()
        self.objet_manager.tick()

    def render(self, surface: Surface):
        surface.fill(color.WHITE)

        self.state_manager.render(surface)
        self.objet_manager.render(surface)

        display.flip()

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render(self.display.window)
