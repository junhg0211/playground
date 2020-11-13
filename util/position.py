def lerp(start: float, end: float, friction: float) -> float:
    return (end - start) / friction + start


def center(large: float, small: float) -> float:
    return (large - small) / 2
