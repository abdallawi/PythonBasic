class Point:
    default_col = 'red'
    z = 22

    def __init__(self, x, y, z, ):
        self.x = x
        self.y = y
        self.z = z


    @classmethod
    def one(cls):
        print(issubclass(cls, object))

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    def draw(self):
        print(f'x: {self.x}, y: {self.y}, z: {self.z}')


point = Point(1, 2, 3)
point.draw()
second_point = Point(9, 8, 72)
# second_point.draw()
# second_point.one()
Point.one()
Point.zero()
print(Point.z)
print(type(point).z)
print(point.z)



