from pygame.event import Event

from handler import Handler


class HandlerManager:
    """Basis-에서 Handler-를 모아 관리하기 위한 클래스입니다."""

    def __init__(self):
        self.handlers = list()

    def add(self, handler: Handler):
        """handler_manager-에 handler-를 추가합니다."""

        self.handlers.append(handler)
        return self

    def handle(self, event: Event):
        """handler_manager-에 저장되어 있는 handler-를 모두 실행합니다."""

        for handler in self.handlers:
            handler.handle(event)
