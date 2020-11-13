from pygame import image, Surface, transform

from objet import Objet


class Image(Objet):
    def __init__(self, x: int, y: int, photo=None):
        super().__init__(x, y)
        if photo is None:
            raise TypeError("missing 1 required positional argument: 'photo'")
        elif isinstance(photo, str):
            self.surface = image.load(photo)
        elif isinstance(photo, Surface):
            self.surface = photo
        else:
            raise TypeError(f"invalid image type: '{photo}'")

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))

    def scale(self, width: int, height: int):
        self.surface = transform.scale(self.surface, (width, height))
        return self

    def smooth_scale(self, width: int, height: int):
        self.surface = transform.smoothscale(self.surface, (width, height))
        return self

    def crop(self, x: int, y: int, width: int, height: int):
        surface = Surface((width, height))
        surface.blit(self.surface, (-x, -y))
        self.surface = surface
        return self
