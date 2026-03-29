"""
An updated implementation of pygame 3d vector class.
"""

import math
import operator
from collections.abc import Callable, Sequence


class Vec3:
    """3d vector class, supports vector and scalar operators,
    and also provides a bunch of high level functions.
    reproduced from the vec3d class on the pygame wiki site.

    See https://www.pygame.org/wiki/3DVectorClass
    """

    __slots__ = ['x', 'y', 'z']

    x: float
    y: float
    z: float

    def __init__(
        self,
        x_or_triple: 'float | int | Sequence[float | int] | Vec3',
        y: float | int | None = None,
        z: float | int | None = None,
    ):
        if isinstance(x_or_triple, Vec3):
            self.x = x_or_triple.x
            self.y = x_or_triple.y
            self.z = x_or_triple.z
        elif isinstance(x_or_triple, Sequence):
            assert len(x_or_triple) >= 3, 'x_or_triple must have 3 floats'
            self.x = x_or_triple[0]
            self.y = x_or_triple[1]
            self.z = x_or_triple[2]
        elif y is None:
            self.x = x_or_triple
            self.y = x_or_triple
            self.z = x_or_triple
        else:
            assert z is not None, 'Missing z component'
            self.x = x_or_triple
            self.y = y
            self.z = z

    def __len__(self):
        return 3

    def __getitem__(self, key: int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise IndexError(f'Invalid subscript {key} to Vec3, must be 0, 1 or 2')

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise IndexError(f'Invalid subscript {key} to Vec3, must be 0, 1 or 2')

    # String representation (for debugging)
    def __repr__(self):
        return f'Vec3({self.x}, {self.y}, {self.z})'

    # Comparison
    def __eq__(self, other: 'Sequence[float | int] | Vec3'):
        if isinstance(other, Vec3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, Sequence):
            assert len(other) >= 3, 'other must have 3 floats'
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        else:
            raise ValueError(f'Cannot compare Vec3 with scalar {other}')

    def __ne__(self, other: 'Sequence[float | int] | Vec3'):
        return not self.__eq__(other)

    def __bool__(self):
        return bool(self.x or self.y or self.z)

    # Generic operator handlers
    def _o2(
        self,
        other: 'float | int | Sequence[float | int] | Vec3',
        f: Callable[[float, float], float],
    ) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(f(self.x, other.x), f(self.y, other.y), f(self.z, other.z))
        elif isinstance(other, Sequence):
            assert len(other) >= 3, 'other must have 3 floats'
            return Vec3(f(self.x, other[0]), f(self.y, other[1]), f(self.z, other[2]))
        else:
            return Vec3(f(self.x, other), f(self.y, other), f(self.z, other))

    def _r_o2(
        self,
        other: 'float | int | Sequence[float | int] | Vec3',
        f: Callable[[float, float], float],
    ) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(f(other.x, self.x), f(other.y, self.y), f(other.z, self.z))
        elif isinstance(other, Sequence):
            assert len(other) >= 3, 'other must have 3 floats'
            return Vec3(f(other[0], self.x), f(other[1], self.y), f(other[2], self.z))
        else:
            return Vec3(f(other, self.x), f(other, self.y), f(other, self.z))

    def _io(
        self,
        other: 'float | int | Sequence[float | int] | Vec3',
        f: Callable[[float, float], float],
    ):
        if isinstance(other, Vec3):
            self.x = f(self.x, other.x)
            self.y = f(self.y, other.y)
            self.z = f(self.z, other.z)
        elif isinstance(other, Sequence):
            assert len(other) >= 3, 'other must have 3 floats'
            self.x = f(self.x, other[0])
            self.y = f(self.y, other[1])
            self.z = f(self.z, other[2])
        else:
            self.x = f(self.x, other)
            self.y = f(self.y, other)
            self.z = f(self.z, other)
        return self

    # Addition
    def __add__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.add)

    __radd__ = __add__

    def __iadd__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._io(other, operator.add)

    # Subtraction
    def __sub__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.sub)

    def __rsub__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._r_o2(other, operator.sub)

    def __isub__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._io(other, operator.sub)

    # Multiplication
    def __mul__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.mul)

    __rmul__ = __mul__

    def __imul__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._io(other, operator.mul)

    # Division
    def __floordiv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.floordiv)

    def __rfloordiv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._r_o2(other, operator.floordiv)

    def __ifloordiv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._io(other, operator.floordiv)

    def __truediv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.truediv)

    def __rtruediv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._r_o2(other, operator.truediv)

    def __itruediv__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._io(other, operator.floordiv)

    # Modulo
    def __mod__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.mod)

    def __rmod__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._r_o2(other, operator.mod)

    def __divmod__(
        self, other: 'float | int | Sequence[float | int] | Vec3'
    ) -> 'tuple[Vec3, Vec3]':
        return self // other, self % other

    def __rdivmod__(
        self, other: 'float | int | Sequence[float | int] | Vec3'
    ) -> 'tuple[Vec3, Vec3]':
        return other // self, other % self

    # Exponential
    def __pow__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._o2(other, operator.pow)

    def __rpow__(self, other: 'float | int | Sequence[float | int] | Vec3'):
        return self._r_o2(other, operator.pow)

    # Unary operations
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __abs__(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))

    # vector functions
    def get_length_sqrd(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def set_length(self, value: float):
        length = self.get_length()
        self.x *= value / length
        self.y *= value / length
        self.z *= value / length

    def rotate_around_x(self, radians: float):
        cos = math.cos(radians)
        sin = math.sin(radians)
        y = self.y * cos - self.z * sin
        z = self.y * sin + self.z * cos
        self.y = y
        self.z = z

    def rotate_around_x_deg(self, degrees: float):
        self.rotate_around_x(math.radians(degrees))

    def rotate_around_y(self, radians: float):
        cos = math.cos(radians)
        sin = math.sin(radians)
        z = self.z * cos - self.x * sin
        x = self.z * sin + self.x * cos
        self.z = z
        self.x = x

    def rotate_around_y_deg(self, degrees: float):
        self.rotate_around_y(math.radians(degrees))

    def rotate_around_z(self, radians: float):
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        self.x = x
        self.y = y

    def rotate_around_z_deg(self, degrees: float):
        self.rotate_around_z(math.radians(degrees))

    def rotated_around_x(self, radians: float) -> 'Vec3':
        cos = math.cos(radians)
        sin = math.sin(radians)
        y = self.y * cos - self.z * sin
        z = self.y * sin + self.z * cos
        return Vec3(self.x, y, z)

    def rotated_around_x_deg(self, degrees: float) -> 'Vec3':
        return self.rotated_around_x(math.radians(degrees))

    def rotated_around_y(self, radians: float) -> 'Vec3':
        cos = math.cos(radians)
        sin = math.sin(radians)
        z = self.z * cos - self.x * sin
        x = self.z * sin + self.x * cos
        return Vec3(x, self.y, z)

    def rotated_around_y_deg(self, degrees: float) -> 'Vec3':
        return self.rotated_around_y(math.radians(degrees))

    def rotated_around_z(self, radians: float) -> 'Vec3':
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vec3(x, y, self.z)

    def rotated_around_z_deg(self, degrees: float) -> 'Vec3':
        return self.rotated_around_z(math.radians(degrees))

    def get_angle_around_x(self) -> float:
        if self.x == 0 and self.y == 0 and self.z == 0:
            return 0
        return math.atan2(self.z, self.y)

    def get_angle_around_x_deg(self) -> float:
        return math.degrees(self.get_angle_around_x())

    def set_angle_around_x(self, radians: float):
        self.y = math.sqrt(self.y**2 + self.z**2)
        self.z = 0
        self.rotate_around_x(radians)

    def set_angle_around_x_deg(self, degrees: float):
        self.set_angle_around_x(math.radians(degrees))

    def get_angle_around_y(self) -> float:
        if self.x == 0 and self.y == 0 and self.z == 0:
            return 0
        return math.atan2(self.x, self.z)

    def get_angle_around_y_deg(self) -> float:
        return math.degrees(self.get_angle_around_y())

    def set_angle_around_y(self, radians: float):
        self.z = math.sqrt(self.z**2 + self.x**2)
        self.x = 0
        self.rotate_around_y(radians)

    def set_angle_around_y_deg(self, degrees: float):
        self.set_angle_around_y(math.radians(degrees))

    def get_angle_around_z(self) -> float:
        if self.get_length_sqrd() == 0:
            return 0
        return math.atan2(self.y, self.x)

    def get_angle_around_z_deg(self) -> float:
        return math.degrees(self.get_angle_around_z())

    def set_angle_around_z(self, radians: float):
        self.x = math.sqrt(self.x**2 + self.y**2)
        self.y = 0
        self.rotate_around_z(radians)

    def set_angle_around_z_deg(self, degrees: float):
        self.set_angle_around_z(math.radians(degrees))

    def get_angle_between(self, other: 'Vec3') -> float:
        v1 = self.normalized()
        v2 = other.normalized()
        return math.acos(v1.dot(v2))

    def get_angle_between_deg(self, other: 'Vec3') -> float:
        return math.degrees(self.get_angle_between(other))

    def normalized(self) -> 'Vec3':
        if self.x == 0 and self.y == 0 and self.z == 0:
            return Vec3(self)
        return self / self.get_length()

    def normalize(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return
        length = self.get_length()
        self.x /= length
        self.y /= length
        self.z /= length

    def dot(self, other: 'Sequence[float | int] | Vec3') -> float:
        return self.x * other[0] + self.y * other[1] + self.z * other[2]

    def get_distance(self, other: 'Sequence[float | int] | Vec3') -> float:
        return math.sqrt(
            (self.x - other[0]) ** 2
            + (self.y - other[1]) ** 2
            + (self.z - other[2]) ** 2
        )

    def get_dist_sqrd(self, other: 'Sequence[float | int] | Vec3') -> float:
        return (
            (self.x - other[0]) ** 2
            + (self.y - other[1]) ** 2
            + (self.z - other[2]) ** 2
        )

    def projection(self, other: 'Vec3') -> 'Vec3':
        other_length_sqrd = (
            other[0] * other[0] + other[1] * other[1] + other[2] * other[2]
        )
        projected_length_times_other_length = self.dot(other)
        return other * (projected_length_times_other_length / other_length_sqrd)

    def cross(self, other: 'Sequence[float | int] | Vec3') -> 'Vec3':
        return Vec3(
            self.y * other[2] - self.z * other[1],
            self.z * other[0] - self.x * other[2],
            self.x * other[1] - self.y * other[0],
        )

    def interpolate_to(
        self, other: 'Sequence[float | int] | Vec3', range: float
    ) -> 'Vec3':
        return Vec3(
            self.x + (other[0] - self.x) * range,
            self.y + (other[1] - self.y) * range,
            self.z + (other[2] - self.z) * range,
        )

    def convert_to_basis(
        self, x_vector: 'Vec3', y_vector: 'Vec3', z_vector: 'Vec3'
    ) -> 'Vec3':
        return Vec3(
            self.dot(x_vector) / x_vector.get_length_sqrd(),
            self.dot(y_vector) / y_vector.get_length_sqrd(),
            self.dot(z_vector) / z_vector.get_length_sqrd(),
        )
