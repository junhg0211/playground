from pygame import Surface


class State:
    """
    현재 사용자가 하고 있는 작업의 기저입니다.
    예를 들어:
    -   사용자가 캐릭터 디자인을 할지 맵 디자인을 할지 프로그램을 종료할지를 선택해야 한다면,
        state-는 해당 기능을 모두 지원합니다.
    """

    def tick(self):
        pass

    def render(self, surface: Surface):
        pass
