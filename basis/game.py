from pygame import Surface, display, init as pygame_init
from pygame.event import get as event_get

from const import color, project
from handler import Quit
from manager import HandlerManager, KeyManager, StateManager
from screen import Display
from state import INTRO


class Game:
    def __init__(self):
        pygame_init()

        self.running = False

        self.display = Display(1920, 1080, project.NAME)

        self.key_manager = KeyManager()
        self.state_manager = StateManager().set_state(INTRO)

        self.handler_manager = HandlerManager().add(Quit(self.shutdown)).add(self.key_manager)

    def shutdown(self):
        self.running = False

    def handle(self):
        for event in event_get():
            self.handler_manager.handle(event)

    def tick(self):
        pass

    def render(self, surface: Surface):
        surface.fill(color.WHITE)

        display.flip()

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render(self.display.window)
