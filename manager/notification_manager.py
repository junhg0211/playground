from datetime import datetime, timedelta

from pygame import Surface, draw

from const import color, font
from screen import Display
from util import TextFormat


class Notification:
    """화면에 일정한 시간동안 노출시키는 문장(Notification, 알림)입니다."""

    BACKGROUND_COLOR = color.BLACK
    TEXT_FORMAT = None
    MARGIN = 8
    MAX_WIDTH = 640
    LINE_HEIGHT = 18

    @staticmethod
    def init():
        """
        알림의 TEXT_FORMAT-을 지정합니다.
        pygame.init() 후에 한 번 이상 실행되어야 합니다.
        """

        Notification.TEXT_FORMAT = TextFormat(font.DALMOORI, 16, color.WHITE)

    def __init__(self, text: str, duration: float):
        """
        :ivar :param text: 알림의 내용
        :ivar :param duration: 알림을 띄워놓을 시간 [초]
        :ivar self.started_time: 알림을 띄우기 시작한 시각
        :ivar self.expire_time: 알림 띄우기를 종료하는 시각
        """
        self.text = text
        self.duration = timedelta(seconds=duration)
        self.started_time = datetime.now()
        self.expire_time = self.started_time + self.duration

    def is_expired(self) -> bool:
        """:return: 알림 띄우기가 종료되었는지 여부"""

        return self.expire_time <= datetime.now()

    def progress(self) -> float:
        """:return: 알림 띄우기의 시작부터 종료까지에 대해 현재 시각을 0과 1 사이의 실수로 나타낸 값"""

        return (datetime.now() - self.started_time) / self.duration

    def render(self) -> Surface:
        """
        notification.render()는 notification_manager.render()에서 올바른 위치에 배치되어 화면에 보이게 됩니다.

        :return: 화면에 보일 알림 창
        """

        words = self.text.split(' ')
        line = str()
        text_surfaces = list()
        for word in words:
            if Notification.TEXT_FORMAT.get_width(line + ' ' + word) > Notification.MAX_WIDTH:
                text_surfaces.append(Notification.TEXT_FORMAT.render(line))
                line = str()
                line += word
            else:
                line += ' ' + word
        if line:
            text_surfaces.append(Notification.TEXT_FORMAT.render(line))

        width = Notification.MAX_WIDTH + Notification.MARGIN * 2
        result = Surface((width,
                          (len(text_surfaces) - 1) * Notification.LINE_HEIGHT
                          + Notification.TEXT_FORMAT.size
                          + Notification.MARGIN * 2))
        result.fill(color.BLACK)
        for i in range(len(text_surfaces)):
            result.blit(text_surfaces[i], (Notification.MARGIN, Notification.MARGIN + Notification.LINE_HEIGHT * i))

        draw.line(result, Notification.TEXT_FORMAT.color, (0, 0), (self.progress() * width, 0))

        return result


class NotificationManager:
    """Notification(알림)을 저장하고 관리하는 클래스입니다."""

    def __init__(self):
        """:ivar self.notifications: notification_manager-에 등록된 알림을 보관하는 장소입니다."""
        self.notifications = list()

    def add(self, notification: Notification):
        self.notifications.append(notification)
        return self

    def tick(self):
        delete_queue = set()
        for notification in self.notifications:
            if notification.is_expired():
                delete_queue.add(notification)
        for deleted_notification in delete_queue:
            self.notifications.remove(deleted_notification)

    def render(self, surface: Surface):
        """
        surface-의 오른쪽 아래부터 위로 self.notifications-의 Notification-들을 표시합니다.
        위에 있는 알림이 가장 최신의 알림입니다.

        :param surface: 알림을 표시할 Surface-입니다.
        """

        x = surface.get_width() - Notification.MARGIN * 3 - Notification.MAX_WIDTH
        y = surface.get_height() - Notification.MARGIN
        for notification in self.notifications:
            notification_surface = notification.render()
            y -= notification_surface.get_height() + Notification.MARGIN
            surface.blit(notification_surface, (x, y))
            if y <= 0:
                break


if __name__ == '__main__':
    string = input()
    words_ = string.split(' ')
    line_ = str()
    lines = list()
    for word_ in words_:
        if len(line_ + ' ' + word_) > 20:
            lines.append(line_)
            line_ = str()
            line_ += word_
        else:
            line_ += ' ' + word_
    if line_:
        lines.append(line_)

    print('\n'.join(lines))
