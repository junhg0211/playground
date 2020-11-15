from datetime import datetime, timedelta

from pygame import Surface, draw

from const import color, font
from screen import Display
from util import TextFormat


class Notification:
    BACKGROUND_COLOR = color.BLACK
    TEXT_FORMAT = None
    MARGIN = 8
    MAX_WIDTH = 640
    LINE_HEIGHT = 18

    @staticmethod
    def init():
        Notification.TEXT_FORMAT = TextFormat(font.DALMOORI, 16, color.WHITE)

    def __init__(self, text: str, duration: float):
        self.text = text
        self.started_time = datetime.now()
        self.duration = timedelta(seconds=duration)
        self.expire_time = self.started_time + self.duration

    def is_expired(self) -> bool:
        return self.expire_time <= datetime.now()

    def progress(self) -> float:
        return (datetime.now() - self.started_time) / self.duration

    def render(self):
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
    def __init__(self, display: Display):
        self.notifications = list()
        self.display = display
        self.x = self.display.width - Notification.MARGIN * 3 - Notification.MAX_WIDTH

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
        y = self.display.height - Notification.MARGIN
        for notification in self.notifications:
            notification_surface = notification.render()
            y -= notification_surface.get_height() + Notification.MARGIN
            surface.blit(notification_surface, (self.x, y))
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
