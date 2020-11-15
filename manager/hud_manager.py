from pygame.constants import KEYDOWN, K_F3
from pygame.event import Event

from handler import Handler
from manager import ObjetManager, HandlerManager
from objet import HUD


class HUDManager(Handler):
    """
    HUD-를 껐다켰다하는 클래스입니다.
    F3키를 누르면 HUD-를 hud_manager.objet_manager-에 토글-추가합니다.
    """

    def __init__(self, handler_manager: HandlerManager, objet_manager: ObjetManager):
        self.objet_manager = objet_manager
        self.hud_enabled = False
        self.hud = HUD(handler_manager)

    def handle(self, event: Event):
        if event.type == KEYDOWN:
            if event.key == K_F3:
                if self.hud_enabled:
                    self.objet_manager.remove(self.hud)
                else:
                    self.objet_manager.add(self.hud)
                self.hud_enabled = not self.hud_enabled
