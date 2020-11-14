DEFAULT_LERP_FRICTION = 0.1


def get_lerp_friction(fps: float, friction: float = DEFAULT_LERP_FRICTION) -> float:
    return friction * fps


def lerp(start: float, end: float, friction: float = DEFAULT_LERP_FRICTION) -> float:
    return (end - start) / friction + start


def center(large: float, small: float) -> float:
    return (large - small) / 2


def limit(value: float, start: float, end: float) -> float:
    return max(min(end, value), start)
