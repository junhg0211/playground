from pygame import Surface, init as pygame_init, display
from pygame.event import get as event_get

from const import color
from handler import KeyboardBuffer
from manager import KeyManager, MouseManager, StateManager, ObjetManager, HandlerManager
from manager.notification_manager import Notification, NotificationManager
from screen import Display


class Basis:
    def __init__(self, width: int, height: int, title: str):
        pygame_init()
        Notification.init()
        self.running = False
        self.display = Display(width, height, title)
        self.key_manager = KeyManager()
        self.mouse_manager = MouseManager()
        self.objet_manager = ObjetManager()
        self.state_manager = StateManager(self.mouse_manager, self.display)
        self.keyboard_buffer = KeyboardBuffer()
        self.handler_manager = HandlerManager().add(self.mouse_manager).add(self.key_manager).add(self.keyboard_buffer)
        self.notification_manager = NotificationManager(self.display)

    def shutdown(self):
        self.running = False

    def handle(self):
        for event in event_get():
            self.handler_manager.handle(event)

    def tick(self):
        self.display.tick()
        self.key_manager.tick()
        self.mouse_manager.tick()
        self.state_manager.tick()
        self.objet_manager.tick()
        self.notification_manager.tick()

    def render(self, surface: Surface):
        surface.fill(color.WHITE)

        self.state_manager.render(surface)
        self.objet_manager.render(surface)
        self.notification_manager.render(surface)

        display.flip()

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.handle()
            self.tick()
            self.render(self.display.window)
