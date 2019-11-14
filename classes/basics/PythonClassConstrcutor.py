class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f'Point: {self.x}, {self.y}, {self.z}')


point = Point(420, 18, 27)

point.x = 111
point.y = 222
point.z = 333
print(f'x: {point.x}')
print(f'y: {point.y}')
print(f'z: {point.z}')

point.draw()

