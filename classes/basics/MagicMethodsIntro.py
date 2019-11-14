class Point:
    default_col = 'red'
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return f'Point: {self.x}, {self.y}, {self.z}'


point = Point(4,42,25)

print(point)