from pygame import Surface

from objet import Objet


class ObjetManager:
    """Objet-들을 모아두고 관리하는 클래스입니다."""

    def __init__(self):
        self.objets = list()

    def add(self, objet: Objet):
        """새로운 Objet-을 추가합니다."""

        self.objets.append(objet)
        return self

    def remove(self, objet: Objet):
        """기존의 Objet-을 제거합니다."""

        if objet in self.objets:
            self.objets.remove(objet)
        return self

    def tick(self):
        """objet_manager-에 저장된 모든 Objet-의 objet.tick()을 호출합니다."""

        for objet in self.objets:
            objet.tick()

    def render(self, surface: Surface):
        """
        objet_manager-에 저장된 모든 Objet-의 objet.render(surface)를 호출합니다.

        :param surface: objet.render()의 대상 Surface
        """

        for objet in self.objets:
            objet.render(surface)
