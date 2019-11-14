class Point:
    default_col= 'red'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f'x: {self.x}, {self.y}, {self.z}')


first_point = Point(24, 25, 26)

first_point.foo = 'bar'

print(Point.default_col)
print(first_point.default_col)

Point.default_col = 'green'

print(Point.default_col)
print(first_point.default_col)
