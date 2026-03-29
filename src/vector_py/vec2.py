"""
An updated implementation of pygame 2d vector class.

See http://www.pygame.org/wiki/2DVectorClass
"""

import math
import operator
from collections.abc import Callable, Sequence


class Vec2:
    """2d vector class, supports vector and scalar operators,
    and also provides a bunch of high level functions

    See http://www.pygame.org/wiki/2DVectorClass
    """

    __slots__ = ['x', 'y']

    x: float
    y: float

    def __init__(
        self,
        x_or_pair: 'float | int | Sequence[float | int] | Vec2',
        y: float | int | None = None,
    ):
        if isinstance(x_or_pair, Vec2):
            self.x = x_or_pair.x
            self.y = x_or_pair.y
        elif isinstance(x_or_pair, Sequence):
            assert len(x_or_pair) >= 2, 'x_or_pair must have 2 floats'
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        elif y is None:
            self.x = x_or_pair
            self.y = x_or_pair
        else:
            self.x = x_or_pair
            self.y = y

    def __len__(self):
        return 2

    def __getitem__(self, key: int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError(f'Invalid subscript {key} to Vec2, must be 0 or 1')

    def __setitem__(self, key: int, value: float | int):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError(f'Invalid subscript {key} to Vec2, must be 0 or 1')

    # String representation (for debugging)
    def __repr__(self):
        return f'Vec2({self.x}, {self.y})'

    # Comparison
    def __eq__(self, other: 'Sequence[float | int] | Vec2'):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, Sequence):
            assert len(other) >= 2, 'other must have 2 floats'
            return self.x == other[0] and self.y == other[1]
        else:
            raise ValueError(f'Cannot compare Vec2 with scalar {other}')

    def __ne__(self, other: 'Sequence[float | int] | Vec2'):
        return not self.__eq__(other)

    def __bool__(self):
        return bool(self.x or self.y)

    # Generic operator handlers
    def _o2(
        self,
        other: 'float | int | Sequence[float | int] | Vec2',
        f: Callable[[float, float], float],
    ) -> 'Vec2':
        """Any operation where the left operand is self"""
        if isinstance(other, Vec2):
            return Vec2(f(self.x, other.x), f(self.y, other.y))
        elif isinstance(other, Sequence):
            assert len(other) >= 2, 'other must have 2 floats'
            return Vec2(f(self.x, other[0]), f(self.y, other[1]))
        else:
            return Vec2(f(self.x, other), f(self.y, other))

    def _r_o2(
        self,
        other: 'float | int | Sequence[float | int] | Vec2',
        f: Callable[[float, float], float],
    ) -> 'Vec2':
        """Any operation where the right operand is self"""
        if isinstance(other, Vec2):
            return Vec2(f(other.x, self.x), f(other.y, self.y))
        elif isinstance(other, Sequence):
            assert len(other) >= 2, 'other must have 2 floats'
            return Vec2(f(other[0], self.x), f(other[1], self.y))
        else:
            return Vec2(f(other, self.x), f(other, self.y))

    def _io(
        self,
        other: 'float | int | Sequence[float | int] | Vec2',
        f: Callable[[float, float], float],
    ):
        """Any operation where the left operand is self, result will modify self in-place"""
        if isinstance(other, Vec2):
            self.x = f(self.x, other.x)
            self.y = f(self.y, other.y)
        elif isinstance(other, Sequence):
            assert len(other) >= 2, 'other must have 2 floats'
            self.x = f(self.x, other[0])
            self.y = f(self.y, other[1])
        else:
            self.x = f(self.x, other)
            self.y = f(self.y, other)
        return self

    # Addition
    def __add__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.add)

    __radd__ = __add__

    def __iadd__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._io(other, operator.add)

    # Subtraction
    def __sub__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.sub)

    def __rsub__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._r_o2(other, operator.sub)

    def __isub__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._io(other, operator.sub)

    # Multiplication
    def __mul__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.mul)

    __rmul__ = __mul__

    def __imul__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._io(other, operator.mul)

    # Division
    def __floordiv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.floordiv)

    def __rfloordiv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._r_o2(other, operator.floordiv)

    def __ifloordiv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._io(other, operator.floordiv)

    def __truediv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.truediv)

    def __rtruediv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._r_o2(other, operator.truediv)

    def __itruediv__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._io(other, operator.floordiv)

    # Modulo
    def __mod__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.mod)

    def __rmod__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._r_o2(other, operator.mod)

    def __divmod__(
        self, other: 'float | int | Sequence[float | int] | Vec2'
    ) -> 'tuple[Vec2, Vec2]':
        return self // other, self % other

    def __rdivmod__(
        self, other: 'float | int | Sequence[float | int] | Vec2'
    ) -> 'tuple[Vec2, Vec2]':
        return other // self, other % self

    # Exponential
    def __pow__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._o2(other, operator.pow)

    def __rpow__(self, other: 'float | int | Sequence[float | int] | Vec2'):
        return self._r_o2(other, operator.pow)

    # Unary operations
    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))

    # vector functions
    def get_length_sqrd(self) -> float:
        return self.x**2 + self.y**2

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def set_length(self, value: float):
        length = self.get_length()
        self.x *= value / length
        self.y *= value / length

    def rotate(self, radians: float):
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        self.x = x
        self.y = y

    def rotate_deg(self, degrees: float):
        self.rotate(math.radians(degrees))

    def rotated(self, radians: float) -> 'Vec2':
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vec2(x, y)

    def rotated_deg(self, degrees: float) -> 'Vec2':
        return self.rotated(math.radians(degrees))

    def get_angle(self) -> float:
        if self.x == 0 and self.y == 0:
            return 0
        return math.degrees(math.atan2(self.y, self.x))

    def get_angle_deg(self) -> float:
        if self.x == 0 and self.y == 0:
            return 0
        return math.degrees(self.get_angle())

    def set_angle(self, radians: float):
        self.x = self.get_length()
        self.y = 0
        self.rotate(radians)

    def set_angle_deg(self, degrees: float):
        self.set_angle(math.radians(degrees))

    def get_angle_between(self, other: 'Sequence[float | int] | Vec2') -> float:
        cross = self.x * other[1] - self.y * other[0]
        dot = self.x * other[0] + self.y * other[1]
        return math.atan2(cross, dot)

    def get_angle_between_deg(self, other: 'Sequence[float | int] | Vec2') -> float:
        return math.degrees(self.get_angle_between(other))

    def normalized(self) -> 'Vec2':
        length = self.get_length()
        if length != 0:
            return self / length
        return Vec2(self)

    def normalize_return_length(self) -> float:
        length = self.get_length()
        if length != 0:
            self.x /= length
            self.y /= length
        return length

    def perpendicular(self) -> 'Vec2':
        return Vec2(self.y, -self.x)

    def perpendicular_normal(self) -> 'Vec2':
        length = self.get_length()
        if length != 0:
            return Vec2(-self.y / length, self.x / length)
        return Vec2(self)

    def dot(self, other: 'Sequence[float | int] | Vec2') -> float:
        return self.x * other[0] + self.y * other[1]

    def get_distance(self, other: 'Sequence[float | int] | Vec2') -> float:
        return math.sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2)

    def get_dist_sqrd(self, other: 'Sequence[float | int] | Vec2') -> float:
        return (self.x - other[0]) ** 2 + (self.y - other[1]) ** 2

    def projection(self, other: 'Vec2') -> 'Vec2':
        other_length_sqrd = other[0] * other[0] + other[1] * other[1]
        projected_length_times_other_length = self.dot(other)
        return other * (projected_length_times_other_length / other_length_sqrd)

    def cross(self, other: 'Sequence[float | int] | Vec2') -> float:
        return self.x * other[1] - self.y * other[0]

    def interpolate_to(
        self, other: 'Sequence[float | int] | Vec2', range: float
    ) -> 'Vec2':
        return Vec2(
            self.x + (other[0] - self.x) * range, self.y + (other[1] - self.y) * range
        )

    def convert_to_basis(self, x_vector: 'Vec2', y_vector: 'Vec2') -> 'Vec2':
        return Vec2(
            self.dot(x_vector) / x_vector.get_length_sqrd(),
            self.dot(y_vector) / y_vector.get_length_sqrd(),
        )
