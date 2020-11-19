from pygame import Surface, init as pygame_init, display
from pygame.event import get as event_get

from const import color
from handler import KeyboardBuffer, Quit
from manager import KeyManager, MouseManager, StateManager, ObjetManager, HandlerManager, HUDManager
from manager.notification_manager import Notification, NotificationManager
from screen import Display


class Basis:
    """
    Playground-는 basis.run()에서 모든 처리가 시작됩니다.
    basis.run() 안의 while self.running:이 한 번 처리될 때마다 1 프레임이 흐릅니다.
    따라서 self.running-이 False-가 되면 프로그램이 종료됩니다.
    """

    def __init__(self, width: int, height: int, title: str):
        pygame_init()
        Notification.init()
        self.running = False
        self.display = Display(width, height, title)
        self.key_manager = KeyManager()
        self.mouse_manager = MouseManager()
        self.objet_manager = ObjetManager()
        self.keyboard_buffer = KeyboardBuffer()
        self.handler_manager = HandlerManager()
        self.state_manager = StateManager(self.mouse_manager, self.key_manager, self.keyboard_buffer, self.display)
        self.notification_manager = NotificationManager()
        self.handler_manager\
            .add(self.mouse_manager) \
            .add(self.key_manager) \
            .add(self.keyboard_buffer) \
            .add(Quit(self.shutdown)) \
            .add(HUDManager(self.handler_manager, self.objet_manager))

    def shutdown(self):
        """basis.running-을 False-로 만들어 프로그램을 종료합니다."""

        self.running = False

    def handle(self):
        """사용자가 프로그램에 추가하는 이벤트를 받고 저장합니다."""

        for event in event_get():
            self.handler_manager.handle(event)

    def tick(self):
        """basis.handle()에서 받은 이벤트에 따라 화면에 보일 정보를 계산해 냅니다."""

        self.display.tick()
        self.key_manager.tick()
        self.mouse_manager.tick()
        self.state_manager.tick()
        self.objet_manager.tick()
        self.notification_manager.tick()

    def render(self, surface: Surface):
        """basis.tick()에서 계산한 정보를 화면에 노출시킵니다."""

        surface.fill(color.WHITE)

        self.state_manager.render(surface)
        self.objet_manager.render(surface)
        self.notification_manager.render(surface)

        display.flip()

    def start(self):
        self.running = True
        self.run()

    def run(self):
        """
        basis.run() 안에서 1 프레임마다 basis.handle(), basis.tick(), basis.render(surface)가 실행되는데,
        각각의 메소드들이 한 프레임에서 하는 역할은 각각의 메소드의 docstring-에서 확인해볼 수 있습니다.
        """

        while self.running:
            self.handle()
            self.tick()
            self.render(self.display.window)
