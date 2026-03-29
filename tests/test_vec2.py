import math

import pytest

from vector_py.vec2 import Vec2


def test_vec2_init():
    v = Vec2(1)
    assert v.x == 1
    assert v.y == 1

    v = Vec2(2, 3)
    assert v.x == 2
    assert v.y == 3

    v = Vec2([4, 5])
    assert v.x == 4
    assert v.y == 5

    v = Vec2(Vec2(6, 7))
    assert v.x == 6
    assert v.y == 7


def test_vec2_collection():
    v = Vec2(1, 2)

    assert len(v) == 2
    assert v[0] == 1
    assert v[1] == 2

    v[0] = 3
    assert v.x == 3

    v[1] = 4
    assert v.y == 4

    with pytest.raises(IndexError, match='Invalid subscript 2 to Vec2'):
        v[2]

    with pytest.raises(IndexError, match='Invalid subscript -1 to Vec2'):
        v[-1]

    with pytest.raises(IndexError, match='Invalid subscript 2 to Vec2'):
        v[2] = 5

    with pytest.raises(IndexError, match='Invalid subscript -1 to Vec2'):
        v[-1] = 5


def test_vec2_repr():
    v = Vec2(1, 2)

    assert repr(v) == 'Vec2(1, 2)'


def test_vec2_eq():
    v = Vec2(1, 2)

    assert v == v
    assert v == Vec2(1, 2)
    assert v == [1, 2]
    assert v == (1, 2)

    with pytest.raises(ValueError, match='Cannot compare Vec2 with scalar 3'):
        _ = v == 3


def test_vec2_ne():
    v = Vec2(1, 2)

    assert v != Vec2(3, 2)
    assert v != Vec2(1, 3)
    assert v != Vec2(3, 4)
    assert v != [3, 4]
    assert v != (3, 4)

    with pytest.raises(ValueError, match='Cannot compare Vec2 with scalar 3'):
        _ = v != 3


def test_vec2_bool():
    assert Vec2(1, 0)
    assert Vec2(0, 1)
    assert not Vec2(0)


def test_vec2_add():
    v = Vec2(1, 2)

    # __add__
    assert v + Vec2(2, 2) == Vec2(3, 4)
    assert v + [2, 2] == Vec2(3, 4)
    assert v + (2, 2) == Vec2(3, 4)
    assert v + 2 == Vec2(3, 4)

    # __radd__
    assert Vec2(2, 2) + v == Vec2(3, 4)
    assert [2, 2] + v == Vec2(3, 4)
    assert (2, 2) + v == Vec2(3, 4)
    assert 2 + v == Vec2(3, 4)

    # __iadd__
    v = Vec2(1, 2)
    v += Vec2(2, 2)
    assert v == Vec2(3, 4)

    v = Vec2(1, 2)
    v += [2, 2]
    assert v == Vec2(3, 4)

    v = Vec2(1, 2)
    v += (2, 2)
    assert v == Vec2(3, 4)

    v = Vec2(1, 2)
    v += 2
    assert v == Vec2(3, 4)


def test_vec2_sub():
    v = Vec2(1, 2)

    # __sub__
    assert v - Vec2(2, 2) == Vec2(-1, 0)
    assert v - [2, 2] == Vec2(-1, 0)
    assert v - (2, 2) == Vec2(-1, 0)
    assert v - 2 == Vec2(-1, 0)

    # __rsub__
    assert Vec2(2, 2) - v == Vec2(1, 0)
    assert [2, 2] - v == Vec2(1, 0)
    assert (2, 2) - v == Vec2(1, 0)
    assert 2 - v == Vec2(1, 0)

    # __isub__
    v = Vec2(1, 2)
    v -= Vec2(2, 2)
    assert v == Vec2(-1, 0)

    v = Vec2(1, 2)
    v -= [2, 2]
    assert v == Vec2(-1, 0)

    v = Vec2(1, 2)
    v -= (2, 2)
    assert v == Vec2(-1, 0)

    v = Vec2(1, 2)
    v -= 2
    assert v == Vec2(-1, 0)


def test_vec2_mul():
    v = Vec2(2, 3)

    # __mul__
    assert v * Vec2(2, 2) == Vec2(4, 6)
    assert v * [2, 2] == Vec2(4, 6)
    assert v * (2, 2) == Vec2(4, 6)
    assert v * 2 == Vec2(4, 6)

    # __rmul__
    assert Vec2(2, 2) * v == Vec2(4, 6)
    assert [2, 2] * v == Vec2(4, 6)
    assert (2, 2) * v == Vec2(4, 6)
    assert 2 * v == Vec2(4, 6)

    # __imul__
    v = Vec2(2, 3)
    v *= Vec2(2, 2)
    assert v == Vec2(4, 6)

    v = Vec2(2, 3)
    v *= [2, 2]
    assert v == Vec2(4, 6)

    v = Vec2(2, 3)
    v *= (2, 2)
    assert v == Vec2(4, 6)

    v = Vec2(2, 3)
    v *= 2
    assert v == Vec2(4, 6)


def test_vec2_div():
    v = Vec2(8, 6)

    # __truediv__
    assert v / Vec2(2, 3) == Vec2(4, 2)
    assert v / [2, 3] == Vec2(4, 2)
    assert v / (2, 3) == Vec2(4, 2)
    assert v / 2 == Vec2(4, 3)

    # __rtruediv__
    assert Vec2(16, 12) / v == Vec2(2, 2)
    assert [16, 12] / v == Vec2(2, 2)
    assert (16, 12) / v == Vec2(2, 2)
    assert 24 / v == Vec2(3, 4)

    # __itruediv__
    v = Vec2(8, 6)
    v /= Vec2(2, 3)
    assert v == Vec2(4, 2)

    v = Vec2(8, 6)
    v /= [2, 3]
    assert v == Vec2(4, 2)

    v = Vec2(8, 6)
    v /= (2, 3)
    assert v == Vec2(4, 2)

    v = Vec2(8, 6)
    v /= 2
    assert v == Vec2(4, 3)


def test_vec2_floordiv():
    v = Vec2(9, 7)

    # __floordiv__
    assert v // Vec2(2, 3) == Vec2(4, 2)
    assert v // [2, 3] == Vec2(4, 2)
    assert v // (2, 3) == Vec2(4, 2)
    assert v // 2 == Vec2(4, 3)

    # __rfloordiv__
    assert Vec2(18, 14) // v == Vec2(2, 2)
    assert [18, 14] // v == Vec2(2, 2)
    assert (18, 14) // v == Vec2(2, 2)
    assert 20 // v == Vec2(2, 2)

    # __ifloordiv__
    v = Vec2(9, 7)
    v //= Vec2(2, 3)
    assert v == Vec2(4, 2)

    v = Vec2(9, 7)
    v //= [2, 3]
    assert v == Vec2(4, 2)

    v = Vec2(9, 7)
    v //= (2, 3)
    assert v == Vec2(4, 2)

    v = Vec2(9, 7)
    v //= 2
    assert v == Vec2(4, 3)


def test_vec2_mod():
    v = Vec2(9, 7)

    # __mod__
    assert v % Vec2(2, 3) == Vec2(1, 1)
    assert v % [2, 3] == Vec2(1, 1)
    assert v % (2, 3) == Vec2(1, 1)
    assert v % 2 == Vec2(1, 1)

    # __rmod__
    assert Vec2(10, 8) % v == Vec2(1, 1)
    assert [10, 8] % v == Vec2(1, 1)
    assert (10, 8) % v == Vec2(1, 1)
    assert 10 % v == Vec2(1, 3)

    # __imod__
    v = Vec2(9, 7)
    v %= Vec2(2, 3)
    assert v == Vec2(1, 1)

    v = Vec2(9, 7)
    v %= [2, 3]
    assert v == Vec2(1, 1)

    v = Vec2(9, 7)
    v %= (2, 3)
    assert v == Vec2(1, 1)

    v = Vec2(9, 7)
    v %= 2
    assert v == Vec2(1, 1)


def test_vec2_divmod():
    v = Vec2(9, 7)

    # __divmod__
    assert divmod(v, Vec2(2, 3)) == (Vec2(4, 2), Vec2(1, 1))
    assert divmod(v, [2, 3]) == (Vec2(4, 2), Vec2(1, 1))
    assert divmod(v, (2, 3)) == (Vec2(4, 2), Vec2(1, 1))
    assert divmod(v, 2) == (Vec2(4, 3), Vec2(1, 1))

    # __rdivmod__
    assert divmod(Vec2(10, 8), v) == (Vec2(1, 1), Vec2(1, 1))
    assert divmod([10, 8], v) == (Vec2(1, 1), Vec2(1, 1))
    assert divmod((10, 8), v) == (Vec2(1, 1), Vec2(1, 1))
    assert divmod(10, v) == (Vec2(1, 1), Vec2(1, 3))


def test_vec2_pow():
    v = Vec2(2, 3)

    # __pow__
    assert v ** Vec2(2, 2) == Vec2(4, 9)
    assert v ** [2, 2] == Vec2(4, 9)
    assert v ** (2, 2) == Vec2(4, 9)
    assert v**2 == Vec2(4, 9)

    # __rpow__
    assert Vec2(2, 2) ** v == Vec2(4, 8)
    assert [2, 2] ** v == Vec2(4, 8)
    assert (2, 2) ** v == Vec2(4, 8)
    assert 2**v == Vec2(4, 8)

    # __ipow__
    v = Vec2(2, 3)
    v **= Vec2(2, 2)
    assert v == Vec2(4, 9)

    v = Vec2(2, 3)
    v **= [2, 2]
    assert v == Vec2(4, 9)

    v = Vec2(2, 3)
    v **= (2, 2)
    assert v == Vec2(4, 9)

    v = Vec2(2, 3)
    v **= 2
    assert v == Vec2(4, 9)


def test_vec2_neg():
    v = Vec2(1, -2)

    assert -v == Vec2(-1, 2)


def test_vec2_abs():
    v = Vec2(-1, -2)

    assert abs(v) == Vec2(1, 2)


def test_vec2_get_length_sqrd():
    v = Vec2(1, 2)

    assert v.get_length_sqrd() == 5


def test_vec2_get_length():
    v = Vec2(3, 4)

    assert v.get_length() == 5


def test_vec2_set_length():
    v = Vec2(3, 4)

    v.set_length(10)

    assert v.get_length() == 10
    assert v.x == 6
    assert v.y == 8
