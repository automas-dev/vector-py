import math

import pytest

from vector_py.vec3 import Vec3


def test_vec3_init():
    v = Vec3(1)
    assert v.x == 1
    assert v.y == 1
    assert v.z == 1

    v = Vec3(2, 3, 4)
    assert v.x == 2
    assert v.y == 3
    assert v.z == 4

    v = Vec3([4, 5, 6])
    assert v.x == 4
    assert v.y == 5
    assert v.z == 6

    v = Vec3(Vec3(6, 7, 8))
    assert v.x == 6
    assert v.y == 7
    assert v.z == 8


def test_vec3_collection():
    v = Vec3(1, 2, 3)

    assert len(v) == 3
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3

    v[0] = 3
    assert v.x == 3

    v[1] = 4
    assert v.y == 4

    v[2] = 5
    assert v.z == 5

    with pytest.raises(IndexError, match='Invalid subscript 3 to Vec3'):
        v[3]

    with pytest.raises(IndexError, match='Invalid subscript -1 to Vec3'):
        v[-1]

    with pytest.raises(IndexError, match='Invalid subscript 3 to Vec3'):
        v[3] = 5

    with pytest.raises(IndexError, match='Invalid subscript -1 to Vec3'):
        v[-1] = 5


def test_vec3_repr():
    v = Vec3(1, 2, 3)

    assert repr(v) == 'Vec3(1, 2, 3)'


def test_vec3_eq():
    v = Vec3(1, 2, 3)

    assert v == v
    assert v == Vec3(1, 2, 3)
    assert v == [1, 2, 3]
    assert v == (1, 2, 3)

    with pytest.raises(ValueError, match='Cannot compare Vec3 with scalar 3'):
        _ = v == 3


def test_vec3_ne():
    v = Vec3(1, 2, 3)

    assert v != Vec3(3, 2, 3)
    assert v != Vec3(1, 3, 3)
    assert v != Vec3(1, 2, 4)
    assert v != Vec3(3, 4, 5)
    assert v != [3, 4, 5]
    assert v != (3, 4, 5)

    with pytest.raises(ValueError, match='Cannot compare Vec3 with scalar 3'):
        _ = v != 3


def test_vec3_bool():
    assert Vec3(1, 0, 0)
    assert Vec3(0, 1, 0)
    assert Vec3(0, 0, 1)
    assert not Vec3(0)


def test_vec3_add():
    v = Vec3(1, 2, 3)

    # __add__
    assert v + Vec3(2, 2, 2) == Vec3(3, 4, 5)
    assert v + [2, 2, 2] == Vec3(3, 4, 5)
    assert v + (2, 2, 2) == Vec3(3, 4, 5)
    assert v + 2 == Vec3(3, 4, 5)

    # __radd__
    assert Vec3(2, 2, 2) + v == Vec3(3, 4, 5)
    assert [2, 2, 2] + v == Vec3(3, 4, 5)
    assert (2, 2, 2) + v == Vec3(3, 4, 5)
    assert 2 + v == Vec3(3, 4, 5)

    # __iadd__
    v = Vec3(1, 2, 3)
    v += Vec3(2, 2, 2)
    assert v == Vec3(3, 4, 5)

    v = Vec3(1, 2, 3)
    v += [2, 2, 2]
    assert v == Vec3(3, 4, 5)

    v = Vec3(1, 2, 3)
    v += (2, 2, 2)
    assert v == Vec3(3, 4, 5)

    v = Vec3(1, 2, 3)
    v += 2
    assert v == Vec3(3, 4, 5)


def test_vec3_sub():
    v = Vec3(1, 2, 3)

    # __sub__
    assert v - Vec3(2, 2, 2) == Vec3(-1, 0, 1)
    assert v - [2, 2, 2] == Vec3(-1, 0, 1)
    assert v - (2, 2, 2) == Vec3(-1, 0, 1)
    assert v - 2 == Vec3(-1, 0, 1)

    # __rsub__
    assert Vec3(2, 2, 2) - v == Vec3(1, 0, -1)
    assert [2, 2, 2] - v == Vec3(1, 0, -1)
    assert (2, 2, 2) - v == Vec3(1, 0, -1)
    assert 2 - v == Vec3(1, 0, -1)

    # __isub__
    v = Vec3(1, 2, 3)
    v -= Vec3(2, 2, 2)
    assert v == Vec3(-1, 0, 1)

    v = Vec3(1, 2, 3)
    v -= [2, 2, 2]
    assert v == Vec3(-1, 0, 1)

    v = Vec3(1, 2, 3)
    v -= (2, 2, 2)
    assert v == Vec3(-1, 0, 1)

    v = Vec3(1, 2, 3)
    v -= 2
    assert v == Vec3(-1, 0, 1)


def test_vec3_mul():
    v = Vec3(2, 3, 4)

    # __mul__
    assert v * Vec3(2, 2, 2) == Vec3(4, 6, 8)
    assert v * [2, 2, 2] == Vec3(4, 6, 8)
    assert v * (2, 2, 2) == Vec3(4, 6, 8)
    assert v * 2 == Vec3(4, 6, 8)

    # __rmul__
    assert Vec3(2, 2, 2) * v == Vec3(4, 6, 8)
    assert [2, 2, 2] * v == Vec3(4, 6, 8)
    assert (2, 2, 2) * v == Vec3(4, 6, 8)
    assert 2 * v == Vec3(4, 6, 8)

    # __imul__
    v = Vec3(2, 3, 4)
    v *= Vec3(2, 2, 2)
    assert v == Vec3(4, 6, 8)

    v = Vec3(2, 3, 4)
    v *= [2, 2, 2]
    assert v == Vec3(4, 6, 8)

    v = Vec3(2, 3, 4)
    v *= (2, 2, 2)
    assert v == Vec3(4, 6, 8)

    v = Vec3(2, 3, 4)
    v *= 2
    assert v == Vec3(4, 6, 8)


def test_vec3_div():
    v = Vec3(8, 6, 4)

    # __truediv__
    assert v / Vec3(2, 3, 4) == Vec3(4, 2, 1)
    assert v / [2, 3, 4] == Vec3(4, 2, 1)
    assert v / (2, 3, 4) == Vec3(4, 2, 1)
    assert v / 2 == Vec3(4, 3, 2)

    # __rtruediv__
    assert Vec3(16, 12, 8) / v == Vec3(2, 2, 2)
    assert [16, 12, 8] / v == Vec3(2, 2, 2)
    assert (16, 12, 8) / v == Vec3(2, 2, 2)
    assert 24 / v == Vec3(3, 4, 6)

    # __itruediv__
    v = Vec3(8, 6, 4)
    v /= Vec3(2, 3, 4)
    assert v == Vec3(4, 2, 1)

    v = Vec3(8, 6, 4)
    v /= [2, 3, 4]
    assert v == Vec3(4, 2, 1)

    v = Vec3(8, 6, 4)
    v /= (2, 3, 4)
    assert v == Vec3(4, 2, 1)

    v = Vec3(8, 6, 4)
    v /= 2
    assert v == Vec3(4, 3, 2)


def test_vec3_floordiv():
    v = Vec3(9, 7, 5)

    # __floordiv__
    assert v // Vec3(2, 3, 4) == Vec3(4, 2, 1)
    assert v // [2, 3, 4] == Vec3(4, 2, 1)
    assert v // (2, 3, 4) == Vec3(4, 2, 1)
    assert v // 2 == Vec3(4, 3, 2)

    # __rfloordiv__
    assert Vec3(18, 14, 10) // v == Vec3(2, 2, 2)
    assert [18, 14, 10] // v == Vec3(2, 2, 2)
    assert (18, 14, 10) // v == Vec3(2, 2, 2)
    assert 20 // v == Vec3(2, 2, 4)

    # __ifloordiv__
    v = Vec3(9, 7, 5)
    v //= Vec3(2, 3, 4)
    assert v == Vec3(4, 2, 1)

    v = Vec3(9, 7, 5)
    v //= [2, 3, 4]
    assert v == Vec3(4, 2, 1)

    v = Vec3(9, 7, 5)
    v //= (2, 3, 4)
    assert v == Vec3(4, 2, 1)

    v = Vec3(9, 7, 5)
    v //= 2
    assert v == Vec3(4, 3, 2)


def test_vec3_mod():
    v = Vec3(9, 7, 5)

    # __mod__
    assert v % Vec3(2, 3, 4) == Vec3(1, 1, 1)
    assert v % [2, 3, 4] == Vec3(1, 1, 1)
    assert v % (2, 3, 4) == Vec3(1, 1, 1)
    assert v % 2 == Vec3(1, 1, 1)

    # __rmod__
    assert Vec3(10, 8, 6) % v == Vec3(1, 1, 1)
    assert [10, 8, 6] % v == Vec3(1, 1, 1)
    assert (10, 8, 6) % v == Vec3(1, 1, 1)
    assert 10 % v == Vec3(1, 3, 0)

    # __imod__
    v = Vec3(9, 7, 5)
    v %= Vec3(2, 3, 4)
    assert v == Vec3(1, 1, 1)

    v = Vec3(9, 7, 5)
    v %= [2, 3, 4]
    assert v == Vec3(1, 1, 1)

    v = Vec3(9, 7, 5)
    v %= (2, 3, 4)
    assert v == Vec3(1, 1, 1)

    v = Vec3(9, 7, 5)
    v %= 2
    assert v == Vec3(1, 1, 1)


def test_vec3_divmod():
    v = Vec3(9, 7, 5)

    # __divmod__
    assert divmod(v, Vec3(2, 3, 4)) == (Vec3(4, 2, 1), Vec3(1, 1, 1))
    assert divmod(v, [2, 3, 4]) == (Vec3(4, 2, 1), Vec3(1, 1, 1))
    assert divmod(v, (2, 3, 4)) == (Vec3(4, 2, 1), Vec3(1, 1, 1))
    assert divmod(v, 2) == (Vec3(4, 3, 2), Vec3(1, 1, 1))

    # __rdivmod__
    assert divmod(Vec3(10, 8, 6), v) == (Vec3(1, 1, 1), Vec3(1, 1, 1))
    assert divmod([10, 8, 6], v) == (Vec3(1, 1, 1), Vec3(1, 1, 1))
    assert divmod((10, 8, 6), v) == (Vec3(1, 1, 1), Vec3(1, 1, 1))
    assert divmod(10, v) == (Vec3(1, 1, 2), Vec3(1, 3, 0))


def test_vec3_pow():
    v = Vec3(2, 3, 4)

    # __pow__
    assert v ** Vec3(2, 2, 2) == Vec3(4, 9, 16)
    assert v ** [2, 2, 2] == Vec3(4, 9, 16)
    assert v ** (2, 2, 2) == Vec3(4, 9, 16)
    assert v**2 == Vec3(4, 9, 16)

    # __rpow__
    assert Vec3(2, 2, 2) ** v == Vec3(4, 8, 16)
    assert [2, 2, 2] ** v == Vec3(4, 8, 16)
    assert (2, 2, 2) ** v == Vec3(4, 8, 16)
    assert 2**v == Vec3(4, 8, 16)

    # __ipow__
    v = Vec3(2, 3, 4)
    v **= Vec3(2, 2, 2)
    assert v == Vec3(4, 9, 16)

    v = Vec3(2, 3, 4)
    v **= [2, 2, 2]
    assert v == Vec3(4, 9, 16)

    v = Vec3(2, 3, 4)
    v **= (2, 2, 2)
    assert v == Vec3(4, 9, 16)

    v = Vec3(2, 3, 4)
    v **= 2
    assert v == Vec3(4, 9, 16)


def test_vec3_neg():
    v = Vec3(1, -2, 3)

    assert -v == Vec3(-1, 2, -3)


def test_vec3_abs():
    v = Vec3(-1, -2, -3)

    assert abs(v) == Vec3(1, 2, 3)


def test_vec3_get_length_sqrd():
    v = Vec3(1, 2, 2)

    assert v.get_length_sqrd() == 9


def test_vec3_get_length():
    v = Vec3(0, 3, 4)

    assert v.get_length() == 5


def test_vec3_set_length():
    v = Vec3(0, 3, 4)

    v.set_length(10)

    assert v.get_length() == 10
    assert v.x == 0
    assert v.y == 6
    assert v.z == 8

    v = Vec3(0)
    v.set_length(1)
    assert v.get_length() == 0
