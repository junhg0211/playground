def lerp(start: float, end: float, friction: float = 6.0) -> float:
    return (end - start) / friction + start


def center(large: float, small: float) -> float:
    return (large - small) / 2


def limit(value: float, start: float, end: float) -> float:
    return max(min(end, value), start)
