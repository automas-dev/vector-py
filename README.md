# vector-py

An updated implementation of https://www.pygame.org/wiki/2DVectorClass

## Updates

- Updated to python 3
- Renamed `Vec2d` to `Vec2`
- Added a `Vec3`
- Updated constructor to take `Vec2`, `list` and a single value
- Added `as_vec2` and `as_vec3` helper functions
- Added `vec2_like` and `vec3_like` types

## Usage

Vec2 and Vec3

```py
v2 = Vec2(num)
v2 = Vec2(x, y)
v2 = Vec2([x, y])
v2 = Vec2(Vec2(0))

v3 = Vec3(num)
v3 = Vec3(x, y, z)
v3 = Vec3([x, y, z])
v3 = Vec3(Vec3(0))
```

as_vec2 and as_vec3

```py
def as_vec2(obj):
    if isinstance(obj, Vec2):
        return obj
    else:
        return Vec2(obj)

def as_vec3(obj):
    if isinstance(obj, Vec3):
        return obj
    else:
        return Vec3(obj)
```

vec2_like and vec3_like

```py
from typing import NewType, Tuple, Union

vec2_like = NewType('vec2_like', Union[Vec2, Tuple[float, float]])
vec3_like = NewType('vec3_like', Union[Vec3, Tuple[float, float, float]])
```
