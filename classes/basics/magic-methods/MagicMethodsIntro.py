# Today on the course, black magic methods what are they, and where do they live?
# We'll continue with our point class for demonstrating purposes:


class Point:

    default_col = 'red'

    def __init__(self, x, y, z):  # Magic method
        self.x = x
        self.y = y
        self.z = z

    # Default implementation inherited from Obj is the following string: module_name.class_name.memory_address
    def __str__(self):
        return f'Point ({self.x}, {self.y}, {self.z})'

    @classmethod  # learn more about decorators: https://www.python.org/dev/peps/pep-0318/
    def zero(cls):
        return cls(0, 0, 0)


# When creating an instance like the code on line 25,
# the magic method __init__ gets called automatically by the Python interpreter:

point = Point(4, 42, 420)

# If we want to printout a string representation of our instance
# we need to overwrite the magic method ___str___:
print(point)

# We have a lot of magic methods in Python find out more about them with examples:
# https://rszalski.github.io/magicmethods/
