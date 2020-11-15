DEFAULT_LERP_FRICTION = 0.1


def get_lerp_friction(fps: float, friction: float = DEFAULT_LERP_FRICTION) -> float:
    """
    프레임레이트에 따른 lerp(...)의 보간비를 반환합니다.

    :param fps:
    :param friction: 기준 보간비
    :return: fps-에서 friction-을 구현하기 위한 값
    """

    return friction * fps


def lerp(start: float, end: float, friction: float = DEFAULT_LERP_FRICTION) -> float:
    """
    1차원 선형보간을 수행합니다.

    :param start: 선형보간의 시작점
    :param end: 선형보간의 목적지
    :param friction: 선형보간의 비율. 보간의 밀도와 비례합니다.
    """

    try:
        return (end - start) / friction + start
    except ZeroDivisionError:
        return start


def center(large: float, small: float) -> float:
    """
    1차원 물체를 다른 1차원 물체의 중간에 배치할 때, 중간에 배치될 물체의 시작 좌표를 반환합니다.

    :param large: 기준이 될 물체
    :param small: 중간에 배치될 물체
    :return: 중간에 배치될 물체의 시작 좌표
    """

    return (large - small) / 2


def limit(value: float, start: float, end: float) -> float:
    """:return: value-의 값과 start-와 end-의 닫힌구간에서 가장 가까운 값"""

    return max(min(end, value), start)
