class Point:

    default_col = 'red'

    def __init__(self, x, y, z):  # Magic method
        self.x = x
        self.y = y
        self.z = z

    # Default implementation inherited from Obj is the following string: module_name.class_name.memory_address
    def __str__(self):
        return f'Point ({self.x}, {self.y}, {self.z})'

    def __cmp__(self, other):
        return self.__eq__(other)

first_point = Point(2, 5, 3)

sec_point = Point(23, 55,66)

print(first_point == sec_point)

print(id(first_point))
print(id(sec_point))

class Human:

    def __init__(self, surname, name, intelligence):
        self.suname = surname
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __eq__(self, other):
        return self.name == other.name and self.surname==other.surname

    def __gt__(self, other):
        return self.intelligence > other.intelligence


first_human = Human('Elbadellaoui', 'Fares', 50)
wise_old_man = Human('Smith', "Elliot", 420)

print(f'Human 1 and Human 2 have the same value: {first_human == wise_old_man}')
print(f'Human 1 is more advanced than the Human 2: {wise_old_man > first_human }')

print(f'Human 1 object id: {id(first_human)}')
print(f'Human 2 object id: {id(wise_old_man)}')

first_human.intelligence = 680

print(f'Human 1 and Human 2 have the same value: {first_human == wise_old_man}')
print(f'Human 1 is more advanced than the Human 2: {wise_old_man > first_human }')