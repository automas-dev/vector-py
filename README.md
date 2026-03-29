# vector-py

An updated implementation of

- https://www.pygame.org/wiki/2DVectorClass
- https://www.pygame.org/wiki/3DVectorClass

## Updates

- Python3 support
- Renamed `Vec2d` to `Vec2`
- Added a `Vec3`
- Updated constructor to take `Vec2`, `list` and a single value

## Usage

Vec2 and Vec3 can take various types in the constructor.

- Another instance of the same class
- A sequence of integer or float numbers (anything with `__getitem__` eg. list, tuple)
- A single integer or float value

```py
v2 = Vec2(num)
v2 = Vec2(x, y)
v2 = Vec2([x, y])
v2 = Vec2((x, y))
v2 = Vec2(Vec2(0))

v3 = Vec3(num)
v3 = Vec3(x, y, z)
v3 = Vec3([x, y, z])
v3 = Vec3((x, y, z))
v3 = Vec3(Vec3(0))
```

Each class supports most python operators such as `+`, `-`, `*`, `/`, etc. in
addition to several helper methods. See the source code for more details.
