from typing import overload, Union
from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class Vec2:
    x: float
    y: float

    @overload
    def __init__(self, x: float, y: float) -> None:
        ...

    @overload
    def __init__(self, x: float) -> None:
        ...

    def __init__(self, *args: float, **kwargs: float) -> None:
        if len(args) == 0:
            x = kwargs['x']
            y = kwargs['y'] if 'y' in kwargs else kwargs['x']
        elif len(args) == 1:
            x = args[0]
            y = args[0]
        else:
            x = args[0]
            y = args[1]

        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union['Vec2', float]) -> 'Vec2':
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)

        return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other: Union['Vec2', float]) -> 'Vec2':
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)

        return Vec2(self.x / other, self.y / other)
