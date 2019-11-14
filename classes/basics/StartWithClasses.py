class Point:
    def draw(self, rectangle):
        print('drawed: ', rectangle)


first_point = Point()
first_point.draw('rectangle red')

print(type(first_point))
print(f' The point object is an instance of int: {isinstance(first_point, int)}')
print(f' The point object is an instance of Point: {isinstance(first_point, Point)}')
print(f' The point object is a subclass of object: {issubclass(Point, object)}')
